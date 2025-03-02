from app.repositoris import persitance

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

