class Car:
    def __init__(self, registration_num, max_speed, current_speed=0, travel_distance=0):
        self.registration_num = registration_num
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.travel_distance = travel_distance

class new_car:
    def __init__(self,speed_change,):
#main program for this
car = Car("ABC-123", "142 km/h")
print(f" Registration number : {car.registration_num}\n Max speed : {car.max_speed}\n Current speed : {car.current_speed}\n Travelled distance : {car.travel_distance} ")


