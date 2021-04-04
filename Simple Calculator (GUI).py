from tkinter import *

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
    try:
        if value == 'C':
            text_area.delete(0, END)

        elif value == '=':
            screen_text = eval(text_area.get())
            text_area.delete(0, END)
            text_area.insert(INSERT, screen_text)

        else:
            text_area.insert(INSERT, value)
    
    # Handling error raised by wrong input.
    except SyntaxError:
        text_area.delete(0, END)
        text_area.insert(INSERT, 'ERROR press C')
    
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
