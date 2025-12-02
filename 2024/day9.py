from math import floor
#read input
with open('2024/day9-input.txt') as f :
    data = f.read()
def convertRepresentation(data):
    reparesentation = []
    for i in range(len(data)):
        if i%2==0:
            for j in range(int(data[i])):
                reparesentation.append(str(floor(i/2)))
        else:
            for j in range(int(data[i])):
                reparesentation.append('.')
    return reparesentation
representation=convertRepresentation(data)
def compactPart1(representation):
    i=0
    j=len(representation)-1
    while i<j:
        while representation[i]!='.':
            i+=1
        while representation[j]=='.':
            j-=1
        if i<j:
            representation[i],representation[j]=representation[j],representation[i]
    return representation
def getNextBlock(representation,start=len(representation)-1):
    blockSize=0
    while representation[start]=='.':
        start-=1
    blockID=representation[start]
    while start > 0 and representation[start]==blockID:
        blockSize+=1
        start-=1
    start+=1
    return start,blockSize
def getNextFreeSpace(representation,start=0):
    freeSpaceSize=0
    while representation[start]!='.':
        start+=1
    while start+freeSpaceSize<len(representation) and representation[start+freeSpaceSize]=='.':
        freeSpaceSize+=1    
    return start,freeSpaceSize
def compactPart2(representation):
    blockPos,blockSize=getNextBlock(representation=representation)
    freeSpacePos=0
    while blockPos>1:
        freeSpacePos,freeSpaceSize=getNextFreeSpace(representation=representation)
        while freeSpacePos<=blockPos and blockSize>freeSpaceSize:
            freeSpacePos,freeSpaceSize=getNextFreeSpace(representation=representation,start=freeSpacePos+freeSpaceSize)
        if freeSpaceSize>=blockSize and freeSpacePos<blockPos:
            for i in range(blockSize):
                representation[freeSpacePos],representation[blockPos]=representation[blockPos],representation[freeSpacePos]
                freeSpacePos+=1
                blockPos+=1
            blockPos-=blockSize
        nextBlockPos,nextBlockSize=getNextBlock(representation=representation,start=blockPos-1)
        if representation[blockPos]!='.':
            while(True):
                if( int(representation[blockPos])>int(representation[nextBlockPos])):
                    break
                nextBlockPos,nextBlockSize=getNextBlock(representation=representation,start=nextBlockPos-1)
        blockPos,blockSize=nextBlockPos,nextBlockSize
    return representation        
compact=compactPart2(representation)
sum=0
i=0
while i<len(compact):
    if compact[i]!='.':
        sum+=int(compact[i])*i
    i+=1
print(sum)