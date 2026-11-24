# Type sheet: theory results

## When this applies

- A results, comparative-statics, equilibrium or design-implications section of a theory paper, or any paragraph in one.
- Not setup, empirics or figures: their own sheets.
- Mathematics, a coauthor's section, a part the author calls fine: [HOW_WE_WORK.md](../HOW_WE_WORK.md), who writes each type of text.

## The standard

Hedging, register, one name per object: [STANDARDS.md](../STANDARDS.md). The rules for the two registers live here.
Invented examples below use one imaginary study: outpatient clinics that book more patients than they have slots.

### POINT-FIRST  A results section makes the paper's point

Principle: first have a logical point; the section exists to make it. Each proposition is stated cleanly, light on notation, accurate but not exhaustive.

### RESULT-NOT-TECHNICAL-NOTE  Walk the economics, not the derivation

Principle: the reader should understand the result, not watch the math being solved. The math goes to the appendix unless it is essential; the main text gives the trade-off and a graphical illustration.
- Avoid heavy formalization and heavy notation.

### TWO-REGISTERS  Main text is for the broad reader

Principle: a technical note is one register; the main text is a second register for a broader audience.
- A results subsection does not explain what the assumptions do, list the strategies they eliminate, or rank strategies the result never uses. Their rationale belongs with the setup or the technical appendix.
- Removing inventories and assumption defences must keep the economic trade-off and each channel needed to understand the finding.
- Order: what a choice means in the game, then the picture, then the solved object. Invented: "the clinic picks how many patients to book per session; the figure shows expected cost against that number; the cost-minimizing number is b*."
- The figure carries the trade-off. The prose points at it and does not duplicate it.
- Name the agent's objective in plain words ("the clinic minimizes its expected cost per session"), not the name of the mathematical device that solves it.
- A formula need not be shown: say which term is positive, which is negative, and why.
- Less hedging. Qualifications that protect precision belong to the technical register (appendix and notes).
- The broad register deletes the technical payload. It never moves it into main-text discussion.

### THEOREM-LANGUAGE  A statement names the economic object

Principle: a formal statement uses the field's economic language. Write "there exists a unique optimal booking level", not "the objective has a unique minimizer".
- Every formal statement, locked ones included, is checked against published theorem phrasing (see [published.md](../examples/published.md)). A defect in a locked statement is flagged for the author's approval, never silently kept. Who writes the fix: [HOW_WE_WORK.md](../HOW_WE_WORK.md).

### NOTHING-BEFORE-DEFINITION  No text before a definition

Principle: text placed before a definition is redundant; remove it.

### CS-FORMAL  Comparative statics are stated results, signs plus reasons

Principle: a comparative static is itself a lemma or proposition, readable at once, and it covers every variable the paper tabulates.
- One enumeration per object. Each item says increasing or decreasing in words, plus the cause.
- State what is held fixed once. No displayed partial derivatives in the main text.
- The claim sentence carries what is held fixed and where it holds, in short sentences. Invented: "Hold the other parameters fixed. A higher miss rate raises the optimal booking level. A higher cost of waiting lowers it."
- Coverage default: the proofs cover every primitive or name the ones deferred; the main text carries only what the point needs.

### DECOMPOSITION-ECONOMIC  A decomposition names each payment and its reason

Principle: say "this decomposes into these payments", explain what each payment is, and why each term has its form.

### NO-ONE-SENTENCE-PARAGRAPHS  No paragraph of one sentence

Principle: a single sentence does not make a paragraph.

### POINTERS  Say where the proofs are once; reference only what no result states

Principle: state the point directly instead of sending the reader to an appendix. A claim that no numbered result states keeps its reference.
- Say where the proofs are at most once, in one sentence at the end of the Results opening's second paragraph. Never a pointer after each result; never its own paragraph. Some authors prefer no such sentence at all; the plan offers it in one line.
- A main-text claim whose formal statement lives only in the appendix gets one pointer for the whole paragraph.
- No forward pointers in prose ("Lemma 1 solves this", "see Section 3.5") and no pointer inside a definition.
- A numbered result gets no pointer to its proof.

### NEVER-BY-ASSUMPTION  Never say a result holds by assumption

Principle: an assumption is disclosed where it is made; a result is not described as holding "by assumption".

### FRAME-FROM-RESULT  Surprise, confirmation or test, chosen from what the result is

Principle: an opening has a role. Choose the frame from the result: a surprise, a confirmation or a test. A result that is bad but expected is not framed as a surprise. A question is often a good opening.

