import numpy as np
#read from txt file
file = open("2024/day1-input.txt", "r")
lines = file.readlines()
file.close()
list1 = []
list2 = []
for line in lines:
    #append the integer value of the line to the list split by the space
    list1.append(int(line.split("   ")[0]))
    list2.append(int(line.split("   ")[1]))
#sort the lists
list1.sort()
list2.sort()
locations= np.column_stack((list1,list2))
#initialize the sum
sum = 0
for location1,location2 in locations:
    if location1>location2:
        sum += location1 - location2
    else:
        sum += location2 - location1
print(sum)
    