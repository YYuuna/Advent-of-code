import re
#read input
with open("2024/day17-input.txt") as f:
    lines = f.readlines()

A=int(re.search(r'(\d+)',lines[0]).group(0))
B=int(re.search(r'(\d+)',lines[1]).group(0))
C=int(re.search(r'(\d+)',lines[2]).group(0))
program=[int(op) for op in re.findall(r'(\d+)',lines[4])]


def runInst(IP,program,A,B,C,output):
    comboOperand={
    0:0,
    1:1,
    2:2,
    3:3,
    4:A,
    5:B,
    6:C,
    7:None
}
    opcode=program[IP]
    operand=program[IP+1]
    match opcode:
        case 0:
            A = A//(1<<comboOperand[operand])
            IP+=2
        case 1:
            B=B^operand
            IP+=2
        case 2:
            B=comboOperand[operand]%8
            IP+=2
        case 3:
            if A!=0:
                IP=operand
            else:
                IP+=2
        case 4:
            B=B^C
            IP+=2
        case 5:
            output.append(comboOperand[operand]%8)
            IP+=2
        case 6:
            B = A//(1<<comboOperand[operand])
            IP+=2
        case 7:
            C = A//(1<<comboOperand[operand])
            IP+=2
    return IP,A,B,C,output
print(program)
output=[]
IP=0
while (IP<=len(program)-1):
    IP,A,B,C,output=runInst(IP,program,A,B,C,output)
    print(IP,A,B,C,','.join(str(out) for out in output))
print(output)

# Part 2

def reverseRun(IP,program,A,B,C,output):
    if IP==0 and not output:
            return IP,A,B,C,output
    comboOperand={
    0:0,
    1:1,
    2:2,
    3:3,
    4:A,
    5:B,
    6:C,
    7:None
}
    
    # if IP<8:
        
    # else:




    # return IP,A,B,C,output


