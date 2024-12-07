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

def march(area,position,guard):
    while not hasLeft(area,position,guard):
        if isObstructed(area,position,guard):
                guard=rotate90deg(guard)
        else:
            area[position[0]][position[1]]='X'
            if guard=='>':
                position[1]+=1
            if guard=='v':
                position[0]+=1
            if guard=='<':
                position[1]-=1
            if guard=='^':
                position[0]-=1
            area[position[0]][position[1]]=guard
    area[position[0]][position[1]]='X'

def findGuard(area):
    for i in range(len(area)):
        for j in range(len(area[0])):
            if area[i][j] in ['>','v','<','^']:
                return [i,j],area[i][j]
    return None
position,guard=findGuard(area)
march(area,position,guard)
sum=0
for i in range(len(area)):
    for j in range(len(area[0])):
        if area[i][j]=='X':
            sum+=1
print(sum)



