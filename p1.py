class Car:
    def __init__(self, brand, model, speed=0):
        self.brand = brand
        self.model = model
        self.speed = speed

    def accelerate(self, value):
        self.speed += value

    def brake(self, value):
        self.speed -= value

    def display(self):
        print(self.brand, self.model, "Speed:", self.speed)


c = Car("Honda", "City")
c.accelerate(20)
c.brake(5)
c.display()
