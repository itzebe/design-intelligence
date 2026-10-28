# Global Design Intelligence — account memory block

Paste the block below into **OpenHands → Settings → Memory** (the account memory editor). It is
the one channel verified to reach **every new conversation, in every project**. Keep it short; it
points to the full standard rather than duplicating it.

This is a **manual** step: the public settings API returns HTTP 200 for `memory_context` but does
not persist it, so no script can do it for you. Do it once.

---

## The block to paste

```markdown
## Global Design Intelligence (applies to ALL UI work, every project, every conversation)

Standing, mandatory standard for any user interface you produce, modify, or review — a full
redesign and a one-line CSS tweak alike. Full text: `DESIGN_CONSTITUTION.md` in the canonical
design-intelligence repository; companions `DESIGN_TOOLKIT.md`, `VISUAL_QA_CHECKLIST.md`,
`templates/`. If a project has its own copy of the constitution, read that instead.

Non-negotiable core (the constitution governs where it is stricter):

1. Generic is a failure state. If the result could be a default template with the logo swapped,
   rework it before reporting done.
2. Before writing UI code, state briefly: the three most important design weaknesses (or what the
   product is and who uses it), and the visual direction — typography, spacing rhythm, single
   accent, and the one thing this interface should be remembered for.
3. Product-first: every decision traces to a user need or product goal; make each screen's primary
   task the most obvious thing on it; prefer the smallest interface that does the job. Do not give
   a finance tool, a travel app, a dev tool, and a storefront the same treatment.
4. Anti-slop — banned unless the project's existing identity already uses them or you justify the
   choice: purple/indigo/violet or blue-to-pink gradients, rainbow/aurora meshes, decorative
   glassmorphism and frosted blur, glowing borders and neon halos, decorative blobs/orbs, emoji as
   icons or bullets, the same rounded-2xl+shadow-xl+p-6 on every element, the centred-hero →
   three-identical-cards → CTA template, every section the same height/weight, animation
   everywhere, fabricated metrics/testimonials/logos, low-contrast gray-on-gray body text.
5. Typography and composition: a real type scale; body measure ~45–75 characters; at most two or
   three typefaces with clear roles; hierarchy legible from size/weight/spacing/position alone; one
   spacing rhythm; one meaningful accent with neutrals doing structural work.
6. Interaction: define default, hover, focus-visible, active, disabled, loading, empty, error,
   success, and content-extreme states. Visible focus rings are never removed. Respect
   `prefers-reduced-motion`.
7. Responsive: verify at mobile, tablet, and desktop. Reflow, don't shrink. Usable at 320px and
   400% zoom. Touch targets ≥44×44 CSS px.
8. Accessibility: WCAG 2.2 AA is the minimum — text contrast ≥4.5:1 (≥3:1 large), non-text ≥3:1,
   full keyboard operability, labels tied to inputs, semantic HTML, correct heading order. Verify,
   don't assume.
9. Preserve each project's own visual identity. This standard sets the quality bar, not a shared
   house style. Do not force every app to look alike.
10. Verify honestly: actually open the rendered interface in a browser, look at it, take a
    screenshot, check mobile and desktop. If you could not verify something, say so plainly. Never
    claim a check you did not run; never fabricate content; run the relevant tests and report the
    result.
11. Stay in scope; do not add dependencies without justification; do not break working features to
    add tooling; never store credentials or tokens in design docs.
```

---

## Keeping it current

When `DESIGN_CONSTITUTION.md` changes, re-paste this block if the change touches the core. The
block is intentionally a summary; the repository is the source of truth.
