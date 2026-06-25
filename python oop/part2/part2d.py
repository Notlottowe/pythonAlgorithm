# Polymorphism

# Polymorphism means "Having miltiple froms"

# Poly = many, Morph = forms

class Vehicle:
    def __init__(self, brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print(f"{self.model} is staring")
    
    def stop(self):
        print(f"{self.model} is stopping")

class Car(Vehicle):
    def __init__(self, brand, model,year, number_of_doors):
        super().__init__(brand,model,year)
        self.number_of_doors = number_of_doors

    def start_car(self):
        print(f"{self.model} is staring")
    
    def stop_car(self):
        print(f"{self.model} is stopping")

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand,model,year)

    def start_bike(self):
        print(f"{self.brand} is starting")
    
    def stop_bike(self):
        print(f"{self.brand} is stopping")

class Plane(Vehicle):
    def __init__(self,brand,model, year, number_of_doors):
        self.brand = brand
        self.model = model
        self.year = year
        self.number_of_doors = number_of_doors

vehicles: list[Vehicle] = {
    Car("ford", "Focus", 2008, 5),
    Motorcycle("Honda","scoopy", 2018),
    Plane("Boeing","747",2015,16)
}

for vehicle in vehicles:
    print(f"Inspecting {vehicle.brand}, {vehicle.model},({type(vehicle).__name__})")
    vehicle.start()
    vehicle.stop()

# for vehicle in vehicles:
#     if isinstance(vehicle, Car):
#         print(f"Inspecting {vehicle.brand}, {vehicle.model},({type(vehicle).__name__})")
#         vehicle.start_car()
#         vehicle.stop_car()
#     elif isinstance(vehicle, Motorcycle):
#         print(f"Inspecting {vehicle.brand}, {vehicle.model},({type(vehicle).__name__})")
#         vehicle.start_bike()
#         vehicle.stop_bike()
#     else:
#         raise Exception("Object is not a vehicle")