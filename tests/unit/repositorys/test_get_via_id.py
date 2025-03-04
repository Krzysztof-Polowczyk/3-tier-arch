from app.repositoris import persitance
from pytest import raises


def test_get_user_via_di():
    repo = persitance(
        {
            1:{
            "firstName":"alex",
            "lastName":"zizka",
            "birthYear": 1204,
            "group": "admin"
            },
            2:{
            "firstName":"alex",
            "lastName":"zizka",
            "birthYear": 1204,
            "group": "admin"
            },
            3:{
            "firstName":"alex",
            "lastName":"zizka",
            "birthYear": 1204,
            "group": "admin"
            },
        }
    )

    expe_out = {
        "id": 2,
        "firstName":"alex",
        "lastName":"zizka",
        "birthYear": 1204,
        "group": "admin"
        }
    
    assert repo.get(2) == expe_out


def test_get_user_via_di_wrong_id():
    repo = persitance(
        {
            1:{
            "firstName":"alex",
            "lastName":"zizka",
            "birthYear": 1204,
            "group": "admin"
            },
            2:{
            "firstName":"alex",
            "lastName":"zizka",
            "birthYear": 1204,
            "group": "admin"
            },
            3:{
            "firstName":"alex",
            "lastName":"zizka",
            "birthYear": 1204,
            "group": "admin"
            },
        }
    )

    with raises(ValueError) as e:
        repo.get(10)
    assert str(e.value) == "no id 10"
