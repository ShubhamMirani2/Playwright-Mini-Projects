from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch browser with slow motion
    browser = p.chromium.launch(
        headless=False,
        slow_mo=500   # 1 second delay between actions
    )
    page = browser.new_page()

    # Open website
    page.goto("https://demoqa.com/menu")

    # Hover on "Main Item 2"
    page.hover("text=Main Item 2")

    # Hover on sub menu
    page.hover("text=SUB SUB LIST »")

    # Hover on sub-sub item
    page.hover("text=Sub Sub Item 1")

    # Pause to clearly see hover actions
    page.wait_for_timeout(3000)

    print("Mouse hover actions executed successfully!")

    browser.close()