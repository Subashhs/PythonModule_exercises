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


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.acceleration(speed_change)
            car.drive(1)

    def print_status(self):
        print(f"{'Registration Number':<20} {'Max Speed':<20} {'Current Speed':<20} {'Travel Distance':<20}")
        print("="*80)
        for car in self.cars:
            print(f"{car.registration_num:<20} {car.max_speed:<20} {car.current_speed:<20} {car.travel_distance:<20}")

    def race_finished(self):
        return any(car.travel_distance >= self.distance for car in self.cars)


# Main program
def main():
    # Create a list of 10 cars for the Grand Demolition Derby
    cars = [Car(f"ABC-{i}", f"{random.randint(100, 200)} km/h") for i in range(1, 11)]

    # Create the Grand Demolition Derby race with a distance of 8000 kilometers
    grand_derby = Race("Grand Demolition Derby", 8000, cars)

    # Simulate the race progress
    hours_elapsed = 0
    while not grand_derby.race_finished():
        grand_derby.hour_passes()
        hours_elapsed += 1

        # Print the status every ten hours and at the end of the race
        if hours_elapsed % 10 == 0 or grand_derby.race_finished():
            print(f"\nRace Status After {hours_elapsed} Hours:")
            grand_derby.print_status()

    print("\nRace Finished!")

if __name__ == "__main__":
    main()
