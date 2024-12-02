import re
import  numpy as np
from itertools import permutations

with open("day-13-input.txt", "r") as puzzle_input:
    #part_one
    puzzle_input = re.split("\n", puzzle_input.read())
    earliest_depart_time = int(puzzle_input[0])
    bus_ids=[tuple(reversed(x)) for x in enumerate(map(lambda x : int(x) if x!="x" else None ,re.split(",",puzzle_input[1]))) if x[1]!=None]
    wait_times=[(bus_id,bus_id-(earliest_depart_time % bus_id)) for bus_id in list(zip(*bus_ids))[0]]
    wait_time=min(wait_times,key=lambda x : x[1])
    print(wait_time)
    print(np.prod(wait_time))
    #super_long_part_two
    """bus_ids=sorted(bus_ids,key=lambda id:id[0],reverse=True)#????????????????????
    t=bus_ids[0][0]-bus_ids[0][1]
    valid_time_stamp=False
    while not valid_time_stamp:
        for bus_id in bus_ids[1:]:
            valid_time_stamp=((t+bus_id[1])%bus_id[0]==0)
            if not valid_time_stamp:
                t+=bus_ids[0][0]
                break"""
    #better part two

    bus_ids=list(map(lambda id : (id[0], -id[1]), bus_ids))
    stack=[bus_ids[0]]
    for (q_i,r_i) in bus_ids[1:]:
        for (q_j,r_j) in stack:
            r_i=(r_i-r_j)%q_i
            r_i=(r_i*pow(q_j,-1,q_i))%q_i
        stack.append((q_i,r_i))
    q, t=stack.pop()
    while stack:
        (q,r)=stack.pop()
        t*=q
        t+=r
    print(t)
