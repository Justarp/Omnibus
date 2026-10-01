from fastapi.testclient import TestClient

from app import db
from app.main import app

client = TestClient(app)


def test_health_ok_when_database_reachable(monkeypatch):
    monkeypatch.setattr(db, "database_is_reachable", lambda: True)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "database": "ok"}


def test_health_503_when_database_unreachable(monkeypatch):
    monkeypatch.setattr(db, "database_is_reachable", lambda: False)
    response = client.get("/health")
    assert response.status_code == 503
    assert response.json()["database"] == "unreachable"
