from app.repositoris import persitance

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

