stack = []

num1 = []
op = []
num2 = []

strnum1 = []

arithmetic = input('enter value, operator, then value: ')

for i in arithmetic:
	stack.append(i)

strstack = ''.join(stack)



for i in strstack:

	try:
		num1.append(int(i))

	except:
		operation = stack.index(i)
		newop = i
		op.append(i)
		break

for i in num1:
	strnum1.append(str(i))


num2 = stack[operation:]
num2.pop(0)


num1 = ''.join(strnum1)
operation = newop
num2 = ''.join(num2)




print(f'num1 = {num1}')
print(f'operation = {operation}')
print(f'num2 = {num2}')

print(f'\nstack = {stack}')
