import requests

BASE_URL = "http://localhost:5002"


def test_health():
    response = requests.get(f"{BASE_URL}/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_home():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
    assert "ClientHub" in response.text
