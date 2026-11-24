# The overall standard

What good writing is, whatever the type. Read it all before any card or draft.
- This file holds the standard only. How the team works: [team]. The plan, the card and the checks: [unit].
- A type sheet adds to this file and never loosens it.
- The examples here are invented for teaching. They come from no real paper. Published passages by role: [ex].

## 1. The ten principles

### PERCEPTION-FIRST  Decide what the reader should believe and feel, before anything else
Principle: writing exists to make a reader perceive a point. Before any sentence, name the one belief and the one feeling the text must leave.
Example. Topic: "This section studies appointment reminders." Perception: "Reminders lengthen waits in clinics that keep their old booking level; the reader should feel surprised."

### CHAIN-BEFORE-PROSE  Agree the point, the plan and the chain of logic before any paragraph
Principle: logic comes first. Write the full chain of reasons, and agree it, before polishing any sentence.
Example. Chain: reminders raise attendance; the booking level was set for the old attendance; more patients arrive than there are slots; waits lengthen. Only then draft.

### LINK-AND-RISE  Link every sentence to the last; build a rise, not a flat list
Principle: every sentence follows from the one before, and the paragraph climbs toward what matters most. Correct facts in a flat row do not persuade.
- Flat: "Reminders raise attendance. Clinics overbook. Waits are longer."
- Rise: "Reminders should shorten waits, because fewer slots go unused. In the clinics we study, waits grew. The clinics had kept a booking level set for patients who often missed."

### ROLE-OF-UNIT  Every unit has a role; write to the role
Principle: an opening, a setup, an explanation and a test each have one job. A unit that does its neighbour's job fails, even when every sentence is true. Roles and invented examples: `references/unit-roles.md`.

### PLAIN-PRECISE  Plain, concrete, precise academic language; keep the field's terms
Principle: an outsider should follow every sentence, and a specialist should find every term correct. Dense is not the same as precise; dramatic is not the same as clear.
- No jargon, private label, notation dump, slang or flourish.
- Rejected: "Reminders are a time bomb in the waiting room." Accepted: "Reminders raise attendance above the number of slots, and the patients booked last wait."

### SELECT  Keep only what builds the point; never cut the reasons
Principle: for each fact, ask whether the reader needs it to reach the belief. If not, cut it. Never cut a reason clause.
Example. Cut: the history of reminder software. Keep: "because the booking level was set when one patient in six missed".

### VERIFY-FIRST  Verify facts, sources and mechanism before anything reaches the author
Principle: everything sent to the author has passed the send check. An unverified draft wastes the author's time.
Example: the send check in [unit].

### RESPECT-THE-AUTHOR'S-TEXT  Leave sound sentences, approved text, coauthors' sections and parts the author calls fine
Principle: the writers address what the author asked for. They do not rewrite the whole text.
Example. Asked to fix one paragraph, the writer returns that paragraph only, with any other problem listed, not applied.

### WORK-THE-AUTHOR'S-WAY  The lead writes, a partner writes too, the author never waits
Principle: the procedure serves the author's working rhythm. When it no longer matches how the author actually works, the procedure is stale and is updated.
Example: the loop in [team].

### LEARN-EVERY-CORRECTION  Every correction is diagnosed and learned from
Principle: each criticism leads to a root cause and a lasting change, not only a repaired sentence.
Example: `MAINTENANCE.md`.

## 2. Register rules, always in force

### NO-EM-DASH  No em-dashes
Principle: em-dashes break the chain of a sentence. Use a comma, a short parenthesis, or two sentences.
- A verbatim quotation keeps its characters. Mathematical notation is preserved.

### NO-HEDGING  State a claim at the strength of its evidence, once
Principle: a supported claim is stated as supported. A limitation is stated once, where it binds.
- Do not answer an objection nobody raised.
- When content is cut, delete its hedges; do not move them.
- Keep a qualification whose removal changes the meaning.
- A limitation a reviewer names is never appended to a supported implication in the abstract, introduction or conclusion.
- Sentences about independence of inputs, or pointers to the appendix, do not enter model text.
- A supported result phrased as a caveat is restated as the result it is. Rejected: "Waits need not fall with reminders." Accepted: "Reminders lengthen waits when the booking level is unchanged."
- Reply to reviewers: name and explain only the premise the results rest on, in a footnote. Standard or symmetric choices get no hedge sentence. A main-text claim with no stated result behind it is dropped.

### NO-ANALOGY  Explain a technical result in technical terms
Principle: an analogy for a technical result hides the mechanism. Name the agent, the action and the effect instead.

More rules in force:

- One name per object. Search the document for synonyms; replace each. Only the author ratifies a term.
- Simplicity beats length bands. "As simple as possible" wins over a sentence-length target.
- Academic register. Name the agent or mechanism, its action and the object affected. No slogan.
  - Rejected: "Nobody is in charge of the queue." Accepted: "Each patient who arrives late moves every later patient back by one slot."
  - Keep a familiar metaphor of the field when it conveys a precise concept. Factual accuracy alone does not make the register academic.
- Sentence clarity. Each sentence shows who acts, what happens, the outcome and why it is there.
  - "Lower" and "cheaper" need a clear comparator and cost object.
  - Explain the operative rule and expand unfamiliar acronyms; a label cannot replace who receives what and who pays.
  - A policy implication names an implementable choice, its economic channel and the affected party.
  - Preserve conditions that change the comparison. This is a meaning test, not a sentence template.
- Whole paper. Main-text explanations connect the point, the mechanism and the consequence in natural economic language. Abstracts and conclusions select the central contribution rather than listing every true result.
- No template scaffolds; openers carry logic. Rejected: "Three results emerge." Rejected: "This section proceeds through four claims." Say what the section does, its economics, not its structure. A section's one-sentence opener still names every subsection.

Held elsewhere:
- Matched published exemplars: [ex].
- The two registers of results prose: `types/paper-results.md`.

## 3. Scopes

Principles that pull in opposite directions: both sides, then what the writer does.

| Subject | One side | Other side | Do this |
|---|---|---|---|
| Bold | Bold distracts in body text | A skimming funder needs the parallel points marked (`types/grant.md`) | Papers, academic proposals, letters: no bold in body text. Grants: bold only the parallel points a funder must carry. |
| Setup and results | The setup states the rules once; results do not repeat them | A result needs enough context to be followed | A result restates the stage, the actor and the formal problem, not the rules. |
| Cut and keep | Too verbose | Cutting broke the logic | Cut repetition and side facts. Keep every link and reason clause. |
| The author's wording | The author may prefer their own paragraphs | Agreed wording fixes logic, not exact words; some changes help | The author's sound paragraph is shown with the smallest change, beside the other versions. |
| Plain and academic | Simple to read | Academic where the field expects it | Plain words replace jargon. The field's terms stay. Introduction plainest; body academic. |
| Short and connected | One thought per sentence | Connected reasoning, not staccato | Join steps with causal clauses; no fragments. |
| Hedging and overclaim | NO-HEDGING above | "Does not exist" can be too strong | State the claim at the strength of its evidence, once. |
| Live or prepared | Some authors want only a whole draft | Others want to write together, now | [team], "Live or prepared". |
| How many options | Options for a story arc | One clear recommendation | Arc choice: options, one recommended. Every other case: [team], "One message". |
| Early or late | Walk only near-finished results | Agree what each part teaches early | [unit], "The plan". |
| Work during a walk | Nothing unrelated interrupts | The next part is prepared ahead | Prepare the next part quietly; [team]. |

[unit]: references/unit-plan-card-gate.md
[team]: HOW_WE_WORK.md
[ex]: examples/published.md
