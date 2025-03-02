from app.repositoris import persitance

def test_exsistence_of_persistence():
    repo = persitance()
    assert isinstance(repo, persitance)