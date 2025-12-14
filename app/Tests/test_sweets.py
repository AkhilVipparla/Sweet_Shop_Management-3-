from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)

def test_add_sweet():
    response = client.post("/api/sweets", json={
        "name": "Ladoo",
        "category": "Mithai",
        "price": 20,
        "quantity": 10
    })
    assert response.status_code == 200
