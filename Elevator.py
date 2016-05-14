from threading import Thread


class Elevator(Thread):
    request = 0
    goal = 0

    def __init__(self):
        self.floor = 0
        Thread.__init__(self)
        self.end = False

    def is_elevator_on_goal(self):
        return self.floor == self.goal

    def print_status(self):
        if self.is_elevator_on_goal():
            print("Elevator {0} on goal floor {1}".format(self.getName(), self.goal))
        else:
            print("Elevator {0} in floor {1} going to {2}".format(self.getName(), self.floor, self.goal))

    def step(self):
        if self.floor < self.goal:
            self.floor += 1
        elif self.floor > self.goal:
            self.floor -= 1

    def set_goal(self, new_goal):
        self.goal = new_goal

    def run(self):
        pass

    def stop(self):
        self.end = True
