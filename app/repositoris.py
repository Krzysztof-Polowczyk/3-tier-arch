class persitance:
    def __init__(self, users:dict={}):
        self.users = users
        self.user_count= max(users.keys()) if users else 0

    def get_all(self) -> list:
        l = []
        for i in self.users:
             l.append(self.users[i]|{"id":i})
        return l
    
    def get(self, id:int=0) -> list: 
        if id in self.users:
            return self.users[id] | {"id":id}
        else:
            raise ValueError("no id " + str(id))
    
    def add(self, user:dict):
        
        if user.keys() != {"firstName","lastName","birthYear","group"}: raise ZeroDivisionError("err")
        if not user["group"] in ["user", "premium", "admin"]: raise ZeroDivisionError("err")
        self.user_count +=1
        self.users[self.user_count] = user


    def patch(self, id:int, data:dict):
        if id not in self.users: raise ValueError("no id "+str(id))
        for key in data:
            if key not in {"firstName","lastName","birthYear","group"}: raise ZeroDivisionError("err")
        if not data["group"] in ["user", "premium", "admin"]: raise ZeroDivisionError("err")
        for key, val in data.items():
            self.users[id][key] = val
  
    def dell(self, id:int):
        if id in self.users:
            self.users.pop(id)
        else:
            raise ValueError("no id "+str(id))


    