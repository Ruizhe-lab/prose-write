# Type sheet: research or PhD proposal, reference letter, email

Thin on purpose: the record behind it is short. Each GAP says what to do meanwhile.

## When this applies

- A research or PhD proposal; a reference letter the author signs; an email from the author to a senior person or a note to coauthors.
- A grant or gift bid: [types/grant.md](grant.md).
- Everything this sheet does not state is in the core.
  - The team, the mode, who writes, how many versions, the message, approval, applying, delivery, the record: [HOW_WE_WORK.md](../HOW_WE_WORK.md).
  - The plan, the card, the send check, the fresh reader, a correction: [the unit file](../references/unit-plan-card-gate.md).
- The facts only the author can give, for these types: who the applicant or recipient is, which programme or occasion, which form, the deadline, what the author is asking for. How to ask: the unit file, "The plan".

## The standard

The examples are invented. They concern an imaginary applicant who wants to study how river towns share flood warnings.

### PROPOSAL-CHAIN-FIRST  Agree each section's logical chain before text
Principle: before drafting, agree each section's chain of reasoning with the author: premise, premise, conclusion. Discuss alternatives per section until the chain is clear. Text comes after.

### PROPOSAL-SIMPLE  Plain questions the field already asks
Principle: a proposal should be simple to state. Its questions are ones the field already asks, in plain words. Do not coin constructs. If everything is one question, say so.
Example (invented): "Which towns pass on flood warnings, how fast, and at what cost?" not "We introduce a warning-propagation efficiency index".

### PROPOSAL-READER-FIELD  The claim in the named reader's words
Principle: state the central claim in the vocabulary of the reader's own field. Keep the author's field jargon for the methods.

### PROPOSAL-APPLICANT-AGENDA  The agenda is the applicant's, general and concrete
Principle: a proposal written for someone else is that person's agenda. It is general enough to stand alone and concrete enough to execute. The author's own work is at most one motivating example.

### PROPOSAL-NO-GRANT-FURNITURE  No grant-bid sections
Principle: a research proposal does not need the furniture of a grant bid. Drop reproducibility, data-management, risk, dissemination and impact sections unless the programme requires them.

### PROPOSAL-FORMAL-REGISTER  Dry language, formal headings, no bold
Principle: use dry academic language. Headings are noun-phrase labels. No bold in the body.

### LATEX-DEFAULT  LaTeX to PDF
Principle: author proposals and letters in LaTeX and deliver a PDF. Use Word only when the destination requires it.

### LETTER-SCARCE-HALF  A doctoral letter argues what the applicant brings
Principle: a doctoral reference argues that the applicant already brings what the field lacks, and that the programme is the remaining step. It never says the applicant needs training in that field.

### LETTER-PROGRAMME-GOAL  Each programme changes the argument
Principle: the goal of the letter depends on the programme. A doctorate, a conversion course and a taught degree need different arguments. Read the entry requirements first.

### EMAIL-READY-TO-SEND  Leave the author only the Send button
Principle: whoever prepares an email draft also adds the recipients and attachments. The author's only remaining act is to send.

## Roles of the units in this type

- Proposal: a section; role = the chain line it carries.
- Letter: a paragraph; role = its plan line ("evidence 2: the applicant's thesis method").
- Email: one unit, role "email".
- No paper role table applies to any of the three.

## Workflow, step by step

Only the steps these types add. Every other step is in the core files named above.

Proposal:
1. Recover the programme's requirements, and the applicant's CV or the author's letters about that person.
2. Read the author's nearest own paper for exposition, not content.
3. The plan gives each section's chain: premise, premise, conclusion, what the next section uses. Discuss it in prose. A form or widget only closes a discussion.

Letter:
1. Recover, in order: the author's earlier letters for the person; the applicant's CV, proposal and statement; the author's notes about the person; the programme's entry requirements; the form's criteria. Search the author's sent mail and files if allowed.
2. No earlier letter found: say so in the plan message and ask for one to use as a template. Meanwhile draft in a plain letter layout, marked "letterhead and signature pending".
3. Keep every checkable fact of an earlier letter. Change only what the facts prove.
4. The plan holds: the one belief the committee should hold; three or four pieces of evidence; the questions only the author can answer (how long and how they know the person).
5. In the plan, "Checked against" names the source documents. The author's answers are recorded, not checked.
6. A fact the author has not given stays a marked gap, never a plausible claim.
7. A form's stated criteria become run-in headings, in its order.
8. Template: a copy of the author's nearest letter (letterhead, date, addressee, subject, signature, page size). File name: `<Applicant>_<LetterType>_<Programme>.pdf`.

