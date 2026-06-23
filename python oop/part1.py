#name = "jon" #str
#age = 21 #int

#print(type(name))
#print(name.upper())
#print(type(age))


class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("bark")


dog1 = Dog("Bruce","Lab")
print(dog1.name)


dog2 = Dog("freya","Husky")
print(dog2.name)