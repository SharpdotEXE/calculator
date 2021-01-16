from tkinter import *

root = Tk()
root.title('Calculator')

stack = []

def button_1():
    stack.append('1')
    display_text.set(''.join(stack))
    print(stack)

def button_2():
    stack.append('2')
    display_text.set(''.join(stack))
    print(stack)

def button_3():
    stack.append('3')
    display_text.set(''.join(stack))
    print(stack)

def button_4():
    stack.append('4')
    display_text.set(''.join(stack))
    print(stack)

def button_5():
    stack.append('5')
    display_text.set(''.join(stack))
    print(stack)

def button_6():
    stack.append('6')
    display_text.set(''.join(stack))
    print(stack)

def button_7():
    stack.append('7')
    display_text.set(''.join(stack))
    print(stack)

def button_8():
    stack.append('8')
    display_text.set(''.join(stack))
    print(stack)

def button_9():
    stack.append('9')
    display_text.set(''.join(stack))
    print(stack)

def button_0():
    stack.append('0')
    display_text.set(''.join(stack))
    print(stack)

def clear_stack():
    del stack[::]
    display_text.set(''.join(stack))
    print(stack)

def delete_from_stack():
    del stack[-1]
    display_text.set(''.join(stack))
    print(stack)

def equals():
    #might add try: except here
    str_stack = ''.join(stack)
    print(eval(str_stack))
    display_text.set(eval(''.join(stack)))
    

def append_plus():
    stack.append('+')
    display_text.set(''.join(stack))
    print(stack)

def append_subtract():
    stack.append('-')
    display_text.set(''.join(stack))
    print(stack)

def append_multiply():
    stack.append('*')
    display_text.set(''.join(stack))
    print(stack)

def append_divide():
    stack.append('/')
    display_text.set(''.join(stack))
    print(stack)





################frames################
display_frame = Frame(root, bg='lightgray', borderwidth=5)
display_frame.pack()

clear_del_frame = Frame(root, bg='yellow', borderwidth=5)
clear_del_frame.pack()

one_4_7_frame = Frame(root, bg='skyblue', borderwidth=5)
one_4_7_frame.pack(side='left')

two_5_8_frame = Frame(root, bg='purple', borderwidth=5)
two_5_8_frame.pack(side='left')

three_6_9_frame = Frame(root, bg='green', borderwidth=5)
three_6_9_frame.pack(side='left')

operator_frame = Frame(root, bg='pink', borderwidth=5)
operator_frame.pack(side='right')

zero_equal_frame = Frame(root, bg='orange', borderwidth=5)
zero_equal_frame.pack(side='bottom', anchor='sw')
################frames################





################buttons#################
clearbutton = Button(clear_del_frame, text='clear', padx=30, pady=10,
                        font=('fixedsys', 10), command=clear_stack)
clearbutton.pack(side='left')

delbutton = Button(clear_del_frame, text='del', padx=30, pady=10,
                        font=('fixedsys', 10), command=delete_from_stack)
delbutton.pack(side='right')


number1_button = Button(one_4_7_frame, text='1', padx=30, pady=10,
                        font=('fixedsys', 10), command=button_1)
number1_button.pack()

number4_button = Button(one_4_7_frame, text='4', padx=30, pady=10,
                        font=('fixedsys', 10), command=button_4)
number4_button.pack()

number7_button = Button(one_4_7_frame, text='7', padx=30, pady=10,
                        font=('fixedsys', 10), command=button_7)
number7_button.pack()


number2_button = Button(two_5_8_frame, text='2', padx=30, pady=10,
                        font=('fixedsys', 10), command=button_2)
number2_button.pack()

number5_button = Button(two_5_8_frame, text='5', padx=30, pady=10,
                        font=('fixedsys', 10), command=button_5)
number5_button.pack()

number8_button = Button(two_5_8_frame, text='8', padx=30, pady=10,
                        font=('fixedsys', 10), command=button_8)
number8_button.pack()


number3_button = Button(three_6_9_frame, text='3', padx=30, pady=10,
                        font=('fixedsys', 10), command=button_3)
number3_button.pack()

number6_button = Button(three_6_9_frame, text='6', padx=30, pady=10,
                        font=('fixedsys', 10), command=button_6)
number6_button.pack()

number9_button = Button(three_6_9_frame, text='9', padx=30, pady=10,
                        font=('fixedsys', 10), command=button_9)
number9_button.pack()

plus_button = Button(operator_frame, text='+', padx=30, pady=10,
                        font=('fixedsys', 10), command=append_plus)
plus_button.pack()

minus_button = Button(operator_frame, text='-', padx=30, pady=10,
                        font=('fixedsys', 10), command=append_subtract)
minus_button.pack()

multiply_button = Button(operator_frame, text='*', padx=30, pady=10,
                        font=('fixedsys', 10), command=append_multiply)
multiply_button.pack()

divide_button = Button(operator_frame, text='/', padx=30, pady=10,
                        font=('fixedsys', 10), command=append_divide)
divide_button.pack()

zero_button = Button(zero_equal_frame, text='0', padx=30, pady=10,
                        font=('fixedsys', 10), command=button_0)

zero_button.pack(side='left')

equal_button = Button(zero_equal_frame, text='=', padx=30, pady=10,
                        font=('fixedsys', 10), command=equals)

equal_button.pack(side='right')
################buttons#################



display_text = StringVar()



display = Label(display_frame, textvariable=display_text, font=('fixedsys', 30), width=20)
display.pack()

display_text.set(''.join(stack))




root.mainloop()
