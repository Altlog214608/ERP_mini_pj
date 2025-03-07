import tkinter as tk
from tkinter import ttk
from color import Color

class Notification(tk.Frame):

    def __init__(self,root):
        super().__init__(root, width=350, height=350)
        self.root = root

        self.mainframe = tk.Frame(self,width=360,height=360,bg=Color.GRAY,relief='solid', bd=1)
        self.nt_frame1 = tk.Frame(self.mainframe,width=350,height=70,bg=Color.FOCUS)
        self.nt_frame2 = tk.Frame(self.mainframe,width=350,height=70,bg=Color.WHITE)
        self.nt_frame3 = tk.Frame(self.mainframe,width=350,height=70,bg=Color.WHITE)
        self.nt_frame4 = tk.Frame(self.mainframe,width=350,height=70,bg=Color.WHITE)
        self.nt_frame5 = tk.Frame(self.mainframe,width=350,height=70,bg=Color.WHITE)
        # self.nt_frame6 = tk.Frame(self,width=350,height=58,bg=Color.BLACK)

        self.nt_frame1.grid_propagate(False)
        self.nt_frame1.pack_propagate(False)
        self.nt_frame2.grid_propagate(False)
        self.nt_frame2.pack_propagate(False)
        self.nt_frame3.grid_propagate(False)
        self.nt_frame3.pack_propagate(False)
        self.nt_frame4.grid_propagate(False)
        self.nt_frame4.pack_propagate(False)
        self.nt_frame5.grid_propagate(False)
        self.nt_frame5.pack_propagate(False)
        # self.nt_frame6.grid_propagate(False)
        # self.nt_frame6.pack_propagate(False)

        self.mainframe.grid(row=0, column=0)
        self.nt_frame1.grid(row=0, column=0)
        self.nt_frame2.grid(row=1, column=0)
        self.nt_frame3.grid(row=2, column=0)
        self.nt_frame4.grid(row=3, column=0)
        self.nt_frame5.grid(row=4, column=0)
        # self.nt_frame6.grid(row=5, column=0)

        # image = tk.PhotoImage(file="monster2.png")
        self.ui_frame1 = tk.Frame(self.nt_frame1,width=70,height=70, bg="skyblue")
        self.ui_frame1.grid(row=0,column=0)
        self.text_frame1 = tk.Frame(self.nt_frame1, width=280, height=70, bg="coral")
        self.text_frame1.grid(row=0, column=1,columnspan=2,sticky="nswe")
        self.name_label1 = tk.Label(self.text_frame1,text="박민환박민환박민환박민환박민환박민환",anchor="w")
        self.content_label1 = tk.Label(self.text_frame1,text="코피 뻥",anchor="w")
        # self.check_button1 = tk.Button(self.text_frame1, text="확인", width=20)
        # self.ignore_button1 = tk.Button(self.text_frame1, text="무시", width=20)
        self.name_label1.grid(row= 0 ,column=0,columnspan=2,sticky ="nswe",pady=7)
        self.content_label1.grid(row= 1 ,column=0,columnspan=2,sticky ="nswe",pady=7)
        # self.check_button1.grid(row= 2 ,column=0,sticky ="nswe",pady=1)
        # self.ignore_button1.grid(row= 2 ,column=1,sticky ="nswe",pady=1)

        self.ui_frame2 = tk.Frame(self.nt_frame2,width=70,height=70,bg="red")
        self.ui_frame2.grid(row=0, column=0)
        self.text_frame2 = tk.Frame(self.nt_frame2, width=292, height=70, bg="coral")
        self.text_frame2.grid(row=0, column=1, columnspan=2, sticky="nswe")
        self.name_label2 = tk.Label(self.text_frame2, text="박민환", anchor="w")
        self.content_label2 = tk.Label(self.text_frame2, text="코피 뻥", anchor="w")
        # self.check_button2 = tk.Button(self.text_frame2, text="확인", width=20)
        # self.ignore_button2 = tk.Button(self.text_frame2, text="무시", width=20)
        self.name_label2.grid(row=0, column=0, columnspan=2, sticky="nswe", pady=1)
        self.content_label2.grid(row=1, column=0, columnspan=2, sticky="nswe", pady=1)
        # self.check_button2.grid(row=2, column=0, sticky="nswe", pady=1)
        # self.ignore_button2.grid(row=2, column=1, sticky="nswe", pady=1)

        # self.ui_frame3 = tk.Frame(self.nt_frame3,width=58,height=58,bg="gray")
        # self.ui_frame3.grid(row=0, column=0)
        # self.ui_frame4 = tk.Frame(self.nt_frame4,width=58,height=58,bg="skyblue")
        # self.ui_frame4.grid(row=0, column=0)
        # self.ui_frame5 = tk.Frame(self.nt_frame5,width=58,height=58,bg="red")
        # self.ui_frame5.grid(row=0, column=0)
        # self.ui_frame6 = tk.Frame(self.nt_frame6,width=58,height=58,bg="gray")
        # self.ui_frame6.grid(row=0, column=0)



if __name__ == "__main__":
    r = tk.Tk()
    r.geometry("1300x700")
    r.config(bg="white")
    nt = Notification(r)
    nt.place(x=0, y=0)

    r.mainloop()