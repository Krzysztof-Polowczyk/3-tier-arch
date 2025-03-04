from app.repositoris import persitance
from pytest import raises

def test_user_delete():

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
    }
    repo.dell(2)
    assert expe_out == data

def test_user_delete_wrong_id():

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
    }

    with raises(ValueError) as e:
        repo.dell(10)
    assert str(e.value) == "no id 10"

