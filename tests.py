from falcon import testing
import pytest

import app


@pytest.fixture()
def client():
    return testing.TestClient(app.create_api())


def test_parse_members_count():
    text = """foo bar 123456 uživatelů asd fgh"""
    assert app.parse_members_count(text) == 123456


def test_get_members(client, mocker):
    mocker.patch("app.get_members_list_page", return_value="1234 uživatelů")
    result = client.simulate_get("/members")
    assert result.json == {"members": 1234}
