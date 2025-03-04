from app.repositoris import persitance
class controlers:
    def __init__(self, repo: persitance = persitance()):
        self.repo = repo

    def get(self, id:int) -> dict:
        return self.repo.get(id)
   
    
    def get_all(self) -> dict:
        return self.repo.get_all()
    
    def put(self, user:dict):
        self.repo.add(user)

    
    def patch(self, id:int, user:dict):
        self.repo.patch(id,user)

    def dellete(self, id:int):
        self.repo.dell(id)
