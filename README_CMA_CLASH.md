# CMA Clash

**CMA Clash** is CCMA and allied health exam prep, forked from [ClassQuiz](https://github.com/mawoka-myblock/ClassQuiz): live quizzes, battles, XP/leaderboards, and seeded CCMA, EKG, phlebotomy, CPR/BLS, and clinical skills banks.

See [docs/CMA_CLASH.md](docs/CMA_CLASH.md) for API endpoints, data model, socket events, and seed instructions.

## Quick start (development)

1. Start dependencies: `docker compose -f docker-compose.dev.yml up -d db redis meilisearch`
2. Configure `.env` (mail + `SECRET_KEY` + `DB_URL` — see the self-hosting docs at `/docs/self-host`).
3. `pipenv run alembic upgrade head`
4. `pipenv run python -m classquiz.seed.runner`
5. Run API and frontend per in-app develop docs at `/docs/develop`.
6. Use **http://localhost:8080** (Caddy) so `/api` reaches the backend — not `:3000` alone.

**Vercel (frontend only):** see [docs/DEPLOY_VERCEL.md](docs/DEPLOY_VERCEL.md). Set `BACKEND_URL` and `API_URL` on Vercel; host Postgres/Redis/Meilisearch/API elsewhere.

**Production split (Vercel + Render):** [docs/DEPLOY_VERCEL.md](docs/DEPLOY_VERCEL.md) and [`render.yaml`](render.yaml).

Production Docker: `docker compose up` runs migrations and seed when `AUTO_SEED_CONTENT=true`.

## Content

2,115 multiple-choice questions across 45 topics, published as one public quiz per topic. Each quiz merges the beginner, intermediate and advanced questions of its topic; questions that duplicate a harder one are dropped during the merge. Medically reviewed against common standards (NHA CCMA test plan, AHA BLS, CLSI order of draw, CDC infection control).
