import re
import numpy as np
#read input
with open('2024/day8-input.txt') as f:
    data=f.read()
#get set of frequencies
pattern=re.compile(r'(?!\.).')
frequencies=set(pattern.findall(data))
area=[[location for location in row ] for row in data.split()]
def getVectors(area,frequncy):
    vectors=[]
    for i in range(len(area)):
        for j in range(len(area[i])):
            if area[i][j]==frequncy:
                vectors.append([i,j])
    return vectors
def countAntinodes(area,vectors, totalAntinodes):
    antinodesCount=0
    for i in range(len(vectors)):
        for j in range(i+1,len(vectors)):
            vector=np.subtract(vectors[i],vectors[j])
            antinodes=[list(np.add(vectors[i],vector)),list(np.subtract(vectors[j],vector))]
            for antinode in antinodes:
                if antinode[0]>=0 and antinode[1]>=0 and antinode[0]<len(area) and antinode[1]<len(area[0]) and antinode not in totalAntinodes:
                    antinodesCount+=1
                    totalAntinodes.append(antinode)
    return antinodesCount
sum=0
antinodes=[]
for frequncy in frequencies:
    sum+=countAntinodes(area,getVectors(area,frequncy),antinodes)
print(sum)
    
