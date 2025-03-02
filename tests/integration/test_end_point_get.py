import pytest
import json
from app.app import get_via_id
from app.repositoris import persitance



# def test_is_users_returning_users():
#     assert get_via_id(1, persitance({
#                 1: {
#         "firstName":"alex",
#         "lastName":"zizka",
#         "birthYear": 1204,
#         "group": "admin"
#         }}
#     )) ==  ({
#         "id": 1,
#         "firstName":"alex",
#         "lastName":"zizka",
#         "birthYear": 1204,
#         "group": "admin"
#     },200)

import requests

from app.app import *
import pytest

@pytest.fixture
def client():
    return App.test_client()

@pytest.mark.parametrize("config",
                            [
        [1, {"firstName":"alex", "lastName":"zizka", "birthYear": 1204, "group": "admin", "id": 1}, 200],
        [5, {}, 404]
                            ]
                        )
def test_user_get_responce_code(client, config):
    assert config[2] == client.get(f"/users/{config[0]}").status_code
    assert config[1] == client.get(f"/users/{config[0]}").json

@pytest.mark.parametrize("config",
                            [
        [
            [
        {
        "id": 1,
        "firstName":"alex",
        "lastName":"zizka",
        "birthYear": 1204,
        "group": "admin"
        },
        {
        "id": 2,
        "firstName":"alex",
        "lastName":"zizka",
        "birthYear": 1204,
        "group": "admin"
        },
        {
        "id": 3,
        "firstName":"alex",
        "lastName":"zizka",
        "birthYear": 1204,
        "group": "admin"
        },
    ]
    , 200],
                            ]
                        )
def test_user_get_all_responce_code(client, config):
    assert config[1] == client.get(f"/users").status_code
    assert config[0] == client.get(f"/users").json

@pytest.mark.parametrize("config",
                            [
        [{"firstName":"alexxxx", "lastName":"zizka", "birthYear": 45, "group": "admin"}, 200],
                            ]
                        )
def test_user_add_responce_code(client, config):
    assert config[1] == client.post(f"/users", json=config[0]).status_code

@pytest.mark.parametrize("config",
                            [
        [{"firstName":"alexxxx", "lastName":"zizka", "birthYear": 45, "group": "admin"}, 200, 1],
                            ]
                        )
def test_user_patch_responce_code(client, config):
    assert config[1] == client.patch(f"/users/{config[2]}", json=config[0]).status_code

@pytest.mark.parametrize("config",
                            [
        [ 200, 1],
                            ]
                        )
def test_user_delete_responce_code(client, config):
    assert config[0] == client.delete(f"/users/{config[1]}").status_code
