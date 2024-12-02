input = open("day-3-input.txt", "r")
biome = [line.strip() for line in input]
pattern_width = len(biome[0])
pattern_leangth = len(biome)

'''Starting at the top-left corner of your map and following a slope of right 3 and down 1,
    how many trees would you encounter?'''

slopes = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]


def traverse(biome, slope):
    trees_count = 0
    location = [0, 0]
    while pattern_leangth > location[0]:
        if biome[location[0]][location[1]] == "#":
            trees_count += 1
        location[0] += slope[0]
        location[1] += slope[1]
        location[1] %= pattern_width
    return (trees_count)


part2_answer = 1
for slope in slopes:
    part2_answer *= traverse(biome, slope)
print(part2_answer)
