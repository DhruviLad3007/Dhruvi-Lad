class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

class ElectricCar(Car):
    def charge(self):
        print("Electric car is charging")

e = ElectricCar()
e.start()
e.drive()
e.charge()
