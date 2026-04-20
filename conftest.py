import pytest

@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context(
        record_video_dir="videos/"
    )
    yield context
    context.close()