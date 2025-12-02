#read input
with open('2024/day11-input.txt') as f :
    stones = f.read().strip().split()

def changeStone(stone):
    if stone=='0':
        newStones=['1']
    elif len(stone)%2==0:
        mid=len(stone)//2
        newStones=[str(int(stone[:mid])),str(int(stone[mid:]))]
    else:
        newStones=[str(int(stone)*2024)]
    return newStones

graph={}

# get the count of stones using a graph to store the count of stones for each iteration
def countStonesGraph(graph,stone,iterations):
    if stone not in graph:
        graph[stone]=[changeStone(stone),{0:1}]
    if iterations in graph[stone][1]:
        return graph[stone][1][iterations]
    sum=0
    for newStone in graph[stone][0]:
        sum+=countStonesGraph(graph,newStone,iterations-1)
    graph[stone][1][iterations]=sum
    return sum

sum=0
for stone in stones:
    sum+=countStonesGraph(graph,stone,75)
print(sum)
