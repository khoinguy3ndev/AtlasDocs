import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check_status_code():
    response = client.get("/health")
    assert response.status_code == 200


def test_health_check_response_body():
    response = client.get("/health")
    data = response.json()
    assert data["status"] == "ok"
    assert data["message"] == "Server is running"


def test_health_check_content_type():
    response = client.get("/health")
    assert response.headers["content-type"] == "application/json"
