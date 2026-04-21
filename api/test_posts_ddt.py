import pytest

@pytest.mark.parametrize(
    "post_id",
    [1, 2, 3]
)
def test_get_post_by_id(api_context, post_id):
    response = api_context.get(
        f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    )

    assert response.status == 200