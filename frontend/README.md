<!--
SPDX-FileCopyrightText: 2026 CMA Clash contributors

SPDX-License-Identifier: MPL-2.0
-->

# CMA Clash — frontend

The SvelteKit frontend of [CMA Clash](https://github.com/wuxnz/CMA-Clash), the open-source quiz
platform for CCMA and allied health exam prep.

## Requirements

- [Node.js](https://nodejs.org/) 20.19+ or 22.12+ (required by Vite 7)
- [pnpm](https://pnpm.io/) 10 (the version the CI workflow pins)
- A running CMA Clash API (see the [development docs](../frontend/src/routes/docs/develop/+page.svelte))

## Developing

```bash
pnpm install
pnpm dev

# or start the server and open the app in a new browser tab
pnpm dev -- --open
```

The dev server proxies API requests to the backend, so the app talks to a real CMA Clash API
instance while you work on it.

## Building

```bash
pnpm build
pnpm preview
```

The production build targets Vercel (`@sveltejs/adapter-vercel`). The build regenerates
`vercel.json` from the `BACKEND_URL` environment variable, so the API rewrites always match the
backend host you deploy against. See [docs/DEPLOY_VERCEL.md](../docs/DEPLOY_VERCEL.md) for the full
deployment setup.

## Quality checks

```bash
pnpm check   # svelte-check / TypeScript
pnpm lint    # prettier + eslint
pnpm test    # vitest
pnpm test:e2e # playwright
```

## Layout

| Path | What's in it |
| --- | --- |
| `src/routes/` | Pages and API routes |
| `src/lib/ui/` | Shared UI primitives (`Button`, `Card`, `PageHeader`, …) |
| `src/lib/i18n/locales/` | Translations, one JSON file per locale |
| `src/lib/cma/` | CMA Clash domain logic (text, hosts, …) |
| `e2e/` | Playwright end-to-end tests |

## Translations

Translations live in `src/lib/i18n/locales/`, one JSON file per locale code. Copy `en.json` as a
starting point, translate the values, and open a pull request. See
[CONTRIBUTING.md](../CONTRIBUTING.md) for details.
