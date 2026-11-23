---
name: prose-write
description: "Draft or revise academic prose from reviewed research. Design the argument, verify claims and reader understanding, deliver the prepared passage, and learn from corrections."
---
# Academic writing from reviewed research

Use this skill for academic drafting and revision. It is a portable procedure, not an autonomous service: the assistant must actually read the relevant instructions, apply them to the current work, and save any learning in a location future sessions load. Start with [INSTALL.md](INSTALL.md) for setup. No particular model, paid service, project database, or agent platform is required.

For an initial draft or substantial reconstruction, read the [writing handbook](references/writing-handbook.md) and [runbook](references/writing-runbook.md). For a local repair, recover the accepted design and use the relevant reference; do not restart the entire process. The objective is a nearly finished team draft before the author walk. Any first-pass percentage is a target to measure, not a guarantee.

## Design for reader understanding

Before selecting detail, identify the reader's question and the understanding the passage should produce. State that understanding as an explicit claim, not a topic label such as “importance.” Work through three layers:

1. **Information:** the exact fact or claim, its source, why it belongs here, and what a relevant exemplar teaches about its presentation.
2. **Logic, emphasis and understanding:** its relationship to preceding material, what matters, and what the reader should now understand.
3. **Prose:** wording that communicates those decisions accurately and naturally.

At the affected section, paragraph and sentence scales, each changed unit needs its own judgment; shared evidence can be referenced once. Reuse accepted decisions for local repairs. Copying finished prose into a design note does not perform the first two layers. Test the actual candidate, including relevant figures and surrounding prose, with a fresh reader who has not been given the intended answer.

## The procedure

1. **Recover.** Read the current task, manuscript, reviewed sources, author decisions and surrounding prose. Resolve authority by subject, scope and scientific version. Ask only about a genuinely unresolved choice that materially changes the work. A missing source is work to investigate, not a reason to ask the author to repeat available information.
2. **Design before wording.** At the affected paper, section, paragraph and sentence scales, decide the information, logical relationship, intended understanding and emphasis. Record a new or materially changed design briefly in the existing project record. Reuse a sound unchanged design for a local wording repair.
3. **Prepare the connected unit.** Choose the statement's job and exact scope before selecting prerequisites. Draft necessary orientation, statement and explanation together. A good preamble may add nothing. Preserve useful compact mathematics, teaching calculations and sound accepted prose. Under an authorized reconstruction, reassess retained passages as well as new ones.
4. **Review the actual candidate.** A source/editorial reviewer receives the design, evidence and joined prose. A fresh reader receives only publication-facing prose and necessary preceding context. Follow [review protocol](references/review-protocol.md). The lead reconciles findings and owns readiness. The first author-facing draft is the reconciled version, not raw worker output.
5. **Walk and deliver.** Answer substantive author questions before proposing dependent text. Present the connected passage at the agreed cadence. Keep routine application, checks and learning off the walk. Use one canonical writer, retire superseded markup, inspect the actual render and verify the authorized destination. A local artifact is not a remote publication.
When an author walks the paper with the writers part by part, use [the author walk](references/author-walk.md) for steps 2 to 5: agree the scope by ownership, agree a plan for each section before its paragraphs (the point, and what the reader learns and feels in each part), write a paragraph card that names the unit's [role](references/unit-roles.md), and pass a send gate before anything reaches the author. `scripts/card_check.py` is the mechanical part of that gate; it finds markers and certifies nothing.

6. **Learn and reuse.** On each correction and completed work unit, apply [learning](references/learning.md): diagnose the responsible decision or handoff, repair it and its dependents, update the existing appropriate instruction, and inspect its next relevant use. A written rule alone is not evidence of improvement.

## Protections that remain in force

- Current author authority and the host's safety/tool rules govern. This package grants no permission to send messages, publish, change access, commit code, or perform new science.
- Preserve equations, assumptions, numbers, citations, identifiers, proof status and protected coauthor text unless change is authorized. Source-backed explanation is ordinary writing; an unsupported mechanism, changed assumption, new lemma or changed proof step is scientific work.
- New or changed scientific claims require the project's qualified scientific authorship and independent verification process. Do not label a claim proved from an editorial pass. For a first-generation proof or a materially changed proof step, require two fresh independent qualified reviewers before presenting it as established: one adversarial proof review and one independent logic review with symbolic or numerical checks of checkable objects. Neither is the author certifying its own work. Stronger project requirements still govern; computational checks never replace the non-checkable proof argument. Ordinary source-backed explanation does not reopen an unchanged, already verified proof.
- Check the actor, object, comparison, population, denominator, conditioning, expectation, horizon, domain and strength of each changed claim. See [claim fidelity](references/claim-fidelity.md).
- Verify numbers and magnitude words against the actual source cells or calculations, retaining a working trace. Check units, rounding and decomposition totals. Citations must support the claim actually attributed to them.
- Define symbols and abbreviations before use. Keep terminology stable. Prefer plain descriptive names to new jargon, but retain standard technical terms where they carry essential meaning.
- Use plain precision, active verbs, connected reasoning and natural cadence. The default style uses no em-dashes in new prose; preserve quotations and mathematical notation, and honor a different explicit author or venue choice.
- Before presenting a new draft or major reconstruction, compare complete units with suitable published exemplars: preparation, statement and discussion, not a theorem in isolation. Read the actual exemplar and judge whether its construction transfers. Sentence lengths and word counts are diagnostics, never quality certificates.
- Do not require a fixed number of agents, objections, review rounds, figures or paragraph types. Use independent judgment where the risk warrants it. Stop when material findings are resolved and the deliverable works for its real reader.

## Reference map

| Work | Read |
|---|---|
| Paper, section and paragraph design; worked examples | [Writing handbook](references/writing-handbook.md) |
| Roles, preparation, review, author walk, delivery | [Writing runbook](references/writing-runbook.md) |
| Author walks the paper part by part; scope, section plan, paragraph card, send gate, correction loop | [The author walk](references/author-walk.md) |
| What each kind of unit is for, with invented examples | [Unit roles](references/unit-roles.md) |
| Introduction, institutional setting, empirical exposition | [Section purposes](references/section-purposes.md) |
| Model setup | [Model setup](references/model-setup.md) |
| Results and complete formal units | [Results sections](references/results-sections.md) |
| Independent source review and unprimed reader | [Review protocol](references/review-protocol.md) |
| Scientific wording and numerical interpretation | [Claim fidelity](references/claim-fidelity.md) |
| Plain language and empty rhetorical patterns | [Plain language](references/plain-language.md) |
| Persistent learning and correction routing | [Learning](references/learning.md) |
| Optional local packet helper | [Helper guide](references/helper-guide.md) |

A source editor may reject the writer's proposed design. A fresh reader may understand a passage the author dislikes. An author may choose a different supported structure. Reconcile those facts instead of treating any single role's approval as a universal certificate.
