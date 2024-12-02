import re
from bidict import bidict
import numpy as np

with open("day-15-input.txt", "r") as puzzle_input:
    puzzle_input=list(map(int, re.split(",", puzzle_input.read())))
    numbers = dict((i,[j]) for (j,i) in enumerate(puzzle_input[:-1], 1))
    seen_last = puzzle_input[-1]
    numbers[seen_last] =[len(numbers)+1]
    i = len(numbers)+1
    print(numbers)
    placement = numbers[seen_last]
    while i <= 30000000:
        if len(placement)==1:
            new_number=0
        else:
            new_number=i-1-placement[-2]
        try:
            placement=numbers[new_number]
            placement.append(i)
        except:
            placement=numbers[new_number]=[i]
        i += 1

    print(new_number)
