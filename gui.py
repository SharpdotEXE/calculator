from tkinter import *

root = Tk()


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



# display = Label(display_frame, text='Numbers will go here', font=('fixedsys', 30))
# display.pack()

clearbutton = Button(clear_del_frame, text='clear', padx=30, pady=10, font=('fixedsys', 10))
clearbutton.pack(side='left')

delbutton = Button(clear_del_frame, text='del', padx=30, pady=10, font=('fixedsys', 10))
delbutton.pack(side='right')




number1_button = Button(one_4_7_frame, text='1', padx=30, pady=10, font=('fixedsys', 10))
number1_button.pack()

number4_button = Button(one_4_7_frame, text='4', padx=30, pady=10, font=('fixedsys', 10))
number4_button.pack()

number7_button = Button(one_4_7_frame, text='7', padx=30, pady=10, font=('fixedsys', 10))
number7_button.pack()


number2_button = Button(two_5_8_frame, text='2', padx=30, pady=10, font=('fixedsys', 10))
number2_button.pack()

number5_button = Button(two_5_8_frame, text='5', padx=30, pady=10, font=('fixedsys', 10))
number5_button.pack()

number8_button = Button(two_5_8_frame, text='8', padx=30, pady=10, font=('fixedsys', 10))
number8_button.pack()


number3_button = Button(three_6_9_frame, text='3', padx=30, pady=10, font=('fixedsys', 10))
number3_button.pack()

number6_button = Button(three_6_9_frame, text='6', padx=30, pady=10, font=('fixedsys', 10))
number6_button.pack()

number9_button = Button(three_6_9_frame, text='9', padx=30, pady=10, font=('fixedsys', 10))
number9_button.pack()

plus_button = Button(operator_frame, text='+', padx=30, pady=10, font=('fixedsys', 10))
plus_button.pack()

minus_button = Button(operator_frame, text='-', padx=30, pady=10, font=('fixedsys', 10))
minus_button.pack()

multiply_button = Button(operator_frame, text='*', padx=30, pady=10, font=('fixedsys', 10))
multiply_button.pack()

divide_button = Button(operator_frame, text='/', padx=30, pady=10, font=('fixedsys', 10))
divide_button.pack()

zero_button = Button(zero_equal_frame, text='0', padx=30, pady=10, font=('fixedsys', 10))
zero_button.pack(side='left')

equal_button = Button(zero_equal_frame, text='=', padx=30, pady=10, font=('fixedsys', 10))
equal_button.pack(side='right')






















root.mainloop()
