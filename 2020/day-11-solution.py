import numpy as np
import re


def count_occupied_seats(seats):
    occupied = seats == "#"
    return len(seats[occupied])


def cycle(grid):
    new_grid = grid.copy()
    for x in range(1, h_rows + 1):
        for y in range(1, v_rows + 1):
            if grid[x, y] == "L" and visible_occupied_seats(grid, x, y) == 0:
                new_grid[x, y] = "#"
            if grid[x, y] == "#" and visible_occupied_seats(grid, x, y) >= 5:
                new_grid[x, y] = "L"
    return new_grid


def visible_occupied_seats(grid, x, y):
    seats_count = 0
    for i in range(x + 1, len(grid)):
        if grid[i, y] == "L":
            break
        elif grid[i, y] == "#":
            seats_count += 1
            break
    for i in range(x -1, 0, -1):
        if grid[i, y] == "L":
            break
        elif grid[i, y] == "#":
            seats_count += 1
            break
    for i in range(y + 1, len(grid[0])):
        if grid[x, i] == "L":
            break
        elif grid[x, i] == "#":
            seats_count += 1
            break
    for i in range(y-1 , 0, -1):
        if grid[x, i] == "L":
            break
        elif grid[x, i] == "#":
            seats_count += 1
            break
    i=1
    while(grid[x + i, y + i] not in "L!"):
        if grid[x + i, y + i] == "#":
            seats_count += 1
            break
        i+=1
    i=1
    while(grid[x - i, y - i]not in "L!"):
        if grid[x - i, y - i] == "#":
            seats_count += 1
            break
        i+=1
    i=1
    while(grid[x - i, y + i] not in "L!"):
        if grid[x - i, y + i] == "#":
            seats_count += 1
            break
        i+=1
    i=1
    while(grid[x + i, y - i] not in "L!"):
        if grid[x + i, y - i] == "#":
            seats_count += 1
            break
        i+=1
    return seats_count


with open("day-11-input.txt", "r") as puzzle_input:
    seats = re.split("\s", puzzle_input.read())
    seats = np.array([list(row) for row in seats], ndmin=2)
    h_rows = len(seats)
    v_rows = len(seats[0])
    seats = np.insert(seats, (0, h_rows), "!", axis=0)
    seats = np.insert(seats, (0, v_rows), "!", axis=1)
    new_grid = cycle(seats)
    while (not np.array_equal(seats, new_grid)):
        seats = new_grid
        new_grid = cycle(seats)
    print(count_occupied_seats(seats))
