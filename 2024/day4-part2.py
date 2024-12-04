import numpy as np
#read input from text file
file = open("2024/day4-input.txt", "r")
content=file.readlines()
file.close()
content=np.array([list(line.strip()) for line in content])
#check if sub matrix is "X-MAS"
def isXMAS(submatrix):
    MAS=["M","A","S"]
    primaryDiag=submatrix.diagonal().tolist()
    secondaryDiag=np.fliplr(submatrix).diagonal().tolist()
    return (primaryDiag==MAS or primaryDiag==MAS[::-1]) and ((secondaryDiag==MAS) or (secondaryDiag==MAS[::-1]))
# initialize the sum
sum=0
for i in range(1,len(content)-1):
    for j in range(1,len(content[0])-1):
        submatrix=content[i-1:i+2,j-1:j+2]
        if isXMAS(submatrix):
            sum+=1
print(sum)
        