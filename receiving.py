import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("ERP")
root.geometry("1300x700")

class Receiving(tk.Frame):
    def __init__(self):
        super().__init__()
        self.frame_top = tk.Frame(width=950,height=350,relief="solid", bd=2, bg="skyblue")
        self.frame_right = tk.Frame(width=350,height=350,relief="solid", bd=2, bg="green")
        self.frame_bottom = tk.Frame(width=1300,height=350,relief="solid", bd=2, bg="yellow")
        self.frame_top.grid(row=0,column=0)
        self.frame_right.grid(row=0,column=1)
        self.frame_bottom.grid(row=1,column=1)
        self.label=tk.Label(self.frame_top,text="123")
        # self.label= self.label.pack()




receiving = Receiving()
root.mainloop()