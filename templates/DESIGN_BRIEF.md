# DESIGN_BRIEF.md — `<Project name>`

> **Template.** Copy to the project root as `DESIGN_BRIEF.md` and fill it in. This brief
> **specialises** `DESIGN_CONSTITUTION.md` for this product; it never weakens a mandatory rule
> (accessibility, honesty, verification, anti-slop). Where this brief is silent, the constitution
> governs. Each project gets its **own** visual identity — do not copy another project's look.

---

## 1. Product

- **What it is (one sentence):**
- **The job it does for the user:**
- **Primary audience:**
- **Where it is used (device/context):**
- **What "done well" means for this product:**

## 2. Primary task per screen

| Screen / view | Primary task | Secondary |
|---------------|--------------|-----------|
| | | |

## 3. Existing identity to preserve

- **Brand colours:**
- **Typography:**
- **Component conventions:**
- **Anything already working that must not regress:**

## 4. Visual direction (from the gate)

- **Mood / point of view (one or two lines):**
- **Typography choice and roles:**
- **Spacing rhythm:**
- **Single accent colour and what it means:**
- **The one thing this interface should be remembered for:**
- **Explicitly rejected directions (and why):**

## 5. References

| Reference | What we take from it (principle, not pixels) |
|-----------|----------------------------------------------|
| | |

## 6. Content model

- **Real data available:**
- **Placeholders needed (clearly labelled, never fake-real):**
- **Content extremes to handle (long names, empty lists, missing avatars):**

## 7. States to implement

- [ ] default · hover · focus-visible · active · disabled
- [ ] loading (incl. empty-and-loading)
- [ ] empty (with next action)
- [ ] error (with next step)
- [ ] success (inline)
- [ ] content extremes

## 8. Responsive plan

- **Breakpoints / layout shifts:**
- **Mobile behaviour:**
- **Tablet behaviour:**
- **Desktop behaviour:**

## 9. Accessibility plan

- **Contrast targets (AA minimum):**
- **Keyboard/focus plan:**
- **Semantics plan (headings, labels, landmarks):**
- **Motion plan (`prefers-reduced-motion`):**

## 10. Tooling for this project

- **Already present (from package.json / CI):**
- **To use for verification:** built-in browser tools / Playwright / axe-core / Lighthouse / other
- **Justification for anything new:**

## 11. Verification plan

- **How the app runs:**
- **Viewports to inspect:**
- **Automated checks to run:**
- **What cannot be verified here (and why):**

## 12. Open questions / risks

-
