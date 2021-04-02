from tkinter import *

root = Tk()
root.title('On-Screen Keyboard')
root.configure(bg='black')

root.resizable(False, False)

text_area = Text(root, height=10, width=80, font=('arial', 10))
text_area.grid(row=1, columnspan=40)

rows = 2
columns = 0

keys = ['\'', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'BackS', 'Del',
        'Tab', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '\\', '7', '8', '9',
        'caps', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', 'Enter', '4', '5', '6',
        '↑ Shift', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', '↑ Shift', '1', '2', '3',
        'Space']


def press(value):
    if value == 'Space':
        text_area.insert(INSERT, ' ')

    elif value == 'Tab':
        text_area.insert(INSERT, '\t')

    elif value == 'Enter':
        text_area.insert(INSERT, '\n')

    elif value == 'Del':
        text_area.delete(1.0, END)

    elif value == 'BackS':
        screen_text = text_area.get(1.0, END)
        text_area.delete(1.0, END)
        text_area.insert(INSERT, screen_text[:-2])

    elif value == '↑ Shift':
        shift_up_keys = ['\"', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', 'BackS', 'Del',
                         'Tab', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '|', '7', '8', '9',
                         'caps', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', 'Enter', '4', '5', '6',
                         '↓ Shift', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?', '↓ Shift', '1', '2', '3',
                         'Space']

        rows = 2
        columns = 0

        for button in shift_up_keys:
            command = lambda key=button: press(key)

            if button == 'Space':
                Button(root, bg='light sky blue', width=95, text=button, command=command).grid(row=rows, column=columns,
                                                                                               columnspan=15)
            else:
                Button(root, bg='light sky blue', width=5, text=button, command=command).grid(row=rows, column=columns)
                columns += 1

                if columns == 15:
                    columns = 0
                    rows += 1

    elif value == '↓ Shift':
        shift_dn_keys = ['\'', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'BackS', 'Del',
                         'Tab', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '\\', '7', '8', '9',
                         'caps', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', 'Enter', '4', '5', '6',
                         '↑ Shift', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', '↑ Shift', '1', '2', '3',
                         'Space']

        rows = 2
        columns = 0

        for button in shift_dn_keys:
            command = lambda key=button: press(key)

            if button == 'Space':
                Button(root, bg='light sky blue', width=95, text=button, command=command).grid(row=rows, column=columns,
                                                                                               columnspan=15)
            else:
                Button(root, bg='light sky blue', width=5, text=button, command=command).grid(row=rows, column=columns)
                columns += 1

                if columns == 15:
                    columns = 0
                    rows += 1

    elif value == 'caps':
        caps_keys = ['\'', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'BackS', 'Del',
                     'Tab', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '\\', '7', '8', '9',
                     'CAPS', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', 'Enter', '4', '5', '6',
                     '↑ Shift', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/', '↑ Shift', '1', '2', '3',
                     'Space']

        rows = 2
        columns = 0

        for button in caps_keys:
            command = lambda key=button: press(key)

            if button == 'Space':
                Button(root, bg='light sky blue', width=95, text=button, command=command).grid(row=rows, column=columns,
                                                                                               columnspan=15)
            else:
                Button(root, bg='light sky blue', width=5, text=button, command=command).grid(row=rows, column=columns)
                columns += 1

                if columns == 15:
                    columns = 0
                    rows += 1

    elif value == 'CAPS':
        global keys
        rows = 2
        columns = 0

        for button in keys:
            command = lambda key=button: press(key)

            if button == 'Space':
                Button(root, bg='light sky blue', width=95, text=button, command=command).grid(row=rows, column=columns,
                                                                                               columnspan=15)
            else:
                Button(root, bg='light sky blue', width=5, text=button, command=command).grid(row=rows, column=columns)
                columns += 1

                if columns == 15:
                    columns = 0
                    rows += 1

    else:
        text_area.insert(INSERT, value)

    text_area.focus_set()


for button in keys:
    command = lambda key=button: press(key)

    if button == 'Space':
        Button(root, bg='light sky blue', width=95, text=button, command=command).grid(row=rows, column=columns,
                                                                                       columnspan=15)
    else:
        Button(root, bg='light sky blue', width=5, text=button, command=command).grid(row=rows, column=columns)
        columns += 1

        if columns == 15:
            columns = 0
            rows += 1

mainloop()
