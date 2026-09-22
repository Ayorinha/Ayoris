from fastapi.testclient import TestClient
from ayoris.core import create_app

def test_health(): assert TestClient(create_app()).get("/health").json() == {"status": "ok"}
