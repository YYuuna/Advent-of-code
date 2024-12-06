#read input data
with open('2024/day5-input.txt') as f:
    data = f.readlines()
data = [x.strip() for x in data]
rules = data[:data.index('')]
rules = [x.split('|') for x in rules]
rulesViolationGraph = {x[1]:[] for x in rules}
for x in rules:
    rulesViolationGraph[x[1]].append(x[0])
updates = data[data.index('')+1:]
updates = [x.split(',') for x in updates]

sum=0
for update in updates:
    correct =True
    for i in range(len(update)):
        if update[i] not in rulesViolationGraph:
            continue
        for j in range(i+1,len(update)):
            correct = update[j] not in rulesViolationGraph[update[i]]
            if not correct:
                break
        if not correct:
            break
    if correct :
        print (update)
        sum+=int(update[int(len(update)/2)])

print(sum)