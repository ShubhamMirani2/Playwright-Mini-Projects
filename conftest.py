import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def page(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()

        # start tracing
        context.tracing.start(screenshots=True, snapshots=True)

        page = context.new_page()
        yield page

        # save trace only if test failed
        if request.node.rep_call.failed:
            context.tracing.stop(path="trace.zip")
        else:
            context.tracing.stop()

        browser.close()