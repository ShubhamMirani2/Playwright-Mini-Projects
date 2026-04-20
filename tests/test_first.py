import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://demoqa.com/text-box")
    page.get_by_role("textbox", name="Full Name").click()
    page.get_by_role("textbox", name="Full Name").fill("Shubham")
    page.get_by_role("textbox", name="Full Name").press("Tab")
    page.get_by_role("textbox", name="name@example.com").fill("Shubham@gmail.com")
    page.get_by_role("textbox", name="name@example.com").press("Tab")
    page.get_by_role("textbox", name="Current Address").fill("Ahmedabad")
    page.get_by_role("textbox", name="Current Address").press("Tab")
    page.locator("#permanentAddress").fill("Rajkot")
    page.locator("#permanentAddress").press("Tab")
    page.get_by_role("button", name="Submit").press("Enter")
    page.get_by_role("button", name="Submit").click()
