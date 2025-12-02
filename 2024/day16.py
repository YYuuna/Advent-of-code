from math import inf
from heapq import heappop, heappush
# read input
with open("2024/day16-input.txt") as f:
    maze = f.readlines()
maze = [list(row.strip()) for row in maze]

def mazeToGraph(maze):
    graph={}
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            graph[(i,j)]=[]
            if maze[i][j] in {'.','S'}:	
                if maze[i-1][j] in {'.','E'}:
                    graph[(i,j)].append((i-1,j))
                if maze[i+1][j] in {'.','E'}:
                    graph[(i,j)].append((i+1,j))
                if maze[i][j-1] in {'.','E'}:
                    graph[(i,j)].append((i,j-1))
                if maze[i][j+1] in {'.','E'}:
                    graph[(i,j)].append((i,j+1))
    return graph
def findStart(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j]=='S':
                return (i,j)
def findEnd(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j]=='E':
                return (i,j)
def countTurns(path):
    direction=[0,1]
    turns=0
    for i in range(len(path)-1):
        if direction!=subtract(path[i+1],path[i]):
            direction=subtract(path[i+1],path[i])
            turns+=1
    return turns
def calculateCost(path):
    return countTurns(path)*1000 + len(path)-1
def findShortestPathDFS(graph,start,End):
    minimum = inf
    stack = [(start,[start],0)]
    shortestPath=[]
    while stack:
        (vertex,path,cost) = stack.pop()
        if vertex == End:
            if (cost< minimum):
                minimum=cost
                shortestPath=path.copy()
            continue
        for neighbor in graph[vertex]:
            if neighbor not in path:
                newPath=path+[neighbor]
                newCost=calculateCost(newPath)
                if newCost<minimum:
                    stack.append((neighbor,newPath,newCost))
    return shortestPath
def findShortestPathUCS(graph,start,End):
    queue = [(0,[start],(0,1))]
    vertex=start
    visited = {(start,(0,1)): 0}
    while queue:
        path= heappop(queue)
        currentDirection=path[2]
        vertex=path[1][-1]
        if vertex==End:
            return path        
        for neighbor in graph[vertex]:
            if neighbor not in path[1]:
                newDirection=subtract(neighbor,vertex)
                if currentDirection!=newDirection:
                    newCost=path[0]+1001
                else:
                    newCost=path[0]+1
                if (neighbor,currentDirection) not in visited or newCost < visited[(neighbor,currentDirection)]:
                    visited[(neighbor,currentDirection)] = newCost
                    heappush(queue,(newCost,path[1]+[neighbor],newDirection))
def findAllShortestPathUCS(graph,start,End):
    queue = [(0,[start],(0,1))]
    vertex=start
    directions=[(0,1),(0,-1),(1,0),(-1,0)]
    visited = {(start,(0,1)): 0}
    shortestPaths=[]
    minimumCost=None
    while queue:
        path= heappop(queue)
        currentDirection=path[2]
        vertex=path[1][-1]
        if vertex==End:
            if minimumCost==None:
                for dir in directions:
                    if (vertex,dir) in visited:
                        minimumCost=visited[(vertex,dir)]
                        break
            if path[0]==minimumCost:
                shortestPaths.append(path)
                continue        
            else:
                return shortestPaths
        for neighbor in graph[vertex]:
            if neighbor not in path[1]:
                newDirection=subtract(neighbor,vertex)
                if currentDirection!=newDirection:
                    newCost=path[0]+1001
                else:
                    newCost=path[0]+1
                if (neighbor,currentDirection) not in visited or newCost <= visited[(neighbor,currentDirection)]:
                    visited[(neighbor,currentDirection)] = newCost
                    heappush(queue,(newCost,path[1]+[neighbor],newDirection))
    return shortestPaths

subtract=lambda x,y: tuple(x[i]-y[i] for i in range(len(x)))
def printMaze(maze):
    for row in maze:
        print(''.join(row))
    print()
printMaze(maze)
graph=mazeToGraph(maze)
start=findStart(maze)
end=findEnd(maze)
shortestPath=findShortestPathUCS(graph,start,end)
for position in shortestPath[1]:
    maze[position[0]][position[1]]=' '
printMaze(maze)
print(shortestPath[0])
#part2
paths=findAllShortestPathUCS(graph,start,end)
tiles=[]
for path in paths:
    tiles.extend(path[1])
tiles=set(tiles)
print(len(tiles))
            
                
    


