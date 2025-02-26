class User:
    # pass  // to move from this class
    #below clas has the user_id, username which is required to pass when everytime class is called if to make the default attributes then just self.folow = 0
    def __init__(self, user_id,username): 
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        
        #self is mandatory 
    def follow(self,user):
        user.followers += 1
        self.following += 1
        
    
user_1 = User('12','ranjan') 
user_2 = User('23','sam')
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
