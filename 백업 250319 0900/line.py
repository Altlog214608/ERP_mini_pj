import tkinter as tk

class HorizontalLine(tk.Frame):
    def __init__(self, root, x, y, length, color):
        super().__init__(root, width=length, height=1, bd=0, bg=color)
        self.place(x=x, y=y)

class VerticalLine(tk.Frame):
    def __init__(self, root, x, y, length, color):
        super().__init__(root, width=1, height=length, bd=0, bg=color)
        self.place(x=x, y=y)