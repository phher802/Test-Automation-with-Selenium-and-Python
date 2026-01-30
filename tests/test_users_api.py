import requests

def test_list_users(api_base_url):
    url = f"{api_base_url}/users?page=2"
    resp = requests.get(url)

    assert resp.status_code == 200
    data = resp.json()

    assert "data" in data
    assert isinstance(data["data"], list)
    assert len(data["data"]) > 0

def test_create_user(api_base_url):
    url = f"{api_base_url}/users"
    payload = {"name": "Pa Her", "job": "automation engineer"}

    resp = requests.post(url, json=payload)

    assert resp.status_code == 201
    data = resp.json()

    assert data.get("name") == payload["name"]
    assert data.get("job") == payload["job"]
    assert "id" in data
    assert "createdAt" in data