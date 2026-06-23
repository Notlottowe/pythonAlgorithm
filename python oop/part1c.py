
from datetime import datetime

class User:
    def __init__(self, username, email, password):
        self.username = username
        # self.__email === private ! can't be access outside!
        self._email = email
        self.password = password
    
    def get_email(self):
        print(f"Email accesssed at {datetime.now()}")
        return self._email
    
    def set_email(self,new_email):
        if "@" in new_email:
            self._email = new_email

    # def clean_email(self):
        # return self._email.lower().strip()

    # def get_email(self):
        # return self._email
    
    # def say_hello(self,user):
        # print(f"hello {user.username}, it's {self.username}")

# print(user1.clean_email())

user1 = User("bob","bob@","123")
user2 = User("ace","ace@","123")

user1.set_email("123@")

print(user1.get_email())


