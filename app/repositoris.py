class persitance:
    def __init__(self, users={}):
        self.users = users
        self.user_count= max(users.keys()) if users else 0

    def get_all(self) -> list:
        l = []
        for i in self.users:
             l.append(self.users[i]|{"id":i})
        return l
    
    def get(self, id=0) -> list: 
        try:
            return self.users[id] | {"id":id}
        except:
            return {}
    
    def add(self, user:dict):
        self.user_count +=1
        self.users[self.user_count] = user


    def patch(self, id:int, data:dict):
        print(data)
        for key, val in data.items():
            self.users[id][key] = val


        
    def dell(self, id):
        if id in self.users:
            self.users.pop(id)


    