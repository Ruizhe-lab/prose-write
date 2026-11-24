# Paper: model setup, assumptions, equilibrium definition

## When this applies

- You write or revise the section that states a paper's model. Results: [paper-results.md](paper-results.md).
- A symbol, a formula or a formal statement: who writes it is in [HOW_WE_WORK.md](../HOW_WE_WORK.md), who writes each type of text.
- A coauthor's section, or a part the author calls fine: the same place.

## The standard

Invented examples below use one imaginary study: outpatient clinics that book more patients than they have slots.

### SETUP-APART  One thing at a time; setup apart from derivation

Principle: the setup states the game once; how a quantity is computed belongs to the results. Each paragraph teaches one thing.
- Model setup and results are two different sections, always.
- A computation goes just before the proposition that uses it.
- A named cost object may appear in the setup by name and meaning only.
- A figure in the setup can replace a derivation, not accompany one.

### SAY-IT-PLAINLY  Openers and roster in plain words

Principle: say what the section does and who is in it, in plain words.
Invented example: "There are two kinds of agents: a clinic and its patients", not "The model links two node types". Say "uncertain attendance", not a coined label for it.
- Counting openers and template scaffolds: [STANDARDS.md](../STANDARDS.md).

### MINIMAL-NOTATION  Every symbol earns its place

Principle: keep only the notation the logic needs. Ask of every symbol whether it builds the reader's picture.
- Generality that no result uses is cut. Say "a patient's cost of waiting is a constant" when nothing varies it.
- A closed form not used again goes to a footnote or the appendix.

### LESS-DENSE  Reduce the reader's mental load

Principle: a referee skimming the section finds it simple, clean and easy, and still accurate.
- Density is a defect independent of logic. Judge it by a cold read, not by counts.
- Finer sections come first. Other relief (figures, footnoted derivations, landing lines) is proposed to the author as options, never imposed.
- A texture the author has approved is kept.

### KEY-STATE-DISPLAY  A key state object gets its own displayed equation

Principle: when a key state variable is introduced, give it a numbered display.
Invented example: the number of patients who attend beyond the available slots gets its own equation where it first appears.
- Cutting notation is not a ban on useful formulas.

### CHOICE-HAS-REASON  A modelling choice states its reason from the question

Principle: a modelling choice says what it matches in practice and what it lets the paper show.
- No description of the choice's shape, and no contrast with another design.
- When a coauthor asks "why X, not Y", the paper gives the reason for X, not the contrast with Y.
- A tractability device (a distribution, a clock): say what the choice buys.

### COIN-ONLY-IF-REUSED  Name a concept only if the main text uses it again

Principle: a coined term must be used again and again; otherwise describe it in plain words.

### EQUILIBRIUM-DEFINITION  One short definition, each agent's condition in words

Principle: the equilibrium is one short definition with no preamble.
- One Definition titled "Equilibrium". It states every agent's condition in words.
- Payoff functions live in the running text.
- A symbol used only later is introduced where it is used.
- An argument fixed by the surrounding clause ("fix the booking level b") is not carried on any symbol in scope.
- Use the bare canonical name when the published literature has one. Write "Equilibrium", not "Capacity-constrained equilibrium". The qualifier's content belongs in the body. This holds for definition titles, section titles and object names.

### STATE-THE-GAME-FORMALLY  Plain is not thin

Principle: state the game formally enough that the reader sees what is being solved. Cleaner prose keeps the key information; it need not keep the same logic or every detail.

### SETUP-PARAGRAPHS  Connected economic paragraphs; details placed where needed

Principle: develop connected economic paragraphs and introduce notation when needed.
- State the actor and the execution event explicitly.
- Name the familiar object and its function in an analogy.
- Keep supporting examples and institutional matching in the appendix when they interrupt the setup.
- These are placement and meaning judgments, not sentence-count or formula mandates.
- Against NO-ANALOGY in [STANDARDS.md](../STANDARDS.md): here "analogy" means naming the familiar object a setup primitive resembles. It never explains a technical result.

Further rules in force:
- No housekeeping paragraph: no "Section X supplied", no appendix pointers. Housekeeping lines go unless load-bearing, even when an exemplar carries them.
- Verifying derivations go to footnotes. An in-text integral that checks a stated formula is too technical for the body.
- Announce each idea once, in its own place.
- Every primitive gets a concrete anchor a practitioner recognises.
- A chosen quantity is named with who chooses it and when, at first appearance.
- Infrastructure is introduced with the agent who runs it.
- A standard mechanism carries its industry anchor and citation.
- No combat vocabulary ("attack", "raid").
- NO-TRIVIALIZING in [paper-intro-setting.md](paper-intro-setting.md) applies here too.

## Roles of the units in this type

