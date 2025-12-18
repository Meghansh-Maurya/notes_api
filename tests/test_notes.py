import pytest
from fastapi.testclient import TestClient
from app.main import app
import app.storage as storage

client = TestClient(app)


def test_create_note():
    response = client.post(
        "/notes",
        json={"title": "Test", "content": "Isolated"}
    )

    assert response.status_code == 200

    data = response.json()
    assert data["id"] == 1
    assert data["title"] == "Test"
    assert data["content"] == "Isolated"

def test_get_note():
    client.post(
        "/notes",
        json={"title": "Test", "content": "Get"}
    )
    
    response = client.get("/notes/1")

    assert response.status_code == 200

    data = response.json()
    assert data["id"] == 1

@pytest.fixture(autouse=True)
def reset_storage():
    """
    Reset in-memory storage before each test.
    """
    storage.notes.clear()
    storage.note_id = 0

