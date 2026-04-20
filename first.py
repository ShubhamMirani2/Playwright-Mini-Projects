from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch browser with slow motion
    browser = p.chromium.launch(
        headless=False,
        slow_mo=1000   # 1 second delay between each action
    )

    page = browser.new_page()

    # 1️⃣ Open website
    page.goto("https://demoqa.com/text-box")

    # 2️⃣ Fill form fields
    page.fill("#userName", "Shubham")
    page.fill("#userEmail", "shubham@test.com")
    page.fill("#currentAddress", "Surat, India")
    page.fill("#permanentAddress", "Gujarat, India")

    # 3️⃣ Click submit button
    page.click("#submit")

    # 4️⃣ Verify output
    page.wait_for_selector("#output")
    print("Form submitted successfully!")

    # 5️⃣ Pause to see result
    page.wait_for_timeout(3000)

    browser.close()