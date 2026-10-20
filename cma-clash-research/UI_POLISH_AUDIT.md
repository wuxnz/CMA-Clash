# better-ui spec audit (`frontend/src`)

Detection pass run after polish pass on ledger UI surfaces. Legacy editor/account flows retain some `transition-all` on floating labels (LOW); flagship paths updated.

| Severity | Location | Before | After | Why |
|----------|----------|--------|-------|-----|
| HIGH | `navbar.svelte` (theme toggle) | Full page reload on theme swap | `swapThemeClass()` + `html.theme-switching` flush | Theme-switch transition suppression |
| HIGH | `app.css` (`ledger-btn-primary`, `btn-nav`, `action-button`) | `transition-all`, `active:scale-[0.97–0.98]` | `press-scale` (0.96 / 150ms ease-out, `enabled:active`), named transition properties | Press scale + no `transition-all` on primary controls |
| HIGH | `MagneticButton.svelte` | Magnetic + press on all pointers | Magnetic only `(hover: hover) and (pointer: fine)`; hero-only usage on landing | Touch / high-frequency exclusion |
| HIGH | `scrollReveal.ts` | 28px / 650ms, no reduce fallback | 12px + 4px blur / 300ms ease-out, 100ms stagger; opacity-only under `reduce` | Staggered entrances + reduced-motion gate |
| MEDIUM | `BentoSpotlightCard.svelte` | `group-hover` spotlight always | Hover spotlight/tilt gated to fine pointer + hover media | Hover only on hover-capable pointers |
| MEDIUM | `Card.svelte` | `transition-shadow` + always-on hover glow | `card-interactive` with `@media (hover: hover)` | High-frequency card surfaces |
| MEDIUM | `RetentionBar.svelte` | `transition-all` on goal bar | `transition-[width] duration-150` | High-frequency width updates |
| MEDIUM | `leaderboard/+page.svelte` | Tab `transition` class | Instant tab background swap | Tab switches are high-frequency |
| MEDIUM | `play/title.svelte` | Gray border on cover image | `content-image` oklch outline | Image outline spec |
| MEDIUM | `glass-panel` (`app.css`) | Depth-only border | Transparent border + layered shadow ring | Shadows for elevation |
| LOW | `account/login/*`, `register`, `import` labels | `transition-all` on floating labels | Not changed (legacy forms) | Isolated polish; no interaction break |
| LOW | `lib/editor/*`, `quiztivity/*` | Various `transition-all` | Not changed | Out of flagship scope |

**Not verified:** Every modal/drawer `overscroll-behavior` in legacy editor routes (command palette / dashboard modals not exhaustively audited).

**Verdict: Approve** — no remaining HIGH issues on flagship surfaces (landing, play, leaderboard, battle demo, dashboard retention).
