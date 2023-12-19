class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_to_floor(self, target_floor):
        while self.current_floor != target_floor:
            if self.current_floor < target_floor:
                self.floor_up()
            else:
                self.floor_down()

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator moved up to floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator moved down to floor {self.current_floor}")


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]

    def run_elevator(self, elevator_num, destination_floor):
        elevator = self.elevators[elevator_num - 1]  # Elevator numbers start from 1
        print(f"Running Elevator {elevator_num} from floor {elevator.current_floor} to floor {destination_floor}")
        elevator.go_to_floor(destination_floor)


# Test the Building class
building = Building(bottom_floor=1, top_floor=10, num_elevators=3)

# Run elevators in the building
building.run_elevator(1, 7)
building.run_elevator(2, 3)
building.run_elevator(3, 9)
