import re

with open("day-9-input.txt", "r") as puzzle_input:
    data = [int(number) for number in re.findall("\d+", puzzle_input.read())]
    preamble = data[:25]

    for invalid_number in range(25, len(data)):
        sums = set()
        for number1 in preamble:
            for number2 in preamble:
                if number1 != number2: sums.add(number1 + number2)
        if data[invalid_number] not in sums: break
        preamble.pop(0)
        preamble.append(data[invalid_number])
    print("invalid number :" + str(data[invalid_number]))
    for i in range(invalid_number):
        sum = data[i]
        for j in range(i + 1, invalid_number):
            sum += data[j]
            if sum >= data[invalid_number]: break
        if sum == data[invalid_number]: break
    print("{} + {} = {}".format(min(data[i:j+1]), max(data[i:j+1]), min(data[i:j+1]) + max(data[i:j+1])))
    sum = 0
    for x in range(i, j + 1):
        sum += data[x]
    print(sum)
