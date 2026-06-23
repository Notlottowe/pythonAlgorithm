#name = "jon" #str
#age = 21 #int

#print(type(name))
#print(name.upper())
#print(type(age))


class Dog:
    def __init__(self,name,breed,owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def bark(self):
        print("bark")

class owner:
    def __init__(self,name,address,contact_number):
        self.name = name
        self.address = address
        self.phone_number = contact_number

owner1 = owner("bob","101 k st","123456789")

dog1 = Dog("Bruce","Lab",owner1)
#print(dog1.name)
print(dog1.owner.name)


dog2 = Dog("freya","Husky",owner1)
#print(dog2.name)