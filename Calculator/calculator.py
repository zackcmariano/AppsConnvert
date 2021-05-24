import tkinter as tk
from typing import List

def calc_root() -> tk.Tk:
    root = tk.Tk()
    root.title('CALCULATOR')
    root.config(padx=10, pady=10, background='#fff')
    root.resizable(False, False)
    return root

def calc_label(root) -> tk.Label:
    label = tk.Label(
        root, text='RESULTADO',
        anchor='e', justify='right', background='#fff'
    )
    label.grid(row=0, column=0, columnspan=5, sticky='news')
    return label

def calc_display(root) -> tk.Entry:
    display = tk.Entry(root)
    display.grid(row=1, column=0, columnspan=5, sticky='news', pady=(0, 10))
    display.config(
        font=('Helvetica', 40, 'bold'),
        justify='right', bd=1, relief='flat',
        highlightthickness=1, highlightcolor='#ccc'
    )
    display.bind('<Control-a>', display_control_a)
    return display

def display_control_a(event):
    event.widget.select_range(0, 'end')
    event.widget.icursor('end')
    return 'break'

def calc_buttons(root) -> List[List[tk.Button]]:
    button_texts: List[List[str]] = [
        ['7', '8', '9', '+', 'C'],
        ['4', '5', '6', '-', '/'],
        ['1', '2', '3', '*', '^'],
        ['0', '.', '(', ')', '=']
    ]

    buttons: List[List[tk.Button]] = []

    for row, row_value in enumerate(button_texts, start=2):
        button_row = []
        for col_index, col_value in enumerate(row_value):
            btn = tk.Button(root, text=col_value)
            btn.grid(row=row, column=col_index, sticky='news', padx=5, pady=5)
            btn.config(
                font=('Helvetica', 16, 'normal'),
                pady=40, width=1, background='#f2f2f2', bd=0,
                cursor='hand2', highlightthickness=0, highlightcolor='#ccc',
                highlightbackground='#ccc', activebackground='#ccc'
            )
            button_row.append(btn)
        buttons.append(button_row)
    return buttons
