from itertools import product
#read input
with open('2024/day7-input.txt') as f :
    data = f.readlines()
equations = [equation.strip().split(':') for equation in data]
equations = [(int(equation[0]),[int(operand) for operand in equation[1].split()]) for equation in equations]

def evaluate(operand1,operand2,operation):
    if operation=="+":
        return operand1+operand2
    if operation=="*":
        return operand1*operand2
    if operation=="||":
        return int(str(operand1)+ str(operand2))

def equationIsPossible(equation):
    result = equation[0]
    possible=False
    for operations in product(['+','*','||'],repeat=len(equation[1])-1):
        output = equation[1][0]
        for i in range(1,len(equation[1])):
            output = evaluate(output,equation[1][i],operations[i-1])
        if output==result:
            possible=True
            break
    return possible

sum=0

for equation in equations:
    if equationIsPossible(equation):
        sum+=equation[0]

print(sum)