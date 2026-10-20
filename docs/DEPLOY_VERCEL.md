# Deploy CMA Clash on Vercel (frontend) + external API

ClassQuiz is a **split stack**: the SvelteKit UI can run on [Vercel](https://vercel.com), but **FastAPI, PostgreSQL, Redis, Meilisearch, and Socket.IO** must run elsewhere (Docker on a VPS, [Railway](https://railway.app), [Render](https://render.com), [Fly.io](https://fly.io), etc.). The upstream app normally serves `/api` and `/socket.io` from the same origin via Caddy; on Vercel alone, browser calls to `/api/...` would 404 unless you proxy or point the client at a real backend.

This repo had **no `vercel.json` checked in** until you generate one at build time (see below).

## Recommended: same-origin API via Vercel rewrites

Keeps relative `/api/...` URLs in the frontend and **httponly cookies** on your Vercel domain (no cross-site cookie setup).

1. Deploy the **backend** (see [Backend hosting](#backend-hosting)).
2. In Vercel, create a project with **Root Directory** = `frontend`.
3. Set environment variables:

| Variable | Example | Purpose |
|----------|---------|---------|
| `BACKEND_URL` | `https://api.example.com` | Used at build time to write `vercel.json` rewrites |
| `API_URL` | `https://your-app.vercel.app` | Server-side SvelteKit fetches (JWT refresh in `hooks.server.ts`) |
| `SKIP_EMAIL_VERIFICATION` | `true` on backend | Optional: skip SMTP for local/staging |
| `ROOT_ADDRESS` | `https://your-app.vercel.app` | Public site URL (emails, OAuth, WebAuthn) — **not** the raw API host if you use rewrites |

4. Build command (default from generated config): `node scripts/write-vercel-config.mjs && pnpm run build:app`
5. Install command: `pnpm install`

`BACKEND_URL` must be HTTPS in production. Do not add a trailing slash.

### Socket.IO

Vercel rewrites are unreliable for long-lived WebSockets. For live games, set on the **frontend** (Vercel):

| Variable | Example |
|----------|---------|
| `PUBLIC_SOCKET_URL` | `https://api.example.com` |

The browser connects directly to the API host; enable CORS on the backend (below).

## Alternative: cross-origin API (no rewrites)

Set `PUBLIC_API_ORIGIN` (future / manual) or host UI and API on different domains and configure:

**Backend `.env`:**

```env
ROOT_ADDRESS=https://your-app.vercel.app
CORS_ORIGINS=https://your-app.vercel.app
COOKIE_CROSS_SITE=true
```

Cookies use `SameSite=None; Secure`. You must serve the API over HTTPS.

## Backend hosting

Minimum services:

- **PostgreSQL** (managed or container)
- **Redis**
- **Meilisearch**
- **API process**: `uvicorn classquiz:app --host 0.0.0.0 --port 8000 --proxy-headers`
- **Object storage**: `STORAGE_BACKEND=local` with a persistent volume, or S3-compatible storage

Example with Docker on a VPS: use `docker-compose.yml` from this repo (or `docker-compose.dev.yml` for dependencies only + run API from source). Set:

```env
ROOT_ADDRESS=https://your-app.vercel.app
CORS_ORIGINS=https://your-app.vercel.app
SKIP_EMAIL_VERIFICATION=true
SECRET_KEY=...
DB_URL=postgresql://...
REDIS=redis://...
MEILISEARCH_URL=http://...
STORAGE_BACKEND=local
STORAGE_PATH=/data/storage
AUTO_SEED_CONTENT=true
```

Expose the API on HTTPS (Caddy, nginx, or your platform’s TLS).

## Local development (matches production split)

1. `docker compose -f docker-compose.dev.yml up -d db redis meilisearch caddy`
2. API on `:8000`, frontend `API_URL=http://localhost:8080 pnpm dev` (Caddy on `:8080` proxies `/api` → API and `/*` → UI).
3. Open **http://localhost:8080** (not `:3000` alone).

## Troubleshooting

| Symptom | Likely cause |
|---------|----------------|
| Login returns 404 | Frontend not proxied to API (missing `BACKEND_URL` / rewrites or wrong port) |
| Login succeeds but UI still logged out | `API_URL` on Vercel not set to public site URL; SSR cannot refresh JWT |
| No Register link | `VITE_REGISTRATION_DISABLED=true` (fixed semantics: register shows unless explicitly disabled) |
| Live game won’t connect | Set `PUBLIC_SOCKET_URL` + `CORS_ORIGINS` on API |
