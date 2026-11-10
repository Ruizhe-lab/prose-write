#!/usr/bin/env python3
"""Prepare inspectable role packets and account for learning evidence.

No model calls, scores, publication, or claim of prose quality. Paths in a unit
are resolved relative to that unit file. Unknown/missing inputs fail visibly.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

SCHEMA = 1
ROLE_FILES = {'writer': 'writer.json', 'source_and_editorial_reviewer': 'source_editorial.json',
              'cold_reader': 'cold_reader.txt'}

class ConsumedInputs:
    """Keep declared paths and the exact bytes used to construct the packets."""
    def __init__(self):
        self.cache = {}

    def read(self, path):
        # Do not resolve the cache key: retargeting a declared symlink matters.
        declared = Path(path).absolute()
        if declared not in self.cache:
            target = declared.resolve()
            self.cache[declared] = (target, target.read_bytes())
        target, data = self.cache[declared]
        return target, data.decode('utf-8')

    def snapshot(self):
        return [{'path': str(declared), 'resolved_path': str(target),
                 'sha256': hashlib.sha256(data).hexdigest()}
                for declared, (target, data) in self.cache.items()]


def read_unit(path, inputs):
    path, text = inputs.read(path)
    d=json.loads(text)
    if d.get('schema_version') != SCHEMA:
        raise ValueError('unsupported schema_version')
    for key in ('unit_id','task','authority','purpose','candidate','source_materials'):
        if not d.get(key): raise ValueError(f'missing {key}')
    return path,d


def packets(path,out):
    inputs=ConsumedInputs()
    up,d=read_unit(path,inputs); base=up.parent
    def material(base, p):
        return inputs.read(base/Path(p))[1]
    candidate=material(base,d['candidate'])
    preceding='\n\n'.join(material(base,p) for p in d.get('preceding_prose',[]))
    # Explicit allowlist is critical: no design, feedback, expected answer or
    # rubric enters the reader packet, even if new fields appear in the unit.
    reader_candidate_path=d.get('reader_candidate',d['candidate'])
    reader_prior_paths=d.get('reader_preceding_prose',d.get('preceding_prose',[]))
    reader_paths=[reader_candidate_path,*reader_prior_paths]
    if any(Path(p).suffix.lower() in {'.tex','.ltx'} for p in reader_paths):
        raise ValueError('cold reader needs publication-facing text; supply reader_candidate/reader_preceding_prose')
    reader_candidate=material(base,reader_candidate_path)
    reader_preceding='\n\n'.join(material(base,p) for p in reader_prior_paths)
    audience=d.get('reader_audience','a researcher in the intended field')
    reader=(f'Read this as {audience}. Describe what you understand, '
            'what you expect next, and any consequential confusion. Different phrasing '
            'is fine; do not invent improvements to satisfy the task.\n\n'
            + reader_preceding + '\n\n' + reader_candidate)
    design={k:d.get(k) for k in ('unit_id','task','authority','purpose','reader_audience','reader_knows',
                                'central_claims','accepted_constraints','open_choices',
                                'comparison','exemplar_job','review_focus') if k in d}
    source_text=[{'path':p,'text':material(base,p)} for p in d['source_materials']]
    instructions=[{'path':p,'text':material(base,p)} for p in d.get('instruction_materials',[])]
    exemplars=[{'path':p,'text':material(base,p)} for p in d.get('exemplar_materials',[])]
    writer={'role':'writer','contract':design,'source_materials':source_text,
            'instructions':instructions,'exemplars':exemplars,
            'preceding_prose':preceding,'candidate':candidate}
    reviewer=dict(writer,role='source_and_editorial_reviewer')
    reviewer['review_contract']=(
        'Separate source truth, specific causal attribution, information selection/order, '
        'scope, and author-task fit. Review the joined unit. Return located consequential '
        'findings or state no material defect. A narrow scientific pass is not editorial readiness. '
        'Do not treat length, citation counts or a different taste as a defect.')
    out=Path(out);out.mkdir(parents=True,exist_ok=True)
    for name,obj in [('writer.json',writer),('source_editorial.json',reviewer)]:
        (out/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
    (out/'cold_reader.txt').write_text(reader)
    (out/'manifest.json').write_text(json.dumps({'unit_id':d['unit_id'],
        'source_unit':str(up),'reader_materials':reader_paths,
        'inputs':inputs.snapshot(),
        'outputs':[{'path':str((out/name).absolute()),
                    'sha256':hashlib.sha256((out/name).read_bytes()).hexdigest()}
                   for name in ROLE_FILES.values()],
        'role_separation':'packet fields separated; contents and context independence require dispatch review',
        'quality_status':'unassessed','files':['writer.json','source_editorial.json','cold_reader.txt']},indent=2)+'\n')
    return out

def check_current(path):
    d=json.loads(Path(path).read_text())
    if not d.get('inputs'): raise ValueError('manifest has no input snapshot')
    changed=[]
    for r in [*d['inputs'],*d.get('outputs',[])]:
        p=Path(r['path'])
        state='missing' if not p.is_file() else (
            'changed' if (('resolved_path' in r and str(p.resolve())!=r['resolved_path'])
                          or hashlib.sha256(p.read_bytes()).hexdigest()!=r['sha256']) else None)
        if state: changed.append({'path':str(p),'state':state})
    return {'status':'inputs_changed' if changed else 'inputs_current','changed':changed,
            'meaning':'Changed inputs need a scoped editorial assessment; this is not automatic invalidation or permission to rewrite.'}

def lookup_source(path, record_id, role, kind=None):
    """Return exactly one original record, never a suffix or fuzzy match.

    This validates recorded identity fields, not the historical classifier's
    judgment that a user turn is principal speech rather than a quoted relay.
    """
    match=re.fullmatch(r'(.+):L([1-9][0-9]*)',record_id)
    if not match or ':' not in match[1]:
        raise ValueError('full source/seat/line record_id required')
    if role not in {'user','assistant','system','developer','tool'}:
        raise ValueError('explicit original role required')
    source_path=Path(path).absolute(); raw=source_path.read_bytes()
    rows=[json.loads(line) for line in raw.decode('utf-8').splitlines() if line.strip()]
    found=[r for r in rows if r.get('record_id')==record_id]
    if len(found)!=1: raise ValueError('record_id absent or duplicated')
    row=found[0]
    if row.get('source_id')!=match[1] or row.get('raw_line')!=int(match[2]):
        raise ValueError('record_id disagrees with source identity fields')
    if row.get('role')!=role: raise ValueError('record role mismatch')
    if kind is not None and row.get('kind')!=kind: raise ValueError('record kind mismatch')
    if row.get('source_is_primary') is not True or row.get('text_exact') is not True:
        raise ValueError('exact primary source record required')
    return {'record':row,'source_path':str(source_path),
            'source_sha256':hashlib.sha256(raw).hexdigest(),
            'meaning':'Exact identity and recorded role only; acceptance and authority still require reading the words.'}

def bind_review(manifest, role, review, output):
    """Bind an observation to the exact prepared packets, not a PASS label."""
    if role not in {'source_and_editorial_reviewer','cold_reader','delivery'}:
        raise ValueError('unknown review role')
    manifest=Path(manifest).absolute(); raw=manifest.read_bytes()
    if check_current(manifest)['changed']: raise ValueError('cannot bind review to changed work')
    if not json.loads(raw).get('outputs'): raise ValueError('packet output snapshot required')
    review=Path(review).absolute(); review_raw=review.read_bytes()
    record={'role':role,'manifest':{'path':str(manifest),'sha256':hashlib.sha256(raw).hexdigest()},
            'review':{'path':str(review),'sha256':hashlib.sha256(review_raw).hexdigest()},
            'meaning':'Version binding only. Review truth, independence, authority and readiness are unassessed.'}
    Path(output).write_text(json.dumps(record,indent=2)+'\n')
    return record

def check_review(path):
    d=json.loads(Path(path).read_text())
    for field in ('manifest','review'):
        ref=d[field]; data=Path(ref['path']).read_bytes()
        if hashlib.sha256(data).hexdigest()!=ref['sha256']:
            raise ValueError(f'changed {field} evidence')
    return check_current(d['manifest']['path'])

def worker_dispatch(manifest, role, recipient):
    """Create a role-specific saved brief for an internal worker; send nothing.

    It cannot disable or police other platform tools. The caller still has to
    launch the named worker through its internal route and observe custody.
    """
    if role not in ROLE_FILES: raise ValueError('unknown worker role')
    if not isinstance(recipient,dict) or recipient.get('kind')!='worker':
        raise ValueError('recipient must be an internal worker, never the author-input channel')
    if not isinstance(recipient.get('id'),str) or not recipient['id'].strip():
        raise ValueError('named worker recipient required')
    mp=Path(manifest).absolute(); data=json.loads(mp.read_text())
    if check_current(mp)['changed']: raise ValueError('cannot dispatch changed work')
    packet=(mp.parent/ROLE_FILES[role]).absolute()
    refs=[r for r in data.get('outputs',[]) if Path(r['path']).absolute()==packet]
    if len(refs)!=1: raise ValueError('exact role-packet snapshot required')
    raw=packet.read_bytes()
    if hashlib.sha256(raw).hexdigest()!=refs[0]['sha256']:
        raise ValueError('role packet changed during dispatch')
    return {'transport':'private_worker','recipient':recipient,'role':role,
            'body':raw.decode('utf-8'),'packet_sha256':refs[0]['sha256'],
            'delivery_status':'not_sent','quality_status':'unassessed'}

def account(source,dispositions,context_sources=()):
    src=[json.loads(l) for l in Path(source).read_text().splitlines() if l.strip()]
    context=[json.loads(l) for path in context_sources
             for l in Path(path).read_text().splitlines() if l.strip()]
    expected={r['record_id'] for r in src if r.get('kind')=='likely_principal'}
    assigned={}; issues=[]
    for file in dispositions:
        for line in Path(file).read_text().splitlines():
            if not line.strip(): continue
            r=json.loads(line); rid=r.get('record_id')
            if rid is None:
                issues.append({'file':str(file),'issue':'missing record_id'}); continue
            if rid in assigned: issues.append({'record_id':rid,'issue':'duplicate disposition'})
            allowed={'principal_feedback','principal_approval','principal_new_task',
                     'context_or_question','peer_relay','uncertain'}
            if r.get('classification') not in allowed:
                issues.append({'record_id':rid,'issue':'missing/unknown classification'})
            for key in ('distinct_request','disposition_basis'):
                if not isinstance(r.get(key),str) or not r[key].strip():
                    issues.append({'record_id':rid,'issue':f'missing {key}'})
            if r.get('classification') in {'principal_feedback','principal_approval'} and not (r.get('episode_id') or r.get('episode_ids')):
                issues.append({'record_id':rid,'issue':'feedback/approval needs episode linkage'})
            assigned[rid]=r
    missing=sorted(expected-assigned.keys())
    # Non-principal dispositions are useful role adjudications, not unknown errors.
    known={r['record_id'] for r in [*src,*context]}
    unknown=sorted(assigned.keys()-known)
    return {'status':'coverage_complete' if not(missing or unknown or issues) else 'coverage_incomplete',
            'principal_candidates':len(expected),'missing':missing,'unknown':unknown,'issues':issues,
            'meaning':'Coverage only. Episode truth, candidate pairing, acceptance and quality need judgment.'}

def check_feedback(path):
    d=json.loads(Path(path).read_text())
    required=('correction','kind','cause','repair','canonical_home','verification','next_use')
    missing=[k for k in required if not d.get(k)]
    status=d.get('status','captured')
    errors=[]
    allowed={'captured','instruction_written','reader_path_verified','repair_tested',
             'instruction_applied','improvement_observed'}
    if status not in allowed: errors.append('unknown feedback status')
    for field in ('verification','next_use'):
        if not isinstance(d.get(field,{}),dict): errors.append(f'{field} must be an object')
    verification=d.get('verification') if isinstance(d.get('verification'),dict) else {}
    next_use=d.get('next_use') if isinstance(d.get('next_use'),dict) else {}
    if status=='improvement_observed' and not next_use.get('observation'):
        errors.append('improvement_observed requires actual next-use observation')
    if status in {'reader_path_verified','instruction_applied'} and not verification.get('actual_route'):
        errors.append('reader-path claim requires actual consumer-route evidence')
    if status=='repair_tested' and not verification.get('test_result'):
        errors.append('repair_tested requires a recorded repair test result')
    return {'status':status,'missing':missing,'errors':errors,
            'meaning':'Record coherence only; the tool cannot establish a correct cause or good writing.'}

def main():
    p=argparse.ArgumentParser(description=__doc__); sub=p.add_subparsers(dest='action',required=True)
    a=sub.add_parser('packets');a.add_argument('unit');a.add_argument('output')
    a=sub.add_parser('account');a.add_argument('source');a.add_argument('dispositions',nargs='+')
    a.add_argument('--context',action='append',default=[],help='additional source locators; not added as principal feedback')
    a=sub.add_parser('feedback');a.add_argument('record')
    a=sub.add_parser('check-current');a.add_argument('manifest')
    a=sub.add_parser('lookup-source');a.add_argument('source');a.add_argument('record_id');a.add_argument('--role',required=True);a.add_argument('--kind')
    a=sub.add_parser('bind-review');a.add_argument('manifest');a.add_argument('role');a.add_argument('review');a.add_argument('output')
    a=sub.add_parser('check-review');a.add_argument('record')
    a=sub.add_parser('dispatch-worker');a.add_argument('manifest');a.add_argument('role');a.add_argument('--recipient',required=True);a.add_argument('--output',required=True)
    ns=p.parse_args()
    if ns.action=='packets': print(packets(ns.unit,ns.output))
    elif ns.action=='lookup-source': print(json.dumps(lookup_source(ns.source,ns.record_id,ns.role,ns.kind),ensure_ascii=False,indent=2))
    elif ns.action=='bind-review': print(json.dumps(bind_review(ns.manifest,ns.role,ns.review,ns.output),indent=2))
    elif ns.action=='check-review':
        result=check_review(ns.record);print(json.dumps(result,indent=2));sys.exit(bool(result['changed']))
    elif ns.action=='dispatch-worker':
        result=worker_dispatch(ns.manifest,ns.role,{'kind':'worker','id':ns.recipient})
        Path(ns.output).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
        print('Private worker brief prepared; nothing sent.')
    elif ns.action=='account':
        result=account(ns.source,ns.dispositions,ns.context); print(json.dumps(result,indent=2))
        sys.exit(0 if result['status']=='coverage_complete' else 1)
    elif ns.action=='check-current':
        result=check_current(ns.manifest);print(json.dumps(result,indent=2))
        sys.exit(1 if result['changed'] else 0)
    else:
        result=check_feedback(ns.record); print(json.dumps(result,indent=2))
        sys.exit(1 if result['missing'] or result['errors'] else 0)
if __name__=='__main__':main()
