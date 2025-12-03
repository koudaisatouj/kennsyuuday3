# React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Babel](https://babeljs.io/) (or [oxc](https://oxc.rs) when used in [rolldown-vite](https://vite.dev/guide/rolldown)) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

## API server (FastAPI)

An in-memory task API lives in `main.py/app`. It offers typical CRUD endpoints under `/tasks` plus a `/health` ping.

### Run the server

```powershell
cd kennsyuuDay3
.\venv\Scripts\python.exe .\main.py\app
```

The script bootstraps Uvicorn on http://127.0.0.1:8000. When the server is running, the interactive Swagger UI is available at http://127.0.0.1:8000/docs.

### Sample requests

```powershell
# List demo tasks
Invoke-WebRequest http://127.0.0.1:8000/tasks

# Create a new task
Invoke-RestMethod `
  -Uri http://127.0.0.1:8000/tasks `
  -Method Post `
  -Body (@{ title = "Write docs"; description = "Explain API usage" } | ConvertTo-Json) `
  -ContentType "application/json"
```

Use the responses in your React app via `fetch`/`axios` as needed.
