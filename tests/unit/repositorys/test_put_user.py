from app.repositoris import persitance
import pytest


def test_put_user():
    data = {
            2:{
            "firstName":"alex",
            "lastName":"zizka",
            "birthYear": 1204,
            "group": "admin"
            },
        }
    repo = persitance(data)
    expe_out = {
        2:{
            "firstName":"alex",
            "lastName":"zizka",
            "birthYear": 1204,
            "group": "admin"
            },
        3:{
            "firstName":"mike",
            "lastName":"zizka",
            "birthYear": 123,
            "group": "user"
        },
    }
    user_to_add={
            "firstName":"mike",
            "lastName":"zizka",
            "birthYear": 123,
            "group": "user"
        }
    repo.add(user_to_add)

    assert data == expe_out

    