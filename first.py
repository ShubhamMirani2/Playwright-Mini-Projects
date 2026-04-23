import pytest
import random

# ---------------- PASS TEST ----------------
def test_mouse_actions_pass(page):
    page.goto("https://demoqa.com/buttons")

    # Right click
    page.click("text=Right Click Me", button="right")

    # Double click
    page.dblclick("text=Double Click Me")

    assert page.locator("#rightClickMessage").is_visible()
    assert page.locator("#doubleClickMessage").is_visible()


# ---------------- PASS TEST ----------------
def test_drag_and_drop_pass(page):
    page.goto("https://demoqa.com/droppable")

    source = page.locator("#draggable")
    target = page.get_by_text("Drop here")

    source.drag_to(target)

    assert "Dropped!" in target.text_content()


# ---------------- PASS TEST ----------------
def test_scroll_and_keyboard_pass(page):
    page.goto("https://demoqa.com/text-box")

    page.keyboard.press("PageDown")
    page.wait_for_timeout(1000)

    page.fill("#userName", "Shubham")
    page.keyboard.press("Tab")
    page.keyboard.type("shubham@test.com")

    assert page.locator("#userEmail").input_value() == "shubham@test.com"


# ---------------- FLAKY TEST (RANDOM FAIL) ----------------
@pytest.mark.flaky(reruns=2)
def test_flaky_random_fail(page):
    page.goto("https://example.com")

    # Random failure (simulates unstable UI)
    if random.choice([True, False]):
        assert False, "Random flaky failure"

    assert page.locator("h1").is_visible()


# ---------------- INTENTIONAL FAIL ----------------
def test_intentional_fail(page):
    page.goto("https://demoqa.com")

    # This element DOES NOT exist
    assert page.locator("#nonExistingElement").is_visible()