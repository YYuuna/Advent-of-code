import re


def part_one_bitmasking(mask, value):
    masked_value = "".join(map(lambda bitmask, bit: bit if bitmask == "X" else bitmask, (mask), (value)))
    return int(masked_value, 2)


def part_two_bitmasking(mask, value):
    masked_value = list(map(lambda bitmask, bit: bit if bitmask == "0" else bitmask, mask, value))
    floating_addresses = []
    memory_addresses = [masked_value]
    for i in range(36):
        if masked_value[i] == "X":
            while memory_addresses:
                f_adr = memory_addresses.pop()
                f_adr = f_adr.copy()
                f_adr[i] = "0"
                floating_addresses.append(f_adr)
                f_adr = f_adr.copy()
                f_adr[i] = "1"
                floating_addresses.append(f_adr)
            memory_addresses.extend(floating_addresses)
            floating_addresses.clear()
    for i in range (len(memory_addresses)):
        memory_addresses[i]="".join(memory_addresses[i])
    return memory_addresses


with open("day-14-input.txt", "r") as puzzle_input:
    initialization_program = [re.split(" = ", line) for line in re.split("\n", puzzle_input.read())]
    memory = {}
    for instruction in initialization_program:
        if instruction[0] == "mask":
            mask = instruction[1]
        else:
            memory_address = re.search("\d+", instruction[0]).group()
            value = "{0:b}".format(int(instruction[1])).zfill(36)
            memory[memory_address] = int(part_one_bitmasking(mask, value))
    values_sum = 0
    for value in memory.values():
        values_sum += value
    print(values_sum)
    memory = {}
    for instruction in initialization_program:
        if instruction[0] == "mask":
            mask = instruction[1]
        else:
            memory_address = "{0:b}".format(int(re.search("\d+", instruction[0]).group())).zfill(36)
            value = int(instruction[1])
            for masked_memory_address in part_two_bitmasking(mask, memory_address):
                memory[masked_memory_address] = value
    values_sum = 0
    for value in memory.values():
        values_sum += value
    print(values_sum)