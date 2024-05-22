class User():
    
    def __init__(self,user_id,name):
        self.id = user_id
        self.username = name
        self.followers = 0 #This followers attribute has been set to a default value of 0 which can be modified later
        self.following = 0
        
    def follow(self,user):
        user.followers += 1
        self.following += 1
        
    
person1 = User("001","Abhinav")
person2 = User("002","Mars")

person1.follow(person2) #person1 started following person2

print(person1.following)
print(person1.followers)
print(person2.following)
print(person2.followers)