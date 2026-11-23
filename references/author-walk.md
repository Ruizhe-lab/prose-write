# The author walk: a first pass that lands close

Use this when an author goes through a paper with one or two writers, part by part. It adds four things to the [runbook](writing-runbook.md): a scope agreed by ownership, a plan for each section before its paragraphs, a paragraph card that names the unit's role, and a send gate. For an isolated edit, use the paragraph card (stage 3) and the send gate (stage 4) only.

## What the evidence says

This procedure was written after one long revision in which an author corrected the writers paragraph by paragraph, and was then tested once: a blind replay on nine held-out passages of the same paper, the earlier procedure against this one, scored against the text the author had approved. This procedure came closer in seven of nine and kept scope and sources where the earlier one broke scope once and changed the meaning of a footnote. It did **not** make an isolated first pass close: in five of nine passages the judge still expected the author to ask for a different approach, nearly always about the frame of the first sentence, a restructuring, or a fact from elsewhere in the paper. Those are plan decisions. In the revision itself, once a section plan was agreed, its parts passed in one or two rounds. So stage 2 carries the result. Treat "close on the first pass" as a target to measure on your own work: record how many parts the author approves at first showing.

One paper, one author, model judges. Adapt before you rely on it.

## Why first passes miss

| Miss | What prevents it |
|---|---|
| Paragraphs drafted before the section's point was agreed | Stage 2 |
| A unit given its neighbour's job (an opening that explains the whole mechanism) | Stages 2, 3 |
| A surprising result announced, not built; correct facts in a flat row | Stage 3 |
| A mechanism stated loosely, or a label used where the logic should be | Stage 3 (chains before prose), stage 4 |
| Swinging between cutting what the reader needs and keeping every sentence | Stage 3, stage 5 |
| Too many words, symbols, recaps and pointers | Stages 3, 4 |
| Restyling text the author did not want touched | Stage 1 |
| The author waits; "before" is an old proposal; unverified text is sent | Stages 4, 5, 6 |

## Roles

- **Lead**: owns the plan, the card, the message to the author and the decision record, and verifies before sending. One canonical writer applies changes.
- **Second writer**, where available and preferably a different model or person: plans and drafts independently, checks the lead's draft against the card, prepares later units, and audits sections outside the full walk.
- **Fresh reader**: sees only the joined passage, its neighbours and the rendered exhibits.
- **Script** (`scripts/card_check.py`): the mechanical part of the send gate.
- **Author**: confirms the scope, decides each section's point and order, approves each part.

## Stage 1. Scope

Read the whole paper and the author's own earlier writing. Then propose, per section, who wrote it and a depth:

- **Full walk**: the author's own sections and those that carry the paper's point.
- **Material only**: a coauthor's sections and anything the author calls fine. Bring only a wrong or inconsistent number, a claim stronger than its exhibit or formal result, a contradiction with a revised section, a broken reference, or a step a reader cannot follow, each with location, quoted text, evidence and the smallest fix. Style is left alone.
- **Cut plan**: only when asked. Keep in the main text each finding the introduction relies on, in one paragraph with its numbers; move exhibits and detail to the appendix intact; delete nothing unless the author says so.

*Pass:* the author has confirmed the depth for each section. A declined class of change is recorded and not proposed again. A material-only section goes straight to the evidence audit.

## Stage 2. The section plan

Before any paragraph of a section, give the author a plan readable in a minute:

1. **The point**: the one thing the unit exists to make the reader believe. In a results section the solving is the means and the point is the end; they stay in one unit and the point gets the room.
2. **A title**: two or three noun-phrase options and a pick.
3. **The parts, in order**, one line each: what the reader **learns**, how the reader should **feel**, the part's **role** and the **frame** of its first sentence, and whether the current order is kept or restructured.
4. **What is compressed**, moved or cut, and which displays, symbols and figures stay. A display stays only if the text reads it for the point.

Where there is a second writer, it writes its own plan unseen; the author sees one plan and the differences.

*Pass:* the author has decided the point and the order. No paragraph that depends on that decision is drafted before it; evidence, source checks and independent units can be prepared meanwhile.

## Stage 3. Calibrate, then the paragraph card

Read the matching role in [unit roles](unit-roles.md), and any accepted and rejected examples your project has saved for this author. Then state, before drafting:

