import re
#read input
with open('2024/day14-input.txt') as f:
    robots=f.readlines()

def getParameters(robot):
    parameters = tuple(int(parameter) for parameter in re.findall(r'-?\d+',robot))
    return parameters

def getQuadron(wide,tall,seconds,robot):
    px,py,vx,vy=getParameters(robot)
    px=(px+seconds*vx)%wide
    py=(py+seconds*vy)%tall
    if(px<wide//2):
        if(py<tall//2):
            return 0
        if (py>=(tall+1)//2):
            return 2
    if(px>=(wide+1)//2):
        if(py<tall//2):
            return 1
        if (py>=(tall+1)//2):
            return 3
    return None

quadrons=[0,0,0,0]
wide=101
tall=103
for robot in robots:
    quadron=getQuadron(wide,tall,100,robot) 
    if quadron!=None:
        quadrons[quadron]+=1
safetyFactor=1
for robotCount in quadrons:
    safetyFactor*=robotCount
print(safetyFactor)

robotsPosition=[]
robotsVelocity=[]
for robot in robots:
    px,py,vx,vy=getParameters(robot)
    robotsPosition.append((px,py))
    robotsVelocity.append((vx,vy))

def convertRobotsToMap(robotsPosition):
    robotsMap=[['.' for _ in range(tall)] for _ in range(wide)]
    for robot in robotsPosition:        
        robotsMap[robot[0]][robot[1]]='#'
    return robotsMap

def printMap(robotsMap):
    for row in robotsMap:
        print(''.join(row))
    print()
def iterate(robotsPosition,robotsVelocity):
    for i in range(len(robotsPosition)):
        px,py=robotsPosition[i]
        vx,vy=robotsVelocity[i]
        px=(px+vx)%wide
        py=(py+vy)%tall
        robotsPosition[i]=(px,py)
    return robotsPosition
def checkIfOneRobotPerTile(robotsPosition):
    return len(robotsPosition)==len(set(robotsPosition))
iteration=0
while True:
    print(iteration)
    robotsMap=convertRobotsToMap(robotsPosition)
    printMap(robotsMap)
    c=input()
    if c != '':
        break
    while not checkIfOneRobotPerTile(robotsPosition):
        robotsPosition=iterate(robotsPosition,robotsVelocity)
        iteration+=1