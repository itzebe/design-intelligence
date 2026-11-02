# PROJECT_ONBOARDING.md — onboard any repository to the account standards

> **Template / procedure.** The reusable onboarding template applied to **every** repository
> before implementation begins. It makes a project inherit the account-wide engineering and
> design standards **without overwriting that project's own instructions**.
>
> **Version:** 1.0.0 · **Applies to:** every new and existing repository under this account.

The two canonical standards this template binds a project to:

- `ENGINEERING_CONSTITUTION.md` — how software is built, secured, tested, and delivered.
- `DESIGN_CONSTITUTION.md` — how interfaces are designed, built, and verified.
- `DEVELOPMENT_WORKFLOW.md` — the seven-step workflow every task follows.

Canonical source repository: `<CANONICAL_REPO_URL>` (e.g.
`https://raw.githubusercontent.com/itzebe/design-intelligence/main/`).

---

## 0. Onboarding rules (non-negotiable)

1. **Inspect before writing.** Never overwrite an existing `AGENTS.md`, `DESIGN_BRIEF.md`, or
   project instruction file. Read it, then **merge**.
2. **Merge, never clobber.** Project-specific instructions **supplement** the account standards.
   They may specialise them (stack, commands, conventions) but may never weaken a mandatory rule
   (security, honesty, verification, accessibility, no-fake-functionality).
3. **Conflict resolution.** On a *mandatory* item, the constitution wins. On *style*, the
   project's existing convention wins.
4. **No secrets** in any onboarding file, ever.
5. **Leave the project runnable.** Onboarding adds instructions and, at most, a brief file — it
   does not change product behaviour.

---

## 1. Discovery checklist

Complete before writing any code. Record the answers.

### Repository state
- [ ] Repository name and purpose stated in one sentence.
- [ ] Default branch identified; current branch and working-tree state verified.
- [ ] Existing agent instructions found: `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.cursorrules`,
      `.agents/`, `.openhands/memory/`, `CONTRIBUTING.md`, `README`.
- [ ] Existing design/architecture docs found (`DESIGN.md`, `DESIGN_BRIEF.md`, `docs/`).
- [ ] **Nothing existing was overwritten** — confirmed.

### Stack and architecture
- [ ] Language(s), framework(s), and runtime version.
- [ ] Package manager and how dependencies are installed.
- [ ] Entry points, main modules, and where business logic lives.
- [ ] Data stores, external services, and third-party APIs used.
- [ ] Build system and output.
- [ ] Architecture pattern and layering conventions.

### Quality gates already present
- [ ] Test framework(s) and the exact command to run them.
- [ ] Type-check command.
- [ ] Lint and format commands.
- [ ] Build command.
- [ ] CI workflows and what they enforce.
- [ ] Security tooling already configured (audit, secret scanning, SAST).

### Frontend (if applicable)
- [ ] Styling approach (CSS, Tailwind, CSS-in-JS, component library).
- [ ] Design tokens / theme source.
- [ ] Existing visual identity (colours, type, spacing) to preserve.
- [ ] How to run the app locally, and the URL.
- [ ] Accessibility tooling already present.

### Risk
- [ ] Security-sensitive surfaces (auth, payments, PII, file upload, admin routes).
- [ ] Untested or fragile areas.
- [ ] Performance-critical paths.
- [ ] Data-migration or destructive-tooling risks.

---

## 2. Bind the project to the standards

Create or merge a repository-root **`AGENTS.md`** from `templates/AGENTS.md`. It must:

- Point at `ENGINEERING_CONSTITUTION.md`, `DESIGN_CONSTITUTION.md`, and `DEVELOPMENT_WORKFLOW.md`.
- Record the project's own specifics (product, audience, stack, commands, conventions).
- State that the account standards are mandatory and that project notes supplement them.

If a UI is involved, also create a project **`DESIGN_BRIEF.md`** from
`templates/DESIGN_BRIEF.md`.

### Retrieval order for the standards (use the first that works)

1. **Account memory** — the short core of both standards is already in context as the
   `<MEMORY_CONTEXT>` block. It applies here; no fetch needed.
2. **Local copy in the repository** — if the constitution files exist here, read them for the
   full text.
3. **Canonical remote source** — otherwise fetch from `<CANONICAL_REPO_URL>`.

If the full text is unreachable, follow the account-memory summary and **say plainly** that the
full text could not be retrieved.

---

## 3. Development workflow

Every task in the project follows `DEVELOPMENT_WORKFLOW.md`: **Discovery → Requirements →
Design → Implementation → Verification → Independent review → Delivery.** The steps are constant;
their weight scales with the task. Steps 5 (Verification) and 6 (Independent review) are never
skipped.

---

## 4. QA requirements

From `ENGINEERING_CONSTITUTION.md` §6, for every change:

- [ ] Unit tests for changed logic.
- [ ] Integration tests for touched boundaries.
- [ ] End-to-end tests for altered user-visible flows (where the project has them).
- [ ] Type check clean.
- [ ] Lint clean.
- [ ] Build clean.
- [ ] Security checks (dependency audit; secret scan where available).
- [ ] Regression evidence that previously working behaviour still works.
- [ ] **UI work only:** rendered inspection with screenshots at mobile, tablet, and desktop
      widths, plus the `VISUAL_QA_CHECKLIST.md` pass.

Rules: never report a check you did not run; never weaken a test to pass; never mark done while a
required check fails.

---

## 5. Security requirements

From `ENGINEERING_CONSTITUTION.md` §4, confirmed for the project:

- [ ] No secrets in source, logs, errors, fixtures, or commits.
- [ ] Untrusted input validated at every boundary.
- [ ] Authorization checked at the object level on every user-owned resource, not only at the
      route.
- [ ] Public endpoints authenticated, authorized, and rate-limited where exposed.
- [ ] Authentication and session handling reviewed (cookies, expiry, logout, rotation).
- [ ] Injection prevented (parameterised queries; no string-built SQL/shell/HTML).
- [ ] Dependencies free of known, unpatched critical advisories.
- [ ] Security controls are not weakened to make a test pass.

---

## 6. Record the onboarding

- [ ] Project specifics written into the repository's `AGENTS.md`.
- [ ] Durable, non-obvious findings recorded in `.openhands/memory/` (never secrets).
- [ ] The project's own instructions preserved and merged, not replaced.
- [ ] A short note in the reply: what was onboarded, what was preserved, what remains unknown.

---

## 7. Onboarding quick reference

| Step | Action | Guardrail |
|------|--------|-----------|
| 1 | Discovery checklist | Inspect, never overwrite |
| 2 | Merge `AGENTS.md` (+ `DESIGN_BRIEF.md` for UI) | Supplement, never weaken |
| 3 | Adopt the development workflow | Steps 5–6 never skipped |
| 4 | Adopt the QA requirements | No unverified "done" |
| 5 | Adopt the security requirements | Least privilege, validate input |
| 6 | Record findings in project memory | No secrets |
