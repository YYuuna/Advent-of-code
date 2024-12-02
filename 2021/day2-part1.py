input=[line.split() for line in open("day2-part1-input.txt","r")]

position=[0,0]
for move in input:
    if move[0]=="forward":position[0]+=int(move[1])
    elif move[0]=="up":position[1]-=int(move[1])
    else: position[1]+=int(move[1])
print(position)
print(position[0]*position[1])
