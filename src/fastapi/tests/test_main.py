from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_ocr():
    response = client.post("/ocr", json={"image_url": "https://example.com/image.jpg"})
    assert response.status_code == 200
    assert response.json() == {"text": "Hello, World!"}

def test_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert response.json() == {"users": []}