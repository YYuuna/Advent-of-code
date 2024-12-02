import re
import math

orientations = ["E", "S", "W", "N"]
ship = (0+0j)
waypoint = complex(10, 1)


def rotate_waypoint(waypoint,direction,angle):
    angle = int(angle) * math.pi / 180
    if direction=="R":angle=-angle
    rotation = complex(int(math.cos(angle)), int(math.sin(angle)))
    waypoint *= rotation
    return waypoint
def move_waypoint(waypoint,direction, distance):
    distance = int(distance)
    if direction == "N":
        waypoint += distance * complex(0, 1)
    elif direction == "S":
        waypoint -= distance * complex(0, 1)
    elif direction == "E":
        waypoint += distance
    elif direction == "W":
        waypoint -= distance
    return waypoint


def move(ship, waypoint, distance):
    distance = int(distance)
    ship += distance * waypoint
    return ship

with open("day-12-input.txt", "r") as puzzle_input:
    puzzle_input = re.findall("([FEWNSRL])(\d+)", puzzle_input.read())

    orientaion = "E"
    for instruction in puzzle_input:
        if instruction[0] in "RL":
            waypoint=rotate_waypoint(waypoint,*instruction)
        elif instruction[0] in "NESW":
            waypoint=move_waypoint(waypoint,*instruction)
        else:
            ship=move(ship, waypoint, instruction[1])
    print(puzzle_input)
    print(ship)
    manhattan_distance = abs(ship.real) + abs(ship.imag)
    print(manhattan_distance)
