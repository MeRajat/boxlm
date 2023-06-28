from fastapi.testclient import TestClient
from main import get_application


def test_chat_vicuana_llama() -> None:
    app = get_application()
    with TestClient(app) as client:
        response = client.post(
            "/api/v1/chat/completions",
            json={
                "messages": [{"role": "user", "content": "Hello!"}],
            },
        )
        assert response.status_code == 200

        response = client.post(
            "/api/v1/chat/completions",
            json={
                "stream": True,
                "messages": [{"role": "user", "content": "Hello!"}],
            },
        )
        assert response.status_code == 200