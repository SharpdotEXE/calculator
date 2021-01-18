from tkinter import *
import tkinter as tk

root = tk.Tk()
root.title('Greg\'s Calculator')
root.config(bg='#414241')

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
    # might add try: except here
    str_stack = ''.join(stack)
    display_text.set(eval(''.join(stack)))
    return stack


def set():
    #needs work
    stack = equals()


def light_mode():
    root.config(bg='gray')
    display.config(bg='#183321', fg='#33f273')
    clearbutton.config(bg='white', fg='black')
    delbutton.config(bg='white', fg='black')
    number1_button.config(bg='white', fg='black')
    number4_button.config(bg='white', fg='black')
    number7_button.config(bg='white', fg='black')
    number2_button.config(bg='white', fg='black')
    number5_button.config(bg='white', fg='black')
    number8_button.config(bg='white', fg='black')
    number3_button.config(bg='white', fg='black')
    number6_button.config(bg='white', fg='black')
    number9_button.config(bg='white', fg='black')
    number0_button.config(bg='white', fg='black')
    plus_button.config(bg='white', fg='black')
    minus_button.config(bg='white', fg='black')
    multiply_button.config(bg='white', fg='black')
    divide_button.config(bg='white', fg='black')
    equal_button.config(bg='white', fg='black')
    decimal_button.config(bg='white', fg='black')
    square_button.config(bg='white', fg='black')
    open_parenthesis_button.config(bg='white', fg='black')
    close_parenthesis_button.config(bg='white', fg='black')
    set_button.config(bg='white', fg='#2a362e')
    light_mode_button.config(bg='black', fg='#33f273')
    dark_mode_button.config(bg='white', fg='black')

    display_frame.config(bg='gray')
    clear_del_set_frame.config(bg='gray')
    one_4_7_frame.config(bg='gray')
    two_5_8_frame.config(bg='gray')
    three_6_9_frame.config(bg='gray')
    operator_frame.config(bg='gray')
    on_off_frame.config(bg='gray')
    equal_parentheses_frame.config(bg='gray')


def dark_mode():
    root.config(bg='black')
    display.config(bg='#183321', fg='#33f273')
    clearbutton.config(bg='#2a362e', fg='#33f273')
    delbutton.config(bg='#2a362e', fg='#33f273')
    number1_button.config(bg='#2a362e', fg='#33f273')
    number4_button.config(bg='#2a362e', fg='#33f273')
    number7_button.config(bg='#2a362e', fg='#33f273')
    number2_button.config(bg='#2a362e', fg='#33f273')
    number5_button.config(bg='#2a362e', fg='#33f273')
    number8_button.config(bg='#2a362e', fg='#33f273')
    number3_button.config(bg='#2a362e', fg='#33f273')
    number6_button.config(bg='#2a362e', fg='#33f273')
    number9_button.config(bg='#2a362e', fg='#33f273')
    number0_button.config(bg='#2a362e', fg='#33f273')
    plus_button.config(bg='#2a362e', fg='#33f273')
    minus_button.config(bg='#2a362e', fg='#33f273')
    multiply_button.config(bg='#2a362e', fg='#33f273')
    divide_button.config(bg='#2a362e', fg='#33f273')
    equal_button.config(bg='#2a362e', fg='#33f273')
    decimal_button.config(bg='#2a362e', fg='#33f273')
    square_button.config(bg='#2a362e', fg='#33f273')
    open_parenthesis_button.config(bg='#2a362e', fg='#33f273')
    close_parenthesis_button.config(bg='#2a362e', fg='#33f273')
    light_mode_button.config(bg='#2a362e', fg='#33f273')
    dark_mode_button.config(bg='#33f273', fg='black')
    set_button.config(bg='#2a362e', fg='#33f273')

    display_frame.config(bg='black')
    clear_del_set_frame.config(bg='black')
    one_4_7_frame.config(bg='black')
    two_5_8_frame.config(bg='black')
    three_6_9_frame.config(bg='black')
    operator_frame.config(bg='black')
    on_off_frame.config(bg='black')
    equal_parentheses_frame.config(bg='black')

###########button functions###########






################frames################
display_frame = tk.Frame(root, bg='#414241', borderwidth=5)
display_frame.pack()

clear_del_set_frame = tk.Frame(root, bg='#414241', borderwidth=5)
clear_del_set_frame.pack()

one_4_7_frame = tk.Frame(root, bg='#414241', borderwidth=5)
one_4_7_frame.pack(side='left')

two_5_8_frame = tk.Frame(root, bg='#414241', borderwidth=5)
two_5_8_frame.pack(side='left')

