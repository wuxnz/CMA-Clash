# Deploy CMA Clash: Vercel (frontend) + Render (backend)

The UI is a SvelteKit app; the API, Postgres, Redis, Meilisearch, and Socket.IO must run outside Vercel.

## Vercel (frontend)

1. **Root directory:** `frontend`
2. **Environment variables:**

| Variable | Example | Purpose |
|----------|---------|---------|
| `BACKEND_URL` | `https://cmaclash-api.onrender.com` | Build-time `vercel.json` rewrites to your Render API |
| `API_URL` | `https://your-app.vercel.app` | SSR auth refresh (`hooks.server.ts`) |
| `PUBLIC_SOCKET_URL` | `https://cmaclash-api.onrender.com` | Direct Socket.IO (recommended) |

3. Build: `node scripts/write-vercel-config.mjs && pnpm run build:app` (default in `package.json` when using this repo’s frontend).

`BACKEND_URL` must be HTTPS with no trailing slash.

### Private launch headers (PR #3)

Checked-in `frontend/vercel.json` adds `X-Robots-Tag: noindex, nofollow`. The build script **merges** those headers with API rewrites when `BACKEND_URL` is set.

---

## Render (backend) — Blueprint

Use the repo-root [`render.yaml`](../render.yaml) (**New → Blueprint** in Render).

### What the blueprint creates (default: free plans)

| Resource | Render type | Notes |
|----------|-------------|--------|
| `cmaclash-api` | Docker web service | Root `Dockerfile`, `render_start.sh` (migrations + seed + `uvicorn --proxy-headers`) |
| `cmaclash-db` | PostgreSQL | **Free DB expires after 90 days** (Render policy) |
| `cmaclash-redis` | Key Value (Redis) | Sessions / cache |
| `cmaclash-meilisearch` | Docker image web service | **Ephemeral** on free tier; index rebuilt from Postgres via `meilisearch_init` when API starts |

### Free-tier limits that affect you

- **Spin-down:** Free web services sleep after ~15 minutes of no traffic. First request is slow; **Socket.IO live games** need the API awake (paid instance or external keep-alive).
- **Ephemeral disk:** `STORAGE_BACKEND=local` and `STORAGE_PATH=/var/data/uploads` **do not persist** across deploys or restarts. Uploaded quiz media is lost unless you use **S3** (`STORAGE_BACKEND=s3` + keys) or attach a **paid disk** to the API service.
- **Meilisearch:** Free Meilisearch loses its index on redeploy; the API re-syncs public quizzes from Postgres when Meilisearch is reachable. If Meilisearch is down, the API **still starts**; search returns empty results until sync succeeds.
- **Persistent Meilisearch (paid):** Replace the Meilisearch service with a `pserv` + `disk` (see [Render disks](https://render.com/docs/disks)) and point `MEILISEARCH_URL` at that host.

### Values you must enter when applying the blueprint

Render prompts for these (`sync: false`):

| Variable | What to enter |
|----------|----------------|
| `ROOT_ADDRESS` | Your **Vercel** site URL, e.g. `https://cma-clash.vercel.app` (no trailing slash). Used for emails, OAuth callbacks, QR links. |
| `CORS_ORIGINS` | Same URL as `ROOT_ADDRESS`, or comma-separated list if you use preview domains too, e.g. `https://cma-clash.vercel.app` |

Render auto-generates **`SECRET_KEY`**. Other important defaults are set in the blueprint:

- `SKIP_EMAIL_VERIFICATION=true`
- `COOKIE_CROSS_SITE=true` (required for Vercel ↔ Render cookies)
- `AUTO_SEED_CONTENT=true`
- `STORAGE_BACKEND=local`

### After Render deploys

1. Copy the API URL: `https://cmaclash-api.onrender.com` (or your custom domain).
2. On **Vercel**, set `BACKEND_URL` and `PUBLIC_SOCKET_URL` to that URL; set `API_URL` to your Vercel URL.
3. Redeploy Vercel so rewrites regenerate.

### Health check

Render uses `GET /api/v1/health` → `{"status":"ok"}`.

---

## Local development

1. `docker compose -f docker-compose.dev.yml up -d db redis meilisearch caddy`
2. API on `:8000`, `API_URL=http://localhost:8080 pnpm dev` in `frontend/`
3. Open **http://localhost:8080**

Vite dev also proxies `/api` to `:8000` if you use `:3000` directly.

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| Login 404 on Vercel | Set `BACKEND_URL` to Render API; redeploy frontend |
| Logged out after login | Set Vercel `API_URL` to your Vercel origin; set Render `CORS_ORIGINS` + `ROOT_ADDRESS` |
| Live game disconnects | Render free spin-down; use `PUBLIC_SOCKET_URL` + paid API or keep-alive |
| Uploads disappear | Expected on free + `local` storage; switch to S3 or a persistent disk |
