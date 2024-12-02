input=[int(line) for line in open("day1-part1-input.txt")]
counter=0
for i in range(len(input)-3) :
    counter+=(input[i+3]+input[i+2]+input[i+1])>(input[i+2]+input[i+1]+input[i])
print(counter)