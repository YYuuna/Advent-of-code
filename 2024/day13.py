import re
from sympy import symbols,solve
#read input
with open('2024/day13-input.txt') as f:
    claws=f.read()
claws=claws.split('\n\n')
#get parameters of the claws

def getParameters(claw):
    parameters=re.findall(r'(\d+)',claw)
    ax,bx,cx=int(parameters[0]),int(parameters[2]),int(parameters[4])
    ay,by,cy=int(parameters[1]),int(parameters[3]),int(parameters[5])
    return ax,bx,cx,ay,by,cy
def convertClawToEquationsPart1(claw):
    A,B=symbols('A B',integer=True)
    ax,bx,cx,ay,by,cy=getParameters(claw)    
    equations=[(ax*A+bx*B-cx),(ay*A+by*B-cy)]
    return equations

def convertClawToEquationsPart2(claw):
    A,B=symbols('A B',integer=True)
    ax,bx,cx,ay,by,cy=getParameters(claw)    
    equations=[(ax*A+bx*B-cx-10000000000000),(ay*A+by*B-cy-10000000000000)]
    return equations

def countTokens(claw,part=1):
    A,B=symbols('A B',integer=True)
    if part==1:
        equations=convertClawToEquationsPart1(claw)
    else:
        equations=convertClawToEquationsPart2(claw)
    solutions=solve(equations,[A,B],dict=True)
    if not solutions:
        return 0
    return solutions[0][A]*3+solutions[0][B]
tokens=0
for claw in claws:
    tokens+=countTokens(claw)
print(tokens)