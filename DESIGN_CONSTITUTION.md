# Design Constitution

> Canonical, versioned standard for every user interface produced, modified, or reviewed
> under this account. This document is the single source of truth. Skills, templates, and
> project briefs must not contradict it; where they are silent, this document governs.
>
> **Version:** 1.0.0 · **Status:** Active · **Applies to:** all projects, all conversations,
> all agents. A one-line CSS tweak is covered exactly as much as a full redesign.

---

## 0. How to use this document

1. Read it **before** writing or changing any UI code.
2. Apply it as a gate (Section 2) and as an acceptance bar (Sections 4–12).
3. A project's own `DESIGN_BRIEF.md` may **specialise** this constitution for that product
   (its audience, its visual direction, its references). A project brief may never **weaken**
   a mandatory rule here — accessibility, honesty, verification, and the anti-slop rules are
   non-negotiable.
4. When this constitution and a project instruction disagree on a *mandatory* item, this
   constitution wins. When they disagree on *taste*, the project's existing identity wins.

The objective is to create products that feel deliberately designed, not merely generated.

---

## 1. Product-first design

Design serves the product and the person using it. Nothing else.

- Start from **what the product is, who uses it, and what job it does**. If you cannot state
  these in two sentences, you are not ready to design.
- Every visual and interaction decision must be traceable to a user need or a product goal.
  "It looks nice" is not a justification on its own.
- Identify the **primary task** of each screen and make it the most obvious thing on the page.
- Design for the **real content**: real labels, real numbers, real names — or clearly marked
  placeholders that never masquerade as real data (Section 12).
- Prefer the smallest interface that accomplishes the job. Remove anything that does not earn
  its place.
- A financial tool, a travel assistant, a developer tool, and a storefront should **not** receive
  the same treatment. Composition must fit the product's purpose.

---

## 2. The gate: before you write any UI code

Do not open an editor first. Produce these two things in your reply, briefly:

1. **The three most important design weaknesses** in what exists today. If there is no existing
   UI, say what the product actually is and who uses it.
2. **The visual direction in one or two lines:** the typographic choice, the spacing rhythm, the
   single accent, and the one thing this interface should be remembered for.

Then build. Skipping the gate is the most common cause of generic output.

**The one rule that matters most:** Generic is a failure state. If the result could have been
produced by a default template with the logo swapped, you have not finished. Rework it before
reporting done.

---

## 3. Art direction and reference research

- Before styling, decide a **point of view**. Name the mood, the reference class, and the
  constraint that makes it distinct. One strong idea executed well beats five effects stacked.
- **Research references** when you can: real products in the same category, editorial or
  industrial design, print typography, film colour, architecture. Extract *principles*
  (proportion, rhythm, contrast, hierarchy), not pixels to copy.
- **Never clone a competitor's identity.** Use references to raise the ceiling, not to
  reproduce a look.
- Art direction is a decision, not decoration. If a treatment does not reinforce the product's
  meaning, cut it.
- Respect and extend the **existing brand** (Section 8) unless a change is explicitly requested
  or clearly justified by a product need.

---

## 4. Typography and composition

- Use a **type scale with real steps** — a deliberate relationship between sizes and weights,
  not arbitrary values.
- Set **line height and measure for reading**, not to fill a container. Aim for a comfortable
  measure (roughly 45–75 characters for body text); never long lines over ~75 characters.
- Use **no more than two or three typefaces**, with clear roles (display / text / mono).
- **Hierarchy must be legible without being told:** a reader knows what matters first, second,
  third from size, weight, spacing, and position alone.
- Establish **one spacing rhythm** and apply it consistently. Whitespace groups and separates;
  it is not equal padding on every box.
- Use **one accent colour that means something**; neutrals do the structural work.
- Compose with intent: asymmetry, alignment, and negative space are tools, not accidents.
- Avoid oversized display headings that carry no meaning, and text that is large only to fill
  space.
- Avoid centred text across full-width paragraphs.

---

## 5. Avoid generic AI-generated design

These are the tells of generated UI. **Do not use them** unless the product's existing identity
already uses them, or you can justify the specific choice in writing.

