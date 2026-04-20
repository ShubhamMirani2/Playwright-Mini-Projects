import pytest
import os
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def page(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            slow_mo=1000
        )

        context = browser.new_context(
            record_video_dir="videos/"
        )

        page = context.new_page()
        yield page

        # Take screenshot if test fails
        if request.node.rep_call.failed:
            os.makedirs("screenshots", exist_ok=True)
            page.screenshot(path=f"screenshots/{request.node.name}.png")

        context.close()   # ⚠️ video saved here
        browser.close()


# Hook to capture test result
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)