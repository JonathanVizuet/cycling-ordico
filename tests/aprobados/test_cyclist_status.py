from fastapi.testclient import TestClient
from app.main import app
from app.state import cyclist_state

client = TestClient(app)

def setup_function():
    # Limpia el estado global antes de cada prueba
    cyclist_state.clear()

def test_get_status_of_active_cyclist():
    # Given
    event = {
        "cyclist_id": "123",
        "event": "checkpoint",
        "location": "CP1",
        "time": "10:30:00"
    }
    client.post("/events", json=event)

    # When
    response = client.get("/cyclists/123/status")

    # Then
    assert response.status_code == 200
    assert response.json() == {
        "event": "checkpoint",
        "location": "CP1",
        "time": "10:30:00"
    }

def test_get_status_abandoned_cyclist():
    # Given
    event = {
        "cyclist_id": "456",
        "event": "abandoned",
        "time": "11:15:00"
    }
    client.post("/events", json=event)

    # When
    response = client.get("/cyclists/456/status")

    # Then
    assert response.status_code == 200
    assert response.json() == {
        "event": "abandoned",
        "location": None,
        "time": "11:15:00"
    }

def test_get_status_unknown_cyclist():
    # Given: no hay información previa

    # When
    response = client.get("/cyclists/999/status")

    # Then
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}
