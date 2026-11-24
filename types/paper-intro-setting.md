# Paper: introduction and institutional setting

## When this applies

- You write or revise a paper's Introduction or its institutional (setting) section.
- Related literature, abstract and conclusion: [paper-frame.md](paper-frame.md).
- A coauthor's section, or a part the author calls fine: [HOW_WE_WORK.md](../HOW_WE_WORK.md), who writes each type of text.

## The standard

### FIRST-DRAFT-READY  Ask every question before drafting

Principle: settle every open question before the first draft, so the first draft is nearly right and the walk is short.
- Applies to a new or rebuilt section, not to a one-paragraph repair.
- Live: the questions are answered before the first draft.
- Prepared: ask them in the first message and draft on the recommendation (the unit file, "The plan"). Only a fact without which nothing can be drafted stops the draft.

### INTRO-PLAINEST  Just enough; no scope, condition or caveat lines

Principle: the introduction gives the reader only what builds the picture. Technical conditions stay in the theory section.
- Cut lines such as "under conditions stated in Section 3" or "we do not claim this is optimal".
- Cut a secondary fact that builds no picture.

### INTRO-CHAIN  Keep the author's connected chain; link every sentence

Principle: an introduction is one connected argument in academic language, not a row of separate claims.
- Open on the surprise: state what the reader expects, then the finding that overturns it.
- Give the consequence in plain words. The technical condition belongs to the theory section.
- Parallel findings share one sentence.
- A revision stays near the length of the text it replaces.
- Numbers that need qualifiers stay out of framing paragraphs.

### SURPRISE-RISE  An opening that carries a surprise is a rise

Principle: a surprising result is introduced in steps that build on each other.
- State the expectation and its reason, then the finding that contradicts it, then its consequence.
- Each sentence hands over from the one before.
- Example: [unit-roles.md](../references/unit-roles.md), section 1.

### NO-TRIVIALIZING  Never state what makes the result look obvious

Principle: do not add an explanation that makes the headline true by construction.
Invented example: in a study that finds appointment reminders lengthen waits, do not write "waits grow because sessions run longer". It makes the finding look like a definition.

### CONTRIBUTION-SELECTION  The contribution passage opens on the punchline

Principle: start with the supported positive economic punchline. Every later sentence explains the mechanism, develops the consequence or states the implication.
- Cut inventory items, proof detail, preview pointers and defences against objections nobody raised.
- Prefer the economic consequence to equilibrium jargon.
- A punchline needs logical integration, not typographic isolation.
- If a qualification changes the economic meaning, keep it where the claim needs it. Never turn a conditional theorem into an unconditional claim. This governs selection in the Introduction, not theorem statements.
- Apply PLAIN-PRECISE ([STANDARDS.md](../STANDARDS.md)) to inherited prose as well as new sentences. Replace a label with the actor and the action.
- A design paragraph states what the analysis establishes, then the mechanism and the policy implication. A generic opener such as "benefits depend on rules" does not carry that chain.

### NO-INLINE-ROADMAP  No "Section N formalizes Y" inside the results paragraphs

Principle: results paragraphs state results, not where they live. A closing roadmap paragraph is optional.

### SETTING-SCOPE  The setting gives only what the paper's question needs

Principle: the setting lets the reader perceive the environment. It is neither a flat catalogue nor a preview of the results.
- A variant the author wants readers to understand stays a main-text paragraph, never a footnote.
- At most one bridge paragraph points forward.

A default for the overview order, general by analogy:
- The institution; its rules; the activity those rules govern; each variant of the rules in its own paragraph.
- Dense institutional contrasts may earn a comparison table, walked with the author before it lands.

Possible moves of an introduction (optional, not a checklist):
1. The problem from the affected agent's seat. No paper opens with a number, a symbol or a glossary.
2. The documented surprise, attributed to its source. Mine the sources before structuring.
3. The puzzle, as named variation. Never leak the shape of the answer.
4. The hint: one measured fact.
5. The answer in words. No symbols anywhere in the introduction.
6. The mechanism in the field's canonical terms (for example moral hazard, congestion, gains from trade). State an advantage inside an explicit comparison of the designs.
7. Aggregate results anchored on the headline figure, with a self-contained plain caption.
8. A reserved design or policy paragraph, where the paper is design-relevant.
9. An optional closing roadmap.

