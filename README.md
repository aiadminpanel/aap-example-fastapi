# aap-example-fastapi

A minimal **Python FastAPI** app, kept as a deploy example for [AI Admin Panel](https://aiadminpanel.com).

AI Admin Panel deploys it from this repository with **Git Deploy** (and **AI Deploy**) and checks
the result regularly: the page at `/` must contain the marker `aap-example:fastapi`. Use it to see how
your own Python FastAPI project is built, or as a starting point.

`python main.py` starts Uvicorn on `$PORT`. Dependencies are pinned in `requirements.txt`.

- The app listens on `$PORT` (default 8080).
- No secrets in this repository.
- License: MIT.
