from tkinter import *
import random
import pyperclip

alphabets_lower = 'abcdefghijklmnopqrstuvwxyz'
alphabets_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
symbols = '''(){}[]/,.;:@$%&*+-?~#'''
combination = alphabets_lower + alphabets_upper + digits + symbols

while True:
    root = Tk()
    root.title('Python Project')
    root.geometry('300x160')
    root.minsize(300, 160)
    root.maxsize(300, 160)
    root.configure(bg='deep sky blue')

    heading = Label(root, text='Strong Password Generator', bg='black', fg='white', font='poppins 10 bold')
    heading.pack(fill=X)

    ask_input = Label(root, text='Enter password length:', bg='deep sky blue', font='calibri 10 bold')
    ask_input.pack(pady=5)

    def strong_pass(length):
        length = length.get()
        if 8 <= length <= 30:
            text = "".join(random.sample(combination, length))
            pyperclip.copy(text)
        else:
            text = "Min and Max length is 8 and 30."

        display_pass = Label(root, text=text, bg='deep sky blue', fg='black', font='bold 10')
        display_pass.pack(side=BOTTOM, pady=8)


    user_input = IntVar()
    user_input.set('')
    pass_length = Entry(root, textvariable=user_input)
    pass_length.pack()

    generate = Button(root, text='Generate Password', bg='black', fg='white', command=lambda: strong_pass(user_input))
    generate.pack(pady=10)

    exit_button = Button(root, text='Exit', bg='black', fg='white', command=exit)
    exit_button.pack(side=RIGHT)

    root.mainloop()
