import numpy as np


def grow_universe(universe):
    universe = np.insert(universe, (0, forth_dimension), '.', axis=0)
    universe = np.insert(universe, (0, depth), '.', axis=1)
    universe = np.insert(universe, (0, height), '.', axis=2)
    universe = np.insert(universe, (0, width), '.', axis=3)

    return universe


def get_neighbors(universe, cube):
    neighbors = universe[cube[0] - 1:cube[0] + 2, cube[1] - 1: cube[1] + 2, cube[2] - 1:cube[2] + 2,cube[3]-1:cube[3]+2]
    return neighbors


def active_cubes_counter(cubes):
    active_cubes_filter = cubes == "#"
    return len(cubes[active_cubes_filter])


with open("day-17-input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().split("\n")
    #puzzle_input=".#.\n..#\n###".split("\n")
    puzzle_input = [list(line) for line in puzzle_input]
    universe = np.array(puzzle_input, ndmin=4)
    forth_dimension = len(universe)
    depth = len(universe[0])
    height = len(universe[0][0])
    width = len(universe[0][0][0])

    print(universe)
    universe = grow_universe(universe)
    depth += 2
    height += 2
    width += 2
    forth_dimension+=2
    print(universe)
    for cycle in range(6):
        universe = grow_universe(universe)
        forth_dimension+=2
        depth += 2
        height += 2
        width += 2
        new_universe=universe.copy()
        for f in range(1,forth_dimension-1):
            for d in range(1, depth - 1):
                for h in range(1, height - 1):
                    for w in range(1, width - 1):
                        active_cubes = active_cubes_counter(get_neighbors(universe, (f,d, h, w)))
                        if universe[f,d, h, w] == "#":
                            if not (active_cubes == 3 or active_cubes == 4):
                                new_universe[f,d, h, w] = "."
                        elif active_cubes == 3:
                            new_universe[f,d, h, w] = "#"
        universe=new_universe
        print(active_cubes_counter(universe))
