# One unit: plan, card, send check

Every route uses this file.
A unit, also called a part, is one line of the agreed plan: one paragraph, or two or three connected ones. A formal statement and the paragraph that explains it are one unit.
Paths are relative to the skill folder. "The team file" is [`HOW_WE_WORK.md`](../HOW_WE_WORK.md): the seats, the mode, the message, approval, delivery, the record.
A name in capitals is a principle, stated at the end of this file; any other row is the lead's default.

## The plan

A plan message is one message per section, readable in a minute. A section with subsections: first one message with the section's point and the order of its subsections; then one message per subsection, one at a time. Form: [`templates/PLAN_MESSAGE.md`](../templates/PLAN_MESSAGE.md). It holds:
1. The point: one belief and one feeling, not a list.
2. Title options, two or three noun phrases, with a pick.
3. One line per part: what the reader learns and feels, the role, the frame of the first sentence, the current paragraphs it draws on. The part that carries the point is marked.
4. What is compressed, moved or cut.

When it is sent. Use the first row that fits.

| Case | Plan message | Drafting |
|---|---|---|
| The author says the perception is missing, calls a version just shown or an approved part or section bad, or makes the same complaint a second time on one part | Plan alone, on [`templates/PLAN_ALONE_MESSAGE.md`](../templates/PLAN_ALONE_MESSAGE.md). Quote the point on record and ask "Is this still the point?" No point on record: the plan proposes one. | Stops for that part until the author decides. Not this row if the author gave replacement words. |
| An email. A coauthor-section audit. An error with one right answer. | None. | Not applicable. |
| A one-paragraph repair the author asked for, live or prepared | None. The request is the go-ahead. Its card is its plan. | At once. |
| An agreed plan for this section is in the record | None. Reuse it. | At once. |
| Live. The author says "skip the plan" or "just write it". | The plan is the first block of the versions message. | At once. |
| Live. A section or subsection the author works on, a letter and a proposal included. | Plan alone, first. (PLAN-BEFORE-PARAGRAPHS) | Waits for agreement on the point and the order. Meanwhile both writers write plans and gather sources. |
| Prepared | Sent as the first message. | Does not wait. Both writers draft from the plan as sent. The ready notice says "you have not agreed this plan". |

Two cases add to the row that fits.

| Case | Plan message | Drafting |
|---|---|---|
| A fact only the author can give, without which nothing can be drafted (which call, which applicant, which reports) | Look first in the record and the project's files. The first message asks what they leave open, with every other such question. It replaces the plan when the plan cannot be written without it. | Do the work that does not depend on it. Then stop and say what you wait for. Never guess it. |
| Prepared, and a choice that belongs to the author (the team file, "The seats") | The plan gives options and a recommendation. | Draft on the recommendation. List the choice in the ready notice as open. Never start a new task (a literature search, a new analysis) on a recommendation. |

- Drafting starts when the plan is agreed (live, one part ahead) or at once (prepared, every part).
- The live plan message carries the line: "Say 'just write it' and the versions come with the plan." A plan alone after a complaint does not.
- Live, a plan alone, sent within minutes, is a delivery.
- The partner writes its own plan on the same form. The author sees the lead's plan in full and the partner's as differences, one line each.
- Live: before a plan is agreed, the partner returns its plan; after, it drafts the parts in plan order with no new brief, never more than one part ahead of the part the author is on.
- Prepared: the partner drafts every part from the plan as sent, with no new brief.
- Both writers keep the agreed point, roles and order. The partner is not asked to differ.
- Parts go in the document's order unless the author names another. A held part is skipped with one line to the author and shown when it is back.
- No title options for a standard heading (Introduction, Conclusion, Related Literature), for a letter, or where a funder fixes the heading.

## The card

Each writer fills the card before drafting, in its queue sheet ([`templates/QUEUE_SHEET.md`](../templates/QUEUE_SHEET.md)). The first five lines are the five elements (PARAGRAPH-CARD). The last two are working lines.

