import re

jolt_differences_count = {1: 0, 2: 0, 3: 1}
number_of_compositions_size_restricted_by_3 = {0: 1, 1: 1, 2: 2, 3: 4, 4: 7}
# Restricted part size by 3 of partinitions of sub differences of ones
with open("day-10-input.txt", "r") as input:
    jolts = [0]+sorted([int(jolt) for jolt in input.read().split("\n")])
    #example = "0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49"
    #example2="0, 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19"
    jolts = sorted(int(jolt) for jolt in jolts)
    jolt_differences_list=[]
    for i in range(len(jolts)-1):
        jolt_difference = jolts[i + 1] - jolts[i]
        jolt_differences_count[jolt_difference] += 1
        jolt_differences_list.append(jolt_difference)
    partitions = re.split("3+", ''.join(str(diff) for diff in jolt_differences_list))
    arrangements_count = 1
    for partition in partitions:
        arrangements_count *= number_of_compositions_size_restricted_by_3[len(partition)]

    print(jolt_differences_count)
    #answer 1
    #print(jolt_differences_count[1] * jolt_differences_count[3])
    print(partitions)
    print(arrangements_count)
