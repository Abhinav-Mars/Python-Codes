class User():
    
    def __init__(self,user_id,name):
        self.id = user_id
        self.username = name
        self.followers = 10 #This followers attribute has been set to a default value of 10 which can be modified later
        
person1 = User("001","Abhinav")
person2 = User("002","Mars")

print(person2.followers)