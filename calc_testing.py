stack = []

num1 = []
num2 = []

arithmetic = input('enter value, operator, then value: ')

for i in arithmetic:
	stack.append(i)

stack = ''.join(stack)

print(stack)

for i in stack:
	print(i)
	if i == int(i):
		num1.append(i)
	

print(num1)
