# AGENTS.md — canonical engineering & design standards repository

This repository **is** the canonical, account-wide standards set. It holds the source of truth
for how every piece of software under this account is engineered, and how every user interface is
designed, built, and verified.

## What is here

| File | Purpose |
|------|---------|
| `ENGINEERING_CONSTITUTION.md` | **Source of truth** for engineering: architecture, implementation, security, performance, testing, delivery. |
| `DESIGN_CONSTITUTION.md` | **Source of truth** for design: how interfaces are designed, built, and verified. |
| `DEVELOPMENT_WORKFLOW.md` | The seven-step workflow every task follows (Discovery → … → Delivery). |
| `DESIGN_TOOLKIT.md` | Tools for design, accessibility, and real visual verification, and when to use them. |
| `VISUAL_QA_CHECKLIST.md` | The pass/fail checklist to complete before reporting UI work done. |
| `templates/PROJECT_ONBOARDING.md` | **Reusable onboarding template** applied to every repository before implementation. |
| `templates/PROJECT_INIT.md` | The ordered workflow for starting or redesigning a project. |
| `templates/DESIGN_BRIEF.md` | Per-project brief template (specialises the design constitution; never weakens it). |
| `templates/AGENTS.md` | Copy-to-project `AGENTS.md` that binds a project to all three standards. |
| `skills/global-design-intelligence/SKILL.md` | The AgentSkills-format skill that mirrors the standards for global injection. |
| `ACCOUNT_MEMORY.md` | The short block to append to `~/.openhands/memory/MEMORY.md` — the channel verified to reach every new conversation. |
| `scripts/sync-design-standard.py` | Pushes the standards into the OpenHands account + local agent-server layers. |

## For any agent working in or from this repository

1. **Read `ENGINEERING_CONSTITUTION.md` before changing any code**, and `DESIGN_CONSTITUTION.md`
   before writing or changing any UI. Both govern. Every task follows `DEVELOPMENT_WORKFLOW.md`.
   Where a project brief is *less strict* on a mandatory item (security, accessibility, honesty,
   verification, anti-slop), the constitution wins.
2. For a new or existing project, follow `templates/PROJECT_ONBOARDING.md` (onboarding) and
   `templates/PROJECT_INIT.md` (starting or redesigning a UI).
3. Complete `VISUAL_QA_CHECKLIST.md` before reporting UI work done, and report honestly what you
   verified.
4. Record durable, non-obvious decisions in project memory; never record secrets.

## How the standards reach other projects

Four layers, in preference order. Which ones actually reach a fresh conversation was **measured**
(see `DESIGN_TOOLKIT.md` §5 for the evidence):

1. **Account memory** — the short block in `ACCOUNT_MEMORY.md`, appended to
   `~/.openhands/memory/MEMORY.md` (and mirrored in the account `memory_context`).
   **Verified to reach every new conversation, in every project.** This is the layer that makes the
   standards apply account-wide. The public settings API cannot persist it (`memory_context` is
   read-only over the API — verified), so it is a one-time edit of the memory file.
2. **A project's own `AGENTS.md`** (from `templates/AGENTS.md`) — **verified** to reach new
   conversations in that project. This is the per-project enforcement layer.
3. **This canonical repository** — a stable place to retrieve the full current text.
4. **The account skill** (`global-design-intelligence`) — stored durably via
   `python3 scripts/sync-design-standard.py`, but a *custom* account skill is **not** auto-injected
   into new conversations in this deployment. Keep it as a best-effort fallback; do not rely on it
   alone.

**Also available account-wide (verified 2026-11-02):** the public skills catalogue. Setting
`load_public_skills: true` via `POST /api/v1/settings` makes every skill in
`github.com/OpenHands/extensions` available for model invocation in new conversations — including
`frontend-design`, `code-review`, `security`, `qa-changes`, `agent-memory`, `code-simplifier`,
`prd`, `skill-creator`, `github`, and the `onboarding` plugin skills. This is a durable,
API-configurable layer and needs no manual step.

Never store credentials, API keys, or private tokens in any of these layers.

## Editing this standard

- Edit the relevant constitution (`ENGINEERING_CONSTITUTION.md`, `DESIGN_CONSTITUTION.md`) first —
  it is the source of truth for its domain.
- Keep `skills/global-design-intelligence/SKILL.md`, `DEVELOPMENT_WORKFLOW.md`, the toolkit, the
  checklist, and `templates/` consistent with the constitutions. Bump a constitution's version
  header when it changes.
- Run `python3 scripts/sync-design-standard.py` to propagate the change to the account layer, and
  update the block in `ACCOUNT_MEMORY.md` if the core changed.
- Do not weaken a mandatory rule without an explicit, recorded decision.
