# Inheritance

# Inheritance is a fundamental concept in object-oriented programming (OOP) that involves creating new classes (subclasses ot derived calsses) based on 
# exising classes (superclasses or base classes).

# - A Car is-a vehicle
# - A Bike is-a vehicle

class Vehicle:
    def __init__(self, brand, model, year):
         self.brand = brand
         self.model = model
         self.year = year

    def start(self):
         print(f"{self.brand} is staring")
    
    def stop(self):
         print(f"{self.brand} is stopping")


class Car(Vehicle):
    def __init__(self, brand, model, year, numbers_of_doors, numbers_of_wheels):
        super().__init__(brand,model,year)
        self.numbers_of_doors = numbers_of_doors
        self.numbers_of_wheels = numbers_of_wheels


class Bike(Vehicle):
     def __init__(self, brand, model, year, numbers_of_wheels):
        super().__init__(brand,model,year)
        self.numbers_of_wheels = numbers_of_wheels


car = Car("Ford", "Focus", 2008,5,4)
bike = Bike("Honda", "Scoopy", 2018,2)

print(car.__dict__)
print(bike.__dict__)

car.start()
bike.start()
