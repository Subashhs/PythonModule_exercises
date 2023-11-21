class Car:
    def __init__(self, registration_num, max_speed, current_speed= 0, travel_distance=0):
        self.registration_num = registration_num
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.travel_distance = travel_distance

#adding acceleration with min and max
    def acceleration(self, speed_change):
        if speed_change < 0:
            self.current_speed = max(0, self.current_speed + speed_change)
        else:
            self.current_speed = min(0, self.current_speed + speed_change)

#main program for this
car = Car("ABC-123", "142 km/h")

#accelerate the car
car.acceleration(30)
car.acceleration(70)
car.acceleration(50)

#print out the current speed
print(f"Current speed if the Car: {car.current_speed} km\h")
car.acceleration(-200)


print(f"Final speed of the care after emergency brake: {car.current_speed} km/h")





