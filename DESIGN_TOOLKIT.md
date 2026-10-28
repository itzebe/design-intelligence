# Design Toolkit

Practical tools for design, accessibility, and **real visual verification** — and when to use
each. Companion to `DESIGN_CONSTITUTION.md` (which governs) and `VISUAL_QA_CHECKLIST.md` (which
is the checklist).

> **Governing rules (from the constitution §10):** use what the project already has first;
> prefer free and open tools; do not install everything automatically; justify every addition;
> never break the app to add tooling; never require a paid account or a personal computer.

---

## 1. Tool-selection rules

1. **Inventory first.** Read the project's `package.json`, existing config, and CI workflows.
   The project's own stack wins.
2. **Install on demand, for a task.** A tool is installed when a specific job needs it, not
   preemptively.
3. **Justify.** If a tool is added, note in the reply *why* and *what it verifies*.
4. **Free and local.** No paid accounts, no cloud-only tools required to complete the work.
5. **Non-invasive.** Tooling must not change product behaviour or add runtime dependencies to
   the app.
6. **Verify, then report.** A tool you ran is evidence; a tool you merely mention is not.

---

## 2. Tool catalogue

### 2.1 Browser automation and screenshots — **Playwright** (preferred)

- **What it is:** a free, open-source framework to drive real browsers (Chromium, Firefox,
  WebKit) headlessly, take screenshots, and assert on the rendered DOM.
- **Use it when:** you need repeatable visual evidence, multiple viewport widths, interaction
  states (hover/focus/open menu), or visual regression between runs.
- **Install (only when needed):** `npx playwright install chromium` (plus the `@playwright/test`
  package if not already present). In this environment Chromium already exists at
  `/usr/bin/chromium`, but Playwright needs its own browser download.
- **Evidence it produces:** PNG screenshots at named viewports; console/network errors; DOM
  assertions.
- **Notes:** browsers download into an **ephemeral** `$HOME/.cache/ms-playwright`; after a sandbox
  restart you must re-run `npx playwright install chromium`.

### 2.2 Built-in browser tools — **always available, use first**

- **What they are:** the agent's own `browser_*` tools (navigate, get state, screenshot, click,
  type, read storage). They need no install.
- **Use them when:** you need a quick, real look at a running page, or to drive a short flow and
  capture a screenshot — especially on a phone-first workflow where you want evidence without
  writing a test.
- **Evidence:** page state, content, and screenshots.
- **Prefer these over installing Playwright for one-off looks.** Reach for Playwright when you
  need repeatability across many viewports or CI.

### 2.3 Accessibility — **axe-core** (preferred automated check)

- **What it is:** the free, open-source accessibility rules engine behind many a11y tools.
- **Use it when:** you want an automated sweep for contrast, names/roles, labels, landmark and
  heading issues.
- **Install (only when needed):** `npm i -D @axe-core/playwright` (with Playwright) or inject the
  `axe-core` script into a page.
- **Evidence:** a list of violations with impact and the offending selectors.
- **Limits:** automated checks catch only a subset of WCAG. They never replace manual keyboard
  and screen-reader reasoning (see the checklist).

### 2.4 Audits — **Lighthouse**

- **What it is:** Google's free audit tool for performance, accessibility, best practices, and
  SEO, runnable headlessly.
- **Use it when:** you need a broad accessibility/performance score and concrete findings, e.g.
  before shipping a page.
- **Install (only when needed):** `npx lighthouse <url> --output=json` (Chromium already present).
- **Evidence:** category scores and per-audit findings.
- **Limits:** scores vary run to run; treat them as signals, not verdicts.

### 2.5 Visual specifications / prototyping — **Figma** *(only when accessible)*

- **What it is:** a design tool for specs, tokens, and prototypes.
- **Use it when:** a designer provides a Figma file and the agent can read it (via a Figma MCP
  integration or exported specs), or the user asks for a spec to hand off.
- **Constraint:** do **not** require a paid Figma account. If it is not accessible, work from
  the description, existing product, and rendered result instead.

### 2.6 Component systems — **Storybook** *(only when justified)*

- **What it is:** an isolated workshop for building and reviewing components and their states.
- **Use it when:** the project is a component library or design system, or the team already uses
  it, and the value of an isolated catalogue outweighs the setup cost.