Email:
1. The card, at email size: reader, belief, the ask, the reason to say yes, only the facts the ask needs.
2. Which paper version goes out is the author's choice. When you ask, state the version the recipient holds, any public one, and the current one.

## Examples (where)

- No example file yet for these types.
- Meanwhile: for a letter, the author's earlier letters for the person, then the nearest letter for the same programme kind, read as drafts unless signed; for an email, the author's sent mail; for a proposal, the author's nearest paper.
- Anonymize any pair before adding it to the skill ([MAINTENANCE.md](../MAINTENANCE.md)).

## Checks before the author sees it

These are the rows the send check runs for these types ([the unit file](../references/unit-plan-card-gate.md), "The send check").
A row applies only to the type its first word names. None runs on a plan message.

| Standard | Who | How | Pass |
|---|---|---|---|
| Proposal: PROPOSAL-CHAIN-FIRST | Lead | Finds the author's agreement in the record | Live: one dated agreement per drafted section. Prepared: the plan was the first message, and the ready notice says "you have not agreed this plan" |
| Proposal: PROPOSAL-SIMPLE | Lead | Reads each question alone | One line, no method words, in the cited literature's words |
| Proposal: PROPOSAL-READER-FIELD | Lead | Reads the claim beside the named reader's two latest papers | Uses their recurring question |
| Proposal: PROPOSAL-APPLICANT-AGENDA | Lead | Asks: could the applicant present it to someone who never read the author's paper? | Yes; the author's paper is at most one example |
| Proposal: applicant can do it | Lead | Checks each method against the CV | On the CV, or stated as a training goal |
| Proposal: PROPOSAL-NO-GRANT-FURNITURE | Lead | Lists the headings | No reproducibility, data-management, risk, dissemination or impact section |
| Proposal, letter: PROPOSAL-FORMAL-REGISTER | Lead | Greps headings and bold, then reads each sentence | Noun-phrase headings; no bold in body; no sentence about the document itself |
| Proposal, letter: LATEX-DEFAULT | Lead | Lists the source and output files | A `.tex` source and its PDF; a Word file only where required |
| Letter: LETTER-SCARCE-HALF (doctoral letters) | Lead | Reads each paragraph for what it argues | Each argues what the applicant brings; none says the applicant needs training in the field |
| Letter: LETTER-PROGRAMME-GOAL | Lead | Quotes the entry requirements under the draft | The thesis matches the kind (doctoral, conversion, taught) |
| Letter: facts | Lead | Traces each fact to a source document | Every fact cited; every missing fact marked |
| Email: EMAIL-READY-TO-SEND (runs on the draft after the author approves the text) | Lead | Looks at the rendered draft | Recipients and attachments in place; nothing left but Send |
| Email: voice | Lead | Compares greeting, sign-off and warmth with the author's sent emails | Matched, or "tone not matched: sent mail not searched (<reason>)" |
| Email: facts | Lead | Traces each claim | Conditions kept; nothing stronger than the paper |
| All three: no names in the skill | Lead | Rereads an example pair before filing | No person, programme, institution, address or personal fact |

## When the author says it is bad

What to do the same turn, and how to repair: [the unit file](../references/unit-plan-card-gate.md). What enters the skill: [MAINTENANCE.md](../MAINTENANCE.md).

## Gaps

- GAP: no accepted proposal, letter or email on file. Meanwhile: the fallbacks in Examples.
- GAP: no standard for email prose. Meanwhile: match the author's sent mail.

## Craft notes (trial)

Working defaults, not rulings:
- A doctoral letter never says the applicant needs training in the field applied to; a conversion course is the opposite case.
- A research question carries no method. One central question with steps beneath beats parallel questions that are one thing.
- No coined construct and no Definition environment in an empirical proposal.
- Headings are labels; the claim opens the section.
