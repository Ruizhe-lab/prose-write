# Use this portable writing skill

## Quick start

Keep this `prose-write` folder intact. The entry file is `SKILL.md`; all required references are included with relative links. The procedure works as instructions for a human writing team or an assistant capable of reading files.

Give the assistant a request such as:

> Read the prose-write skill and use its runbook to revise this section from the attached reviewed results. Recover our current decisions, prepare the complete argument, obtain independent source/editorial and reader review where available, and show me the reconciled draft. Preserve the scientific claims. Record and apply lessons from my corrections.

Supply the manuscript and actual research sources. Add audience, venue, scope, protected passages, style preferences and delivery destination when those choices are not already in the project. The skill does not contain your research, provide journal-specific requirements, or authorize publication.

## Installation choices

**A compatible file-based agent.** Place the folder in the skill directory recognized by that host. Keep the folder name `prose-write` and the front matter in `SKILL.md`. Skill discovery conventions vary by product/version; use the host's current documentation. Test discovery with a real small task and ask the assistant which entry and reference files it read.

**A chat assistant without skill discovery.** Upload the folder's files if the interface supports them, or provide `SKILL.md` plus the relevant references as attachments. Ask the assistant to read them. A single chat message containing a link does not guarantee that the assistant can retrieve the files. When attachments cannot be followed by relative link, explicitly attach the handbook, runbook and reference for the current task.

**A project with its own instructions.** Add a short pointer to the project's existing instructions: “For drafting and revision, read `path/to/prose-write/SKILL.md` and follow its runbook under this project's authority and scientific verification requirements.” Replace the example path with the real one. Do not copy the full skill into several instruction files.

No installer, network service, API key or background process is needed. The optional helper uses Python 3.9 or later and only the standard library. The skill itself works without it.

## Make learning persist

Choose one existing project note as the home of current decisions and corrections. If none exists, create a small `WRITING_NOTES.md` alongside the project. Ask the assistant to read it at the start of subsequent writing sessions. Keep reusable craft lessons in a maintained local copy of this package, with a brief change record; keep project-specific preferences in the project note.

The learning procedure runs during actual work. Nothing in this folder executes between sessions or modifies another user's copy automatically. Confirm that the next assistant loaded the changed note and applied it to the next relevant draft. For public or shared projects, review notes before sharing: they may contain private feedback or manuscript details.

## A first-use check

Use a small, non-sensitive passage. Verify that the assistant:

1. Identifies the passage's purpose and preserves its supported claim.
2. Reads the relevant reference instead of inventing a different workflow.
3. Keeps source/editorial guidance out of the unprimed reader's packet.
4. Shows the reconciled passage, with unresolved limitations stated honestly.
5. Saves a correction at the intended home and uses it on the next relevant passage.

Passing this check establishes that the route works for that use, not a guaranteed quality rate. If no independent reviewer is available, keep that limitation visible; self-review does not become independent because it has a different heading.

## Contents and boundaries

The references provide construction patterns, a review protocol, author-walk procedure and a learning procedure. `examples/` contains invented, nonconfidential inputs for the optional helper. They illustrate its interface and writing distinctions; they are not research evidence.

This public edition omits private manuscripts, conversations, author rulings, local paths, unpublished results and platform-specific automation. It does not include published papers or grant rights to reproduce them. Obtain exemplar texts through lawful access, and compare their structure without copying protected passages into your paper.

See [EXPORT_NOTES.md](EXPORT_NOTES.md) for adaptation and attribution notes.
