from fastapi import testclient
from task2 import app

client = testclient(app)


def test_read_task2():
    response=client.post("/predict/", json={"text":"Моё имя Рустам и я из Пакистана"}) 
    assert response.status_code == 200 
    # assert json_data["entity_group"] == "DET"