from fastapi.testclient import TestClient


def test_if_root_endpoint_returns_welcome_message(get_app) -> None:
    client = TestClient(get_app)
    response = client.get("/")

    assert (
        response.json()["message"]
        == "Welcome! This is the Animus API. For more details, use the /docs or /redoc endpoints to target documentation."
    )
