# Type sheet: explaining an experiment or a pipeline

## When this applies

- Prose that explains a run, an ablation or a pipeline to a reader meeting it for the first time.
- Inside a slide deck, a shared reading document or a public thread, that format's own procedure governs the steps and the checks. The principle below still binds the text.
- The team, the plan, the versions, the send check and approval: [HOW_WE_WORK.md](../HOW_WE_WORK.md) ("the team file") and [unit-plan-card-gate.md](../references/unit-plan-card-gate.md) ("the unit file").

## The standard

### EXPERIMENT-BOTH-ALTITUDES  The aim at a high level, real samples at a low level

Principle: say at a high level what you are trying to do and prove, then give concrete samples at a low level: what was tried and what came out. Write it as you would write a paper. Define the machine and fix the terms before reporting results.
Invented example: "We test whether a text reminder changes attendance. Here is one appointment record as it enters, the row it becomes, and the attendance the model predicts for it."

## Roles of the units in this type

In this order, once per design:
1. Claim: what we try to do, what it would prove or kill.
2. Picture: one flowchart of input, transform, output, scoring.
3. Real samples: actual input, intermediate and output, quoted from the files, with paths.
4. Result: what was tried, what came out, candidate explanations.

## Workflow, step by step

The general workflow: the team file and the unit file. This sheet adds:
1. The brief names the artifact paths (inputs, logs, outputs).
2. A writer without them stops and asks the lead for them. It never paraphrases a sample.
3. The author says it is bad: first check whether the brief carried the artifact paths. Then the unit file.

## Examples (where)

- None filed. The general paragraph roles: [unit-roles.md](../references/unit-roles.md). Published construction choices: [published.md](../examples/published.md).

## Checks before the author sees it

This sheet's part of the send check (the unit file).
The two fresh-reader rows use one fresh reader, on the unit that first explains the design.

| Check | Who | How | Pass |
|---|---|---|---|
| Claim first | Lead | Reads the first paragraph | It states the aim and what it would prove or kill |
| Picture | Lead | Looks for the flowchart | One flowchart, before the results |
| Real samples | Lead | Opens each quoted path | Each sample is the actual bytes of the file |
| Definitions | Fresh reader, always | Points to the place each term is defined | Every term is defined in this unit or an earlier one |
| Concreteness | Fresh reader, always | Writes one example per object and lists the pipeline's steps in order | Done from the text alone |

## Gaps

- No accepted example. Meanwhile: the order in Roles.

## Craft notes (trial)

- Once the design is taught, a later result paragraph may lead with its finding.
- A repair or preview does not owe a new flowchart.
