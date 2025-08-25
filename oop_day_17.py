# class User:
#     def __init__(self):
#         print("New User being created")  # every time this statement is triggered when we created new object and calls the class

# user_1=User()
# user_1.id="001"
# user_1.username="Jaweria"

# print(user_1.username)
 
# user_2=User()
# user_2.id="002"
# user_2.username="Jia"
# print(user_2.username)

class User:
    def __init__(self,user_id,username):
        self.id=user_id
        self.username=username
        self.followers=0 # default value
        self.following=0
    def follow(self,user):
        user.followers+=1
        self.following+=1
user_1=User("001","Jaweria") # user_1 is the object
# print(user_1.username)
user_2=User("002","Jiya") # user_2 is the object
# print(user_2.username)
# print(user_1.followers)
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)


    
    