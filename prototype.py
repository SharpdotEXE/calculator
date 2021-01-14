import operator

num1 = input('enter a number: ')
op = input('enter an operator: ')
num2 = input('enter a number: ')


def calculate(num1, num2, op):

    num1 = int(num1)
    num2 = int(num2)

    if op == '+':
        result = operator.add(num1, num2)
    elif op == '-':
        result = operator.sub(num1, num2)
    elif op == '*':
        result = operator.mul(num1,num2)
    elif op == '/':
        result = operator.div(num1, num2)

    print(f'{num1} {op} {num2} = {result}')

calculate(num1, num2, op)
