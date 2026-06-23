class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password

    @property
    def email(self):
        print("Email accessed")
        return self._email

    @email.setter
    def email(self,new_email):
        if "@" in new_email:
            self._email = new_email


user1 = User("bob", "bob@", "123")


#user1.email = "123"
user1.email = "123sss"
print(user1.email)

