class Car:
    def __init__(self, make, model, year, color, distance=0, speed=0):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.distance = distance
        self.speed = speed

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}, Color: {self.color}")

    def accelerate(self, acceleration):
        self.speed += acceleration

    def brake(self, deceleration):
        self.speed -= deceleration

    def drive(self, time):

        distance_traveled = self.speed * time
        self.distance += distance_traveled


car = Car("Toyota", "Camry", 2022, "Blue", distance=2000, speed=60)


car.display_info()

car.drive(1.5)

print(f"Traveled Distance: {car.distance} km")
