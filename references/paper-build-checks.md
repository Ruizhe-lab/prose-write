# Paper build checks

Mechanical checks on a built paper and on pasted mathematics.
Who applies, when delivery is allowed, what counts as delivered: [`HOW_WE_WORK.md`](../HOW_WE_WORK.md) ("the team file"), "Approval and applying". Who writes mathematics: there, "Who writes, by type of text".

## When this applies

- After every apply and before every delivery, live or prepared: section A.
- Mathematics pasted from the math author: section B.
- A prepared reading copy, before the ready notice: A.2, C and D.1, on the job's working copy.
- A submission build, only when the author asks for one: sections A to D.

## A. After every apply, before every delivery

Whoever applies runs these on the manuscript files, after applying and before delivery.
They are not run on a draft shown as versions. Before a version is shown, the scope judgment of the send check covers mathematics.
A fail: deliver nothing. Say so in one line, with the check that failed.
1. Statement check. Compare every labelled formal statement (theorem, proposition, lemma, definition) in all manuscript files against the base commit. Use a script if your project has one; otherwise extract and diff the statements. Base commit: the job's, from `DECISIONS.md`, or the commit before the edit. Pass: no labelled statement is missing, changed, duplicated or added, except a new statement from the math author named in advance. Nothing matched counts as a fail.
2. Clean build from the project root, as the destination builds. Pass: 0 errors, 0 undefined citations, 0 undefined references.
3. Markup. Render the changed page to an image and look. Pass: changed text shows in the project's pending markup.

## B. Pasted mathematics

- The math author (the team file, "The seats") sends OLD/NEW pairs in a fixed comment form (`% FILE:`, `% OLD-BEGIN` ... `% OLD-END`, `% NEW-BEGIN` ... `% NEW-END`). Every brief to the math author asks for this form.
- Apply the pairs mechanically: a dry run first, then the real run. Pass: every OLD is found exactly once; otherwise nothing is written.
- Never retype or reflow a pair. All pairs or none. No other applier.
- Then run A.1.

## C. Words, symbols, pointers

1. Term check. Each paper keeps one table: object, its one term, retired synonyms, retired symbols. Search every retired entry in the sources and in the text of the built PDF (statements, appendix, captions, legends): case-insensitive for words, exact for symbols. Pass: zero hits. A new name must not equal another object's name. After a rename, check the new name is defined at first use. Check terms against the field's standard term lists your project keeps.
2. Location and symbol claims. Before an instruction names a file, proof, equation, label or symbol as the home of something, search the live files for it. Pass: the search finds it, and a new symbol is not already used for another object.
3. Dashes. Search the paper prose for `---` and `—`. Pass: zero outside quotations and mathematics. The rule: [`STANDARDS.md`](../STANDARDS.md).
4. Banned frames. Search "Failure of", "should therefore", "can look for". Pass: zero, or each kept with a written reason.
5. Symbol budget. Pass: every defined symbol is used later, or listed as flagged.
6. Hidden results. Search the appendix files for `\refstepcounter`. Pass: no hit outside a visible theorem-like environment.

## D. The built PDF

1. Layout. Look at every rendered page of the changed section. Pass: no half-empty page and no large gap from forced placement (`samepage`, `minipage`, `[H]`, forced breaks). Remove the forcing command, never the content.
2. Clean-PDF sweep, on the submission build with markup off. Extract the text, then search "pending", "TODO", "??", tool names, identifying data sources, retired terms. Pass: zero hits.
3. Venue fit, only for a submission. Build the clean anonymized PDF in the venue's template, every float placed. Measure by the venue's own counting rule. Report total pages separately. Pass: within the limit on that build. A saving is claimed only from a rebuilt PDF. What stays in the main text: [`types/paper-frame.md`](../types/paper-frame.md).

## Checks before the author sees it

A row runs only when "When this applies" calls its section. None runs before a version is shown.

| Check | Who | How | Pass |
|---|---|---|---|
| A.1 to A.3 | Whoever applies | Above | All pass, written in `DECISIONS.md` with the commit |
| B | Whoever applies | Dry run, then run | Every pair applied, or none |
| C.1 to C.6 | Lead or helper | Searches above, output saved in the queue folder | Zero hits, or each hit explained |
| D.1 | Lead | Page images | Every page looked at; none half-empty |
| D.2, D.3 | Lead | Text searches; page measure | Zero hits; within the limit |

A script counts as a check only after it has failed on a planted defect.

## When the author says it is bad

A layout or term complaint: fix the page or the term, then rerun the check that missed it. Recording the words: [`unit-plan-card-gate.md`](unit-plan-card-gate.md), "When the author says it is bad".

## Limits

- No default home for the term table. Meanwhile: search the paper's notes for one; if none, create `TERMS.md` in the record folder and name it in `DECISIONS.md`.
- In trial: retired symbols in the term table, the PDF-text sweep, the rename check, the comment-pair form, the hidden-results search.
