# AGENTS.md — design intelligence for this repository

> **Template.** Copy this file to a project's repository root as `AGENTS.md` (or merge its
> content into an existing `AGENTS.md` without deleting that file's other instructions). Replace
> every `<PLACEHOLDER>`.

This repository follows the **Design Constitution**, a canonical, account-wide standard for every
user interface produced, modified, or reviewed here. It is mandatory, not advisory, and applies to
a one-line CSS change as much as to a full redesign.

## 1. Load the constitution first

Before writing or changing any UI code, load the constitution and the two companions:

1. `DESIGN_CONSTITUTION.md` — the canonical standard (source of truth).
2. `DESIGN_TOOLKIT.md` — tools and when to use them.
3. `VISUAL_QA_CHECKLIST.md` — the pre-report checklist.

Retrieval order (use the first that works):

1. **Account memory** — the short core of the standard is already in your context as a
   `<MEMORY_CONTEXT>` block (the "Global Design Intelligence" section). It applies here. This is
   the layer that reaches every conversation; you do not need to fetch it.
2. **Local copy in this repository** — if `DESIGN_CONSTITUTION.md` exists here, read it for the
   full text.
3. **Canonical remote source** — otherwise fetch it from the canonical repository:
   `<CANONICAL_REPO_URL>` (a raw GitHub URL to `DESIGN_CONSTITUTION.md`).

If the full text is unreachable, follow the account-memory summary above and **say plainly** that
the full constitution could not be retrieved.

## 2. Then follow the project-init workflow

Use `templates/PROJECT_INIT.md` (in the canonical repository) to start or redesign a project:
understand the product, create this project's `DESIGN_BRIEF.md`, define a distinct direction,
implement without unnecessary rewrites, inspect the rendered interface, fix defects, and report.

## 3. This project's specifics

- **Product:** `<what it is, in one sentence>`
- **Primary audience:** `<who uses it>`
- **Existing identity to preserve:** `<brand colours / type / conventions, or "none yet">`
- **Project `DESIGN_BRIEF.md`:** `<path, or "to be created">`
- **How to run the app locally:** `<command and URL>`
- **How to run the tests:** `<command>`

## 4. Non-negotiables (summary — the constitution governs)

- Generic is a failure state. Rework anything that could be a default template with a swapped logo.
- WCAG 2.2 AA is the minimum; verify contrast and keyboard access rather than assuming.
- Define all interaction states: default, hover, focus-visible, active, disabled, loading, empty,
  error, success, and content extremes.
- Verify responsive behaviour at mobile, tablet, and desktop; reflow, don't just shrink.
- **Actually look at the rendered interface in a browser** and take a screenshot. If you cannot,
  say so; never claim visual verification you did not perform.
- No fabricated content; no unnecessary dependencies; do not touch unrelated functionality.
- Preserve this project's own visual identity — the constitution sets the quality bar, not a
  shared house style.

## 5. Memory

Record durable, non-obvious design decisions and constraints in project memory
(`.openhands/memory/`). Do not record secrets, and do not record trivially re-discoverable facts.