1. Perception: the one sentence the reader should believe afterwards, and the one feeling.
2. Concept: the idea or object the reader must understand to get there.
3. Logic: the chain as bullets; the link to the paragraph before; the hand-over to the next; what is stressed.
4. Information: each fact, number, definition and result the chain needs, with its source. Nothing else.
5. Prose: the register ([`STANDARDS.md`](../STANDARDS.md)).
6. Role: the type sheet's row for this unit; if it has none, a row of the table below.
7. Frame: what the first sentence does.

- Check every chain link against its source before any prose. Never state a mechanism from memory.
- A surprise needs two chains: what the reader expects; what the source delivers.
- A light edit's card is one line: "role: light edit".

| Role | Its job | First sentence |
|---|---|---|
| Opening that carries a surprise | The question, the stakes, the route. The worked case waits. | A question, or the expectation that fails |
| Opening of a derivation | Name what is solved and why | The economic question |
| Setup | Rules once, then notation, in separate paragraphs | The object being defined |
| The means (solving) | Reach the result with the least machinery | What is computed and for whom |
| Explanation after a result | Make the reader understand, not restate conditions | The tension or the plain consequence |
| The part that carries the point | One concrete case, then the general statement | The answer to the question the last part ended on |
| Confirmation or test | Prediction, then what the data show | The prediction |
| Light edit | Leave the author's chain; fix a word or a pointer | Unchanged |

One invented example per role, in this order: [`unit-roles.md`](unit-roles.md).

### Craft notes (trial, written by the writers)

- Open from the point of the unit before, then turn to this unit's job.
- Several cases: open with the one claim that unifies them.
- Build a surprise as a rise: the expectation; why it fails; the consequence. One step per sentence.
- Name the relation between each pair of adjacent sentences and the words that carry it.
- Keep a fact without keeping its sentence. Never cut a reason clause.
- Name people, not pronouns, when two actors share one. End on the plain conclusion. Tighten last.

## The send check

One gate (SEND-CHECK). The lead owns it, runs it on every version, and writes its record under the draft in the part's queue sheet. The partner runs step 5, and any type-sheet row of step 4 that names the partner.
A version that fails a step is repaired and rerun, or dropped.

1. The script, [`scripts/card_check.py`](../scripts/card_check.py).
   Who: the lead, or a helper.
   Pass: it ran; every marker says "fixed" or "explained: <reason>".
2. The source check: each number, citation, model claim, grant claim and term against its source.
   Who: the lead; helpers may do the lookups.
   Pass: one line per claim: the claim, the source location, "matches".
3. The seven judgments (below), and each `CHECKLIST.md` line.
   Who: the lead only.
   Pass: one line each: "pass: <evidence>".
4. Every row of "Checks before the author sees it" in the type sheet.
   Who: the lead; a helper may run search rows; any seat a row names.
   Pass: one line per row.
5. The cross-check: each writer checks the other's draft against its own card, when the other's draft arrives.
   Who: the partner on the lead's draft, the lead on the partner's.
   Pass: written in the checker's own sheet. A late partner: "cross-check not run: partner late", repeated in the "Not checked" line.
6. The fresh reader, where "The fresh reader" below requires one.
   Who: a fresh reader started by the lead.
   Pass: as "The fresh reader" below states.
7. The "Checked / Not checked" lines in the message.
   Who: the lead.
   Pass: present, two or three plain lines, true.

Helpers in steps 1, 2 and 4 follow CHECKS-IN-WRITING.

Which steps run, on which text.

| What is sent | Steps | On which text |
|---|---|---|
| Prose to approve (a part, a repair, a letter paragraph) | 1 to 7 | Every version shown. Step 5: versions 1 and 2 only |
| One repaired version, after the author named a fault in a version | 1 to 4, 6 where due, then 7. The partner is told; its check is not awaited. | The repaired version |
| Email | 1 (without `--before`), 2, 3, 4, 7. Write "steps 5 and 6: not applicable, email". | The one draft |
| A plan, audit findings, a warning, a ready notice | 2, the scope judgment, the sheet rows marked for that kind of message, 7 | The message |
| A prepared whole, before the ready notice | Per part as above, then one fidelity read and one fresh read of the whole | The job's parts, as they sit in the reading copy |

