class Car:
    created = 0
    def __init__(self, reg_num, max_speed, travel_dist = 0):
        self.reg_num = reg_num
        self.travel_dist = travel_dist
        self.max_speed = max_speed
        Car.created = Car.created + 1

    def accelerate(self, speed_change):
        self.speed_change = speed_change

    def drive(self, hour):
        self.hour = hour

car1 = Car("ABC-1", "100 km/h")
car2 = Car("ABC-2", "110 km/h")
car3 = Car("ABC-3", "120 km/h")
car4 = Car("ABC-4", "130 km/h")
car5 = Car("ABC-5", "140 km/h")
car6 = Car("ABC-6", "150 km/h")
car7 = Car("ABC-7", "160 km/h")
car8 = Car("ABC-8", "170 km/h")
car9 = Car("ABC-9", "180 km/h")
car10 = Car("ABC-10", "190 km/h")




"""import random


class Car:
    def __init__(self, registration_num):
        self.registration_num = registration_num
        self.max_speed = random.randint(100, 200)
        self.current_speed = 0
        self.travel_distance = 0

    def accelerate(self):
        speed_change = random.randint(-10, 15)
        self.current_speed = max(0, min(self.max_speed, self.current_speed + speed_change))

    def drive(self, hours=1):
        self.accelerate()
        distance_traveled = self.current_speed * hours
        self.travel_distance += distance_traveled


# Main program for the car race
cars = [Car(f"ABC-{i}") for i in range(1, 11)]

race_finished = False

while not race_finished:
    for car in cars:
        car.drive()

    race_finished = any(car.travel_distance >= 10000 for car in cars)

# Print out the properties of each car in a simple format
for car in cars:
    print(f"{car.registration_num}: Distance - {car.travel_distance} km, Current Speed - {car.current_speed} km/h")
"""