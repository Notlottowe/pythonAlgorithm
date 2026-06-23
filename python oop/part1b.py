class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, My name is {self.name}, and I am {self.age} years old")


person1 = Person("bob", 31)

person1.greet()

person2 = Person("Ace", 10)

person2.greet()