#read txt file
with open('2025/day3-input.txt') as f:
    lines = f.readlines()
    lines = [list(line.strip()) for line in lines]
counter1 = 0
for line in lines:
    max_joltage = 0
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            if int(line[i]+line[j]) > max_joltage:
                max_joltage = int(line[i]+line[j])
    counter1 += max_joltage
def joltage_counter(batteries,number_of_batteries):
    if number_of_batteries == 0:
        return ''
    max_jolt_index=0
    for i in range(1,len(batteries)-number_of_batteries+1):
        if int(batteries[i])>int(batteries[max_jolt_index]):
            max_jolt_index=i
    return batteries[max_jolt_index]+joltage_counter(batteries[max_jolt_index+1:],number_of_batteries-1)
counter2 = 0
for line in lines:
    joltage=int(joltage_counter(line,12))
    print(joltage)
    counter2 += joltage
print(counter1)
print(counter2)