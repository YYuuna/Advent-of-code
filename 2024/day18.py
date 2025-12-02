from heapq import heappush, heappop
#read input
with open('2024/day18-input.txt') as f:
    lines = f.readlines()	
#parse input
bytes=[]
for line in lines:
    bytes.append(tuple(int(cord) for cord in line.split(',')))
width=71
length=71
grid=[['.' for j in range(width)] for i in range (length)]
for i in range(1024):
    grid[bytes[i][0]][bytes[i][1]]='#'

graph={}
for i in range (length):
    for j in range(width):
        if grid[i][j]=='.':
            graph[(i,j)]=[]
            if i>0 and grid[i-1][j]=='.':
                graph[(i,j)].append((i-1,j))
            if i<length-1 and grid[i+1][j]=='.':
                graph[(i,j)].append((i+1,j))
            if j>0 and grid[i][j-1]=='.':
                graph[(i,j)].append((i,j-1))
            if j<width-1 and grid[i][j+1]=='.':
                graph[(i,j)].append((i,j+1))

def findShortestPathUCS(graph,start,goal):
    queue = [(0,[start])]
    vertex=start
    visited = {(start): 0}
    while queue:
        path= heappop(queue)
        vertex=path[1][-1]
        if vertex==goal:
            return path        
        for neighbor in graph[vertex]:
            if neighbor not in path[1]:
                newCost = path[0]+1
                if (neighbor) not in visited or newCost < visited[(neighbor)]:
                    visited[(neighbor)] = newCost
                    heappush(queue,(newCost,path[1]+[neighbor]))
    return None

start=(0,0)
goal=(70,70)
path=findShortestPathUCS(graph,start,goal)
print(path)

corruptionGraph={}
def onTopRight(i,j):
    return i==0 or j==width-1
def onBottomleft(i,j):
    return i==length-1 or j==0
for i in range(length):
    for j in range(width):
        if grid[i][j]=='#':
            corruptionGraph[(i,j)]=[]
            if i>0 :
                if grid[i-1][j]=='#':
                    corruptionGraph[(i,j)].append((i-1,j))
                if j>0 and grid[i-1][j-1]=='#':
                    corruptionGraph[(i,j)].append((i-1,j-1))
                if j<width-1 and grid[i-1][j+1]=='#':
                    corruptionGraph[(i,j)].append((i-1,j+1))
            if i<length-1 :
                if grid[i+1][j]=='#':
                    corruptionGraph[(i,j)].append((i+1,j))
                if j>0 and grid[i+1][j-1]=='#':
                    corruptionGraph[(i,j)].append((i+1,j-1))
                if j<width-1 and grid[i+1][j+1]=='#':
                    corruptionGraph[(i,j)].append((i+1,j+1))
            if j>0 and grid[i][j-1]=='#':
                corruptionGraph[(i,j)].append((i,j-1))
            if j<width-1 and grid[i][j+1]=='#':
                corruptionGraph[(i,j)].append((i,j+1))

def findWallDFS(corruptionGraph,start,visited):
    visited.add(start)
    if onBottomleft(start[0],start[1]):
        return True
    for neighbor in corruptionGraph[start]:
        if neighbor not in visited:
            if findWallDFS(corruptionGraph,neighbor,visited):
                return True
    return False
            

def addToGraph(grid,corruptionGraph,byte):
    i=byte[0]
    j=byte[1]
    grid[i][j]='#'
    corruptionGraph[(i,j)]=[]
    if i>0 :
        if grid[i-1][j]=='#':
            corruptionGraph[(i,j)].append((i-1,j))
            corruptionGraph[(i-1,j)].append((i,j))
        if j>0 and grid[i-1][j-1]=='#':
            corruptionGraph[(i,j)].append((i-1,j-1))
            corruptionGraph[(i-1,j-1)].append((i,j))
        if j<width-1 and grid[i-1][j+1]=='#':
            corruptionGraph[(i-1,j+1)].append((i,j))
            corruptionGraph[(i,j)].append((i-1,j+1))
    if i<length-1 :
        if grid[i+1][j]=='#':
            corruptionGraph[(i+1,j)].append((i,j))
            corruptionGraph[(i,j)].append((i+1,j))
        if j>0 and grid[i+1][j-1]=='#':
            corruptionGraph[(i+1,j-1)].append((i,j))
            corruptionGraph[(i,j)].append((i+1,j-1))
        if j<width-1 and grid[i+1][j+1]=='#':
            corruptionGraph[(i+1,j+1)].append((i,j))
            corruptionGraph[(i,j)].append((i+1,j+1))
    if j>0 and grid[i][j-1]=='#':
        corruptionGraph[(i,j-1)].append((i,j))
        corruptionGraph[(i,j)].append((i,j-1))
    if j<width-1 and grid[i][j+1]=='#':
        corruptionGraph[(i,j+1)].append((i,j))
        corruptionGraph[(i,j)].append((i,j+1))
blockingByte=None
for byte in bytes:
    visited=set()
    addToGraph(grid,corruptionGraph,byte)
    for i in range(length):
        if (i,width-1) in corruptionGraph and (i,width-1) not in visited:
            if findWallDFS(corruptionGraph,(i,width-1),visited):
                blockingByte=byte
                break
    if not blockingByte:
        for j in range(width-1):
            if (0,j) in corruptionGraph and (0,j) not in visited:
                if findWallDFS(corruptionGraph,(0,j),visited):
                    blockingByte=byte
                    break
    if blockingByte:
        break
print(blockingByte)

