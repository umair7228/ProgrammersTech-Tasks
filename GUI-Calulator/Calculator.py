from tkinter import *

calculator = Tk()

calculator.title("Calculator")

# Define variables for user inputs
first_number = second_number = operator = None

# Adding icon for calculator
calculator.iconbitmap("D:\ProgrammersTech\GUI-Calulator\images/myIcon.ico")
calculator.geometry("380x450") # To give width and height of window

# Let's set the background color
calculator.configure(bg="gray10")

# Now let's create an entry box to take input and show result
inputLable = Label(calculator, text='', bg="gray10", fg="white")
inputLable.grid(row=0, column=0, columnspan=5, pady=(10, 10), sticky='w')
inputLable.config(font=("Courier", 44, "bold"))

# Function for digits
def inputNumber(number):
    current_number = inputLable['text']
    current_number = current_number + str(number)
    inputLable.config(text=current_number)

# Function for clear
def clear():
    inputLable.config(text='')

# Funtion for getting first number and operator
def get_operator(op_symbol):
    global first_number, operator
    first_number = int(inputLable['text'])
    operator = op_symbol
    inputLable.config(text='')

# Function to take second number and show the result
def result():
    global first_number, second_number, operator

    second_number = int(inputLable['text'])

    # addition
    if operator == '+':
        inputLable.config(text=str(first_number + second_number))

    # subtraction
    elif operator == '-':
        inputLable.config(text=str(first_number - second_number))

    # Multiplication
    elif operator == 'x':
        inputLable.config(text=str(first_number * second_number))

    # division
    else:
        if second_number == 0:
            inputLable.config(text="Error")
        else:
            inputLable.config(text=str(round(first_number / second_number,2)))

# Let's create buttons
# Buttons for first row
btn7 = Button(calculator, text=7, bg="#CCCCCC", fg="yellow", width=5, height=2, command=lambda: inputNumber(7))
btn7.grid(row=1, column=0)
btn7.config(font=("Courier", 22, "bold"))

btn8 = Button(calculator, text=8, bg="#CCCCCC", fg="yellow", width=5, height=2, command=lambda: inputNumber(8))
btn8.grid(row=1, column=1)
btn8.config(font=("Courier", 22, "bold"))

btn9 = Button(calculator, text=9, bg="#CCCCCC", fg="yellow", width=5, height=2, command=lambda: inputNumber(9))
btn9.grid(row=1, column=2)
btn9.config(font=("Courier", 22, "bold"))

division = Button(calculator, text='÷', bg="#CCCCCC", fg="yellow", width=5, height=2, command=lambda: get_operator('÷'))
division.grid(row=1, column=3)
division.config(font=("Courier", 22, "bold"))

# Buttons for second row 
btn4 = Button(calculator, text=4, bg="#CCCCCC", fg="yellow", width=5, height=2, command=lambda: inputNumber(4))
btn4.grid(row=2, column=0)
btn4.config(font=("Courier", 22, "bold"))

btn5 = Button(calculator, text=5, bg="#CCCCCC", fg="yellow", width=5, height=2, command=lambda: inputNumber(5))
btn5.grid(row=2, column=1)
btn5.config(font=("Courier", 22, "bold"))

btn6 = Button(calculator, text=6, bg="#CCCCCC", fg="yellow", width=5, height=2, command=lambda: inputNumber(6))
btn6.grid(row=2, column=2)
btn6.config(font=("Courier", 22, "bold"))

multiply = Button(calculator, text='x', bg="#CCCCCC", fg="yellow", width=5, height=2, command=lambda: get_operator('x'))
multiply.grid(row=2, column=3)
multiply.config(font=("Courier", 22, "bold"))

# Buttons for third row
btn1 = Button(calculator, text=1, bg="#CCCCCC", fg="yellow", width=5, height=2, command=lambda: inputNumber(1))
btn1.grid(row=3, column=0)
btn1.config(font=("Courier", 22, "bold"))

btn2 = Button(calculator, text=2, bg="#CCCCCC", fg="yellow", width=5, height=2, command=lambda: inputNumber(2))
btn2.grid(row=3, column=1)
btn2.config(font=("Courier", 22, "bold"))

btn3 = Button(calculator, text=3, bg="#CCCCCC", fg="yellow", width=5, height=2, command=lambda: inputNumber(3))
btn3.grid(row=3, column=2)
btn3.config(font=("Courier", 22, "bold"))

subtract = Button(calculator, text='-', bg="#CCCCCC", fg="yellow", width=5, height=2, command=lambda: get_operator('-'))
subtract.grid(row=3, column=3)
subtract.config(font=("Courier", 22, "bold"))

# Buttons for fourth row
clr_button = Button(calculator, text='C', bg="#CCCCCC", fg="yellow", width=5, height=2, command=lambda: clear())
clr_button.grid(row=4, column=0)
clr_button.config(font=("Courier", 22, "bold"))

btn0 = Button(calculator, text=0, bg="#CCCCCC", fg="yellow", width=5, height=2, command=lambda: inputNumber(0))
btn0.grid(row=4, column=1)
btn0.config(font=("Courier", 22, "bold"))

equal_button = Button(calculator, text='=', bg="#CCCCCC", fg="yellow", width=5, height=2, command=result)
equal_button.grid(row=4, column=2)
equal_button.config(font=("Courier", 22, "bold"))

add = Button(calculator, text='+', bg="#CCCCCC", fg="yellow", width=5, height=2, command=lambda: get_operator('+'))
add.grid(row=4, column=3)
add.config(font=("Courier", 22, "bold"))

calculator.mainloop()

