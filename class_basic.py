class User:
    def __init__(self,user_id,name):
        self.id = user_id
        self.name = name
        self.followers = 0 #default value


user1 = User("01","Puja")

print(user1.name)
print(user1.followers)
        