# Global Design Intelligence — account memory block

This is the block that carries the standard into **every new conversation, in every project**.

## How account memory actually works (verified, 2026-10-29)

There is **no "Memory" text box in the OpenHands settings UI** — the Memory section contains a
single toggle ("Persistent memory" = `load_memory`). Do not look for a paste target there.

Account memory is the **user memory file**, `~/.openhands/memory/MEMORY.md`. Its content is
injected into each new conversation as the `<MEMORY_CONTEXT>` block. It is populated from disk, so
the way to set it is to put the text in that file:

1. Append the block below to the **end** of `~/.openhands/memory/MEMORY.md`.
2. In a conversation whose workspace is available, edit that file with the **`file_editor` tool**
   (not `bash`). A `MemoryChangeCallbackProcessor` detects `MEMORY.md` writes made via
   `file_editor` and persists the new content to your account record. A plain shell `cp`/`echo`
   does **not** trigger it.

The public settings API accepts a `memory_context` field with HTTP 200 but **silently ignores it**
— verified: the value is unchanged after the POST. `POST /api/v1/settings` persists the
`load_memory` flag and skills, not the memory text.

### The truncation rule — put this block LAST

The SDK's own memory instructions say: *"Keep the indexes concise (aim under ~6000 characters
combined; **older top content is truncated first**)."* Measured: only roughly the **last ~100 lines
(~3000 characters)** of each tier survive into the prompt. Content near the top of `MEMORY.md` is
dropped. **Therefore the GDI block must be at the very end of the file**, after all other notes.
Putting it first — the intuitive choice — makes it invisible.

Keep the block short; it points to the full standard rather than duplicating it. One block, set
once, then it follows you into every project.

---

## The block (append this to the END of `~/.openhands/memory/MEMORY.md`)

```markdown
## Global Design Intelligence (GDI) - mandatory for ALL UI work, every project
Source of truth: https://github.com/itzebe/design-intelligence — read DESIGN_CONSTITUTION.md there
(companions: DESIGN_TOOLKIT.md, VISUAL_QA_CHECKLIST.md, templates/). If unreachable, apply this core:
- Generic is a failure state. If the result could be a default template with the logo swapped,
  rework it before reporting done.
- Before writing UI code, state the visual direction: type scale, spacing rhythm, one accent, and
  the one thing this interface should be remembered for. Product-first; smallest interface that
  does the job. Do not give a finance tool, a travel app, and a storefront the same treatment.
- Banned unless the project already uses them: purple/indigo/blue-pink gradients, glassmorphism,
  glow/neon, decorative blobs, emoji as icons, uniform rounded-2xl+shadow-xl cards,
  hero -> three identical cards -> CTA, low-contrast gray-on-gray body text.
- Define every state: default, hover, focus-visible, active, disabled, loading, empty, error,
  success. Never remove focus rings. Respect prefers-reduced-motion.
- Responsive: verify mobile, tablet, desktop. Reflow, do not shrink. Usable at 320px and 400% zoom.
  Touch targets >= 44x44 CSS px.
- Accessibility: WCAG 2.2 AA is the minimum - text contrast >= 4.5:1 (>= 3:1 large), non-text
  >= 3:1, full keyboard operability, labels tied to inputs, correct heading order.
- Preserve each project's own visual identity. This sets the quality bar, not a shared house style.
- Verify honestly: open the rendered UI in a real browser, screenshot it, check mobile and desktop,
  run the relevant tests, and say plainly what you could not verify. Never fabricate content.
```

This is deliberately shorter than the constitution. The full non-negotiable core lives in
`DESIGN_CONSTITUTION.md`; the memory block only has to be enough to make an agent stop, load the
constitution, and apply it. Keeping it under ~1800 characters means it fits inside the truncation
window even when other notes sit above it.

---

## Keeping it current

When `DESIGN_CONSTITUTION.md` changes, update this block if the change touches the core, then
re-apply it to `~/.openhands/memory/MEMORY.md` with `file_editor`. The block is a summary; the
repository is the source of truth.
