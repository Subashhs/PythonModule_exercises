class Car:
    def __init__(self, registration_num, max_speed, current_speed=0, travel_distance=0):
        self.registration_num = registration_num
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.travel_distance = travel_distance

car = Car("ABC-123", "142 km/h")

print(f"Registration number : {car.registration_num} Max speed : {car.max_speed} Current speed :{car.current_speed} Travelled distance : {car.travel_distance} ")

