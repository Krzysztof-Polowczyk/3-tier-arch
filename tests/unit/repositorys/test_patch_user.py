from app.repositoris import persitance
import pytest
from pytest import raises

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


def test_put_user_wrong_id():
    data = {
            2:{
            "firstName":"alex",
            "lastName":"zizka",
            "birthYear": 1204,
            "group": "admin"
            },
        }
    repo = persitance(data)
    changes={
            "birthYear": 33446,
            "group": "user"
        }
    id = 20
    

    with raises(ValueError) as e:
        repo.patch(id, changes)
    assert str(e.value) == "no id 20"


def test_put_user_wrong_data():
    data = {
            2:{
            "firstName":"alex",
            "lastName":"zizka",
            "birthYear": 1204,
            "group": "admin"
            },
        }
    repo = persitance(data)
    changes={
            "birthYear": 33446,
            "group": "user",
            "sss":23
        }
    id = 2
    

    with raises(ZeroDivisionError) as e:
        repo.patch(id, changes)
    assert str(e.value) == "err"

def test_put_user_wrong_authority():
    data = {
            2:{
            "firstName":"alex",
            "lastName":"zizka",
            "birthYear": 1204,
            "group": "admin"
            },
        }
    repo = persitance(data)
    changes={
            "birthYear": 33446,
            "group": "kkk"
        }
    id = 2
    

    with raises(ZeroDivisionError) as e:
        repo.patch(id, changes)
    assert str(e.value) == "err"