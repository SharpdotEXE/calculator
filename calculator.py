from tkinter import *
import tkinter as tk

root = tk.Tk()
root.title('Calculator')

stack = []


def append_to_stack(element):
    stack.append(element)
    display_text.set(''.join(stack))


def clear_stack():
    del stack[::]
    display_text.set(''.join(stack))

def delete_from_stack():
    del stack[-1]
    display_text.set(''.join(stack))

def equals():
    #might add try: except here
    str_stack = ''.join(stack)
    display_text.set(eval(''.join(stack)))
    

def square():
    #needs work
    stack.append('**(2)')
    display_text.set(''.join(stack))

def on():
    display.config(bg='lightgreen')
    clear_stack()

def off():
    display.config(bg='black')
    clear_stack()
###########button functions###########



################frames################
display_frame = tk.Frame(root, bg='black', borderwidth=5)
display_frame.pack()

clear_del_frame = tk.Frame(root, bg='yellow', borderwidth=5)
clear_del_frame.pack()

one_4_7_frame = tk.Frame(root, bg='skyblue', borderwidth=5)
one_4_7_frame.pack(side='left')

two_5_8_frame = tk.Frame(root, bg='purple', borderwidth=5)
two_5_8_frame.pack(side='left')

three_6_9_frame = tk.Frame(root, bg='green', borderwidth=5)
three_6_9_frame.pack(side='left')

operator_frame = tk.Frame(root, bg='pink', borderwidth=5)
operator_frame.pack(side='right')

zero_equal_frame = tk.Frame(root, bg='orange', borderwidth=5)
zero_equal_frame.pack(side='bottom', anchor='sw')

on_off_frame = tk.Frame(root, bg='lightgreen', borderwidth=5)
on_off_frame.pack()
################frames################





################buttons#################
clearbutton = tk.Button(clear_del_frame, text='clear', padx=30, pady=10,
                        font=('fixedsys', 10), command=clear_stack)
clearbutton.pack(side='left')

delbutton = tk.Button(clear_del_frame, text='del', padx=30, pady=10,
                        font=('fixedsys', 10), command=delete_from_stack)
delbutton.pack(side='right')


number1_button = tk.Button(one_4_7_frame, text='1', padx=30, pady=10,
                        font=('fixedsys', 10), command=lambda: append_to_stack('1'))
number1_button.pack()

number4_button = tk.Button(one_4_7_frame, text='4', padx=30, pady=10,
                        font=('fixedsys', 10), command=lambda: append_to_stack('4'))
number4_button.pack()

number7_button = tk.Button(one_4_7_frame, text='7', padx=30, pady=10,
                        font=('fixedsys', 10), command=lambda: append_to_stack('7'))
number7_button.pack()


number2_button = tk.Button(two_5_8_frame, text='2', padx=30, pady=10,
                        font=('fixedsys', 10), command=lambda: append_to_stack('2'))
number2_button.pack()

number5_button = tk.Button(two_5_8_frame, text='5', padx=30, pady=10,
                        font=('fixedsys', 10), command=lambda: append_to_stack('5'))
number5_button.pack()

number8_button = tk.Button(two_5_8_frame, text='8', padx=30, pady=10,
                        font=('fixedsys', 10), command=lambda: append_to_stack('8'))
number8_button.pack()


number3_button = tk.Button(three_6_9_frame, text='3', padx=30, pady=10,
                        font=('fixedsys', 10), command=lambda: append_to_stack('3'))
number3_button.pack()

number6_button = tk.Button(three_6_9_frame, text='6', padx=30, pady=10,
                        font=('fixedsys', 10), command=lambda: append_to_stack('6'))
number6_button.pack()

number9_button = tk.Button(three_6_9_frame, text='9', padx=30, pady=10,
                        font=('fixedsys', 10), command=lambda: append_to_stack('9'))
number9_button.pack()

plus_button = tk.Button(operator_frame, text='+', padx=30, pady=10,
                        font=('fixedsys', 10), command=lambda: append_to_stack('+'))
plus_button.pack()

minus_button = tk.Button(operator_frame, text='-', padx=30, pady=10,
                        font=('fixedsys', 10), command=lambda: append_to_stack('-'))
minus_button.pack()

multiply_button = tk.Button(operator_frame, text='*', padx=30, pady=10,
                        font=('fixedsys', 10), command=lambda: append_to_stack('*'))
multiply_button.pack()

divide_button = tk.Button(operator_frame, text='/', padx=30, pady=10,
                        font=('fixedsys', 10), command=lambda: append_to_stack('/'))
divide_button.pack()

zero_button = tk.Button(one_4_7_frame, text='0', padx=30, pady=10,
                        font=('fixedsys', 10), command=lambda: append_to_stack('0'))

zero_button.pack(side='left')

equal_button = tk.Button(zero_equal_frame, text='=', padx=30, pady=10,
                        font=('fixedsys', 10), command=equals)

equal_button.pack(side='right')

decimal_button = tk.Button(two_5_8_frame, text='.', padx=30, pady=10,
                        font=('fixedsys', 10), command=lambda: append_to_stack('.'))

decimal_button.pack()

square_button = tk.Button(three_6_9_frame, text='^2', padx=26, pady=10,
                        font=('fixedsys', 10), command=lambda: append_to_stack('**2'))

square_button.pack()

open_parenthesis_button = tk.Button(zero_equal_frame, text='(', padx=30, pady=10,
                        font=('fixedsys', 10), command=lambda: append_to_stack('('))

open_parenthesis_button.pack()

close_parenthesis_button = tk.Button(zero_equal_frame, text=')', padx=30, pady=10,
                        font=('fixedsys', 10), command=lambda: append_to_stack(')'))

close_parenthesis_button.pack()

on_button = tk.Button(on_off_frame, text='on', padx=34, pady=10,
                        font=('fixedsys', 10), command=on)

on_button.pack()

off_button = tk.Button(on_off_frame, text='off', padx=30, pady=10,
                        font=('fixedsys', 10), command=off)

off_button.pack()


################buttons#################


display_text = StringVar()

display = tk.Label(display_frame, bg='black', textvariable=display_text, 
                    font=('fixedsys', 30), width=20)

display.pack()


root.mainloop()
