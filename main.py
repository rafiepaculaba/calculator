import tkinter as tk
from tkinter import font


height = 500
width = 350
value = ""


def button_click(number):
    global value
    entry.delete(0, 'end')
    str(value)
    print(type(value))
    print(type(number))
    str(number)
    str(value)
    value += number
    entry.insert('end', value)



def clear_it():
    global value
    entry.delete(0, 'end')
    value = ''


def solve_it():
    global value
    entry.delete(0, 'end')
    value = eval(value)
    value = str(value)
    print(type(value))
    print(value)

    print(type(value))
    entry.insert('end', str(value))

root = tk.Tk()
root.title("Calculator")

canvas = tk.Canvas(root, height=height, width=width)
canvas.pack()

frame = tk.Frame(root, bg='#000')
frame.place(relwidth=1, relheight=1)

entry = tk.Entry(frame, font=('Tahoma', 30), bg="#fff", bd=5, justify='right')
entry.place(relwidth=1, relheight=0.2)

button1 = tk.Button(frame, font=('Tahoma', 30), bg="gray", bd=5, text="1", command= lambda: button_click("1"))
button1.place(relx=0, rely=0.2, relwidth=0.25, relheight=0.2)

button2 = tk.Button(frame, font=('Tahoma', 30), bg="gray", bd=5, text="2", command= lambda: button_click("2"))
button2.place(relx=0.25, rely=0.2, relwidth=0.25, relheight=0.2)

button3 = tk.Button(frame, font=('Tahoma', 30), bg="gray", bd=5, text="3", command= lambda: button_click("3"))
button3.place(relx=0.5, rely=0.2, relwidth=0.25, relheight=0.2)

button_plus = tk.Button(frame, font=('Tahoma', 30), bg="gray", bd=5, text="+", command= lambda: button_click("+"))
button_plus.place(relx=0.75, rely=0.2, relwidth=0.25, relheight=0.2)

button4 = tk.Button(frame, font=('Tahoma', 30), bg="gray", bd=5, text="4", command= lambda: button_click("4"))
button4.place(relx=0, rely=0.4, relwidth=0.25, relheight=0.2)

button5 = tk.Button(frame, font=('Tahoma', 30), bg="gray", bd=5, text="5", command= lambda: button_click("5"))
button5.place(relx=0.25, rely=0.4, relwidth=0.25, relheight=0.2)

button6 = tk.Button(frame, font=('Tahoma', 30), bg="gray", bd=5, text="6", command= lambda: button_click("6"))
button6.place(relx=0.5, rely=0.4, relwidth=0.25, relheight=0.2)

button_minus = tk.Button(frame, font=('Tahoma', 30), bg="gray", bd=5, text="-", command= lambda: button_click("-"))
button_minus.place(relx=0.75, rely=0.4, relwidth=0.25, relheight=0.2)

button7 = tk.Button(frame, font=('Tahoma', 30), bg="gray", bd=5, text="7", command= lambda: button_click("7"))
button7.place(relx=0, rely=0.6, relwidth=0.25, relheight=0.2)

button8 = tk.Button(frame, font=('Tahoma', 30), bg="gray", bd=5, text="8", command= lambda: button_click("8"))
button8.place(relx=0.25, rely=0.6, relwidth=0.25, relheight=0.2)

button9 = tk.Button(frame, font=('Tahoma', 30), bg="gray", bd=5, text="9", command= lambda: button_click("9"))
button9.place(relx=0.5, rely=0.6, relwidth=0.25, relheight=0.2)

button_multiply = tk.Button(frame, font=('Tahoma', 30), bg="gray", bd=5, text="*", command= lambda: button_click("*"))
button_multiply.place(relx=0.75, rely=0.6, relwidth=0.25, relheight=0.2)

button_clear = tk.Button(frame, font=('Tahoma', 30), bg="red", bd=5, text="C", command= lambda: clear_it())
button_clear.place(relx=0, rely=0.8, relwidth=0.25, relheight=0.2)

button0 = tk.Button(frame, font=('Tahoma', 30), bg="gray", bd=5, text="0", command= lambda: button_click("0"))
button0.place(relx=0.25, rely=0.8, relwidth=0.25, relheight=0.2)

button_divide = tk.Button(frame, font=('Tahoma', 30), bg="gray", bd=5, text="/")
button_divide.place(relx=0.5, rely=0.8, relwidth=0.25, relheight=0.2)

button_equal = tk.Button(frame, font=('Tahoma', 30), bg="gray", bd=5, text="=", command= lambda: solve_it())
button_equal.place(relx=0.75, rely=0.8, relwidth=0.25, relheight=0.2)

root.mainloop()