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
| `ACCOUNT_MEMORY.md` | The short block to paste into OpenHands account **Memory** — the channel verified to reach every new conversation. |
| `templates/AGENTS.md` | Drop into a project root so that project enforces the standard. |
| `templates/DESIGN_BRIEF.md` | Per-project brief that specialises the standard for that product. |
| `templates/PROJECT_INIT.md` | The 11-step workflow for starting or redesigning a project. |
| `skills/global-design-intelligence/SKILL.md` | The standard as an OpenHands skill (best-effort layer). |
| `scripts/sync-design-standard.py` | Checks/pushes the standard to the durable layers and prints the memory block. |

## How it stays in effect (verified, not assumed)

Measured against real fresh conversations in this OpenHands deployment:

| Layer | Reaches a new conversation? |
|-------|------------------------------|
| **Account memory** (`<MEMORY_CONTEXT>` block) | **Yes** — every project, every conversation. |
| Project root `AGENTS.md` | **Yes** — within that project. |
| Project skill `.agents/skills/<name>.md` (flat file) | **Yes** — within that project. |
| Custom account **skill** | **No** — stored durably, but not auto-injected here. Kept as a fallback. |

So the two working channels are **account memory** (global) and a project's **`AGENTS.md`**
(per-project). The canonical repository is the source of truth both point to.

## One-time setup (2 minutes, from your phone)

1. **Paste the account memory block.** Open OpenHands → **Settings → Memory**, and paste the
   contents of the code block in `ACCOUNT_MEMORY.md`. This is the step that makes the standard
   apply account-wide. (The settings API cannot persist memory, so it must be done in the UI.)
2. **Give each project the project layer.** Copy `templates/AGENTS.md` into the project root as
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

Edit `DESIGN_CONSTITUTION.md`, bump its version header, and re-paste `ACCOUNT_MEMORY.md` if the
core changed. Keep the account skill in sync with
`python3 scripts/sync-design-standard.py`.

**Never store credentials, API keys, or tokens in this repository.**
