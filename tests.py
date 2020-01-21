from falcon import testing
import pytest

import app


@pytest.fixture()
def client():
    return testing.TestClient(app.create_api())


def test_get_members(client):
    result = client.simulate_get("/members")
    assert result.json == {"members": 1234}
