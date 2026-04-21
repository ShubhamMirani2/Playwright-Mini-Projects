import csv
import pytest
from playwright.sync_api import expect


def load_login_data():
    with open("testdata/login_data.csv", newline="") as file:
        return list(csv.DictReader(file))


@pytest.mark.parametrize("data", load_login_data())
def test_login_using_csv(page, data):

    username = data["username"]
    password = data["password"]

    page.goto("https://practicetestautomation.com/practice-test-login/")

    page.get_by_role("textbox", name="Username").fill(username)
    page.get_by_role("textbox", name="Password").fill(password)
    page.get_by_role("button", name="Submit").click()

    # ✅ Validation logic
    if username == "student" and password == "Password123":
        expect(page.get_by_role("link", name="Log out")).to_be_visible()
    else:
        expect(page.locator("#error")).to_be_visible()

    page.wait_for_timeout(3000)  # just to SEE each run