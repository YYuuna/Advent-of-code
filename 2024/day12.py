#reda input
with open('2024/day12-sample-input.txt') as f:
    plots = f.readlines()

plots =[['.']+list(row.strip())+['.'] for row in plots]
plots.insert(0,['.' for i in range(len(plots[0]))])
plots.append(['.' for i in range(len(plots[0]))])


graph={}
for i in range(1,len(plots)-1):
    for j in range(1,len(plots[0])-1):
        graph[(i,j)]=[]
        if i>0:
            graph[(i,j)].append((i-1,j))
        if i<len(plots)-1:
            graph[(i,j)].append((i+1,j))
        if j>0:
            graph[(i,j)].append((i,j-1))
        if j<len(plots[0])-1:
            graph[(i,j)].append((i,j+1))

def findRegion(graph,plots,i,j,region=[]):
    if (i,j) in region:
        return region
    region.append((i,j))
    for neighbor in graph[(i,j)]:
        if plots[neighbor[0]][neighbor[1]]==plots[i][j]:
            findRegion(graph,plots,neighbor[0],neighbor[1],region)
    return region

def countAreaPerimeter(graph,plots,region):
    area=len(region)
    perimter=0
    for plot in region:
        for neighbor in graph[plot]:
            if plots[plot[0]][plot[1]]!=plots[neighbor[0]][neighbor[1]]:
                perimter+=1
        perimter+=4-len(graph[plot])    
    return (area,perimter)
def countCorners(graph,plots,plot):
    neighborsCount=sum([1 for neighbor in graph[plot] if plots[plot[0]][plot[1]]==plots[neighbor[0]][neighbor[1]]])
    if neighborsCount==0:
         return 4
    elif neighborsCount==1:
        return 2
    elif neighborsCount==2:
        if plots[plot[0]][plot[1]]==plots[plot[0]-1][plot[1]] and plots[plot[0]][plot[1]]==plots[plot[0]+1][plot[1]]:
            corners=0
        elif plots[plot[0]][plot[1]]==plots[plot[0]][plot[1]-1] and plots[plot[0]][plot[1]]==plots[plot[0]][plot[1]+1]:
            corners=0
        else:
            corners=1
    else:
        corners=0
    if plots[plot[0]][plot[1]]==plots[plot[0]-1][plot[1]]:
        if plots[plot[0]][plot[1]]==plots[plot[0]][plot[1]-1] and plots[plot[0]][plot[1]]!=plots[plot[0]-1][plot[1]-1]:
            corners+=1
        if plots[plot[0]][plot[1]]==plots[plot[0]][plot[1]+1] and plots[plot[0]][plot[1]]!=plots[plot[0]-1][plot[1]+1]:
            corners+=1
    if plots[plot[0]][plot[1]]==plots[plot[0]+1][plot[1]]:
        if plots[plot[0]][plot[1]]==plots[plot[0]][plot[1]-1] and plots[plot[0]][plot[1]]!=plots[plot[0]+1][plot[1]-1]:
            corners+=1
        if plots[plot[0]][plot[1]]==plots[plot[0]][plot[1]+1] and plots[plot[0]][plot[1]]!=plots[plot[0]+1][plot[1]+1]:
            corners+=1
    return corners
    
def countAreaSides(graph,plots,region):
    area=len(region)
    sides=0
    for plot in region:
        sides+=countCorners(graph,plots,plot)
    return (area,sides)

regions=[[],[]]
for plot in graph:
    included=False
    for region in regions[0]:
        if plot in region:
            included=True
            break
    if included:
        continue
    regions[0].append(findRegion(graph,plots,plot[0],plot[1],[]))
    regions[1].append(countAreaSides(graph,plots,regions[0][-1]))

totalPrice=0
for i in range (len(regions[0])):
    print("A region of ",plots[regions[0][i][0][0]][regions[0][i][0][1]]," plants with price ",regions[1][i][0]," * ",regions[1][i][1]," = ",regions[1][i][0]*regions[1][i][1])
    totalPrice+=regions[1][i][0]*regions[1][i][1]
print(totalPrice)


