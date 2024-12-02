input=[line.strip() for line in open("day3-part1-input.txt","r")]
oxygen=0
co2=0
for j in range(len(input[0])):
    counter=0
    for line in (input):
        counter+=line[j]=="1"
    if counter>=500:
        for line in input:
            if line[j]=="0":
                input.remove(line)
    else:
        for line in input:
            if line[j]=="1":
                input.remove(line)
print(input)
        