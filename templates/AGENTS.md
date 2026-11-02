# AGENTS.md — account standards for this repository

> **Template.** Copy this file to a project's repository root as `AGENTS.md`. If an `AGENTS.md`
> already exists, **merge** this content into it — do not delete the file's existing
> instructions. Replace every `<PLACEHOLDER>`.

This repository follows the **account-wide engineering and design standards**. They are
mandatory, not advisory, and apply to a one-line fix as much as to a full feature.

The three canonical standards:

1. `ENGINEERING_CONSTITUTION.md` — how software is built, secured, tested, and delivered.
2. `DESIGN_CONSTITUTION.md` — how interfaces are designed, built, and verified.
3. `DEVELOPMENT_WORKFLOW.md` — the seven-step workflow every task follows.

Canonical source repository: `<CANONICAL_REPO_URL>` (e.g.
`https://raw.githubusercontent.com/itzebe/design-intelligence/main/`).

---

## 1. Load the standards first

Before writing or changing any code, load the standards you need:

- Always: `ENGINEERING_CONSTITUTION.md` and `DEVELOPMENT_WORKFLOW.md`.
- For any UI work: also `DESIGN_CONSTITUTION.md`, `DESIGN_TOOLKIT.md`, and
  `VISUAL_QA_CHECKLIST.md`.

Retrieval order (use the first that works):

1. **Account memory** — the short core of both standards is already in your context as the
   `<MEMORY_CONTEXT>` block. It applies here; you do not need to fetch it.
2. **Local copy in this repository** — if these files exist here, read them for the full text.
3. **Canonical remote source** — otherwise fetch them from `<CANONICAL_REPO_URL>`.

If the full text is unreachable, follow the account-memory summary and **say plainly** that the
full text could not be retrieved.

## 2. Follow the development workflow

Every task follows `DEVELOPMENT_WORKFLOW.md`:

**Discovery → Requirements → Design → Implementation → Verification → Independent review → Delivery.**

The steps are constant; their weight scales with the task. **Verification (step 5) and
Independent review (step 6) are never skipped.**

## 3. Onboard this project if it is not yet onboarded

If this repository has not been onboarded to the standards, follow
`templates/PROJECT_ONBOARDING.md` (in the canonical repository) before implementing. It inspects
the project, merges these instructions, and records the project's specifics — **without
overwriting existing project instructions**.

## 4. This project's specifics

- **Product:** `<what it is, in one sentence>`
- **Primary audience:** `<who uses it>`
- **Stack:** `<language / framework / runtime>`
- **How to run the app locally:** `<command and URL>`
- **How to run the tests:** `<command>`
- **Type check / lint / build:** `<commands>`
- **Existing identity to preserve:** `<brand colours / type / conventions, or "none yet">`
- **Project `DESIGN_BRIEF.md`:** `<path, or "to be created">`

## 5. Non-negotiables (summary — the constitutions govern)

### Engineering
- **Never report work as done that you have not verified.** Run the checks; report the exact
  commands and results.
- **No fake functionality** — no dead buttons, no stubbed handlers, no fake success states, no
  fabricated production data.
- **Preserve existing working features.** Do not regress behaviour outside the scope.
- **Security by default** — least privilege, validate untrusted input at the boundary, check
  authorization at the object level, never expose secrets.
- **Keep changes focused.** One concern per change; no drive-by refactors.
- **Independent review before delivery** — review your own change as a separate senior engineer.

### Design (any UI work)
- **Generic is a failure state.** Rework anything that could be a default template with a swapped
  logo.
- **WCAG 2.2 AA is the minimum**; verify contrast and keyboard access rather than assuming.
- **Define all interaction states**: default, hover, focus-visible, active, disabled, loading,
  empty, error, success, and content extremes.
- **Verify responsive behaviour** at mobile, tablet, and desktop; reflow, do not just shrink.
- **Actually look at the rendered interface in a browser** and take a screenshot. If you cannot,
  say so; never claim visual verification you did not perform.
- **Preserve this project's own visual identity** — the constitution sets the quality bar, not a
  shared house style.

### Delivery
- Do not commit, push, merge, deploy, or release unless the task authorises it and verification
  has passed. Never push directly to `main`/`master`.

## 6. Memory

Record durable, non-obvious decisions and constraints in project memory
(`.openhands/memory/`): the constraint, the decision, and the reason. Do not record secrets, and
do not record trivially re-discoverable facts.
