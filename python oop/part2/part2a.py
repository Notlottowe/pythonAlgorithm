# Static Attributes
# A static attribute (sometimes called a class attributes) is an attribute that belongs to the class itself, not to any specific instance of the calss.


class User:
    user_count = 0

    def __init__(self,username,email):
        self.username = username
        self.email = email
        User.user_count += 1
    
    def display_user(self):
        print(f"username : {self.username}, email: {self.email}")


user1 = User("bob","123")
user1 = User("ace","321")

print(User.user_count)