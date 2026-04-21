import json

def test_get_posts_with_headers(api_context):
    headers = {
        "Accept": "application/json",
        "Custom-Header": "Playwright-Test"
    }

    response = api_context.get(
        "https://jsonplaceholder.typicode.com/posts",
        headers=headers
    )

    assert response.status == 200

    body = response.json()

    print("\nAPI RESPONSE JSON:")
    print(json.dumps(body, indent=2))