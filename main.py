import os
from datetime import datetime, timezone

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def index() -> str:
    now = datetime.now(timezone.utc).isoformat()
    return (
        "<!doctype html><title>aap-example:fastapi</title><h1>FastAPI</h1>"
        f"<p>Served at {now}. Marker: <code>aap-example:fastapi</code></p>"
    )


@app.get("/healthz")
def healthz() -> dict:
    return {"ok": True}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", "8080")))
