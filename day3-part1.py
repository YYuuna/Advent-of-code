#read content of file
file = open("day3-input.txt", "r")
content=file.read()
file.close()
#read using regex of the pattern "mul(\d+,\d+)" then split
import re
pattern = "mul\\(\\d+,\\d+\\)"
instructions = re.findall(pattern, content)
factors = []
# get the degits couple into a list on integers
for insturction in instructions:
    factors.append([int(factor) for factor in re.findall("\\d+",insturction)])
#initialize the sum
sum = 0
for factor in factors:
    sum+=factor[0]*factor[1]
print(sum)