import numpy as np
#read from txt file
file = open("day1-input.txt", "r")
lines = file.readlines()
file.close()
list1 = []
list2 = []
for line in lines:
    #append the integer value of the line to the list split by the space
    list1.append(int(line.split("   ")[0]))
    list2.append(int(line.split("   ")[1]))

counter={}
sum=0
#iterate over the first list
for location in list1:
    if location not in counter:
        counter[location]=list2.count(location)
    sum+=counter[location]*location
print(sum)