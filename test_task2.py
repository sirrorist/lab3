from fastapi.testclient import TestClient
from task2 import app


client = TestClient(app)


def test_read_task2():
    response = client.post("/predict/", json={"text": "Я Артём живу в Питере"})
    json_data = response.json()
    json_data1 = json_data[0]
    assert response.status_code == 200
    assert json_data1["entity_group"] == "PROPN"
