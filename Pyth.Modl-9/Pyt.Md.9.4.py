import random


class Car:
    def __init__(self, registration_num, max_speed, current_speed=0, travel_distance=0):
        self.registration_num = registration_num
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.travel_distance = travel_distance

    def acceleration(self, speed_change):
        if speed_change > 0:
            self.current_speed = min(self.max_speed, self.current_speed + speed_change)
        else:
            self.current_speed = max(0, self.current_speed + speed_change)

    def drive(self, hours):
        self.travel_distance += self.current_speed * hours


# Create a list of 10 cars with random speeds
cars = [Car(f"ABC-{i}", f"{random.randint(100, 200)} km/h") for i in range(1, 11)]

# Race loop
while all(car.travel_distance < 10000 for car in cars):
    for car in cars:
        # Change speed with a random value between -10 and +15
        speed_change = random.randint(-10, 15)
        car.acceleration(speed_change)

        # Drive for one hour
        car.drive(1)

# Print the results in a clear table
print(f"{'Registration Number':<20} {'Max Speed':<20} {'Final Speed':<20} {'Travel Distance':<20}")
print("=" * 80)
for car in cars:
    print(f"{car.registration_num:<20} {car.max_speed:<20} {car.current_speed:<20} {car.travel_distance:<20}")
