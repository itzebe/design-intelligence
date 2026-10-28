# Visual QA Checklist

A concrete, runnable checklist to complete **before reporting any UI work done**. It turns
`DESIGN_CONSTITUTION.md` into pass/fail checks. Copy it into your reply or a project doc and mark
each line: **pass**, **fail**, or **n/a (with reason)**.

> Honest reporting rule: a box is only "pass" if you actually verified it. If you could not
> verify it, mark it **not verified** and say why. Never tick a box you did not check.

---

## A. Before implementation (the gate)

- [ ] I can state what the product is and who uses it, in two sentences.
- [ ] I listed the three most important design weaknesses in the current UI (or described the
      product if there is no UI yet).
- [ ] I stated the visual direction: typography, spacing rhythm, single accent, and the one thing
      this interface should be remembered for.
- [ ] I inspected the existing code, design tokens, and conventions.
- [ ] I confirmed the change is inside the requested scope and preserves unrelated functionality.

## B. Visual hierarchy and composition

- [ ] The primary task of each screen is the most obvious element.
- [ ] Hierarchy is legible from size, weight, spacing, and position alone.
- [ ] One consistent spacing rhythm is used throughout.
- [ ] One accent colour, used meaningfully; neutrals do the structural work.
- [ ] No more than two or three typefaces, with clear roles.
- [ ] Body text measure is comfortable (roughly 45–75 characters); no long lines over ~75.
- [ ] No oversized headings that carry no meaning.
- [ ] Sections are not all the same height, background, and weight.

## C. Anti-slop

- [ ] No purple/indigo/violet/blue-to-pink or rainbow/aurora gradients (unless justified).
- [ ] No decorative glassmorphism / frosted-blur / translucent cards.
- [ ] No glowing borders, neon shadows, or coloured halos.
- [ ] No decorative blobs/orbs/abstract shapes without informational purpose.
- [ ] No emoji used as icons or bullet markers.
- [ ] Not every element uses the same `rounded-2xl` + `shadow-xl` + `p-6`.
- [ ] Not the centred-hero → three identical cards → CTA-band template.
- [ ] Animations clarify state change only; no gratuitous hover transforms.
- [ ] No fabricated metrics, testimonials, customers, or placeholder logos.

## D. Interaction states

- [ ] Default, hover, focus-visible, active, and disabled are each defined and distinct.
- [ ] Focus is visible and never removed.
- [ ] Loading state exists, including empty-and-loading.
- [ ] Empty state exists and offers a useful next action.
- [ ] Error state says what went wrong and what to do next.
- [ ] Success is confirmed inline without a modal celebration for routine actions.
- [ ] Long/short content and missing data are handled gracefully.

## E. Responsive

- [ ] Verified at mobile width (~360–390 px).
- [ ] Verified at tablet width (~768 px).
- [ ] Verified at desktop width (~1280 px+).
- [ ] No horizontal scrolling at 320 px width or at 400 % zoom.
- [ ] Layouts reflow (structure changes), not merely shrink.
- [ ] Touch targets are at least ~44×44 CSS px on mobile.

## F. Accessibility (WCAG 2.2 AA)

- [ ] Body-text contrast ≥ 4.5:1; large text ≥ 3:1; non-text UI ≥ 3:1.
- [ ] Meaning is never conveyed by colour alone.
- [ ] Everything is keyboard reachable and operable; no keyboard traps.
- [ ] Focus order is logical; skip link for repeated navigation.
- [ ] One `h1`; headings are in order with no skipped levels.
- [ ] Inputs have associated labels; errors are described in text.
- [ ] Images have meaningful `alt` or are marked decorative.
- [ ] `prefers-reduced-motion` is respected.
- [ ] Automated a11y check run (axe-core and/or Lighthouse) — **or** manual equivalent, with the
      reason recorded.
- [ ] Screen-reader semantics sanity-checked (roles/names/states) — **or** marked not verified.

## G. Real visual verification

- [ ] The app runs and the page was opened in a real browser.
- [ ] I looked at an actual screenshot / live render (not just the source).
- [ ] Mobile and desktop were inspected (tablet too if layout changes there).
- [ ] Meaningful states were exercised.
- [ ] I compared against the original and the stated direction.
- [ ] I re-read the result as a critic and fixed the most significant remaining problem.

## H. Engineering and honesty

- [ ] Semantic HTML (buttons/links/labels/headings/lists correct).
- [ ] Design tokens used consistently; no magic numbers.
- [ ] No unnecessary dependencies added; any addition is justified.
- [ ] Unrelated functionality untouched.
- [ ] Relevant tests run, with results reported.
- [ ] I have not claimed verification I did not perform.
- [ ] Weaknesses that remain are stated plainly.

---

## Verdict line (fill this in)

> **Verified:** <what, at which widths, with which tools>.
> **Not verified:** <what remains unverified, and why>.
> **Remaining weaknesses:** <the honest list>.
