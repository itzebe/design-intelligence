# Development Workflow

> The standard, ordered workflow for **every** development task under this account — a feature, a
> bug fix, a refactor, a security fix, or a UI change. It turns `ENGINEERING_CONSTITUTION.md` and
> `DESIGN_CONSTITUTION.md` into a repeatable sequence.
>
> **Version:** 1.0.0 · **Status:** Active · **Applies to:** all projects, all conversations.

Follow the steps in order. The depth of each step scales with the task; the steps themselves do
not get skipped. A one-line fix still gets a two-line Discovery and a real Verification.

---

## Step 1 — Discovery

- Verify the **repository**, the **branch**, and the **working tree state**.
- Inspect the project structure and the relevant implementation.
- Read the project's own instructions: `AGENTS.md`, `README`, `CONTRIBUTING`, architecture and
  design docs, and `.openhands/memory/`.
- Locate the entry points, the business logic, the data access, and the tests for the area.
- Identify **risks**: what could break, what is untested, what is security-sensitive, what is on a
  hot path.
- State the blast radius of the intended change.

## Step 2 — Requirements

- Restate the objective in one or two sentences.
- Define **acceptance criteria** as observable, checkable statements ("X returns Y when Z").
- Identify **constraints**: compatibility, performance, security, platform, deadline, existing
  conventions.
- Identify **affected functionality** beyond the immediate target.
- If the objective is ambiguous, resolve the ambiguity (ask, or state your assumption explicitly)
  before implementing.

## Step 3 — Design and architecture

- Define the **implementation strategy** — the shape of the change, not yet the code.
- Confirm it fits the existing architecture (`ENGINEERING_CONSTITUTION.md` §2). Prefer the
  smallest change that fully solves the problem.
- When **frontend work** is involved, establish the **visual direction** first, per
  `DESIGN_CONSTITUTION.md` §2 (the gate): the product, the audience, the primary task, the
  typographic and spacing direction, the single accent, and the one thing to be remembered for.
- Consider **security, scalability, and maintainability** explicitly: trust boundaries, failure
  modes, data volume, and who will read this code next.
- Decide the **verification plan**: which checks and which evidence will prove the change works.

## Step 4 — Implementation

- Make **focused** changes. One concern per change.
- **Avoid unrelated modifications** — no drive-by refactors, reformats, or renames.
- **Preserve working functionality.** Do not regress behaviour outside the scope.
- **Follow existing conventions** — naming, structure, error handling, and style.
- Implement the complete functionality: no stubs, no dead controls, no fake success states
  (`ENGINEERING_CONSTITUTION.md` §3).
- Validate input at the boundary; handle errors explicitly; implement loading, empty, and error
  states.
- Add or update tests **with** the code, not after.

## Step 5 — Verification

- Run the relevant tests and the project's standard checks: unit, integration, end-to-end, type
  check, lint, build, and security checks (`ENGINEERING_CONSTITUTION.md` §6).
- **Verify actual application behaviour**, not only that the code compiles. Run it and exercise
  the changed path.
- When **UI changes** are involved, inspect the **rendered interface in a browser** and take
  screenshots at mobile, tablet, and desktop widths, exercising the meaningful states
  (`DESIGN_CONSTITUTION.md` §11).
- Review for **security and regressions**.
- **Fix every failure you discover** and re-run. Do not report a failing check as done.
- Record the exact commands and their exact results.

## Step 6 — Independent review

Review the change as a **separate senior engineer** who did not write it. Ask:

- Is this actually **production-ready**?
- Is the **architecture** appropriate?
- Is the **UI distinctive** (not generic), and does it match the stated direction?
- Are **all interactions functional** — nothing dead, stubbed, or faked?
- Are there **security weaknesses** — unvalidated input, an authorization gap, a leaked secret?
- Are there **hidden regressions** outside the touched code?
- Have **all acceptance criteria** been satisfied, with evidence for each?

Fix what the review finds, then re-verify. State plainly what the review could not settle.

## Step 7 — Delivery

Report, factually:

- **What changed** and why.
- **Files modified** (created / changed / deleted).
- **Tests executed** — exact commands.
- **Test results** — counts and outcome.
- **Visual QA evidence** — what was inspected, at which widths (UI work only).
- **Security findings** — what was checked, what remains open.
- **Remaining limitations** — the honest list.
- **Commit and PR references**, and **deployment evidence**, where applicable.

**Never claim completion without evidence.** A truthful "unverified, and here is why" beats a
confident summary that cannot be backed up.

---

## Quick reference

| # | Step | Output |
|---|------|--------|
| 1 | Discovery | Repo/branch/tree verified; risks and blast radius named |
| 2 | Requirements | Objective, acceptance criteria, constraints |
| 3 | Design | Strategy; visual direction for UI; verification plan |
| 4 | Implementation | Focused, complete, convention-matching change + tests |
| 5 | Verification | Checks run, app exercised, UI inspected, failures fixed |
| 6 | Independent review | Adversarial self-review; findings fixed |
| 7 | Delivery | Honest, evidence-backed report |

**Scaling rule.** The steps are constant; their weight is proportional. A typo fix is a short
Step 1, a one-line Step 2, and a real Step 5 (does it still build and pass?). A new feature is
all seven steps in full. Skipping Step 5 or Step 6 is never allowed.
