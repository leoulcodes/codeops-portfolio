
# day05/practice.py

from abc import ABC, abstractmethod

# 1 & 5. Vehicle as Abstract Base Class
class Vehicle(ABC):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def describe(self):
        return f"{self.make} {self.model}"

    @abstractmethod
    def wheels(self):
        pass


# 1. Car subclass
class Car(Vehicle):
    def wheels(self):
        return 4


# 2 & 3. Truck subclass using super() and overriding
class Truck(Vehicle):
    def __init__(self, make, model, capacity):
        super().__init__(make, model)  # using super()
        self.capacity = capacity

    # 3. Override describe()
    def describe(self):
        return f"{self.make} {self.model} with capacity {self.capacity} tons"

    def wheels(self):
        return 6


# 4. Polymorphism
if __name__ == "__main__":
    vehicles = [
        Car("Toyota", "Corolla"),
        Truck("Volvo", "FH16", 20),
        Car("Honda", "Civic"),
        Truck("Mercedes", "Actros", 25)
    ]

    for v in vehicles:
        print(v.describe())
        print(f"Wheels: {v.wheels()}")
        print("-" * 30)