- Purple, indigo, violet, or blue-to-pink gradients; rainbow and "aurora" mesh backgrounds.
- Glassmorphism, frosted-blur panels, and translucent cards used as decoration.
- Glowing borders, neon shadows, and coloured box-shadow halos.
- Decorative blobs, floating orbs, and abstract SVG shapes with no informational purpose.
- Emoji used as interface icons or bullet markers.
- The same `rounded-2xl` + `shadow-xl` + `p-6` treatment on every element on the page.
- The centred hero, then three identical feature cards with an icon on top, then a CTA band.
- Every section the same height, the same background, and the same visual weight.
- Animations on everything, hover transforms on static content, and easing used as a substitute
  for hierarchy.
- Fabricated metrics, fake user counts, invented testimonials, and placeholder logos presented
  as real customers.
- Low-contrast gray-on-gray body text that looks tasteful and is hard to read.

**Restraint is the default.** One strong idea executed well beats five effects stacked.

---

## 6. Interaction design and meaningful UI states

Every interactive surface must define and visually distinguish a full set of states:

- **Default, hover, focus-visible, active, disabled** — each visibly distinct, with a visible
  focus ring that is never removed.
- **Loading** — including the empty-and-loading case; use skeletons or progress that reflect the
  real layout, not a spinner pasted in the middle.
- **Empty** — never a blank panel; offer a useful next action.
- **Error** — say what went wrong and what to do next, in plain language, near the cause.
- **Success** — confirm routine actions inline; do not interrupt with a modal celebration.
- **Content extremes** — overflowing labels, missing avatars, very long names, very short ones.

Interaction rules:

- Every action gives immediate feedback.
- Destructive actions are hard to trigger by accident and recoverable where possible.
- Motion clarifies state change and nothing more; respect `prefers-reduced-motion`.
- Keyboard and pointer are equal citizens (Section 7).

---

## 7. Responsive design and accessibility (WCAG 2.2 AA)

### Responsive

- Design and verify at **mobile, tablet, and desktop** widths. Reflow rather than shrink.
- Content is readable and operable without horizontal scrolling at 320 px width and at 400 %
  zoom.
- Touch targets are large enough on mobile (aim for at least 44×44 CSS px).
- Layouts adapt structure, not just scale: navigation, tables, and dense data reflow sensibly.
- No fixed pixel widths that break narrow viewports; no content hidden on small screens that a
  user needs.

### Accessibility — WCAG 2.2 Level AA is the minimum

- **Perceivable:** text contrast at least 4.5:1 (normal) and 3:1 (large); non-text UI contrast at
  least 3:1; images have meaningful `alt` or are marked decorative; never encode meaning in
  colour alone.
- **Operable:** everything keyboard reachable and operable; visible focus indicators; no keyboard
  traps; sensible focus order; skip links for repeated navigation.
- **Understandable:** labels tied to inputs; errors identified and described; consistent
  navigation and identification; help for non-obvious input.
- **Robust:** semantic HTML; correct roles, names, and states; works with assistive technology;
  correct heading order (one `h1`, no skipped levels).
- Respect `prefers-reduced-motion` and `prefers-color-scheme` where a dark mode exists.
- Check contrast and semantics **rather than assuming** (see `VISUAL_QA_CHECKLIST.md` and
  `DESIGN_TOOLKIT.md`).

---

## 8. Preserve identity

- Keep the existing **brand colours, type, and component conventions** unless a change is
  explicitly requested or justified by a clear product need.
- If you believe the identity itself is the problem, **say so and propose the change** rather
  than silently restyling.
- Do not force all applications to share the same visual identity. The constitution sets the
  *quality bar*, not a house style. Each product gets its own direction (Section 3).

---

## 9. Engineering quality

- **Semantic HTML first.** Buttons are `<button>`, links are `<a>`, labels are tied to inputs,
  headings are in order, lists are lists.
- Use **consistent design tokens** for type, spacing, and colour. No magic numbers scattered
  through the code.
- Keep changes **inside the requested scope**. Do not delete working features or refactor
  unrelated code to achieve an effect.
