from tkinter import *
import re

# Generating window
root = Tk()
root.title('')
root.configure(bg='black')

# Disabling maximize
root.resizable(False, False)

# Heading
heading = Label(root, text='SIMPLE CALCULATOR', bg='black', fg='white', font='poppins 10 bold')
heading.grid(columnspan=50)

# Generating entry widget
text_area = Entry(root, justify='right', width=25, font=('arial', 11), bg='white', borderwidth=4, relief=SUNKEN)
text_area.grid(columnspan=40)

# List of buttons
buttons = ['7', '8', '9', '+',
           '4', '5', '6', '-',
           '1', '2', '3', '*',
           'C', '0', '/', '=']

# Initial point for rows and columns.
rows = 2
columns = 0

def press(value):
    '''This function contains actions for different buttons.'''
    if value == 'C':
        text_area.delete(0, END)

    elif value == '=':
        screen_text = text_area.get()

        # Regex for matching valid input.
        input_check_regex = re.compile(r'^-?\d+[-/+*\d]+-?\d+$')

        # findall() method returns a list.
        input = input_check_regex.findall(screen_text)

        if len(input) != 0:
            text_area.delete(0, END)
            text_area.insert(INSERT, eval(input[0]))

        else:
            text_area.delete(0, END)
            text_area.insert(INSERT, 'ERROR press C')

    else:
        text_area.insert(INSERT, value)
    
    # This will make sure that cursor is continuously blinking to make it visible to us.
    text_area.focus_set()

# Looping through the list of buttons and generating buttons in our root window.
for button in buttons:
    Button(root, bg='deep sky blue', text=button, font='poppins', width=4, command=lambda key=button: press(key), borderwidth=5, relief=RAISED).grid(row=rows, column=columns)
    columns += 1

    if columns == 4:
        columns = 0
        rows += 1

mainloop()
