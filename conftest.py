import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def api_context():
    with sync_playwright() as p:
        request_context = p.request.new_context(
            extra_http_headers={
                "x-api-key": "reqres-free-v1"
            }
        )
        yield request_context
        request_context.dispose()