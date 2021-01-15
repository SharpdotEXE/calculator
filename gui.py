from tkinter import *

root = Tk()

display_frame = Frame(root, bg='lightgray')
display_frame.pack()

clear_del_frame = Frame(root, bg='yellow')
clear_del_frame.pack()

number_frame = Frame(root, bg='skyblue')
number_frame.pack(side='left')

operator_frame = Frame(root, bg='pink')
operator_frame.pack(side='right')

zero_equal_frame = Frame(root, bg='orange')
zero_equal_frame.pack()

clearbutton = Button(clear_del_frame, text='clear', padx=5)
clearbutton.pack(side='left')

delbutton = Button(clear_del_frame, text='del', padx=10)
delbutton.pack(side='right')




number1_button = Button(number_frame, text='1')
number1_button.pack(side='left', anchor='nw')

number2_button = Button(number_frame, text='2')
number2_button.pack(side='right', anchor='nw')

number3_button = Button(number_frame, text='3')
number3_button.pack(side='right', anchor='ne')

# number4_button = Button(number_frame, text='4')
# number4_button.pack(side='left', anchor='n')








root.mainloop()
