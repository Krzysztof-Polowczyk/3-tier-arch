from app.repositoris import persitance

def test_get_all():
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
    expe_out = [
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
    assert repo.get_all() == expe_out
