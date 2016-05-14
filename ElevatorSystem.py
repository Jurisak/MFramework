from Elevator import Elevator


class ElevatorSystem(object):

    def __init__(self, floor_size, elevators):
        self.floor_size = floor_size
        self.elevators_num = elevators

    def get_elevators(self):
        output = []
        for i in range(1, self.elevators_num + 1):
            output.append(Elevator())
            output[-1].setName("{0}".format(i))
        return output

    @staticmethod
    def start_elevators(elevators):
        for elevator in elevators:
            elevator.start()

    @staticmethod
    def end_elevators(elevators):
        for elevator in elevators:
            elevator.join()

    @staticmethod
    def is_end_of_listening(input_data):
        return input_data.find("end") != -1

    @staticmethod
    def is_status_printing(input_data):
        return input_data.find("print") != -1

    @staticmethod
    def print_elevators_status(elevators):
        for elevator in elevators:
            elevator.print_status()

    @staticmethod
    def is_digit(input_data):
        possible_digit = input_data.strip()
        return possible_digit.isdigit()

    def is_correct_goal(self, goal):
        return int(self.floor_size) >= goal

    def get_goal(self, data):
        return int(data.strip())

    @staticmethod
    def do_step(elevators):
        for elevator in elevators:
            elevator.step()

    def run_system(self):
        elevators = self.get_elevators()
        self.start_elevators(elevators)
        print("Pass orders")
        input_data = input()
        while not self.is_end_of_listening(input_data):
            self.print_elevators_status(elevators)
            self.do_behavior_logic(input_data, elevators)
            self.do_step(elevators)
            input_data = input()
        self.end_elevators(elevators)

    def access_goal(self, elevators, goal, floor):
        for elevator in elevators:
            if elevator.is_elevator_on_goal():
                elevator.set_goal(floor)
                elevator.set_goal(goal)
                return True
            elif elevator.is_possible_pickup(floor) and elevator.is_possible_pickup(goal):
                elevator.add_pickup(floor)
                elevator.set_goal(goal)
                return True
        return False

    def do_elevator_logic(self, floor, goal, elevators):
        if not self.access_goal(elevators, goal, floor):
            # I don't have suitable elevator for a human so I will assigned it to the first one
            for elevator in elevators:
                elevator.set_goal(floor)
                elevator.set_goal(goal)


    @staticmethod
    def is_order_in_input(input_data):
        first_num = input_data[0]
        second_num = input_data[-1]
        return first_num.isdigit() and second_num.isdigit() and input_data.find(" ") != -1

    @staticmethod
    def parse_data_digits(input_data):
        splited_by_space = input_data.split(" ")
        return int(splited_by_space[0]), int(splited_by_space[-1])

    def is_correct_floor_or_goal(self, data):
        return int(self.floor_size) >= data

    def do_behavior_logic(self, input_data, elevators):
        if len(input_data.strip()) == 0:
            return

        if self.is_order_in_input(input_data.strip()):
            floor, goal = self.parse_data_digits(input_data)
            if self.is_correct_floor_or_goal(floor) and self.is_correct_floor_or_goal(goal):
                self.do_elevator_logic(floor, goal, elevators)
            else:
                print("You've passed higher floor or goal value than it's possible")
                print("Maximum floor size is {0}".format(self.floor_size))


# Run following code when the program starts
if __name__ == '__main__':
    system = ElevatorSystem(10, 2)
    system.run_system()
