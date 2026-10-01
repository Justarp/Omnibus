from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app import db

app = FastAPI(title="Omnibus API")


@app.get("/health")
def health():
    if not db.database_is_reachable():
        return JSONResponse(status_code=503, content={"status": "error", "database": "unreachable"})
    return {"status": "ok", "database": "ok"}
