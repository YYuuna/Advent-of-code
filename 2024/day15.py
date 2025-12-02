#reqd input
with open('2024/day15-input.txt') as f:
    input=f.read().split('\n\n')
area=[list(row.strip()) for row in input[0].split()]
moves=''
for row in input[1].split():
    moves+=row
def printArea(area):
    for row in area:
        print(''.join(row))
    print()
def findRobot(area):
    for i in range(len(area)):
        for j in range(len(area[0])):
            if area[i][j]=='@':
                return i,j
    return None

def adjacent(i,j,direction):
    if direction=='^':
        return i-1,j
    if direction=='v':
        return i+1,j
    if direction=='<':
        return i,j-1
    if direction=='>':
        return i,j+1
def movePart1(i,j,area,direction):
    if area[i][j]=='#':
        return False
    adjacentCords=adjacent(i,j,direction)
    if area[adjacentCords[0]][adjacentCords[1]]!='.':
        if not movePart1(adjacentCords[0],adjacentCords[1],area,direction):
            return False
        area[i][j],area[adjacentCords[0]][adjacentCords[1]]=area[adjacentCords[0]][adjacentCords[1]],area[i][j]
        return True
    area[i][j],area[adjacentCords[0]][adjacentCords[1]]=area[adjacentCords[0]][adjacentCords[1]],area[i][j]
    return True

i,j=findRobot(area)
for direction in moves:
    if movePart1(i,j,area,direction):
        i,j=adjacent(i,j,direction)
sum=0
for i in range(len(area)):
    for j in range(len(area[0])):
        if area[i][j]=='O':
            sum+=100*i+j
print(sum)

# Part 2
def widenArea(area):
    for i in range(len(area)):
        j=0
        while(j<len(area[0])):
            if area[i][j]=='#':
                area[i].insert(j+1,'#')
            if  area[i][j]=='@':
                area[i].insert(j+1,'.')
            if area[i][j]=='.':
                area[i].insert(j+1,'.')
            if area[i][j]=='O':
                area[i][j]='['
                area[i].insert(j+1,']')
            j+=2
def movablePart2(i,j,area,direction,checked):
    if area[i][j]=='#':
        return False
    adjacentCords=adjacent(i,j,direction)
    if area[adjacentCords[0]][adjacentCords[1]]!='.':
        if checked[adjacentCords[0]][adjacentCords[1]]==-1:
                checked[adjacentCords[0]][adjacentCords[1]]=movablePart2(adjacentCords[0],adjacentCords[1],area,direction,checked)
        movable=checked[adjacentCords[0]][adjacentCords[1]]
        if direction in {'^','v'}:
            if area[adjacentCords[0]][adjacentCords[1]]=='[':
                if checked[adjacentCords[0]][adjacentCords[1]+1]==-1:
                    checked[adjacentCords[0]][adjacentCords[1]+1]= movablePart2(adjacentCords[0],adjacentCords[1]+1,area,direction,checked)
                movable = movable and checked[adjacentCords[0]][adjacentCords[1]+1]
            if area[adjacentCords[0]][adjacentCords[1]]==']':
                if checked[adjacentCords[0]][adjacentCords[1]-1]==-1:
                    checked[adjacentCords[0]][adjacentCords[1]-1]= movablePart2(adjacentCords[0],adjacentCords[1]-1,area,direction,checked)
                movable = movable and checked[adjacentCords[0]][adjacentCords[1]-1]
        return movable
    checked[i][j]=True
    return True
def movePart2(i,j,area,direction):
    adjacentCords=adjacent(i,j,direction)
    if area[adjacentCords[0]][adjacentCords[1]]=='.':
        area[i][j],area[adjacentCords[0]][adjacentCords[1]]=area[adjacentCords[0]][adjacentCords[1]],area[i][j]
        return
    if direction in {'^','v'}:
        if area[adjacentCords[0]][adjacentCords[1]]=='[':
            movePart2(adjacentCords[0],adjacentCords[1]+1,area,direction)
        if area[adjacentCords[0]][adjacentCords[1]]==']':
                movePart2(adjacentCords[0],adjacentCords[1]-1,area,direction)
    movePart2(adjacentCords[0],adjacentCords[1],area,direction)    
    area[i][j],area[adjacentCords[0]][adjacentCords[1]]=area[adjacentCords[0]][adjacentCords[1]],area[i][j]
    return

area=[list(row.strip()) for row in input[0].split()]
widenArea(area)
i,j=findRobot(area)
for direction in moves:
    checked=[[-1 for j in range(len(area[0]))] for i in range(len(area))]
    if movablePart2(i,j,area,direction,checked):
        movePart2(i,j,area,direction)
        i,j=adjacent(i,j,direction)   
sum=0
for i in range(len(area)):
    for j in range(len(area[0])):
        if area[i][j]=='[':
            sum+=100*i+j
print(sum)
    
        



