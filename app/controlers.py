from app.repositoris import persitance
class controlers:
    def __init__(self, repo: persitance = persitance()):
        self.repo = repo

    def get(self, id):
        return self.repo.get(id)
   
    
    def get_all(self):
        return self.repo.get_all()
    
    def put(self, user):
        self.repo.add(user)

    
    def patch(self, id, user):
        self.repo.patch(id,user)

    def dellete(self, id):
        self.repo.dell(id)
