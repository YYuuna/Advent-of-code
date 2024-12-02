import re
accumulator=0
oc=0
def acc(oc,accumulator,offset):
    return (oc+1,accumulator+offset)
def jmp(oc,accumulator,offset):
    return (oc+offset,accumulator)
def nop(oc,accumulator,offset):
    return (oc+1,accumulator)
operation={"acc":acc,"jmp":jmp,"nop":nop}
oposite_opreration={"acc":"acc","jmp":"nop","nop":"jmp"}
with open("day-8-input.txt","r") as puzzle_input:
    instructions=list(re.findall("([a-z]+) ([+-]\d+)", puzzle_input.read()))
    print(instructions)
    for i in range(len(instructions)):
        instructions[i]=(oposite_opreration[instructions[i][0]],instructions[i][1])
        done_instructions=[]
        oc=0
        accumulator=0
        while (oc < len(instructions) and oc not in done_instructions):
            done_instructions.append(oc)
            instruction = instructions[oc]
            oc, accumulator = operation[instruction[0]](oc, accumulator, int(instruction[1]))
        if oc==len(instructions): break
        instructions[i] = (oposite_opreration[instructions[i][0]], instructions[i][1])
    print(accumulator)