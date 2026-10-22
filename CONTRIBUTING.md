<!--
SPDX-FileCopyrightText: 2026 CMA Clash contributors

SPDX-License-Identifier: MPL-2.0
-->
# Contribute to CMA Clash

For the development-setup, please check out the
[development docs](frontend/src/routes/docs/develop/+page.svelte) (when running the frontend locally).

## Coding guidelines
- _Try_ to use type hints (python) and TypeScript everywhere possible (for python `foo() -> dict` is better than nothing)

### Frontend
- Follow the existing coding style
	- The UI layer (`frontend/src/lib/ui/`) uses camelCase for functions and Tailwind utility classes for styling
	- Older parts of the app still use snake_case for functions — don't rename them as a drive-by change
- Feel free to reduce complexity in the code you're already touching
- always make sure the frontend builds (`pnpm build`) as it catches most typos
- Stick to current design language
- Use the shared UI primitives in `frontend/src/lib/ui/` (`Button.svelte`, `Card.svelte`, `PageHeader.svelte`, …) instead of hand-rolling new ones


## AI Usage
- Feel free to use AI help, coding agents included
- Please be transparent about it in your pull request description

## Formatting git-commits

Please use [Conventional Commits](https://www.conventionalcommits.org/) to format your commits
(`feat(scope): …`, `fix(scope): …`, `docs: …`).

## Opening PRs

Just do so.

## Found a bug

If it is a security-related bug, please open a [private security advisory](https://github.com/wuxnz/CMA-Clash/security/advisories/new) on GitHub. Otherwise, open a public issue.


## Want to translate?

Translations live in `frontend/src/lib/i18n/locales/`, one JSON file per language, named after the
locale code (`en.json`, `de.json`, `pt_BR.json`, `zh_Hans.json`, …). Copy `en.json` as a starting
point, translate the values, and open a pull request.

If the language isn't available, please open
an issue here, so I'll be able to add it.
