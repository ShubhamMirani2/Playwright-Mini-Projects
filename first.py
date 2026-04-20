from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False,
        slow_mo=1000   # 👈 1000 ms = 1 second delay between actions
    )
    page = browser.new_page()

    page.goto("https://the-internet.herokuapp.com/login")

    page.fill("#username", "tomsmith")
    page.fill("#password", "SuperSecretPassword!")
    page.click("button[type='submit']")

    page.wait_for_selector(".flash.success")
    print("Login successful!")

    browser.close()