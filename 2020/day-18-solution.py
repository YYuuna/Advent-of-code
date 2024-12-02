import re

operations = {"+": lambda x, y: x + y,
              "-": lambda x, y: x - y,
              "*": lambda x, y: x * y,
              "/": lambda x, y: x / y,
              "%": lambda x, y: x % y}
priority = {"+": 1, "-": 0, "*": 0, "/": 1, "%": 1}


def is_operand(symbol):
    return symbol not in operations and symbol not in ["(", ")"]


def convert_to_postfixed(symbols_list):
    value_stack = []
    operator_stack = []
    for symbol in symbols_list:
        if is_operand(symbol):
            value_stack.append(int(symbol))
        if symbol == "(":
            operator_stack.append(symbol)
        if symbol == ")":
            # checking emptiness of the stack is for the sake of design by contract
            while operator_stack and operator_stack[-1] != "(":
                x = operator_stack.pop()
                value_stack.append(x)
            operator_stack.pop()
        if symbol in operations:
            while operator_stack and operator_stack[-1] in operations and priority[symbol] <= priority[operator_stack[-1]]:
                x = operator_stack.pop()
                value_stack.append(x)
            operator_stack.append(symbol)
    while value_stack:
        x = value_stack.pop()
        operator_stack.append(x)
    return operator_stack

def evaluate_postfixed(operator_stack):
    value_stack=[]
    while operator_stack:
        x=operator_stack.pop()
        if is_operand(x) : value_stack.append(x)
        else:#x is operator
            operand1=value_stack.pop()
            operand2=value_stack.pop()
            result=operations[x](operand1,operand2)
            value_stack.append(result)
    return value_stack.pop()
with open("day-18-input.txt", "r") as puzzle_input:
    puzzle_input = puzzle_input.read().split("\n")
    match=r"\(|\)|"+r"|".join("\\"+operation for operation in operations.keys())+"|\d+"
    puzzle_input=[re.findall(match,symbols_list) for symbols_list in puzzle_input]
    expressions_sum=0
    for symbols_list in puzzle_input:
        print(symbols_list)
        postfixed_form=convert_to_postfixed(symbols_list)
        print(postfixed_form)
        result=evaluate_postfixed(postfixed_form)
        print(result)
        expressions_sum+=result
    print(expressions_sum)

