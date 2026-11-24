# Type sheet: title, abstract, conclusion, related literature, appendix, figures, footnotes

## When this applies

- A paper's title page, abstract, conclusion, related literature, appendix, figures, tables, footnotes and citations.
- Related literature: if the project has a separate literature-search procedure, it owns the source set; this sheet covers the wording.
- The team, the plan, the versions, the send check, approval, applying and the record are not stated here. They are in [HOW_WE_WORK.md](../HOW_WE_WORK.md) ("the team file") and [unit-plan-card-gate.md](../references/unit-plan-card-gate.md) ("the unit file").

## The standard

### ABSTRACT-CORE  An abstract hits the core

Principle: an abstract states the core of the paper without filler.
- The central policy implication, not a list of every case.
- No catalogue of caveats.
- No "quasi-experiment" without its identification argument.

### ABSTRACT-LENGTH  The venue sets the limit

Principle: the limit is the target venue's, counted at the submission build. No venue named: no limit applies; show the word count.

### CONCLUSION-SHORT  One or two paragraphs

Principle: a conclusion is one or two paragraphs, held to the same standard as the body.
- It states no new result. An implication is allowed when it follows from a stated main-text result and is sized to it.
- In a conclusion the author calls fine, small fixes are not offered; a large cut may be (see MATERIAL-NOT-WORDING in [HOW_WE_WORK.md](../HOW_WE_WORK.md)). A new request to rewrite it reopens it: Workflow step 4.

### APPENDIX-JUST-PROOFS  A proofs appendix is just proofs

Principle: the model is self-contained in the main text, and the proofs appendix holds proofs. Never hide a model detail in the appendix; it goes in the main text or a footnote, or it is not needed.
- Trial: every result the appendix proves is a visible statement before its proof.

### FEWER-FOOTNOTES  A footnote must justify its existence

Principle: a point not important enough for the text must still earn a footnote; otherwise cut it.

### PAGES  No white gaps

Principle: break text into paragraphs without jargon, and leave no large white spaces.
- No half-empty page and no large white gap. The layout check: [paper-build-checks.md](../references/paper-build-checks.md), the built PDF.

### ESSENTIAL-EXHIBITS  Only essential tables and figures stay in the main text

Principle: in a page-limited submission, keep only the tables and figures that must stay; the rest go to the appendix.

### FIGURES  A figure shows the mechanism, after its inputs

Principle: a figure shows the mechanism, which a numerical magnitude does not show. It comes after the objects it plots are introduced. If no figure can show the mechanism, use none.
Invented example: a figure of the average wait against the miss rate comes after the text defines both, and it shows where waits start to lengthen.
- No label over a line. Regions visibly distinct.
- One visual per comparison. Show the result's actual shape.

Further rules in force:
- Title page: title and abstract on their own page (`\newpage` before the introduction).
- Citations: cite the published version, not the working paper, when one exists. Attribute and check every industry number. Re-check every institutional fact by a second method.
- Whether a contribution paragraph closes the related literature is a plan option, never a default.

## Roles of the units in this type

| Unit | Job |
|---|---|
| Abstract | Question, core force, answer, the test; no model tour |
| Conclusion | Answer to the paper's tension, what changes in our understanding, a warranted implication; no new result |
| Related-literature opener | Names the strands and stops |
| Strand paragraph | What the closest work delivers, then the remaining difference |
| Footnote | A limit at the place it changes interpretation |
| Figure | One inference the viewer recovers without decoding |

- The abstract and the conclusion are two units. Each has its own plan. Live: its own plan message. Prepared: both plans go in the first message (the team file).
- Related literature: a part is the opener, one strand, or a contribution paragraph the author chose. A strand is one paragraph, or two (what is established; what we add).
- Related literature: the part that carries the point is the strand paragraph on the closest work, unless the plan names another.

## Workflow, step by step