## Roles of the units in this type

- Introduction: motivation and question; contribution; model overview (who acts, what they choose, the rule that drives the result, what varies); theory results; evidence (the point before its numbers); optional closing roadmap.
- Setting: environment; landscape (category, scale, range, dated); the rule and its meaning; one worked case; modern variants; the obstacle that makes the question arise; the question as landing.
- Working default: the opening may hold the surprise for a few sentences, but the answer is stated within the opening paragraphs. The introduction never ends with the puzzle open.

## Workflow, step by step

Every step not stated here: [HOW_WE_WORK.md](../HOW_WE_WORK.md) and [unit-plan-card-gate.md](../references/unit-plan-card-gate.md).

For a new or rebuilt section, before the plan:
1. Write the contract into `DECISIONS.md`: the contribution; what this section must teach the next; what is kept; which facts are open; which approvals stay untouched.
2. Settle each open fact by read-only research.
3. Put what only the author can answer in the plan message.

## Examples (where)

- Invented openings by role: [unit-roles.md](../references/unit-roles.md), sections 1 and 6.
- Published openings: [published.md](../examples/published.md).

## Checks before the author sees it

Which versions, and where each line is written: the send check in [unit-plan-card-gate.md](../references/unit-plan-card-gate.md).
A grep runs on `pdftotext` of the built PDF, or on the source. A "section pointer" is a hit of `Section[~ ]\\ref|\\S\\ref|Section [0-9]`.

| Standard | Who | How | Pass |
|---|---|---|---|
| FIRST-DRAFT-READY (new or rebuilt section) | Lead | Read the contract in `DECISIONS.md` | Every item has an answer, or is an open question in the plan |
| INTRO-PLAINEST | Lead | Grep the passage for `condition`, `we do not claim`, `we claim no` and inline math (`\$`) | Each hit is removed, or its line says what perception it builds and that cutting it changes the economic meaning |
| INTRO-CHAIN, links | Lead | List the first words of every sentence | Each shows its link to the sentence before |
| INTRO-CHAIN, lists and numbers | Lead | Read the framing paragraphs | Parallel findings share one sentence and one grammatical form; no number that needs a qualifier |
| SURPRISE-RISE | Lead | The card lists the expected chain and the actual chain as bullets | Each sentence of the opening maps to one step of the rise, in order |
| NO-TRIVIALIZING | Partner on the lead's version; lead on the others | Read for a fact that makes the headline true by construction | None |
| CONTRIBUTION-SELECTION | Lead | For each sentence of the contribution passage, write what the reader loses if it is cut | The first sentence is the punchline; no answer is only an inventory item, a proof detail, a pointer or a defence |
| NO-INLINE-ROADMAP | Lead | Grep for a section pointer | Zero hits outside a closing roadmap paragraph |
| The puzzle default | Fresh reader, always: once, on a new or rebuilt introduction when it is assembled | It reads the whole introduction | It states the paper's answer; it reports that the answer appears before the model overview |
| Overview order | Lead | List the setting's paragraphs | Institution, then its rules, then the activity, then one paragraph per variant; a different order has its reason in the plan |
| SETTING-SCOPE | Lead | Map each setting paragraph to the reader need it supplies for the question | None unmapped; no "we show", "in equilibrium" or "our model" outside the one bridge paragraph; no main-text paragraph moved to a footnote without the author's word |

## When the author says it is bad

Follow [unit-plan-card-gate.md](../references/unit-plan-card-gate.md). Then by what the author disputes:
- A fact or link: check its source; show the shortest distinction.
- Why a paragraph is there: repair its job and place before its wording.
- Density: separate the steps; never delete the mechanism or demote a wanted variant.

## Gaps

- CONTRIBUTION-SELECTION and NO-INLINE-ROADMAP are working summaries. Apply them as written.

## Craft notes (trial)

- An agenda paragraph's first sentence tells the reader what it will explain.
- A worked case: one calculation step per sentence.
