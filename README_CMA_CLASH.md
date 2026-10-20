# CMA Clash

**CMA Clash** transforms this CMA Clash fork into gamified certification exam prep: real-time quizzes, multiplayer battles, XP/leaderboards, and curated CCMA, EKG, phlebotomy, CPR/BLS, and clinical skills content.

See [docs/CMA_CLASH.md](docs/CMA_CLASH.md) for API endpoints, data model, socket events, and seed instructions.

## Quick start (development)

1. Start dependencies: `docker compose -f docker-compose.dev.yml up -d db redis meilisearch`
2. Configure `.env` (mail + `SECRET_KEY` + `DB_URL` as in upstream CMA Clash docs).
3. `pipenv run alembic upgrade head`
4. `pipenv run python -m classquiz.seed.runner`
5. Run API and frontend per in-app develop docs at `/docs/develop`.

**Production split (Vercel + Render):** [docs/DEPLOY_VERCEL.md](docs/DEPLOY_VERCEL.md) and [`render.yaml`](render.yaml).

Production Docker: `docker compose up` runs migrations and seed when `AUTO_SEED_CONTENT=true`.

## Content

372 multiple-choice questions (12 per topic × 31 topics), grouped into public quizzes of 8 questions. Medically reviewed against common standards (NHA CCMA test plan, AHA BLS, CLSI order of draw, CDC infection control).
