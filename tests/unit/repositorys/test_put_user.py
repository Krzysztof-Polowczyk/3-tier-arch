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

def test_put_user_wrong_user():
    data = {
            2:{
            "firstName":"alex",
            "lastName":"zizka",
            "birthYear": 1204,
            "group": "admin"
            },
        }
    repo = persitance(data)

    user_to_add={
            "firstName":"mike",
            "lastName":"zizka",
            "birthYear": 123,
            "group": "user",
            "kkk": "user"
        }
    

    with raises(ZeroDivisionError) as e:
        repo.add(user_to_add)
    assert str(e.value) == "err"
    

def test_put_user_wrong_acces():
    data = {
            2:{
            "firstName":"alex",
            "lastName":"zizka",
            "birthYear": 1204,
            "group": "admin"
            },
        }
    repo = persitance(data)

    user_to_add={
            "firstName":"mike",
            "lastName":"zizka",
            "birthYear": 123,
            "group": "special"
        }
    

    with raises(ZeroDivisionError) as e:
        repo.add(user_to_add)
    assert str(e.value) == "err"
    