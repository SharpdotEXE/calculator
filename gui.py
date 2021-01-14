import tkinter as tk
import tkinter.font as tkFont

height, width = 300, 300

root = tk.Tk()

display_font = tkFont.Font(size=20)

canvas = tk.Canvas(root, height=height, width=width)
canvas.pack()

frame = tk.Frame(root)
frame.place(relwidth=.8, relheight=.8, relx=.1, rely=.1)

number_display = tk.Label(frame, text='Things will go here', bg='#b8b6b0', font=display_font, pady=5, padx=10)
number_display.pack()


button1 = tk.Button(frame, text='1', padx=30, pady=10)
button1.pack(side='left', anchor='n')

button2 = tk.Button(frame, text='2', padx=30, pady=10)
button2.pack(side='left', anchor='n')

button3 = tk.Button(frame, text='3', padx=30, pady=10)
button3.pack(side='left', anchor='n')

button4 = tk.Button(frame, text='4', padx=30, pady=10)
button4.pack()

button5 = tk.Button(frame, text='5', padx=30, pady=10)
button5.pack()

button6 = tk.Button(frame, text='6', padx=30, pady=10)
button6.pack()

button7 = tk.Button(frame, text='7', padx=30, pady=10)
button7.pack()

button8 = tk.Button(frame, text='8', padx=30, pady=10)
button8.pack()

button9 = tk.Button(frame, text='9', padx=30, pady=10)
button9.pack()

button0 = tk.Button(frame, text='0')
button0.pack()



root.mainloop()

