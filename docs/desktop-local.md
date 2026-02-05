# Desktop (macOS) — Local Setup

## How it works

The desktop app uses [Tauri](https://tauri.app/) to wrap the web frontend in a native macOS window. The backend (API, Celery workers, Postgres, Redis) runs locally via Docker Compose on port `8081`.

When running in desktop mode, Vite loads `frontend/.env.desktop` which points the frontend at `localhost:8081`. The Tauri shell connects to this local backend — there is no embedded server in the app itself.

```
┌─────────────────────┐       ┌──────────────────────────────┐
│   Tauri (native)    │       │   Docker Compose             │
│                     │       │                              │
│   React frontend    │──────▶│   API         (port 8081)    │
│   (.env.desktop)    │       │   Celery worker              │
│                     │       │   Celery beat                │
└─────────────────────┘       │   Postgres    (port 5432)    │
                              │   Redis       (port 6379)    │
                              └──────────────────────────────┘
```

## Requirements

- Docker Desktop (running)
- Node.js
- Rust

## Dev workflow

1. Start Docker services:
   ```sh
   docker compose -f docker-compose.desktop.yml up -d --remove-orphans
   ```
2. In `frontend/`:
   ```sh
   npm install
   npm run desktop:dev
   ```

## Build (unsigned dev)

```sh
cd frontend && npm run desktop:build
```

The app bundle will be at `frontend/src-tauri/target/release/bundle/macos/Claudex.app`.

## Troubleshooting

- **Backend unavailable**: Ensure Docker Desktop is running and the compose stack is up.
- **Database connection errors**: Confirm Postgres is listening on `localhost:5432`.
- **Port conflict**: Desktop defaults to port `8081` to avoid conflicts. To change it, update `docker-compose.desktop.yml` and `frontend/.env.desktop`.
