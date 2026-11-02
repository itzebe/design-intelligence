# Design Intelligence

A reusable, persistent **engineering and design standard** that OpenHands applies to every
project, in every conversation — managed entirely from a phone through OpenHands and GitHub.

It raises the quality bar and enforces real, evidence-based verification. It does **not** force
every app to look the same: each project keeps its own visual identity.

## What's here

| File | Purpose |
|------|---------|
| `ENGINEERING_CONSTITUTION.md` | **The engineering standard.** Architecture, implementation, security, performance, testing, delivery. Read before any code change. |
| `DESIGN_CONSTITUTION.md` | **The design standard.** Single source of truth for UI work. |
| `DEVELOPMENT_WORKFLOW.md` | The seven-step workflow every task follows (Discovery → Requirements → Design → Implementation → Verification → Independent review → Delivery). |
| `DESIGN_TOOLKIT.md` | Tools (browser, Playwright, axe-core, Lighthouse, Figma, Storybook) and when to use them. Includes the **verified** persistence model. |
| `VISUAL_QA_CHECKLIST.md` | Pass/fail checklist to complete before reporting UI work done. |
| `templates/PROJECT_ONBOARDING.md` | **Reusable onboarding template** applied to every repository before implementation. |
| `templates/AGENTS.md` | Drop into a project root so that project inherits the standards. |
| `templates/PROJECT_INIT.md` | The 11-step workflow for starting or redesigning a UI. |
| `templates/DESIGN_BRIEF.md` | Per-project brief that specialises the design standard for that product. |
| `ACCOUNT_MEMORY.md` | The short block to append to `~/.openhands/memory/MEMORY.md` — the channel verified to reach every new conversation. |
| `skills/global-design-intelligence/SKILL.md` | The standard as an OpenHands skill (best-effort layer). |
| `scripts/sync-design-standard.py` | Checks/pushes the standard to the durable layers and prints the memory block. |

## How it stays in effect (verified, not assumed)

Measured against real fresh conversations in this OpenHands deployment (2026-10-29, re-verified
2026-11-02):

| Layer | Reaches a new conversation? |
|-------|------------------------------|
| **Account memory** (`~/.openhands/memory/MEMORY.md` → `<MEMORY_CONTEXT>`) | **Yes** — every project, every conversation. **But** only the last ~100 lines (~3000 chars) of each tier are injected, so the block must be at the **end**. Persisted durably to the account record by a `file_editor` edit. |
| Project root `AGENTS.md` | **Yes** — within that project, once `load_project_skills` is on. |
| Project skill `.agents/skills/<name>.md` (flat file) | **Yes** — same flag. |
| **Public skills catalogue** (`load_public_skills: true`) | **Yes** — every skill in `github.com/OpenHands/extensions` is loaded automatically. Durable and API-configurable. |
| **MCP servers** (`agent_settings.mcp_config`) | **Yes** — persisted and propagated into new conversations. |
| Account `system_message_suffix` setting | **No** — persists via the API, but was not injected into any prompt in testing. |
| Custom account **skill** | **No** — stored durably, but not auto-injected here. Kept as a fallback. |

So the working channels are: **account memory** (global), a project's **`AGENTS.md`**
(per-project), the **public skills catalogue** (account-wide, API-configurable), and **MCP
servers** (account-wide, API-configurable). The canonical repository is the source of truth they
all point to.

### How account memory is actually set

There is **no "Memory" text box in the settings UI** — the Memory section holds only a
"Persistent memory" toggle. Account memory is a **file**, `~/.openhands/memory/MEMORY.md`, and its
content is injected into each new conversation. To set it, append the block to the **end** of that
file and then edit the file with the **`file_editor` tool** — a `MemoryChangeCallbackProcessor`
persists `MEMORY.md` edits made through that tool, whereas a plain shell write is not detected. The
public settings API accepts a `memory_context` field with HTTP 200 but silently ignores it.

## Setup (all of it scriptable)

1. **Account memory block.** Run `python3 scripts/sync-design-standard.py --install-memory`, then
   edit `~/.openhands/memory/MEMORY.md` once with the `file_editor` tool (any trivial change) so the
   callback persists it to your account record. This is the step that makes the standards apply
   account-wide.
2. **Enable the layers.** Run `python3 scripts/sync-design-standard.py`. It sets
   `load_project_skills`, `load_user_skills`, `load_memory`, and `load_public_skills`, stores both
   standards as account skills (best-effort), and writes the verified MCP server map. Verify with
   `--check`.
3. **Give each project the project layer.** Copy `templates/AGENTS.md` into the project root as
   `AGENTS.md` and fill in the placeholders.

New conversations then inherit the standards automatically.

## Everyday use

- **Starting a new project:** copy `templates/AGENTS.md` → the repo root, and tell the agent to
  follow `templates/PROJECT_ONBOARDING.md` (onboard) and `templates/PROJECT_INIT.md` (start/redesign).
- **Any code change:** tell the agent to load `ENGINEERING_CONSTITUTION.md` and follow
  `DEVELOPMENT_WORKFLOW.md`.
- **Redesigning an existing UI:** tell the agent to load `DESIGN_CONSTITUTION.md` and complete
  `VISUAL_QA_CHECKLIST.md`.
- **Checking the setup:** run `python3 scripts/sync-design-standard.py --check`.

## Maintaining it

Edit the relevant constitution, bump its version header, and if the core changed update the block in
`ACCOUNT_MEMORY.md`, re-run `--install-memory`, and touch the memory file with `file_editor`. Keep
the account skills and MCP map in sync with `python3 scripts/sync-design-standard.py`.

**Never store credentials, API keys, or tokens in this repository.**
