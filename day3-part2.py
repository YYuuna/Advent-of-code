#read content of file
file = open("day3-input.txt", "r")
content=file.read()
file.close()
# read valid instructions using regex
import re
pattern = "mul\\(\\d+,\\d+\\)|do\\(\\)|don't\\(\\)"
instructions = re.findall(pattern, content)
factors = []
state=True
for insturction in instructions:
    if insturction == "do()":
        state=True
    elif insturction == "don't()":
        state=False
    elif state:
        factors.append([int(factor) for factor in re.findall("\\d+",insturction)])
#initialize the sum
sum = 0
for factor in factors:
    sum+=factor[0]*factor[1]
print(sum)