The script. `python3 scripts/card_check.py <draft.txt> --before <current.txt> --max-ratio 1.0`.
- Add `--rise` for a surprise. Add `--actors she:nurse,she:patient` when two actors share a pronoun.
- A new text: leave out `--before` and `--max-ratio`.
- Exit 0: no marker. Exit 1: markers. Exit 2: it did not run; fix the call.
- A draft longer than the current text needs a reason.

The source check, by kind of claim.
- A number or magnitude word ("large", "most", "doubles"): print the source cell first, with its sample and denominator. Write file and line. Pass: the text matches the cell exactly, everywhere the number appears.
- A number whose source cell cannot be found: trace it to the typeset table and write "traced to the table only".
- A citation or quotation: open the local copy of the source. Write the page. Pass: the page says it, about the same object. No local copy: [`types/paper-frame.md`](../types/paper-frame.md).
- A model claim: write the tag of the proposition, lemma or equation. Pass: the sentence claims no more than the statement. The lead always runs it, with [`theory-claim-fidelity.md`](theory-claim-fidelity.md).
- A grant claim (a partner, dataset, result or past award): written evidence in the application folder. Pass: the matching row of [`types/grant.md`](../types/grant.md).
- A term: search the term lists named in [`paper-build-checks.md`](paper-build-checks.md). Pass: the field's standard term is used.

The seven judgments. A fail is written "fail: <repair made>".
1. Perception. Write the sentence the reader should believe. Pass: the text alone delivers it. A list of topics fails.
2. Role. Pass: the unit does its job and no other.
3. Logic. Pass: each chain link is in the text, in order; the first sentence carries the frame; both ends link.
4. Information. For each fact ask: would the reader lose the perception without it? Pass: all needed, each stated once, nothing missing.
5. Source. Pass: the source-check lines are written under the draft.
6. Scope. Pass: no symbol, formula or formal statement differs from the current text, except a change from the math author, shown as old and new; a coauthor's text is touched only as the scope allows.
7. Prose. Pass: no clause can go without losing an inference or a fact the reader uses.

The fidelity read. A second view of a prepared whole. This is its one home.
- Who: the fidelity reader, a seat that wrote none of the text and is not the fresh reader. For a grant: the coordinator.
- Gets: the plan, the cards, the text, the reviewed sources and any certified formal statements.
- Pass: every link of the plan is present; every claim, number and citation matches its source; certified formal statements are unchanged.

## What the author is shown about the checks

Every message carries, just before its recommendation or question:
- "Checked: sources (<n> claims against <where>); numbers traced (<n>, or none); fresh reader (<passed / not required>)."
- "Not checked: <item and reason>", or "Nothing left unchecked."
- Never write "verified" without the source lines behind it.

The checking loop ends on the lead's judgment, stated on the record (CHECK-ON-ARRIVAL).

## The fresh reader

A fresh reader has no history with the text: a new person, or a new assistant session on the most capable reader available, never a quick helper.
It gets the passage, the paragraph before and after, and the figures and tables the passage cites. For a reply to a referee: also the comment and the paper passage the reply cites.
It never gets the card, the plan or the intended answer.

| Case | Fresh reader |
|---|---|
| The part the plan marks as carrying the point | Yes |
| A prepared whole (section, letter, proposal), once, before the ready notice | Yes |
| A type-sheet row that says "always" | Yes, for the unit that row names |
| A type-sheet row that names a fresh reader for an assembled new or rebuilt section | Yes, once, when the section is assembled, live or prepared |
| Any other part | No. The lead reads and writes "lead read; no fresh reader due". |
| A one-paragraph repair; one repaired version | No, unless the agreed plan marks that part as carrying the point |
| A plan, findings message, warning or ready notice; an email | No |

