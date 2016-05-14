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
            elevator.stop()
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
    def is_order_in_input(input_data):
        first_num = input_data[0]
        second_num = input_data[-1]
        return first_num.isdigit() and second_num.isdigit() and input_data.find(" ") != -1

    def is_correct_floor_or_goal(self, data):
        return int(self.floor_size) >= int(data)

    @staticmethod
    def parse_data_digits(input_data):
        splited_by_space = input_data.split(" ")
        return splited_by_space[0], splited_by_space[-1]

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

    def do_elevator_logic(self, floor, goal, elevators):
        for elevator in elevators:
            if elevator.is_elevator_on_goal():
                elevator.set_goal(int(goal))
                break

    def do_behavior_logic(self, input_data, elevators):
        if self.is_status_printing(input_data):
            self.print_elevators_status(elevators)
        elif self.is_order_in_input(input_data.strip()):
            self.parse_data_digits(input_data)
            floor, goal = self.parse_data_digits(input_data)
            if self.is_correct_floor_or_goal(floor) and self.is_correct_floor_or_goal(goal):
                self.do_elevator_logic(floor, goal, elevators)
            else:
                print("You've passed higher floor or goal value than it's possible")
                print("Maximum floor size is {0}".format(self.floor_size))


# Run following code when the program starts
if __name__ == '__main__':
    system = ElevatorSystem(10, 4)
    system.run_system()
