input=[line.strip() for line in open("day3-part1-input.txt","r")]
gammaRate=0
for j in range(len(input[0])):
    counter=0
    for i in range(len(input)):
        counter+=input[i][j]=="1"
    gammaRate<<=1
    gammaRate+=counter>len(input)/2
epsilonRtae=2**len(input[0])-1-gammaRate
print(bin(gammaRate))
print(bin(epsilonRtae))
print(bin(2**len(input[0])))
powerConsumption=gammaRate*epsilonRtae
print((powerConsumption))
