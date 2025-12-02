#read input
with open('2024/day10-input.txt') as f:
    data=f.readlines()
#convert to matrix
area=[[int(location) for location in row.strip() ] for row in data]
#convert to graph
graph={}
#adding corners
graph[(0,0)]=[]
if area[0][0]==area[0][1]-1:
    graph[(0,0)].append((0,1))
if  area[0][0]==area[1][0]-1:
    graph[(0,0)].append((1,0))
graph[(0,len(area[0])-1)]=[]
if area[0][len(area[0])-1]==area[0][len(area[0])-2]-1:
    graph[(0,len(area[0])-1)].append((0,len(area[0])-2))
if area[0][len(area[0])-1]==area[1][len(area[0])-1]-1:
    graph[(0,len(area[0])-1)].append((1,len(area[0])-1))
graph[(len(area)-1,0)]=[]
if area[len(area)-1][0]==area[len(area)-1][1]-1:
    graph[(len(area)-1,0)].append((len(area)-1,1))
if area[len(area)-1][0]==area[len(area)-2][0]-1:
    graph[(len(area)-1,0)].append((len(area)-2,0))
graph[(len(area)-1,len(area[0])-1)]=[]
if area[len(area)-1][len(area[0])-1]==area[len(area)-1][len(area[0])-2]-1:
    graph[(len(area)-1,len(area[0])-1)].append((len(area)-1,len(area[0])-2))
if area[len(area)-1][len(area[0])-1]==area[len(area)-2][len(area[0])-1]-1:
    graph[(len(area)-1,len(area[0])-1)].append((len(area)-2,len(area[0])-1))
#adding borders
for i in range(1,len(area[0])-1):
    graph[(0,i)]=[]
    if area[0][i]==area[0][i-1]-1:
        graph[(0,i)].append((0,i-1))
    if area[0][i]==area[0][i+1]-1:
        graph[(0,i)].append((0,i+1))
    if area[0][i]==area[1][i]-1:
        graph[(0,i)].append((1,i))
for i in range(1,len(area)-1):
    graph[(i,0)]=[]
    if area[i][0]==area[i-1][0]-1:
        graph[(i,0)].append((i-1,0))
    if area[i][0]==area[i+1][0]-1:
        graph[(i,0)].append((i+1,0))
    if area[i][0]==area[i][1]-1:
        graph[(i,0)].append((i,1))
for i in range(1,len(area[0])-1):
    graph[(len(area)-1,i)]=[]
    if area[len(area)-1][i]==area[len(area)-1][i-1]-1:
        graph[(len(area)-1,i)].append((len(area)-1,i-1))
    if area[len(area)-1][i]==area[len(area)-1][i+1]-1:
        graph[(len(area)-1,i)].append((len(area)-1,i+1))
    if area[len(area)-1][i]==area[len(area)-2][i]-1:
        graph[(len(area)-1,i)].append((len(area)-2,i))
for i in range(1,len(area)-1):
    graph[(i,len(area[0])-1)]=[]
    if area[i][len(area[0])-1]==area[i-1][len(area[0])-1]-1:
        graph[(i,len(area[0])-1)].append((i-1,len(area[0])-1))
    if area[i][len(area[0])-1]==area[i+1][len(area[0])-1]-1:
        graph[(i,len(area[0])-1)].append((i+1,len(area[0])-1))
    if area[i][len(area[0])-1]==area[i][len(area[0])-2]-1:
        graph[(i,len(area[0])-1)].append((i,len(area[0])-2))
#adding inner nodes
for i in range(1,len(area)-1):
    for j in range(1,len(area[0])-1):
        graph[(i,j)]=[]
        if area[i][j]==area[i-1][j]-1:
            graph[(i,j)].append((i-1,j))
        if area[i][j]==area[i+1][j]-1:
            graph[(i,j)].append((i+1,j))
        if area[i][j]==area[i][j-1]-1:
            graph[(i,j)].append((i,j-1))
        if area[i][j]==area[i][j+1]-1:
            graph[(i,j)].append((i,j+1))

def findSummits(graph,tailhead,summits):
    for position in graph[tailhead]:
        if area[position[0]][position[1]] == 9:
            summits.add(position)
        else:
            findSummits(graph,position,summits)

def findTrails(graph,tailhead,trail,trails):
    for position in graph[tailhead]:
        if area[position[0]][position[1]] == 9:
            trails.append(trail+[position])
        else:
            findTrails(graph,position,trail+[position],trails)
#part 1
sum=0
for position in graph:
    if area[position[0]][position[1]] == 0:
        summits=set()
        findSummits(graph,position,summits)
        sum+=len(summits)
print(sum)
#part 2
sum=0
for position in graph:
    if area[position[0]][position[1]] == 0:
        trails=[]
        findTrails(graph,position,[position],trails)
        sum+=len(trails)
print(sum)
    
        