- **Do not add dependencies** without a clear, justified need (see `DESIGN_TOOLKIT.md` for
  tool-selection rules). Prefer existing dependencies and free alternatives.
- **Do not modify unrelated application functionality** to add design tooling.
- Write accessible, maintainable markup and styles; keep comments purposeful, not decorative.
- Respect the framework's idioms and the project's existing conventions.
- Prefer CSS for state and layout over JavaScript where practical.

---

## 10. Design tools and tool-selection rules

Full detail lives in **`DESIGN_TOOLKIT.md`**. The governing rules:

- **Use what the project already has first.** Check `package.json`, existing config, and CI
  before proposing anything new.
- **Prefer free and open tools.** No tool may require a paid account or a personal computer.
- **Do not install all tools automatically.** Install a tool only when the task needs it and the
  user or project context allows it.
- **Justify every addition.** A tool earns its place only if it improves design quality,
  accessibility, or verification in a way the existing stack cannot.
- **Do not break the app to add tooling.** Tooling must not change product behaviour.
- Candidates, in order of default preference: the built-in browser tools and a headless Chromium
  for screenshots; **Playwright** for scripted visual/interaction checks; **axe-core** for
  automated accessibility; **Lighthouse** for performance and accessibility audits; **Figma** for
  specifications/prototyping *when accessible*; **Storybook** for a component system *when
  justified*.

---

## 11. Actual browser-based visual inspection

Rendering is the only honest test of a visual change.

- After implementing, **open the real interface in a browser** and look at it. Take a screenshot
  and inspect the actual pixels.
- Check **mobile, tablet, and desktop** viewports, and the states from Section 6.
- Compare against the original and against the stated direction from the gate.
- Re-read your own markup and styles **as a critic**, fix the most significant remaining problem,
  and repeat until it holds up.
- **If no browser is available, say so plainly.** Never claim visual verification you did not
  perform.

---

## 12. Design critique and refinement

- Critique the work, not the author. Be specific: name the element, the problem, and the fix.
- Prioritise by impact: hierarchy and clarity first, polish last.
- After the first pass, ask: *what is the single most significant remaining problem?* Fix that,
  then look again.
- Verify honesty (Section 13) as part of critique — remove anything fabricated.
- Stop when the interface is coherent, accessible, and clearly deliberate; do not gild.

---

## 13. Evidence-based verification and honest reporting

- **Do not claim work you did not verify.** No "looks great" without having looked.
- **Do not inflate quality.** State the real state of the work, including what is still weak.
- **Do not present a first draft as finished** when meaningful improvements remain.
- **No fabricated content.** Real metrics, or clearly labelled placeholders. Never invented
  testimonials, customers, or usage numbers.
- Report **what you verified and what you did not**, and how (which tool, which viewport, which
  check).
- Run the relevant tests after implementation and report the result (Section 9, and
  `VISUAL_QA_CHECKLIST.md`).

---

## 14. Persistent design memory across projects

Design intelligence must survive between sessions and between projects.

- The durable layers and their **verified** reach are described in `DESIGN_TOOLKIT.md` §5 and the
  repository `AGENTS.md`. In short: the canonical text lives in this file (source of truth); the
  short core block is mirrored into **OpenHands account memory**, which is verified to reach every
  new conversation in every project; each project's `AGENTS.md` carries the standard into that
  project; and the account skill is kept as a best-effort fallback.
- When you learn something **durable and non-obvious** about design in a project — a constraint,
  a preference, a decision and its reason — record it in project memory. Do not record secrets,
  and do not record trivially re-discoverable facts.
- When this constitution changes, update the version header, the account-memory block
  (`ACCOUNT_MEMORY.md`), and the mirrored account skill so the layers never drift.

---

## 15. Execution and safety

- Do not commit, push, merge, deploy, or take other consequential external actions unless the
  task authorises them **and** the required verification has passed.
- Never store credentials, API keys, or private tokens in this constitution, its templates, or
  any repository that mirrors it.

---

*End of constitution. This file is the canonical source of truth for design quality under this
account.*
