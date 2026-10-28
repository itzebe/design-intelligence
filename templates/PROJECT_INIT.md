# PROJECT_INIT.md — starting or redesigning a project

> **Template / workflow.** The ordered procedure an agent follows when beginning UI work on a
> new or existing project. It is referenced by `templates/AGENTS.md` and enforced by
> `DESIGN_CONSTITUTION.md`. It **preserves project-specific requirements** and **does not force
> all applications to share the same visual identity** — each project defines its own direction
> in step 6.

Follow the steps in order. Do not skip the gate (steps 3–6) before writing UI code.

---

## Step 1 — Load the constitution

The short core of the standard is already in your context as a `<MEMORY_CONTEXT>` block (the
"Global Design Intelligence" section) — it applies here. For the full text, read, in order:
`DESIGN_CONSTITUTION.md`, `DESIGN_TOOLKIT.md`, `VISUAL_QA_CHECKLIST.md`. If the local copy is
absent, retrieve the canonical versions from `<CANONICAL_REPO_URL>`. State which source you used,
or say plainly that the full text was not reachable.

## Step 2 — Inspect existing project instructions

Read the repository's `AGENTS.md`, any `DESIGN.md` / `DESIGN_BRIEF.md`, `README`, contribution
rules, and existing agent/memory files. **Do not overwrite them.** If a `DESIGN_BRIEF.md` exists,
update it rather than replacing it. Merge, never clobber.

## Step 3 — Understand the product and its audience

Write, briefly: what the product is, who uses it, the job it does, and the context of use
(device, frequency, stakes). If there is no product yet, state the intended one. This is the
foundation every later decision rests on.

## Step 4 — Inspect existing functionality and design conventions

- Inventory the stack: framework, styling approach, design tokens, component library, existing
  pages/components.
- Note the current visual identity (colours, type, spacing) — it must be preserved unless a change
  is explicitly requested (constitution §8).
- Identify what already works so you do not regress it.
- Note the tests and how to run the app.

## Step 5 — Create or update the project `DESIGN_BRIEF.md`

Copy `templates/DESIGN_BRIEF.md` to the project root and fill it in from steps 3–4. This brief
specialises the constitution for **this** product. Keep it specific; do not restate the whole
constitution.

## Step 6 — Define a distinct visual direction

Complete the constitution's gate (§2): the three most important weaknesses (or a product
description), and the direction — typography, spacing rhythm, single accent, and the one thing
this interface should be remembered for. Add references (step 7). **This direction is unique to
this product;** do not import another project's identity.

## Step 7 — Identify relevant design references

Collect real references (products in the category, editorial/industrial design, print typography,
film colour, architecture). Record *what principle* each contributes. Never clone a competitor's
identity.

## Step 8 — Implement without unnecessary rewrites

- Work inside the requested scope; preserve unrelated functionality.
- Use semantic HTML and consistent tokens.
- Implement all interaction states (constitution §6).
- Add no dependency without justification (constitution §10).
- Do not restyle beyond the direction you stated, and do not break working features.

## Step 9 — Inspect the actual rendered interface

Run the app, open it in a real browser, and **look at it**. Take screenshots at mobile, tablet,
and desktop widths; exercise the states. See `DESIGN_TOOLKIT.md` §4 for what "real visual
verification" requires. If no browser is available, say so.

## Step 10 — Correct visual and functional defects

Compare against the original and the stated direction. Fix the most significant problem first,
then look again. Complete `VISUAL_QA_CHECKLIST.md`; every line is pass, fail, or n/a-with-reason.

## Step 11 — Run relevant tests and report

Run the project's tests and any automated a11y checks available. Report:

- What you verified (and with which tools, at which widths).
- What you did **not** verify, and why.
- Test results.
- Remaining weaknesses, honestly.

Then, and only then, consider committing/pushing if the task authorises it.

---

### Quick reference: the eleven steps

1. Load the constitution. 2. Inspect existing instructions (merge, don't overwrite).
3. Understand product + audience. 4. Inspect functionality + conventions.
5. Create/update `DESIGN_BRIEF.md`. 6. Define a distinct direction.
7. Identify references. 8. Implement without unnecessary rewrites.
9. Inspect the rendered interface. 10. Correct defects.
11. Run tests and report.
