# Design Intelligence

A reusable, persistent **UI/UX design standard** that OpenHands applies to every interface, on
every project, in every conversation — managed entirely from a phone through OpenHands and GitHub.

It raises the quality bar and enforces real visual verification. It does **not** force every app to
look the same: each project keeps its own visual identity.

## What's here

| File | Purpose |
|------|---------|
| `DESIGN_CONSTITUTION.md` | **The canonical standard.** Single source of truth. Read before any UI work. |
| `DESIGN_TOOLKIT.md` | Tools (browser, Playwright, axe-core, Lighthouse, Figma, Storybook) and when to use them. Includes the **verified** persistence model. |
| `VISUAL_QA_CHECKLIST.md` | Pass/fail checklist to complete before reporting UI work done. |
| `ACCOUNT_MEMORY.md` | The short block to append to `~/.openhands/memory/MEMORY.md` — the channel verified to reach every new conversation. |
| `templates/AGENTS.md` | Drop into a project root so that project enforces the standard. |
| `templates/DESIGN_BRIEF.md` | Per-project brief that specialises the standard for that product. |
| `templates/PROJECT_INIT.md` | The 11-step workflow for starting or redesigning a project. |
| `skills/global-design-intelligence/SKILL.md` | The standard as an OpenHands skill (best-effort layer). |
| `scripts/sync-design-standard.py` | Checks/pushes the standard to the durable layers and prints the memory block. |

## How it stays in effect (verified, not assumed)

Measured against real fresh conversations in this OpenHands deployment (2026-10-29):

| Layer | Reaches a new conversation? |
|-------|------------------------------|
| **User memory file** `~/.openhands/memory/MEMORY.md` → `<MEMORY_CONTEXT>` block | **Yes** — every project, every conversation. **But** only the last ~100 lines (~3000 chars) of each tier are injected, so the GDI block must be at the **end** of the file. |
| Project root `AGENTS.md` | **Yes** — within that project, once `load_project_skills` is on. |
| Project skill `.agents/skills/<name>.md` (flat file) | **Yes** — same flag. |
| Account `system_message_suffix` setting | **No** — persists via the API, but was not injected into any prompt in testing. |
| Custom account **skill** | **No** — stored durably, but not auto-injected here. Kept as a fallback. |

So the two working channels are the **user memory file** (global) and a project's **`AGENTS.md`**
(per-project, gated by `load_project_skills`). The canonical repository is the source of truth both
point to.

### How account memory is actually set

There is **no "Memory" text box in the settings UI** — the Memory section holds only a
"Persistent memory" toggle. Account memory is a **file**, `~/.openhands/memory/MEMORY.md`, and its
content is injected into each new conversation. To set it, append the block to the **end** of that
file and then edit the file with the **`file_editor` tool** — a `MemoryChangeCallbackProcessor`
persists `MEMORY.md` edits made through that tool, whereas a plain shell write is not detected. The
public settings API accepts a `memory_context` field with HTTP 200 but silently ignores it.

## One-time setup (2 minutes, from your phone)

1. **Install the account memory block.** Run
   `python3 scripts/sync-design-standard.py --install-memory`. It appends the block from
   `ACCOUNT_MEMORY.md` to the end of `~/.openhands/memory/MEMORY.md`. Then, in an OpenHands
   conversation, edit that file once with the `file_editor` tool (any trivial change) so the
   callback persists it to your account record. This is the step that makes the standard apply
   account-wide.
2. **Turn on project skills.** So the per-project layer is actually read, run
   `python3 scripts/sync-design-standard.py` (or set it in Settings). It enables
   `load_project_skills`, which is what makes a repo's `AGENTS.md` and `.agents/skills/` reach the
   agent. Verify with `--check`.
3. **Give each project the project layer.** Copy `templates/AGENTS.md` into the project root as
   `AGENTS.md` and fill in the placeholders. This enforces the standard in that repo.

That's it. New conversations then inherit the standard automatically.

## Everyday use

- **Starting a new project:** copy `templates/AGENTS.md` → the repo root, and tell the agent to
  follow `templates/PROJECT_INIT.md`.
- **Redesigning an existing UI:** tell the agent to load `DESIGN_CONSTITUTION.md` and complete
  `VISUAL_QA_CHECKLIST.md`.
- **Checking the setup:** run
  `python3 scripts/sync-design-standard.py --check`.

## Maintaining it

Edit `DESIGN_CONSTITUTION.md`, bump its version header, and if the core changed update the block in
`ACCOUNT_MEMORY.md`, re-run `--install-memory`, and touch the memory file with `file_editor`. Keep
the account skill in sync with `python3 scripts/sync-design-standard.py`.

**Never store credentials, API keys, or tokens in this repository.**
