# read input
with open('2024/day6-input.txt') as f :
    area = f.readlines()
area=[ list(row.strip()) for row in area]

def rotate90deg(guard):
    if  guard=='>':
        return 'v'
    if  guard=='v':
        return '<'
    if  guard=='<':
        return '^'
    if  guard=='^':
        return '>'
    
def isObstructed(area,position,guard):
    if guard=='>':
        return area[position[0]][position[1]+1]=='#'
    if guard=='v':
        return  area[position[0]+1][position[1]]=='#'
    if guard=='<':
        return area[position[0]][position[1]-1]=='#'
    if guard=='^':
        return area[position[0]-1][position[1]]=='#'
    
def hasLeft(area,position,guard):
    if guard=='>':
        return position[1]+1==len(area[0])
    if guard=='v':
        return  position[0]+1==len(area)
    if guard=='<':
        return position[1]==0
    if guard=='^':
        return position[0]==0

def findGuard(area):
    for i in range(len(area)):
        for j in range(len(area[0])):
            if area[i][j] in ['>','v','<','^']:
                return [i,j],area[i][j]
    return None

initialPosition,guard=findGuard(area)

def checkLoop(area,position,guard):    
    markedPatrol=[[[] for j in range(len(area))] for i in range(len(area[0]))]
    markedPatrol[position[0]][position[1]].append(guard)
    looping=False
    while not hasLeft(patroledArea,position,guard):
        if isObstructed(patroledArea,position,guard):
                guard=rotate90deg(guard)
                markedPatrol[position[0]][position[1]].append(guard)
                continue
        else:
            if guard=='>':
                position[1]+=1
            if guard=='v':
                position[0]+=1
            if guard=='<':
                position[1]-=1
            if guard=='^':
                position[0]-=1
        if guard in markedPatrol[position[0]][position[1]]:
            looping=True
            break
        else:
            markedPatrol[position[0]][position[1]].append(guard)
    return looping

sum=0
for i in range(len(area)):
    for j in range(len(area[0])):
        if area[i][j]=='.' and [i,j]!=initialPosition:
            patroledArea=[row.copy() for row in area]
            patroledArea[i][j]='#'
            position=initialPosition.copy()
            if checkLoop(patroledArea,position,guard):
                sum+=1
print(sum)
                