The general workflow: the team file and the unit file. This sheet adds:
1. Abstract and conclusion: draft against the current body.
2. An approved body unit later changes a claim the abstract or conclusion repeats: name that passage to the author with a repair. Never reopen approved text silently.
3. Conclusion: its plan says in one line whether the paper should have a conclusion at all, with a recommendation.
4. On reopening: a new request from the author to write or rewrite the abstract or the conclusion reopens that unit, whatever was said of it before.
5. The outside review: the team file. This sheet adds nothing to it.
6. Related literature: word claims only from the reviewed source set. Strand maps and unpruned search lists are inputs, never the wording source.
7. A cited paper with no local copy: try to obtain it. Still missing: a citation already in the manuscript at the base version stays, unstrengthened; write "source not read: no local copy" in the message's "Not checked" line, not in the text. Any other claim on that paper is left out and named in the message as waiting.
8. The author says an abstract or conclusion is bad: first check whether the body changed under it. Then the unit file.

## Examples (where)

- Abstract, conclusion and related literature: [published.md](../examples/published.md), by role.
- Invented paragraph roles: [unit-roles.md](../references/unit-roles.md).

## Checks before the author sees it

These rows are this sheet's part of the send check (the unit file). The number trace and the check of a quotation against its page are in the unit file's source check.
A row marked (apply) needs a build. It runs after the text is applied, or on a prepared reading copy, with [paper-build-checks.md](../references/paper-build-checks.md).

| Check | Who | How | Pass |
|---|---|---|---|
| ABSTRACT-CORE | Lead | Tags each sentence's job | Question, force, answer; no inventory, no caveat list |
| ABSTRACT-LENGTH | Lead or helper | `wc -w` on the abstract text | The count is shown; within the venue's limit at the submission build |
| Abstract and conclusion match the body | Lead | Finds each claim and number in the body | Each is in the body; none is stronger than the body |
| CONCLUSION-SHORT | Lead | Counts paragraphs; matches each claim to a body result | One or two paragraphs; no new result |
| APPENDIX-JUST-PROOFS | Lead | Reads the appendix headings and the text between proofs | Proofs only; no model rule housed there |
| FEWER-FOOTNOTES | Lead | Asks of each footnote "what is lost if it is deleted?" | Each kept footnote changes interpretation |
| FIGURES | Lead | Renders the page and reads the figure with its text | It shows the named object; it comes after its inputs; no label over a line |
| ESSENTIAL-EXHIBITS | Lead | Lists the main-text exhibits | Each one is needed there |
| PAGES (apply) | Lead | The layout check of [paper-build-checks.md](../references/paper-build-checks.md) | No half-empty page, no large white gap |
| Title page (apply) | Whoever applies | Looks at page 1 of the build | Title and abstract alone on it |
| Citations | Lead | Reads each new citation's bibliography entry | Published version cited; industry numbers attributed |
| Contribution paragraph | Lead | Reads the plan | Offered as an option. Live: in the text only if the author chose it. Prepared: shown as a choice that is the author's |
| Citation exists | Lead, or a helper | The bibliography file, a DOI registry lookup, a title search | Found; "fabricated" only if all three fail |
| Source set only (related literature) | Lead | Matches each cited paper to the reviewed source set | Every paper this job adds or rewords a claim about is in the set. A citation outside the set, already in the manuscript at the base version, stays unstrengthened and is listed in the message |

## Gaps

- No accepted conclusion is filed. Meanwhile, in order: the rules above; the published conclusions; the conclusion role. The message says "no accepted example for this role".
- No accepted related-literature passage is filed. Meanwhile: the published quotes.
- Venue unnamed. Meanwhile: show the word count and say "no venue named, so no limit applied". A named venue: look up its limit; do not ask the author.

## Craft notes (trial)

- Omitting a conclusion is an option: Duffie, Gârleanu and Pedersen (2005) has none ([published.md](../examples/published.md)).
