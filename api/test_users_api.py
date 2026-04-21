import json

def test_get_posts(api_context):
    response = api_context.get(
        "https://jsonplaceholder.typicode.com/posts"
    )

    assert response.status == 200

    body = response.json()

    # 🔹 Print JSON nicely in terminal
    print("\nAPI RESPONSE JSON:")
    print(json.dumps(body, indent=2))