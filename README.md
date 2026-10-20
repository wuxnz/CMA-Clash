<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

# CMA Clash

**Live site:** [https://cmaclash.com](https://cmaclash.com)

**CMA Clash** is CCMA and allied health exam prep: live quizzes with a PIN, battles, timed practice, XP, streaks, and leaderboards. It is built on the open-source [ClassQuiz](https://github.com/mawoka-myblock/ClassQuiz) stack (FastAPI, SvelteKit, PostgreSQL, Redis, Socket.IO, Meilisearch).

## Features

- Live Kahoot-style play with PIN/QR lobbies
- Battle mode and matchmaking (`/api/v1/clash/battles`)
- Gamification: XP, levels, streaks, weekly/all-time leaderboards
- Seeded CCMA, EKG, phlebotomy, CPR/BLS, and clinical skills question banks
- Self-hostable (Docker Compose)

## Quick start

See [README_CMA_CLASH.md](README_CMA_CLASH.md) and [docs/CMA_CLASH.md](docs/CMA_CLASH.md).

```bash
docker compose up -d
# or local dev: see /docs/develop
```

## Attribution

CMA Clash is a derivative work based on **ClassQuiz** by Marlon W (Mawoka), licensed under MPL-2.0. See [LICENSE](LICENSE) and [NOTICE](NOTICE).

Upstream copyright and license notices in source files are retained where required.

## Docs

In-app documentation: `/docs` (self-host, development, privacy).

## Translation

Community translations live under `frontend/src/lib/i18n/locales/`. Contributions welcome via pull request.
