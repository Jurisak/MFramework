# MFramework
The purpose of this project is to implement simple elevator program

## 1. Implementation
MFramework was implemented in python3.4 and it should work also for python3.5.

### 1.1 class Elevator
This class represent single elevator. It has knowledge about floor, list of goals and list of people who want to get in. Important methods are:
- `print_status` - printing the status of a single elevator
- `do_move` - do a move according to a given movement
- `get_movement` - returns a move for a elevator step

### 1.2 class ElevatorSystem
It's a main class which runs whole elevator behavior. It expects two variables. `floor_size` is indicating size of a house on which elevators are operating. elevators is number of elevators in a house.
The most important method is `run_system` which runs the whole program. This method creates parallel `Elevator` classes and listens from input for commands. The commands are described in 1.3.

### 1.3 input commands
- end - will end whole program
- x y - where x and y are digits. X represents floor on which human push a button and y is floor on which human want to go. There must be a space between those digits
others - anything else just activate a step method for elevators.

The parsing of commands it's not made properly and as improvement I would parse it by `argparse` module.

## 2. How it works
Program expects orders which are described above. If you provide command "2 3" then first elevator which can move to 2 will be chosen. Afterwards you can easily pres enter and program will do single step of elevator movement. Also if the elevator is moving from floor 0 to 2 and there is a man who pressed a button on floor 1 then also this man will be picked up by the elevator in way up. In this case there is a "small" problem. For example if someone is traveling to 9th floor from 0th floor and the elevator picked up a human at 5th floor who wants to go to 8th floor. The elevator will go first to 9th floor and then 8th floor. I wanted to make it in normal way but due the time rush I did not make it. 

## 3. Example
```
> python3.4 ElevatorSystem.py 
Pass orders
2 3          -- passed order
Elevator 1 on floor 0
Elevator 2 on floor 0
3 4          -- passed order
Elevator 1 in floor 1 going to [2, 3]
Elevator 2 on floor 0

Elevator 1 on floor 2
Elevator 2 on floor 0

Elevator 1 in floor 2 going to [3, 4]
Elevator 2 on floor 0

Elevator 1 on floor 3
Elevator 2 on floor 0
Picked Up a human in way

Elevator 1 on floor 3
Elevator 2 on floor 0

Elevator 1 in floor 3 going to [4]
Elevator 2 on floor 0

Elevator 1 on floor 4
Elevator 2 on floor 0
end -- passed order
```

## 4. features
Fix the "small" problem described above
Make some gui for better output
Do some simulations to choose the best behavior according to floor size, number of elevators and number of possible people who would like to use it.
Better format of orders.

## 5. Usage
`python3.4 ElevatorSystem.py` and then type commands after message `Pass orders`.

If you wnat to change number of floors or elevators then change this data at line 117 in ElevatorSystem.py

\end{document}
