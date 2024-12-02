input = [line.split() for line in open("day2-part1-input.txt","r")

position= [0, 0, 0]
for move in input:
    if "forward" == move[0]:
        position[0]+=int(move[1])
        position[1]+=position[2]*int(move[1])
    elif move[0]=="up":position[2]-=int(move[1])
    else: position[2]+=int(move[1])
print(position)
print(position[0]*position[1])