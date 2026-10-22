# CMA Clash

CMA Clash is CCMA and allied health exam prep built on the [ClassQuiz](https://github.com/mawoka-myblock/ClassQuiz) stack (FastAPI, Svelte, Redis/Socket.IO, Meilisearch, PostgreSQL).

## Architecture

### Content model

- **Certifications** (`certifications`): CCMA, EKG, Phlebotomy, CPR/BLS, Clinical Skills.
- **Topics** (`topics`): exam domains and skill areas linked to a certification.
- **Quizzes** (`quiz`): existing CMA Clash JSON questions, extended with `certification_id`, `topic_id`, `difficulty`, and optional `seed_slug` for idempotent imports.
- **Questions** (embedded JSON): optional `explanation` and `references` on each `QuizQuestion`.

Every topic ships as one public quiz that merges the beginner, intermediate and
advanced questions of that topic. Questions that duplicate a harder one are
dropped during the merge (see `classquiz/seed/quiz_merge.py`), and the merged
quiz is marked with the `mixed` difficulty because it spans all three tiers.

Browse public content via `GET /api/v1/clash/quizzes` with filters `certification_slug`, `topic_slug`, `difficulty`.

### Gamification

- **UserGamificationProfile**: XP, level, streaks, battle and accuracy totals.
- **UserTopicStat**: per-topic accuracy and XP.
- **XpEvent** audit log; **LeaderboardScore** aggregates for global and weekly boards (optionally per certification).

Endpoints:

- `GET /api/v1/clash/me/gamification`
- `GET /api/v1/clash/me/stats/by-topic`
- `GET /api/v1/clash/leaderboards?period=all_time|weekly&certification_slug=ccma`

XP is awarded for correct answers, hosting games, and battle results. Levels use a stepped XP curve (`classquiz/gamification/service.py`).

### Real-time play & battles

Standard live games are unchanged. **Battle mode** uses `game_mode=battle` on `PlayGame`:

- Create/join via REST: `POST /api/v1/clash/battles`, `POST .../join`, `POST .../start`.
- Matchmaking queue: `POST /api/v1/clash/matchmaking/queue?certification_slug=ccma`.
- Socket.IO: when all players answer, battle games **auto-advance** to the next question (`_battle_maybe_advance`); emits `battle_finished` when complete.
- `finalize_battle` persists `BattleResult` and updates gamification stats.

### Seed content

Idempotent seed (`classquiz/seed/runner.py`):

```bash
# After migrations
python -c "import asyncio; from classquiz.seed.runner import run_seed; asyncio.run(run_seed())"
```

Or set `AUTO_SEED_CONTENT=true` in Docker (runs from `prestart.sh`). Skip with `CMA_CLASH_SKIP_SEED=1`.

Question banks live under `classquiz/seed/banks/` (372 exam-style items, 12 per topic). Counts:

```bash
python -c "import asyncio; from classquiz.seed.runner import seed_counts; print(asyncio.run(seed_counts()))"
```

Quizzes are created in sets of 8 questions per topic (`seed_slug` like `quiz:ccma-anatomy:1`).

### Migrations

```bash
alembic upgrade head
```

Revision `a1b2c3d4e5f6` adds CMA Clash tables and quiz metadata columns.

### Configuration

| Variable | Purpose |
|----------|---------|
| `ROOT_ADDRESS` | Public site URL for links in email/OAuth/QR (e.g. `https://cmaclash.com`) |
| `CORS_ORIGINS` | Allowed browser origins, comma-separated (e.g. `https://cmaclash.com,https://cmaclash.vercel.app`) |
| `AUTO_SEED_CONTENT` | Run seed on container prestart (default `true` in prestart.sh) |
| `CMA_CLASH_SKIP_SEED` | Skip seed when set |
| `MEILISEARCH_INDEX` | Default `cmaclash` |

The frontend has been rebuilt around CMA Clash — new landing page, docs, dashboard and play UI — on top of the upstream ClassQuiz routing and API layer.
