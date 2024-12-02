input=open("day1-part1-input.txt","r")
measurments=[int(measurment) for measurment in input]
counter=0
for i in range(1,len(measurments)):
    counter+=(measurments[i]-measurments[i-1])>0
print(counter)