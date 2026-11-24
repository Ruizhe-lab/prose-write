# Maintenance: how a correction enters the skill

Read this at a section's end or a sitting's end, when a correction may change the skill.
What happens in the same turn: [the unit file](references/unit-plan-card-gate.md), on corrections.
Every row is a default. The author's word replaces it.
Keep one maintained local copy of this skill. Change that copy, never a second one.

## When, what, who

| When | What happens | Who |
|---|---|---|
| During a part | Nothing enters the skill. A helper may prepare the classification. | |
| The section's end, or the sitting's end, the same day | Classify each correction: what decision or handoff let it through. Give it a home (next table). | The writer who heard it |
| In the skill | The steps below. | The writer who heard it writes. The skill's owner reviews. |
| Never | A writer's own generalisation is entered as the author's principle. It goes under craft notes. It becomes a principle only on the author's word, asked at a review, never mid-walk. | |

| Kind of correction | Home |
|---|---|
| This text only: a fact, a name or a choice of this text, not a fault another text could repeat | The project record, nowhere else |
| An accepted or rejected passage | Your team's example file for that type (`examples/<type>.md` in your own copy, created on first use), under the passage's role |
| A rule for one type | Its sheet in `types/` |
| How we work | [HOW_WE_WORK.md](HOW_WE_WORK.md) |
| All writing | [STANDARDS.md](STANDARDS.md) |

A fault another text could repeat, at its first occurrence: at the section's end, steps 1 to 8 below. If no principle covers it and step 3 does not fit, write an example pair: the rejected text, the accepted text, the reason.
`CHECKLIST.md` counts faults within one text. A correction reaches another project only by entering the skill.

## Changing the skill

1. Search first: the home file by subject, then every principle.
2. A principle already covers it: add no rule. Add one "recurred" line to it, with the date and why the writer missed it. Repair that cause.
3. Nothing covers it, and the author's own words are general ("always", "never", "every", or they name a kind of text): add one entry in the form below. Otherwise the example pair only.
4. It contradicts a principle: replace in place. Keep the old wording in a history section, with "replaced by" and the date.
5. State it in one file. Make every other mention a pointer.
6. Keep each file within the size your team set for it. If a principle needs more room, raise the size and say why.
7. Advance the edition line in [SKILL.md](SKILL.md).
8. Check that every relative link still resolves.

## The form of one principle

```
### IDENTIFIER  One-line statement
Status: in force.   Scope: <type, or all writing>.   First stated: YYYY-MM-DD.
Principle: <one or two plain sentences>
Example: <example file>, "<role>".
Recurred after the principle existed: <one line per recurrence, from step 2>
```

- Statuses: in force; trial (with admitted and review-by dates); one text only; retired (with reason and replacement).
- A principle the author stated is never entered as a trial.
- A writer's advice goes under "Craft notes (trial)", never among the author's principles.
- A team may keep the author's exact words beside a principle in its private copy. Do not publish them.

## Owner and reviews

- Name one owner for the local copy. It owns file sizes, routes, checks and any public export.
- Review trials on a set date. The owner prepares one page: each trial's evidence, keep or retire.
- After each finished paper or submitted proposal, the owner reads the "recurred" lines. A principle that recurred twice gets a repaired route or an example, never more words.

## History

- No old file sits beside a live one. Keep retired files in version history, with a note of how to restore them.
- Before a large rebuild, keep a snapshot of the old skill.