- **Constraint:** do not add Storybook to an app that does not need it just to satisfy tooling.

---

## 3. Choosing the right tool

| Goal | Default choice |
|------|----------------|
| A quick real look at a running page | **Built-in browser tools** |
| Repeatable screenshots across viewports / states | **Playwright** |
| Automated accessibility sweep | **axe-core** (via Playwright or injected) |
| Broad a11y + performance audit | **Lighthouse** |
| Read a designer's spec / prototype | **Figma** — only if accessible |
| Document components and states | **Storybook** — only if justified |

Rule of thumb: **built-in browser tools first; Playwright when you need repeatability;
axe-core and Lighthouse when you need a systematic audit; Figma and Storybook only when the
project already lives there or the user asks.**

---

## 4. What "real visual verification" means here

A change is visually verified only when **all** of the following are true:

1. The app runs and the page is opened in a real browser.
2. You looked at an actual screenshot or live render — not just the source.
3. You checked at least mobile and desktop widths (tablet when layout changes there).
4. You exercised the meaningful states (Section 6 of the constitution).
5. You ran the relevant automated checks available to you (axe/Lighthouse/tests).
6. You can state plainly what you verified and what you did not.

If any of these were impossible, **say which**, and do not claim the verification.

---

## 5. Persistence: how the constitution reaches future sessions

Four layers carry the standard. Which ones actually reach a fresh conversation was **measured**,
not assumed — the "Verified" column records what a real fresh conversation received.

| # | Layer | Mechanism | Verified reaching a fresh conversation? |
|---|-------|-----------|------------------------------------------|
| 1 | **Account memory** | OpenHands account memory (settings → Memory), injected as a `<MEMORY_CONTEXT>` block | **Yes.** Verified in a brand-new cloud sandbox and in a GUI-launched session. |
| 2 | **Project `AGENTS.md`** | Repo-root `AGENTS.md`, injected as a context block | **Yes.** Verified: root `AGENTS.md` content appeared in a new conversation's context. |
| 3 | **Project skills** | `.agents/skills/<name>.md` (flat file) in the repo | **Yes.** Verified. (Directory form `.agents/skills/<name>/SKILL.md` was discovered but did not reach the prompt — prefer the flat file.) |
| 4 | **Account skill** | A custom skill in the account agent context | **No — in this deployment.** Verified negative: a custom account skill stored in `agent_settings.agent_context.skills` was **not** merged into a GUI-launched session or a freshly API-launched cloud conversation. Public catalogue skills *are* loaded automatically; custom account skills are not. |

### What this means in practice

- **The durable, cross-project channel is account memory (layer 1).** Because a custom account
  skill is not auto-injected here, put the *core* of the standard (the gate, the anti-slop list,
  accessibility minimum, verification rule, and a pointer to the full text) into account memory.
  That is what every new conversation, in every project, will actually receive.
- **Per-project enforcement is `AGENTS.md` (layer 2).** Copy `templates/AGENTS.md` into each
  project so the standard is present there too, with the project's own specifics.
- **The canonical repository is the source of truth** for the full text, and the place account
  memory and project files point to.
- **The account skill (layer 4) is kept anyway** — it is harmless, is the documented OpenHands
  mechanism, and will work if a future deployment starts injecting account skills. Do not rely on
  it alone.

Account memory is written through the OpenHands **settings UI (Memory)**. The public settings API
accepts a `memory_context` value with HTTP 200 but does **not** persist it, so this is a
one-time manual paste, not something a script can do.

**Never store credentials, API keys, or private tokens in any of these layers.**

---

## 6. Environment notes (this OpenHands sandbox)

Discovered during setup; useful to know before relying on a tool:

- Only `/workspace` is a persistent volume. `$HOME` and `/tmp` are **ephemeral** — anything a tool
  installs there is lost on a sandbox restart.
- Chromium is present at `/usr/bin/chromium`. Playwright browsers are **not** installed by
  default and must be re-installed after a restart.
- The agent's built-in browser tools require no installation and are the fastest path to a real
  screenshot.
- Always load project secrets in a **subshell** so they do not leak into the test environment.
