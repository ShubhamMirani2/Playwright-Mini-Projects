from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False,
        slow_mo=1000
    )

    # Create context with video recording
    context = browser.new_context(
        record_video_dir="videos/",
        record_video_size={"width": 1280, "height": 720}
    )

    page = context.new_page()

    page.goto("https://demoqa.com/buttons")

    page.click("text=Click Me")

    page.wait_for_timeout(3000)

    context.close()   # ⚠️ IMPORTANT: video is saved only after context is closed
    browser.close()