1. **Perception**: the one thing the reader should believe afterwards.
2. **Concept**: the idea or object the reader must understand to get there.
3. **Logic**: the chain of steps, the link to the paragraph before, the hand-over to the next, and what is emphasized.
4. **Information**: the facts, numbers, definitions and results the chain needs, each with its source, and nothing else.
5. **Prose**: each item written once, in the register of the section.
6. **Role and frame**: the unit's job and the kind of first sentence that job calls for.
7. **Chains as bullets, checked against the source**: for a surprise, two chains, what the reader expects (the standard logic stated exactly) and what the paper delivers (each link with the result or table cell behind it). Do not answer a mechanism question from memory.

Drafting defaults:

- Open from the point of the unit before, then turn to this unit's job.
- Where several cases follow from one claim, find that claim and open with it.
- A surprise is built as a rise, one step per sentence: what one expects; it is absent, and things even look better; yet there is a harm, precisely because of what looked good; who gains.
- Every sentence hands over from the one before. The test is that you can name the relation between each adjacent pair and point to the words that carry it. A sentence giving evidence for the previous one needs no connective.
- List what the reader must know here, order it, and write each item once. Keeping information does not mean keeping the order; cutting does not mean dropping a reason.
- Shorter than the original unless there is a reason: an identity the argument does not use goes to a footnote; no preview of a result stated a few lines later; no symbol or cross-reference that is not used again.
- An equation that carries the point gets a home: a short formal statement, explained after it. A statement drafted by a writer restates what the scientific author has already derived and is flagged for that author.
- Name people, not pronouns, when two actors share a pronoun.
- End on the plain conclusion the reader should carry out. Tighten last.
- In a material-only section the answer is one line: no change, plus at most one check for the owner.

## Stage 4. The send gate

Nothing reaches the author before it passes.

Mechanical: `python3 scripts/card_check.py draft.txt [--rise] [--before before.txt] [--actors she:buyer,she:seller]`. Record each marker as fixed or explained. The script finds mechanical faults only; in the test above it did not separate accepted drafts from rejected ones, because rejections were about role, logic and perception.

Judgment, on the text itself:

1. **Perception**: write the sentence the reader should believe, and check that the text alone delivers it. For a surprise, why it is surprising and why it matters are both in the text.
2. **Role**: the unit does its job and no other.
3. **Logic**: each chain link is present, in order; the first sentence carries the frame; both ends link.
4. **Information**: each item is needed, sourced and stated once; nothing needed is missing.
5. **Source**: each claim is checked against its result, table cell or document, and the check is written under the draft. A claim no numbered result states keeps its reference.
6. **Scope**: mathematics untouched; others' text touched only as the scope allows.
7. **Prose**: tight means no clause can be removed without losing an inference or a fact the reader uses.

For the unit that carries the paper's point, and where the writers disagree, a fresh reader says unaided what it now believes, why it follows and what remains unshown. Compare that with the intended claim and repair the missing inference.

## Stage 5. The message and the correction loop

One part per message, self-contained: the goal, the step and what comes next; the short card; the paper's current text in full; the proposed text in full; what happened to each piece; the source check; a recommendation. Show two versions only when they build the perception differently, and then offer a mix. Reply first; apply and build in the background; have the next unit prepared.

On a correction:

1. Say what was wrong in a sentence or two, then show the repair. Repair what was named; do not swing to the opposite.
2. If it concerns logic, show the chain as bullets before new prose.
3. Record the lesson in the project note and pass it to the other writer in the same turn.
4. If the same kind of correction comes twice, return to stage 2 for that unit. The plan is wrong, not the sentence.

A message with one correction is not approval of the rest. Ask in one line, or state your reading and make it easy to reverse.

## Stage 6. Apply, assemble, hand over

Follow the runbook for application, rendering and delivery authority. Record the author's acceptance against the candidate that was shown. Keep prepared, shown, applied and delivered as separate states; refresh a prepared draft against the current text before showing it. After a section is approved piece by piece, read the assembled whole once and remove what the pieces repeat. At the end, prepare one note for coauthors: what changed in whose section, what needs their confirmation, and each material issue with its evidence. Whether and by whom it is sent is the author's decision.

## What not to generalize

How a surprise is paced, whether derivations open with a question, and how hard to cut are one author's taste. A confirmation is not written as a surprise. A coauthor's section is not restyled. A light edit is often the right answer. Keep your own author's accepted and rejected examples in the project, not in a shared copy of this skill.
