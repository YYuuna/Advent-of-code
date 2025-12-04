#read txt input
import numpy as np
with open('2025/day4-input.txt') as f:
    lines = f.readlines()
    lines = [list(line.strip()) for line in lines]
grid = np.array(lines)
rows, cols = grid.shape
counter1 = 0
def get_adjacent_paper_number(grid,r, c):
    adjacent = 0
    if grid[r, c] != '@':
        return adjacent
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr, nc] == '@':
                adjacent += 1
    return adjacent
accessible_papers = set()
for i in range(rows):
    for j in range(cols):
        adj = get_adjacent_paper_number(grid, i, j)
        if adj < 4 and grid[i, j] == '@':
            accessible_papers.add((i, j))
            counter1+=1
print("Part 1:", counter1)
counter2 = 0
while accessible_papers:
    for r, c in list(accessible_papers):
        grid[r, c] = '.'
    counter2 += len(accessible_papers)
    accessible_papers=set()
    for i in range(rows):
        for j in range(cols):
            adj = get_adjacent_paper_number(grid, i, j)
            if adj < 4 and grid[i, j] == '@':
                accessible_papers.add((i, j))
print("Part 2:", counter2)