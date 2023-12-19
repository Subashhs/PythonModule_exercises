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


class ElectricCar(Car):
    def __init__(self, registration_num, max_speed, battery_capacity):
        super().__init__(registration_num, max_speed)
        self.battery_capacity = battery_capacity


class GasolineCar(Car):
    def __init__(self, registration_num, max_speed, tank_volume):
        super().__init__(registration_num, max_speed)
        self.tank_volume = tank_volume


# Main program
def main():
    # Create an electric car and a gasoline car
    electric_car = ElectricCar("ABC-15", "180 km/h", 52.5)
    gasoline_car = GasolineCar("ACD-123", "165 km/h", 32.3)

    # Set speeds for both cars
    electric_car.acceleration(30)
    gasoline_car.acceleration(20)

    # Drive both cars for three hours
    electric_car.drive(3)
    gasoline_car.drive(3)

    # Print out the values of their kilometer counters
    print(f"Electric Car (ABC-15) Travel Distance: {electric_car.travel_distance} km")
    print(f"Gasoline Car (ACD-123) Travel Distance: {gasoline_car.travel_distance} km")


if __name__ == "__main__":
    main()