### STANDS-ON-ITS-OWN  A results section restates the stage, the actor and the formal object

Principle: the setup and the results are separate, but the results section gives enough context that the reader does not lose track.

### RESULTS-DETAILS  Rules for a results section

- No qualifier the setting already implies ("in the baseline model", "stationary symmetric" on a threshold policy). Where a later section relaxes the object, one footnote says how.
- A load-bearing equation never floats. It becomes a named lemma or proposition, and the explanation follows it.
- Merge results that answer one question. Existence, uniqueness and ranking are one theorem: "There exists a unique X ... . [ranking]".
- A subsection opening is a paragraph, never itemized. Inside it, one sentence says what is solved ("We now solve for the clinic's booking level"). It does not recap earlier subsections. Example: [unit-roles.md](../references/unit-roles.md), section 1.
- Say a condition by what the agents do, case by case. Invented: "when a patient can rebook within the week ...; when she cannot ...", never an abstract predicate ("whether the outside option binds").
- Do not justify what the reader never doubted. Do not reconcile two forms of a formula unless the reader would be confused without it.
- The explanation after a result does not repeat the result or the preview.
- A definition's title is its object's name ("Equilibrium"); qualifiers go in the text.
- Split partial from full equilibrium. A design comparison ends in a formal result comparing equilibria.
- Verification detail goes to footnotes; the main text keeps the logic. Step-by-step text with no focus fails.
- A rule stated in the model is not restated where it is used.

### DESIGN-SECTIONS  Rules for design, extension and implication sections

- Open simply with the question the section answers, in the introduction's own terms, then the one-line answer. No technical foundation in the opening. Invented: "Why do reminders shorten waits in some clinics and not in others? The answer lies in whether the clinic revisits its booking level."
- Parallel alternatives are a numbered list; an argument is not. Each item keeps all its content (mechanism, implication, examples, citations), only cleaner.
- A per-case characterization is a Lemma, not a Definition.
- Assume a degenerate case away in the statement, with a footnote on why.
- Weight on the implications. Side conditions, bounds and caveats go to footnotes.
- No section pointers in parentheses and no "in our model" hedge. Accurate scope stays ("Part of the answer").
- No helper symbol for one use.
- The explanation after a comparative result is its causal chain in a few words. Invented: "higher miss rate, more empty slots, more bookings". Side comparisons go to a footnote.
- Name the baseline plainly ("our baseline model's rule"), not by a section range.
- Implications and suggestions, not a second tour of examples.
- Define a result's notation in words, in a short paragraph just before it, not inside the proposition.
- After a comparative result, say plainly who wins on each dimension, before any mechanism.
- A few direct sentences: what to do and why; at most one short clause of scope; caveats to footnotes.
- Visuals: [paper-frame.md](paper-frame.md).

### PLACEMENT-AND-MECHANISM  Placement, comparison and mechanism

- Headline first: lead a main-text result with its central economic conclusion and explain it right after. Minimal definitions may precede a concise theorem; its intuition can follow.
- Place a characterization equation where it answers the economic question just explained.
- A short roadmap earns its place by explaining how the argument reaches the result, not by listing results or section labels.
- Theorem statements and appendix proofs keep every truth condition, admissible policy class, dependency and distinction that makes the claim valid.
- A result relies on the global setup; a local condition is stated only when it changes the reading.
- Name compared objects directly. Keep a comparison apart from a separate question of which option agents choose; a separate selection result earns space only when it advances the paragraph's question.
- Explain the intermediate economic steps. Do not compress them into one slogan ("reminders help patients").
- Fluency connects steps rather than giving each its own sentence: causal or conditional clauses, varied cadence, stable referents, no mechanical restarts, no invented synonyms. The logic skeleton fixes coverage and order, not sentence boundaries.
- A payment decomposition explains who pays, for what, and how the choice changes that payment. A label is not the explanation.
- Simplifying exposition does not authorize deleting substance. State the comparative statics as a corollary after the optimal-policy proposition, then explain the forces below it. Prose does not replace the formal result. A clear but materially incomplete passage fails.
- Distinguish the definition the reader needs, the result itself, and the calculation that establishes it. A closed form earns main-text space only when it is the result or shows the force.
- Keep policy details in the main discussion when they explain an incentive, cost or design trade-off. Move only implementation history and technical support that interrupt it.
- When comparing institutional rules, first explain the concrete decision each rule makes, with an example, before the statistic used to compare them. A rule's name does not define it; a ratio does not explain a mechanism.
- Keep a rule's definition, example and mechanism close together. Develop the next rule through the comparison it adds.
- If formalizing the first cases would interrupt a comparison, give the reader a complete verbal map first. Use headings for real changes in the reader's task, not as a cure for difficult prose.
- A proposition comparing several rules includes all established cases, even ones that follow from definitions.

