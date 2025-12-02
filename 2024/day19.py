import re
#read input
with open('2024/day19-input.txt') as f:
    data = f.read()
data = data.split('\n\n')
towels = re.findall(r'([a-z]+)',data[0])
designs = data[1].split('\n')
designsArrangementsPossibilities = {'':{('',)}}
def possibleDesignArrangements(design,towels):
    if design in designsArrangementsPossibilities:
        return designsArrangementsPossibilities[design]
    designsArrangementsPossibilities[design]=set()
    pattern=r'(?!'+ '|'.join(towels)+')'
    if re.match(pattern,design):
        return designsArrangementsPossibilities[design]
    for towel in towels:
        towelPos= design.find(towel)
        if towelPos!=-1:
            subDesign1 = design[:towelPos]
            subDesign2 = design[towelPos+len(towel):]
            if re.match(pattern,subDesign1) and subDesign1!='' or re.match(pattern,subDesign2) and subDesign2!='':
                continue
            if subDesign1 not in designsArrangementsPossibilities:
                designsArrangementsPossibilities[subDesign1]=possibleDesignArrangements(subDesign1,towels)
            if subDesign2 not in designsArrangementsPossibilities:
                designsArrangementsPossibilities[subDesign2]=possibleDesignArrangements(subDesign2,towels)
            for arrangement1 in designsArrangementsPossibilities[subDesign1]:
                for arrangement2 in designsArrangementsPossibilities[subDesign2]:
                    if arrangement1==('',):
                        if arrangement2==('',):
                            designsArrangementsPossibilities[design].add((towel,))
                        else:
                            designsArrangementsPossibilities[design].add((towel,)+arrangement2)
                    else:
                        if arrangement2==('',):
                            designsArrangementsPossibilities[design].add(arrangement1+(towel,))
                        else:
                            designsArrangementsPossibilities[design].add(arrangement1+(towel,)+arrangement2)
    return designsArrangementsPossibilities[design]
#part1
sum=0
for design in designs:
    print(design)
    for arrangement in possibleDesignArrangements(design,towels):
        print(arrangement)
    print(len(possibleDesignArrangements(design,towels)))
    if possibleDesignArrangements(design,towels):
        sum+=1
print(sum)

#part2
sum=0
for design in designs:
    print(design)
    for arrangement in possibleDesignArrangements(design,towels):
        print(arrangement)
    print(len(possibleDesignArrangements(design,towels)))
    sum+=len(possibleDesignArrangements(design,towels))
print(sum)

