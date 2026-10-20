<!--
SPDX-FileCopyrightText: 2026 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->
# Contribute to CMA Clash

For the development-setup, please check out the
docs: [/docs/develop](/docs/develop) (when running the frontend locally)

## Coding guidelines
- _Try_ to use type hints (python) and TypeScript everwhere possible (for python `foo() -> dict` is better than nothing)

### Frontend
- Follow the existing coding style
	- CamelCase for classnames
	- snake_case for function names, variables and everything else
	- aka Rust-style
- Feel free to reduce complexity in the code you're already touching
- always make sure the frontend builds (`pnpm build`) as it catches most typos
- Stick to current design language
- Use premade Brown and GreyButton components


## AI Usage
- Feel free to use any AI help
- Please refrain from using coding agents

## Formatting git-commits

Please use [Gitmoji](https://gitmoji.dev/) to format your commits.

## Opening PRs

Just do so.

## Found a bug

If it is a security-related bug, please open a [private security advisory](https://github.com/wuxnz/CMA-Clash/security/advisories/new) on GitHub. Otherwise, open a public issue.


## Want to translate?

Go to [Weblate](https://hosted.weblate.org/projects/classquiz/).
If the language isn't available, please open
an issue here, so I'll be able to add it.
