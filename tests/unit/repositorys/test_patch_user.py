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
            "birthYear": 33446,
            "group": "user"
            },
    }
    changes={
            "birthYear": 33446,
            "group": "user"
        }
    id = 2
    repo.patch(id, changes)

    assert data == expe_out