three_6_9_frame = tk.Frame(root, bg='#414241', borderwidth=5)
three_6_9_frame.pack(side='left')

operator_frame = tk.Frame(root, bg='#414241', borderwidth=5)
operator_frame.pack(side='right')

equal_parentheses_frame = tk.Frame(root, bg='#414241', borderwidth=5)
equal_parentheses_frame.pack(side='bottom', anchor='sw')

on_off_frame = tk.Frame(root, bg='#414241', borderwidth=5)
on_off_frame.pack()
################frames################



###########labels#############
display_text = StringVar()

display = tk.Label(display_frame, bg='black', textvariable=display_text,
                   font=('fixedsys', 30), relief='raised', wraplength=360, width=20)

display.pack()
###########labels#############



################buttons#################
clearbutton = tk.Button(clear_del_set_frame, text='Clear', padx=30, pady=10,
                        font=('fixedsys', 10), command=clear_stack)

clearbutton.pack(side='left')

delbutton = tk.Button(clear_del_set_frame, text='Del', padx=30, pady=10,
                      font=('fixedsys', 10), command=delete_from_stack)

delbutton.pack(side='right')

set_button = tk.Button(clear_del_set_frame, text='Set', padx=22, pady=10,
                       font=('fixedsys', 10), state='disabled', command=set)

set_button.pack()

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

decimal_button = tk.Button(three_6_9_frame, text='.', padx=30, pady=10,
                           font=('fixedsys', 10), command=lambda: append_to_stack('.'))

decimal_button.pack()

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

number0_button = tk.Button(two_5_8_frame, text='0', padx=30, pady=10,
                        font=('fixedsys', 10), command=lambda: append_to_stack('0'))

number0_button.pack()

equal_button = tk.Button(equal_parentheses_frame, text='=', padx=30, pady=10,
                         font=('fixedsys', 10), command=equals)

equal_button.pack(side='bottom', anchor='s')



square_button = tk.Button(one_4_7_frame, text='^2', padx=26, pady=10,
                          font=('fixedsys', 10), command=lambda: append_to_stack('**2'))

square_button.pack()

open_parenthesis_button = tk.Button(equal_parentheses_frame, text='(', padx=30, pady=10,
                                    font=('fixedsys', 10), command=lambda: append_to_stack('('))

open_parenthesis_button.pack(side='left', anchor='nw')

close_parenthesis_button = tk.Button(equal_parentheses_frame, text=')', padx=30, pady=10,
                                     font=('fixedsys', 10), command=lambda: append_to_stack(')'))

close_parenthesis_button.pack(side='left', anchor='ne')


light_mode_button = tk.Button(on_off_frame, text='Light Mode', padx=34, pady=10,
                      font=('fixedsys', 10), command=light_mode)

light_mode_button.pack()

dark_mode_button = tk.Button(on_off_frame, text='Dark Mode', padx=38, pady=10,
                       font=('fixedsys', 10), command=dark_mode)

dark_mode_button.pack()



################buttons#################

root.config(bg='gray')
display.config(bg='#183321', fg='#33f273')
clearbutton.config(bg='white', fg='black')
delbutton.config(bg='white', fg='black')
number1_button.config(bg='white', fg='black')
number4_button.config(bg='white', fg='black')
number7_button.config(bg='white', fg='black')
number2_button.config(bg='white', fg='black')
number5_button.config(bg='white', fg='black')
number8_button.config(bg='white', fg='black')
number3_button.config(bg='white', fg='black')
number6_button.config(bg='white', fg='black')
number9_button.config(bg='white', fg='black')
number0_button.config(bg='white', fg='black')
plus_button.config(bg='white', fg='black')
minus_button.config(bg='white', fg='black')
multiply_button.config(bg='white', fg='black')
divide_button.config(bg='white', fg='black')
equal_button.config(bg='white', fg='black')
decimal_button.config(bg='white', fg='black')
square_button.config(bg='white', fg='black')
open_parenthesis_button.config(bg='white', fg='black')
close_parenthesis_button.config(bg='white', fg='black')
set_button.config(bg='white', fg='#2a362e')
light_mode_button.config(bg='black', fg='#33f273')
dark_mode_button.config(bg='white', fg='black')


display_frame.config(bg='gray')
clear_del_set_frame.config(bg='gray')
one_4_7_frame.config(bg='gray')
two_5_8_frame.config(bg='gray')
three_6_9_frame.config(bg='gray')
operator_frame.config(bg='gray')
on_off_frame.config(bg='gray')
equal_parentheses_frame.config(bg='gray')


root.mainloop()