## Roles of the units in this type

| Unit | Job |
|---|---|
| Subsection opening | The new question: a question, a surprise on a stated expectation, or a recalled mechanism |
| Pre-result orientation | The economic problem, then the exact object; nothing if already supplied |
| Formal statement | Central claim first, naming the economic object |
| Explanation after | The mechanism (actor, choice, force), never the result restated |
| Comparative statics | Sign in words plus cause; held-fixed once |
| Design implications | What to do and why |
| Bridge | The tension the next part answers |

## Workflow, step by step

Every step not stated here: [HOW_WE_WORK.md](../HOW_WE_WORK.md) and [unit-plan-card-gate.md](../references/unit-plan-card-gate.md).

1. Before its plan, each writer writes the subsection's economic conclusion in one sentence and tags each available result main, supporting or appendix.
2. Each card's chain link names its lemma, proposition or equation tag.
3. A change to a symbol, a formula or a condition, and a part that waits on it: [paper-model-setup.md](paper-model-setup.md), "Workflow, step by step" and "Different from the general case".
4. When one displayed equation carries the subsection's point, consider stating it as a corollary and explaining it in the sentences right after. A corollary is a formal statement; who writes it: [HOW_WE_WORK.md](../HOW_WE_WORK.md).

## Examples (where)

- [unit-roles.md](../references/unit-roles.md): an opening that carries a surprise, the opening of a derivation, the means, the explanation after a result, the part that carries the point.
- [published.md](../examples/published.md): openings, a surprise after its benchmark, a comparative static with its reason.

## Checks before the author sees it

Which versions, and where each line is written: the send check in [unit-plan-card-gate.md](../references/unit-plan-card-gate.md).
Mathematics untouched: the line under this heading in [paper-model-setup.md](paper-model-setup.md).

| Standard | Who | How | Pass |
|---|---|---|---|
| POINT-FIRST | Lead | Map each unit to the plan's point | Every unit serves the point; units with one job are merged |
| RESULT-NOT-TECHNICAL-NOTE, TWO-REGISTERS | Lead | List the main-text displays and helper symbols | Each is the result or shows the force; no restriction restated |
| THEOREM-LANGUAGE | Lead | Read the first clause of each statement | It names an economic object |
| NOTHING-BEFORE-DEFINITION | Lead | Read the text before each Definition | No preamble |
| CS-FORMAL | Lead | Read each comparative static | A numbered result; sign in words plus cause; held-fixed once; every primitive proved or deferred by name |
| DECOMPOSITION-ECONOMIC | Lead | Read each decomposition | Each term is named as a payment, with who pays and why; a functional form has its one-line reason |
| NO-ONE-SENTENCE-PARAGRAPHS | Lead | Count the sentences of each paragraph | None has one |
| POINTERS | Lead | `grep -n "Appendix\|ref{\|see "` on the passage | A reference only for a claim no numbered result states; no forward pointer; none inside a definition |
| NEVER-BY-ASSUMPTION | Lead | `grep -n "by assumption"` | No hit |
| FRAME-FROM-RESULT | Lead | Compare the opening's frame with the result | No confirmation written as a surprise |
| STANDS-ON-ITS-OWN | Fresh reader when one is due; else the lead | Read the passage without the setup | The reader states the stage, the actor and the object solved |
| RESULTS-DETAILS, DESIGN-SECTIONS, PLACEMENT-AND-MECHANISM | Lead | Read the passage against each bullet of the three blocks | None violated, or the reason written |

## When the author says it is bad

Follow [unit-plan-card-gate.md](../references/unit-plan-card-gate.md). Then:
- Name the layer first: wording, missing step, emphasis, purpose, architecture or scientific scope.
- A scientific-scope fault goes to the author and then the math author, never into a rewording.

## Gaps

- No rule on a results section's length. Meanwhile: no longer than the current text unless the plan says why.
- The comparative-statics coverage default was never confirmed by the author. Meanwhile apply the default under CS-FORMAL.

## Craft notes (trial)

- Keep a short calculation when it reveals the force; leave routine arithmetic in the proof.
- A same-parameter comparison is not a comparative static; a local peak is not a global one.
