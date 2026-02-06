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

---

# Setup

#### 1. Prerequisites

- Python 3.9+
- Google Chrome installed (Selenium 4 can manage ChromeDriver automatically, but having Chrome installed is required.)

#### 2. Create and activate a virtual environment (optional but recommended)

```bash
python3 -m venv venv
source venv/bin/activate    # macOS / Linux
# venv\Scripts\activate     # Windows (PowerShell or cmd)
```

#### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Tests

From the project root (`test-automation-demo/`):

### Run all tests:

```bash
pytest
```

or with more verbose output:

```bash
pytest -v
```

### Run only UI tests

```bash
pytest tests/test_login_ui.py tests/test_inventory_ui.py
```

### Run only API tests

```bash
pytest tests/test_users_api.py
```

---

## Headless vs. Visible Browser

By default, the tests run Chrome in headless mode (no visible browser window), configured in `conftest.py`:

```python
options.add_argument("--headless=new")  # remove or comment this out to see the browser
```

If you want to see the browser while the tests run:

1. open `conftest.py`
2. Comment out or remove the `--headless=new` line
3. Re-run `pytest`

---

## How the Page Object Model is Used

#### BasePage (`pages/base_page.py`):

- Wraps the Selenium driver and a `WebDriverWait`
- Provides helper methods like `open()` and `wait_for()`

#### LoginPage (`pages/login_page.py`):

- Knows how to:
  - Open the login page
  - Fill username/password
  - Click the login button
  - Read the error message on invalid login

#### InventoryPage (`pages/inventory_page.py`)

- Knows how to:
  - Detect if the page is loaded
  - Return the list of product names

The tests themselves stay small and focused because the page objects encapsulate the locators and UI interactions.

---

## What This Project Demonstrates

- Writing UI test automation in Python with Selenium and pytest
- Writing API tests using `requests`
- Using Fixtures to share setup like `driver` and `base_url`
- Applying the Page Object Model to keep tests clean and maintainable
- Verifying both happy path and error scenarios

---

## Possible Future Enhancements

- Add more UI flows (add to car, logout, sorting, etc.)
- Add negative API tests (validation errors, 4xx/5xx handing)
- Generate HTML or JUnit test reports
- Integrate with CI pipepline (e.g. GitHub Actions) to run tests on every push
