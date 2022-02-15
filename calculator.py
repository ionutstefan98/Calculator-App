from tkinter import *


def button_press(number):
    global eq_text

    eq_text = eq_text + str(number)
    eq_textLabel.set(eq_text)


def equals():
    global eq_text
    try:
        total = str(eval(eq_text))
        eq_textLabel.set(total)
        eq_text = total

    except ZeroDivisionError:
        eq_textLabel.set("YOU CAN NOT DIVIDE BY 0!")
        eq_text=""
    except SyntaxError:
        eq_textLabel.set("Syntax Error")
        eq_text=""



def clear():
    global eq_text

    eq_text = ""
    eq_textLabel.set(eq_text)


calcwindow = Tk()
calcwindow.title("Calculator")
calcwindow.geometry("500x500")
calcwindow.config(bg="light grey")

eq_text = ""
eq_textLabel = StringVar()

eq_label = Label(calcwindow, textvariable=eq_textLabel, height=3,width=30, bg="white", text=eq_text,
                 font=("Arial", 12), bd=2, relief=SUNKEN)
eq_label.pack(padx=5, pady=5)

button_frame = Frame(calcwindow)
button_frame.pack()

button1 = Button(button_frame, text="1", width=8, height=4, bd=3, command=lambda: button_press(1))
button1.grid(column=0, row=0)

button2 = Button(button_frame, text="2", width=8, height=4, bd=3, command=lambda: button_press(2))
button2.grid(column=1, row=0)

button3 = Button(button_frame, text="3", width=8, height=4, bd=3, command=lambda: button_press(3))
button3.grid(column=2, row=0)

button4 = Button(button_frame, text="4", width=8, height=4, bd=3, command=lambda: button_press(4))
button4.grid(column=0, row=1)

button5 = Button(button_frame, text="5", width=8, height=4, bd=3, command=lambda: button_press(5))
button5.grid(column=1, row=1)

button6 = Button(button_frame, text="6", width=8, height=4, bd=3, command=lambda: button_press(6))
button6.grid(column=2, row=1)

button7 = Button(button_frame, text="7", width=8, height=4, bd=3, command=lambda: button_press(7))
button7.grid(column=0, row=2)

button8 = Button(button_frame, text="8", width=8, height=4, bd=3, command=lambda: button_press(8))
button8.grid(column=1, row=2)

button9 = Button(button_frame, text="9", width=8, height=4, bd=3, command=lambda: button_press(9))
button9.grid(column=2, row=2)

button0 = Button(button_frame, text="0", width=8, height=4, bd=3, command=lambda: button_press(0))
button0.grid(column=0, row=3)

decimal_button = Button(button_frame, text=".", width=8, height=4, bd=3, command=lambda: button_press("."))
decimal_button.grid(column=1, row=3)

equal_button = Button(button_frame, text="=", width=8, height=4, bd=3, command=equals)
equal_button.grid(column=2, row=3)

add_button = Button(button_frame, text="+", width=8, height=4, bd=3, command=lambda: button_press("+"))
add_button.grid(column=3, row=0)

minus_button = Button(button_frame, text="-", width=8, height=4, bd=3, command=lambda: button_press("-"))
minus_button.grid(column=3, row=1)

times_button = Button(button_frame, text="*", width=8, height=4, bd=3, command=lambda: button_press("*"))
times_button.grid(column=3, row=2)

subs_button = Button(button_frame, text="/", width=8, height=4, bd=3, command=lambda: button_press("/"))
subs_button.grid(column=3, row=3)

clear_button = Button(calcwindow, text="CLEAR", width=25, height=4, bd=3, command=clear)
clear_button.pack()


calcwindow.mainloop()
