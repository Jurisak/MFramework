from threading import Thread
from enum import Enum


class Movement(Enum):
    up = 1
    down = 2
    pick = 3
    skip = 4
    unknown = 5


class Elevator(Thread):

    def __init__(self):
        self.floor = 0
        self.goal = []
        self.pickups = []
        Thread.__init__(self)
        self.end = False

    def is_elevator_on_goal(self):
        return self.floor in self.goal or self.goal == []

    def get_movement(self):
        if len(self.goal) == 0:
            return Movement.skip

        if self.floor < self.goal[0]:
            self.goal.sort()
            return Movement.up
        elif self.floor > self.goal[0]:
            return Movement.down
        elif self.floor in self.goal:
            return Movement.skip
        else:
            return Movement.unknown

    def do_move(self, move):
        if self.floor in self.pickups:
            self.pickups.remove(self.floor)
            print("Picked Up a human in way")
        elif move == Movement.skip and self.floor in self.goal:
            self.goal.remove(self.floor)
        elif move == Movement.up:
            self.floor += 1
        elif move == Movement.down:
            self.floor -= 1

    def print_status(self):
        if self.is_elevator_on_goal():
            print("Elevator {0} on floor {1}".format(self.getName(), self.floor))
        else:
            print("Elevator {0} in floor {1} going to {2}".format(self.getName(), self.floor, self.goal))

    def step(self):
        move = self.get_movement()
        self.do_move(move)

    def set_goal(self, new_goal):
        if new_goal not in self.goal:
            self.goal.append(new_goal)

    def add_pickup(self, pickup):
        self.pickups.append(pickup)

    def is_possible_pickup(self, pickup):
        move = self.get_movement()
        return (self.floor < pickup and move == Movement.up) or (self.floor > pickup and move == Movement.down) or \
            (self.floor == pickup)

    def run(self):
        pass

