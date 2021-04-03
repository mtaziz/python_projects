from tkinter import *
import random
import pyperclip

# Main variables
alphabets_lower = 'abcdefghijklmnopqrstuvwxyz'
alphabets_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
symbols = '''(){}[]/,.;:@$%&*+-?~#'''

# Adding everything to make a long string.
combination = alphabets_lower + alphabets_upper + digits + symbols

# Mainloop
while True:
    # Main window
    root = Tk()
    root.title('Python Project')
    
    # Dimensions
    root.geometry('300x160')
    root.minsize(300, 160)
    root.maxsize(300, 160)
    root.configure(bg='deep sky blue')
    
    # Heading
    heading = Label(root, text='Strong Password Generator', bg='black', fg='white', font='poppins 10 bold')
    heading.pack(fill=X)
    
    # Text for asking input.
    ask_input = Label(root, text='Enter password length:', bg='deep sky blue', font='calibri 10 bold')
    ask_input.pack(pady=5)

    def strong_pass(length):
        '''This function creates random strong passwords.'''
        length = length.get()
        if 8 <= length <= 30:
            text = "".join(random.sample(combination, length))
            # Copying the generated password to clipboard.
            pyperclip.copy(text)
        else:
            # If valid lenght is not provided then this text will be displayed in place of password.
            text = "Min and Max length is 8 and 30."
        
        # Displaying password or message.
        display_pass = Label(root, text=text, bg='deep sky blue', fg='black', font='bold 10')
        display_pass.pack(side=BOTTOM, pady=8)

    # Storing integer value.
    user_input = IntVar()
    user_input.set('')
    
    # Entry widget to type lenght.
    pass_length = Entry(root, textvariable=user_input)
    pass_length.pack()
    
    # Button to generate password.
    generate = Button(root, text='Generate Password', bg='black', fg='white', command=lambda: strong_pass(user_input))
    generate.pack(pady=10)
    
    # Exit button.
    exit_button = Button(root, text='Exit', bg='black', fg='white', command=exit)
    exit_button.pack(side=RIGHT)

    mainloop()
