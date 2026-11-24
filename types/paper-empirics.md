# Type sheet: empirical results, and checking a coauthor's section

The team, the plan, the versions, the send check, approval, applying and the record are not stated here.
They are in [HOW_WE_WORK.md](../HOW_WE_WORK.md) ("the team file") and [unit-plan-card-gate.md](../references/unit-plan-card-gate.md) ("the unit file").

## When this applies

- An empirical results section or paragraph that the author owns, or a coauthor's that the author asked to rewrite.
- A coauthor's section, or any part the author calls fine, of any paper: the audit below.
- Which of the two cases a text is: the team file, who writes each type of text.
- Exhibit selection (ESSENTIAL-EXHIBITS): [paper-frame.md](paper-frame.md).

## The standard

This sheet is thin: no rule yet says how an empirical paragraph is built.

The audit rests on MATERIAL-NOT-WORDING. The principle, its five classes of material change and its cut-plan rule are stated once, in [the team file](../HOW_WE_WORK.md), under "Principles".

## Roles of the units in this type

| Unit | Job | First sentence |
|---|---|---|
| Prediction | Theory object, its observable counterpart, the expected relation | The model's claim |
| Design | Variation, comparison, identifying condition, estimand | What the comparison isolates |
| Result | The finding, then the estimate with magnitude and uncertainty | The finding, in words, before the estimates |
| Confirmation or test | Prediction, then what the data show | "The model predicts ..., and the data let us check" |

## Workflow, step by step

The author's own empirical text: the general workflow in the team file and the unit file. This sheet adds only the roles above and the checks below.

The audit of a coauthor's section, or of a part the author calls fine. Who audits, who verifies and what the author is sent: the team file. This sheet adds:
1. The partner writes one entry per finding in the audit file: class, file, line, quoted text, evidence cell, smallest fix in exact words.
2. The class is one of the five in the team file (MATERIAL-NOT-WORDING). A wrong population or denominator is a wrong number. A missing measurement step is a step a reader cannot follow.
3. "The revised sections" are those with parts marked "applied" or "delivered" in `DECISIONS.md`, in this record or any older record of the same text. None: the sections changed since the last version the coauthors saw, by `git log`; name them in the findings message.
4. One finding is one problem at one place. Repeats of one problem are one finding that lists every place.
5. The lead opens the source of each finding. A finding that does not hold is dropped. A finding whose source cannot be opened is not a finding: it goes in the coauthor note as "needs their confirmation". Several sections audited at once share one audit file, grouped by section.
6. A question only the coauthor can answer (a data choice) is not a finding. It goes in the coauthor note as "needs their confirmation".
7. The author declines a class of change: that class is not proposed again in this paper.
8. The author calls a finding wrong: open the cell again, report what it shows in one line, then drop or correct the finding.
9. A cut plan is made only when the author asks. Unasked: at most one line in the findings message naming what a cut would move. A condensed paragraph that replaces a moved block is new prose: two writers, three versions.

## Examples (where)

- Invented: [unit-roles.md](../references/unit-roles.md), section 7 (confirmation or test) and section 8 (light edit, and no change).
- Published: [published.md](../examples/published.md). No empirical results paragraph is filed yet.

## Checks before the author sees it

These rows are this sheet's part of the send check (the unit file). The number trace is in the unit file's source check and is not repeated here.

| Check | Runs on | Who | How | Pass |
|---|---|---|---|---|
| Finding first (trial) | The author's own text, a Result unit | Lead | Reads the first sentence | It states the finding in words; the estimate follows |
| Confirmation frame (trial) | The author's own text, a Confirmation unit | Lead | Reads the first sentence against the unit's role | A confirmation is not framed as a surprise |
| Each finding holds | Findings message | Lead | Opens each cited cell and line | Every kept finding is reproduced; the others are dropped |
| Material only | Findings message | Lead | Reads each finding against the five classes of the team file | Every finding is in a class; no rewording is offered |
| One finding per problem | Findings message | Lead | Reads the list for repeats | No problem appears twice |
| Cut plan moves (only if the author asked for one) | Findings message | Lead | Diffs the cut plan against the text | Every moved item is in the appendix; nothing is deleted; every finding the introduction relies on is still in the main text |

## When the author says it is bad

- The author's own empirical paragraph: the unit file, "When the author says it is bad".
- A finding or a class of change: audit steps 7 and 8 above.

## Gaps

- No rule on how an empirical paragraph is built. Meanwhile: the roles table, the number trace, and [STANDARDS.md](../STANDARDS.md).
- No accepted empirical results paragraph is filed.
- The two checks marked "trial" come from the roles table, not from a ruling.

## Craft notes (trial)

- A confirmation is not written as a surprise.
- A proxy does not measure an unobserved mechanism; an association is not a cause.
- An insignificant estimate is not evidence of no effect.
- A rate per unit and a total can move in opposite directions; say which one the estimate measures.
