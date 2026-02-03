import requests

def test_list_users(api_base_url):
    url = f"{api_base_url}/users"
    resp = requests.get(url)
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_create_user(api_base_url):
    url = f"{api_base_url}/posts"
    payload = {
        "title": "Test post from automation",
        "body": "Hello from test_create_user",
        "userId": 1
    }
   
    resp = requests.post(url, json=payload)
    assert resp.status_code in (200, 201)
    data = resp.json()

    assert data.get("title") == payload["title"]
    assert data.get("body") == payload["body"]
    assert "id" in data