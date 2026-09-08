from app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "running"


def test_add_api():
    client = app.test_client()

    response = client.get("/add?a=10&b=20")

    assert response.status_code == 200

    data = response.get_json()

    assert data["result"] == 30


def test_multiply_api():
    client = app.test_client()

    response = client.get("/multiply?a=5&b=5")

    assert response.status_code == 200

    data = response.get_json()

    assert data["result"] == 25