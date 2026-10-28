# AGENTS.md — canonical design intelligence repository

This repository **is** the canonical, account-wide design standard. It holds the source of truth
for how every user interface under this account is designed, built, and verified.

## What is here

| File | Purpose |
|------|---------|
| `DESIGN_CONSTITUTION.md` | **Source of truth.** The full, mandatory design standard. |
| `DESIGN_TOOLKIT.md` | Tools for design, accessibility, and real visual verification, and when to use them. |
| `VISUAL_QA_CHECKLIST.md` | The pass/fail checklist to complete before reporting UI work done. |
| `templates/PROJECT_INIT.md` | The ordered workflow for starting or redesigning a project. |
| `templates/DESIGN_BRIEF.md` | Per-project brief template (specialises the constitution; never weakens it). |
| `templates/AGENTS.md` | Copy-to-project `AGENTS.md` that points an agent at the constitution. |
| `skills/global-design-intelligence/SKILL.md` | The AgentSkills-format skill that mirrors the standard for global injection. |
| `scripts/sync-design-standard.py` | Pushes the standard into the OpenHands account + local agent-server layers. |

## For any agent working in or from this repository

1. **Read `DESIGN_CONSTITUTION.md` before writing or changing any UI code.** It governs. Where a
   project brief is silent, the constitution applies; where a project brief is *less strict* on a
   mandatory item (accessibility, honesty, verification, anti-slop), the constitution wins.
2. For a new or redesigned project, follow `templates/PROJECT_INIT.md`.
3. Complete `VISUAL_QA_CHECKLIST.md` before reporting done, and report honestly what you verified.
4. Record durable, non-obvious design decisions in project memory; never record secrets.

## How the standard reaches other projects

Four layers, in preference order. Which ones actually reach a fresh conversation was **measured**
(see `DESIGN_TOOLKIT.md` §5 for the evidence):

1. **Account memory** — the short block in `ACCOUNT_MEMORY.md`, pasted into the OpenHands settings
   UI (Memory). **Verified to reach every new conversation, in every project.** This is the layer
   that makes the standard apply account-wide. The public API cannot persist it, so it is a
   one-time manual paste.
2. **A project's own `AGENTS.md`** (from `templates/AGENTS.md`) — **verified** to reach new
   conversations in that project. This is the per-project enforcement layer.
3. **This canonical repository** — a stable place to retrieve the full current text.
4. **The account skill** (`global-design-intelligence`) — stored durably via
   `python3 scripts/sync-design-standard.py`, but a *custom* account skill is **not** auto-injected
   into new conversations in this deployment. Keep it as a best-effort fallback; do not rely on it
   alone.

Never store credentials, API keys, or private tokens in any of these layers.

## Editing this standard

- Edit `DESIGN_CONSTITUTION.md` (the source of truth) first.
- Keep `skills/global-design-intelligence/SKILL.md`, the toolkit, and the checklist consistent with
  it. Bump the constitution's version header when the standard changes.
- Run `python3 scripts/sync-design-standard.py` to propagate the change to the account layer.
- Do not weaken a mandatory rule without an explicit, recorded decision.
