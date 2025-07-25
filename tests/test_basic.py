import json
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import app



def test_shorten_success():
    client = app.test_client()
    response = client.post("/api/shorten", json={"url": "https://test.com"})
    data = json.loads(response.data)
    assert response.status_code == 200
    assert "short_code" in data
    assert "short_url" in data

def test_shorten_invalid_url():
    client = app.test_client()
    response = client.post("/api/shorten", json={"url": "invalid-url"})
    assert response.status_code == 400

def test_redirect_and_stats():
    client = app.test_client()
    res = client.post("/api/shorten", json={"url": "https://example.com"})
    short_code = json.loads(res.data)["short_code"]

    for _ in range(3):
        redirect_res = client.get(f"/{short_code}")
        assert redirect_res.status_code == 302

    stats = client.get(f"/api/stats/{short_code}")
    data = json.loads(stats.data)
    assert data["clicks"] == 3
    assert data["url"] == "https://example.com"

def test_missing_url_field():
    client = app.test_client()
    response = client.post("/api/shorten", json={})  # No "url" key
    assert response.status_code == 400

def test_stats_nonexistent_code():
    client = app.test_client()
    response = client.get("/api/stats/abcdef")  # Assuming this code doesn’t exist
    assert response.status_code == 404