- Opener; environment and primitives; players and choices (each actor's primitives once); states and information; rules (unavailable, not optimal and selected are three different claims); payoffs for a given history; assumptions (one plain sentence per condition, exact inequality beside it); equilibrium definition.

## Workflow, step by step

Every step not stated here: [HOW_WE_WORK.md](../HOW_WE_WORK.md) and [unit-plan-card-gate.md](../references/unit-plan-card-gate.md).

1. Before the plan, read the setup together with the first results subsection.
2. Write into `DECISIONS.md`: what varies and what is fixed; who chooses what and when; what each player observes; which equilibrium class is verified; which assumptions are common and which belong to one result.
3. A missing scientific ingredient goes to the author with evidence and a recommendation. Meanwhile draft only the passages that do not depend on it. Never fill a gap with a textbook equilibrium.
4. A needed formal change: the lead asks the math author for old/new pairs, in the form [paper-build-checks.md](../references/paper-build-checks.md) gives.
5. Verifying a pair, and any new lemma or changed proof step: the project's own mathematics and proof rules.
6. Applying a pair: [paper-build-checks.md](../references/paper-build-checks.md).
7. Before deleting a sentence or a display, write what it alone told the reader.
8. After a term or symbol change, sweep every file, appendix included, with the term check of [paper-build-checks.md](../references/paper-build-checks.md).

## Different from the general case

- A part that waits on the math author. Mark the part "waiting on the math author" in `DECISIONS.md` and go on to the next part. The author is told what the plan says. No prose-only version is shown meanwhile. Not back by the session's end: list it as open, with what was sent and when.

## Examples (where)

- Invented: [unit-roles.md](../references/unit-roles.md), sections 2 (opening of a derivation), 3 (setup) and 4 (the means).
- Published: [published.md](../examples/published.md), "A modelling choice: what it matches, what it isolates". No published setup opening or equilibrium definition is filed yet.

## Checks before the author sees it

Which versions, and where each line is written: the send check in [unit-plan-card-gate.md](../references/unit-plan-card-gate.md).
Mathematics untouched: before showing, the scope judgment of the send check; after applying, the statement check of [paper-build-checks.md](../references/paper-build-checks.md).

| Standard | Who | How | Pass |
|---|---|---|---|
| SETUP-APART | Lead | List every formula in the setup | Each specifies the environment or accounts for an action; none depends on solved behaviour or computes a threshold |
| SAY-IT-PLAINLY | Lead | List the first sentence of the section and of every paragraph | The section opener names its contents in one sentence; no opener starts with a count of items; the roster opens with a plain count |
| MINIMAL-NOTATION | Lead | For each symbol defined in the setup, grep its later uses in all `.tex` files | Each has a later use; for each general object, at least one result does not specialise it |
| LESS-DENSE, STATE-THE-GAME-FORMALLY | Fresh reader, always: once, on a new or rebuilt setup section when it is assembled | It names the players, choices, timing, information, payoffs and equilibrium conditions | All six correct |
| KEY-STATE-DISPLAY | Lead | Find where the key state object is introduced | It has a numbered display there |
| CHOICE-HAS-REASON | Lead | List each substantive modelling choice | Each has a sentence giving its reason from the question; no shape description, no contrast with another design |
| COIN-ONLY-IF-REUSED | Lead | Grep each coined term in the main text | Used in at least three statements; else described in plain words |
| EQUILIBRIUM-DEFINITION | Lead | Grep `\begin{definition}`; read the text just before it | Exactly one titled "Equilibrium", unqualified; one item per agent, in words; no payoff function and no formula inside; no preamble before it |
| SETUP-PARAGRAPHS | Lead | Read each paragraph | Each names the actor and the event; no supporting example or institutional match interrupts the setup |
| Housekeeping and verification | Lead | Grep `Section\|Appendix\|\\int` in the setup | No "Section X supplied" line, no appendix pointer, no verifying integral in the body |
| Each idea once | Lead | Grep each key concept | Its first full statement sits in one place |
| Anchors | Lead | List each primitive, chosen quantity, piece of infrastructure and standard mechanism | Each primitive has a recognisable anchor; each chosen quantity names who chooses it and when; each piece of infrastructure arrives with its agent; each standard mechanism has its anchor and citation |
| Combat vocabulary | Lead | Grep `attack\|raid` | Zero hits |
| Assumptions | Lead | Read each condition | Each has one plain sentence and its exact inequality |
| NO-TRIVIALIZING | Partner on the lead's version; lead on the others | Read for a fact that makes the headline true by construction | None |

## When the author says it is bad

Follow [unit-plan-card-gate.md](../references/unit-plan-card-gate.md). Then:
- Classify: wording, missing step, emphasis, density, placement, scientific scope, changed preference.
- Answer a mechanism question from the checked source first.
- Never swing between cutting all and keeping all.

## Gaps

- No time limit for a math-author round during a live walk. Meanwhile: "Different from the general case" above.
- "Three uses" for a coined term is a working reading; "one or two" was judged too few.

## Craft notes (trial)

- An assumption's gloss names whose primitive it bounds; keep that apart from what it helps prove.
