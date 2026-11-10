# Optional local packet helper

`scripts/writing_unit.py` uses Python 3.9+ and the standard library. It prepares inspectable reviewer inputs, records exact declared versions and helps bind observations to a version. It makes no model calls, launches no agent, publishes nothing and assigns no quality score. The writing procedure works without it.

Run the examples below from the `prose-write` folder. Output belongs in a private working directory. Packets can contain manuscript text, source excerpts and local paths; review them before sharing.

## Prepare and inspect packets

```sh
python3 scripts/writing_unit.py packets examples/unit.json /tmp/prose-write-packets
python3 scripts/writing_unit.py check-current /tmp/prose-write-packets/manifest.json
```

The first command writes `writer.json`, `source_editorial.json`, `cold_reader.txt` and `manifest.json`. The JSON unit's paths are relative to that unit file. The example is an invented editing exercise, not a real scientific source.

Required unit fields are `schema_version: 1`, `unit_id`, `task`, `authority`, `purpose`, `candidate` and a nonempty `source_materials` array. Optional fields include:

- `preceding_prose`, `reader_audience`, `reader_knows`, `central_claims`, `accepted_constraints`, `open_choices`, `comparison`, `exemplar_job`, `review_focus`;
- `instruction_materials` and `exemplar_materials`, each an array of text-file paths;
- `reader_candidate` and `reader_preceding_prose`, for publication-facing text differing from raw editing source.

The reader packet is allowlisted to audience, publication-facing candidate and preceding prose. The helper rejects `.tex`/`.ltx` reader inputs; supply rendered/extracted readable text. It cannot detect leading answers or internal comments hidden in an allowed text file. The dispatch owner must inspect the actual packet and use a fresh context.

`check-current` detects changed declared inputs or packet bytes and exits nonzero. That calls for scoped editorial reassessment; it does not automatically invalidate unrelated work or authorize a rewrite. The helper cannot infer undeclared semantic dependencies.

## Prepare a worker brief without sending it

```sh
python3 scripts/writing_unit.py dispatch-worker \
  /tmp/prose-write-packets/manifest.json cold_reader \
  --recipient reader-1 --output /tmp/prose-write-reader-brief.json
```

The saved brief says `delivery_status: not_sent`. Use the host's authorized internal worker mechanism to deliver it, then observe custody. Do not send it through an author-question or approval tool. An informed reviewer and a fresh reader need different packets and appropriate independent contexts.

## Bind an actual review

After a reviewer has returned a real response saved as a text file:

```sh
python3 scripts/writing_unit.py bind-review \
  /tmp/prose-write-packets/manifest.json cold_reader \
  /path/to/actual-reader-response.md /tmp/prose-write-reader-binding.json
python3 scripts/writing_unit.py check-review /tmp/prose-write-reader-binding.json
```

Replace the example response path. Accepted roles are `cold_reader`, `source_and_editorial_reviewer` and `delivery`. The binding proves only which bytes were assessed. It does not establish reviewer independence, truth, acceptance or readiness.

## Check a learning record

```sh
python3 scripts/writing_unit.py feedback examples/feedback.json
```

The record needs correction, kind, cause, repair, canonical_home, verification and next_use. States include captured, instruction_written, reader_path_verified, repair_tested, instruction_applied and improvement_observed. Some states require route, test or next-use evidence. The checker verifies record coherence, not whether the cause or repair is correct. The example deliberately remains `captured`.

## Optional historical accounting functions

These are useful only if a project already maintains an exact conversation archive. They are not required to adopt the skill.

`lookup-source ARCHIVE RECORD_ID --role ROLE [--kind KIND]` returns exactly one original JSONL record. IDs have the form `provider:session:L123`; the record must agree on `source_id`, `raw_line`, `role`, `source_is_primary: true`, and `text_exact: true`. It rejects fuzzy/suffix matches. The recorded role alone cannot decide whether a user turn is an author's own words or a quoted relay; read the text.

`account SOURCE DISPOSITION... [--context CONTEXT]` checks coverage of source rows marked `likely_principal`. Dispositions require `record_id`, `classification`, `distinct_request` and `disposition_basis`; feedback/approval rows also need episode linkage. Classifications are `principal_feedback`, `principal_approval`, `principal_new_task`, `context_or_question`, `peer_relay` and `uncertain`. “Principal” here means the author/requester, not a named individual. Coverage does not certify pairing or interpretation.

Do not build a new transcript archive merely to satisfy these optional commands. Existing project records remain the canonical decision home.
