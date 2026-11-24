# Use this portable writing skill

## Quick start

Keep the `prose-write` folder intact. The entry is `SKILL.md`. All other files are reached by relative links.
The procedure works for a team of people, for AI assistants that can read files, or for a mix.

You need:
- an author, who decides;
- a lead writer, who talks to the author;
- a partner writer, from a different model family or a different person;
- a fresh reader for blind reads, and an outside reviewer for new sections.

Give the lead a request such as:

> Read the prose-write skill. Revise this section with me part by part. Start a partner writer, give it the whole text, the plan and the checklist. Keep the scientific claims and their status.

Supply the manuscript and the research sources. Name the audience, venue and any protected passages if the project does not record them.

## Installation choices

**An agent that discovers skills from files.** Place the folder where that tool looks for skills. Keep the folder name and the front matter in `SKILL.md`. Test with a small real task, and ask which files it read.

**A chat assistant without skill discovery.** Attach `SKILL.md`, `HOW_WE_WORK.md`, `STANDARDS.md`, `references/unit-plan-card-gate.md` and the sheet in `types/` for your text. Ask the assistant to read them. A link in a message does not guarantee the assistant can open the files.

**A project with its own instructions.** Add one pointer line: "For drafting and revision, read `<path>/prose-write/SKILL.md` and follow it under this project's rules." Do not copy the skill into several instruction files.

**The partner writer.** Start it in whatever tool your team uses. Give it the whole text, the plan and the checklist from the project record. Keep it for the whole job.

No installer, network service or background process is needed.
`scripts/card_check.py` needs Python 3 and only the standard library. The skill works without it.
Usage: `python3 scripts/card_check.py draft.txt [--before current.txt] [--rise]`. Exit 1 means markers to inspect, not a failed text.

## Make learning persist

The project record lives in `notes/writing/` inside the project (see [HOW_WE_WORK.md](HOW_WE_WORK.md), "The record"). Create it from `templates/` at the first job.
Have every writer read `DECISIONS.md` and `CHECKLIST.md` at the start of each session.
Keep reusable lessons in one maintained local copy of this skill, following [MAINTENANCE.md](MAINTENANCE.md).
Nothing here runs between sessions. Check that the next session read the changed note and applied it.
Records hold private feedback and manuscript text. Do not publish them.

## A first-use check

Use a small, non-sensitive section of two or three paragraphs. Check that the lead:

1. Sends a plan before any paragraph: the point and the parts.
2. Briefs a partner, and shows three versions with one recommendation.
3. States what was checked and what was not.
4. Gives the fresh reader only the prose, not the intended answer.
5. Records your choice and your correction, and applies the correction to the next part.

Passing this check shows the route works once. It is not a quality rate.
If no partner or fresh reader is available, say so. Self-review does not count as independent review.

## Boundaries

This edition omits private manuscripts, conversations, the author's own words and platform automation. It includes no published papers. Obtain exemplar texts lawfully, and compare their structure without copying protected passages.
See [EXPORT_NOTES.md](EXPORT_NOTES.md).
