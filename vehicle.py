# Vehicle classes demonstrating polymorphism

class Vehicle:
    def move(self):
        pass  # To be overridden by subclasses


class Car(Vehicle):
    def move(self):
        print("Driving on the road 🚗")


class Plane(Vehicle):
    def move(self):
        print("Flying in the sky ✈️")


class Boat(Vehicle):
    def move(self):
        print("Sailing on water 🚢")


# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    vehicle.move()
