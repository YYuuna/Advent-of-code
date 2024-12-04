import numpy as np
#read input from text file
file = open("2024/day4-input.txt", "r")
content=file.readlines()
file.close()
content=np.array([list(line.strip()) for line in content])
#count the number of occurances of word "XMAS" in string
def countXMAS(array):
    count=0
    array=array.tolist()
    for i in range(len(array)-3):
        if (array[i:i+4]==["X","M","A","S"]):
            count+=1
    return count
# initialize the sum
sum=0
#count the number of occurances of word "XMAS" in each row and its reverse
sum=0
for row in content:
    sum+=countXMAS(row)
    sum+=countXMAS(row[::-1])
#count the number of occurances of word "XMAS" in each column and its reverse
for i in range(len(content[0])):
    column=content[:,i]
    sum+=countXMAS(column)
    sum+=countXMAS(column[::-1])
#count the number of occurances of word "XMAS" in each upper-right-to-lower-left diagonal and its reverse
diags1 = [content[::-1,:].diagonal(i) for i in range(-content.shape[0]+1,content.shape[1])]
for diag in diags1:
    sum+=countXMAS(diag)
    sum+=countXMAS(diag[::-1])
#count the number of occurances of word "XMAS" in each upper-left-to-lower-right diagonal and its reverse
diags2=[content.diagonal(i) for i in range(content.shape[1]-1,-content.shape[0],-1)]
for diag in diags2:
    sum+=countXMAS(diag)
    sum+=countXMAS(diag[::-1])
print(sum)

