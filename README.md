# Test Automation Demo (Python, Selenium, Pytest)

This project is a small end-to-end test automation demo that shows how I approach:

- **UI testing** with Selenium WebDriver
- **API testing** with `requests`
- **Test structure** using the Page Object Model (POM)
- **Pytest fixtures** and reusable setup/teardown

It uses a public demo web app and a public demo API so everything can be run locally without any credentials.

---

## Tech Stack

- **Language:** Python 3.9
- **Test runner:** pytest
- **UI automation:** Selenium WebDriver (Chrome, headless by default)
- **API testing:** `requests`
- **Pattern:** Page Object Model (POM)

---

## What This Project Tests

### UI Tests (Selenium)

Target site: [`https://www.saucedemo.com`](https://www.saucedemo.com)

1. **Successful login**
   - Uses valid credentials (`standard_user` / `secret_sauce`)
   - Verifies that the inventory page loads after login.

2. **Invalid login**
   - Uses an incorrect password
   - Verifies that an error message is displayed to the user.
   - Verifies that that the user is not taken to the inventory page after a failed login.

3. **Inventory page**
   - Logs in successfully
   - Verifies that product items are visible on the inventory page.

### API Tests (Requests)

Target API: [`https://jsonplaceholder.typicode.com`](https://jsonplaceholder.typicode.com)

1. **List users (GET)**
   - Calls `GET /users`
   - Verifies:
     - Status code is `200`
     - Response body contains a non-empty `list` of users.

2. **Create post (POST)**
   - Calls `POST /posts` with a JSON payload
   - Verifies:
     - Status code is `200` or `201`
     - The response echoes back the `title` and `body`
     - The response contains an `id` field.

These examples are intentionally simple, but they mirror the kinds of checks you’d perform in real UI and API test suites.

---

## Project Structure

```text
test-automation-demo/
├─ pages/
│  ├─ __init__.py
│  ├─ base_page.py         # Base class with common Selenium helpers
│  ├─ login_page.py        # Page object for the login screen
│  └─ inventory_page.py    # Page object for the inventory/products page
├─ tests/
│  ├─ test_login_ui.py     # UI tests for login scenarios
│  ├─ test_inventory_ui.py # UI tests for the inventory page
│  └─ test_users_api.py    # API tests (GET + POST)
├─ conftest.py             # Pytest fixtures (driver, base URLs)
├─ requirements.txt        # Python dependencies
├─ pytest.ini              # Pytest configuration
└─ README.md               # You are here
```
