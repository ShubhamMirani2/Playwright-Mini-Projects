import pytest


# ---------- 1. Valid login ----------
def test_login_valid_credentials(page):
    page.goto("https://practicetestautomation.com/practice-test-login/")

    page.fill("#username", "student")
    page.fill("#password", "Password123")
    page.click("#submit")

    assert page.locator(".post-title").inner_text() == "Logged In Successfully"
    assert page.locator("text=Congratulations").is_visible()


# ---------- 2. Invalid username ----------
def test_login_invalid_username(page):
    page.goto("https://practicetestautomation.com/practice-test-login/")

    page.fill("#username", "wronguser")
    page.fill("#password", "Password123")
    page.click("#submit")

    assert page.locator("#error").inner_text() == "Your username is invalid!"


# ---------- 3. Invalid password ----------
def test_login_invalid_password(page):
    page.goto("https://practicetestautomation.com/practice-test-login/")

    page.fill("#username", "student")
    page.fill("#password", "wrongpass")
    page.click("#submit")

    assert page.locator("#error").inner_text() == "Your password is invalid!"


# ---------- 4. Empty username ----------
def test_login_empty_username(page):
    page.goto("https://practicetestautomation.com/practice-test-login/")

    page.fill("#password", "Password123")
    page.click("#submit")

    assert page.locator("#error").is_visible()


# ---------- 5. Empty password ----------
def test_login_empty_password(page):
    page.goto("https://practicetestautomation.com/practice-test-login/")

    page.fill("#username", "student")
    page.click("#submit")

    assert page.locator("#error").is_visible()


# ---------- 6. Logout after successful login ----------
def test_logout_after_login(page):
    page.goto("https://practicetestautomation.com/practice-test-login/")

    page.fill("#username", "student")
    page.fill("#password", "Password123")
    page.click("#submit")

    page.click("text=Log out")

    assert page.url == "https://practicetestautomation.com/practice-test-login/"