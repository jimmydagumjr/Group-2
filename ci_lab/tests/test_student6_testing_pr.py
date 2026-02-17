import pytest
from http import HTTPStatus
from src import app


@pytest.fixture()
def client():
    return app.test_client()


def test_list_counters_empty_returns_empty_dict(client):
    """It should return an empty dict when no counters exist"""
    client.post("/counters/reset")  # ensure clean state
    response = client.get("/counters")
    assert response.status_code == HTTPStatus.OK
    assert response.get_json() == {}