| Question | Answer |
|---|---|
| When it starts | When the recommended version has passed steps 1 to 4. With drafting one part ahead, that is before the author reaches the part. |
| What it reads | The recommended version only. |
| What it answers | What do you now believe? Why does it follow? What remains unproved? Then the question of each sheet row that names it. |
| Pass | Its answer states the card's belief, gives the chain's links, and claims no more than the source supports. |
| Fail | Repair and rerun. Two fails on one part: back to the plan. |
| While it is out | The writers go on with the next part. |
| Not back when the part is due | The part is held. Tell the author in one line: "Part 3 is with the fresh reader." |
| A unit with no neighbours (an abstract) | It reads the unit alone. The "no more than the source supports" test is then the lead's. |

## The perception gate

Runs only when the author has not fixed the point of a new or rebuilt section or of a whole grant proposal. The lead runs it before the plan message, with fresh readers as the cold readers. In every other case it does not run: the author's point, or the agreed plan, is the perception.
Live, it never delays the plan message: if it is not back within minutes, send the plan with the lead's proposed point and say the candidates will follow.
The author is never the first verifier of a candidate point.
1. Candidates: when the author has not fixed the perception, write up to five distinct ones, each as one belief sentence, one feeling and its chain of four to six links.
2. Readers: at least three cold readers per candidate, each playing the actual reviewer (for a grant, the funder's stated reviewers), seeing only the candidate.
3. Scores, 1 to 5 each: LOGICAL (each link follows; no jump the reader must supply), EXCITING (the stakes feel real and large), CURIOUS (the reader wants the result and can say what they would want to know), MATCH (the reader's one-sentence restatement matches the intended belief).
4. Pass: every reader gives 4 or more on all four. Ties go to the higher minimum score.
5. Show the author only passing candidates, ranked, each with its median scores and one reader quote. None pass: repair and rerun; never send a failing one.
6. The finished text: the fresh reader of "The fresh reader" above, where one is due. No second panel.

## When the author says it is bad

The same turn, the seat that heard it does four things.
1. Write the author's exact words in `DECISIONS.md`.
2. Add one line to `CHECKLIST.md` ([form](../templates/CHECKLIST.md)), or raise its count.
3. Repair the text.
4. Tell the partner. Rerun step 3 of the send check on every part already drafted.

How to repair, and what the author then sees: the team file, "One message". The plan alone: "The plan" above.

- "Calls it bad": the author rejects a version just shown, or an approved part or section, and names no fault a repair can fix. Back to the plan alone. A named fault gets one repaired version instead (the team file, "One message").
- "The same fault": the words name a fault a `CHECKLIST.md` line already names.
- The same fault on another part: handle the part normally and raise the count.
- Nothing enters the skill during a part. What happens at the section's end: [`MAINTENANCE.md`](../MAINTENANCE.md).

## Principles

### PLAN-BEFORE-PARAGRAPHS  Agree the point and the parts of a section before any paragraph
Principle: a section, like a paragraph, needs a point, a logic and the information that carries it. Decide what each part teaches and how the reader should feel before drafting.

### PARAGRAPH-CARD  Five elements settled before writing, the same five checked after
Principle: perception, concept, logic, information and prose are made explicit before writing and checked after. Role and frame are working lines.

### SEND-CHECK  Nothing reaches the author unverified
Principle: every step, from perception to prose, passes verification against the standard before the author sees it.

### CHECK-ON-ARRIVAL  Measure every draft when it arrives; the author sees it after it converges
Principle: check each draft as it comes; send it once it passes or the lead judges it good enough.

### CHECKS-IN-WRITING  Checks are part of writing; small checkers may run in parallel
Principle: sentence, paragraph and section checks belong to writing itself. Quick helpers may run mechanical checks in parallel.
