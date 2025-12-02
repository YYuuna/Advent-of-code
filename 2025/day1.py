#read from txt file
file = open("2025/day1-input.txt", "r")
lines = file.readlines()
file.close()
dial=50
counter1=0
counter2=0

print("dial:", dial)
for line in lines:
    move=line.strip()[0]
    steps=int(line.strip()[1:])
    print("move:", move, steps)
    if move=="L":
        print("adding ", (steps+100-dial)//100-(dial==0))
        counter2+=(steps+100-dial)//100-(dial==0)
        dial=(dial-steps)%100
    elif move=="R":
        print("adding ", (steps+dial)//100)
        counter2+=(steps+dial)//100
        dial=(dial+steps)%100   
    if dial==0:
        counter1+=1
    print("dial:", dial)

print("part 1 :",counter1)
print("part 2 :",counter2)