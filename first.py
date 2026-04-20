from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False,
        slow_mo=1000
    )
    page = browser.new_page()

    page.goto("https://demoqa.com/text-box")

    page.fill("#userName", "Shubham")
    page.fill("#userEmail", "shubham@test.com")

    # Take screenshot before submit
    page.screenshot(path="before_submit.png")

    page.click("#submit")

    # Take screenshot after submit
    page.screenshot(path="after_submit.png", full_page=True)

    browser.close()