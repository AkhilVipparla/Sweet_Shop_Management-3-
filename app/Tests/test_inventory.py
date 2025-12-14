from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)

def test_purchase_out_of_stock():
    response = client.post("/api/sweets/invalid-id/purchase")
    assert response.status_code in [400, 404]
