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
        self.goal = 0
        self.pickups = []
        Thread.__init__(self)
        self.end = False

    def is_elevator_on_goal(self):
        return self.floor == self.goal

    def get_movement(self):
        if self.floor < self.goal:
            return Movement.up
        elif self.floor > self.goal:
            return Movement.down
        elif self.floor == self.goal:
            return Movement.skip
        else:
            return Movement.unknown

    def translate_move(self, move):
        if move == Movement.up:
            return "up"
        elif move == Movement.down:
            return "down"
        else:
            raise Exception("Unknown movement {0}".format(move))

    def do_move(self, move):
        if self.floor in self.pickups:
            self.pickups.remove(self.floor)
            goal_movement = self.get_movement()
            print("Picked Up a human in way {0}".format(self.translate_move(goal_movement)))
        elif move == Movement.up:
            self.floor += 1
        elif move == Movement.down:
            self.floor -= 1

    def print_status(self):
        if self.is_elevator_on_goal():
            print("Elevator {0} on goal floor {1}".format(self.getName(), self.goal))
        else:
            print("Elevator {0} in floor {1} going to {2}".format(self.getName(), self.floor, self.goal))

    def step(self):
        move = self.get_movement()
        self.do_move(move)

    def set_goal(self, new_goal):
        self.goal = new_goal

    def add_pickup(self, pickup):
        self.pickups.append(pickup)

    def is_possible_pickup(self, pickup):
        move = self.get_movement()
        return (self.floor < pickup and move == Movement.up) or (self.floor > pickup and move == Movement.down) or \
            (self.floor == pickup)

    def run(self):
        pass

