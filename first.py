def test_mouse_actions(page):
    page.goto("https://demoqa.com/menu")

    # Hover Main Item 2
    page.locator("text=Main Item 2").hover()

    # Wait until SUB SUB LIST is visible
    page.locator("text=SUB SUB LIST »").wait_for(state="visible")

    # Hover SUB SUB LIST
    page.locator("text=SUB SUB LIST »").hover()

    # Wait and hover Sub Sub Item 1
    page.locator("text=Sub Sub Item 1").wait_for(state="visible")
    page.locator("text=Sub Sub Item 1").hover()

    page.wait_for_timeout(3000)

    assert page.locator("text=Sub Sub Item 1").is_visible()