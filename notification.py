import tkinter as tk
from tkinter import ttk
from color import Color

class NotificationFrame(tk.Frame):
    def __init__(self,root):
        super().__init__(root, width=350, height=350)
        self.root = root
        self.nt_list=[]

        self.mainframe = tk.Frame(self, width=350, height=350, bg=Color.GRAY)
        self.mainframe.place(x=0,y=0)

    def add_notification(self,message):
        if len(self.nt_list) >= 5:
            old_nt = self.nt_list.pop(0)
            old_nt.destroy()

        new_nt = Notification(self.mainframe, message)
        self.nt_list.append(new_nt)

        self.deployment()

    def deployment(self):
        for i, item in enumerate(self.nt_list):
            item.grid(row=i,column=0)


class Notification(tk.Frame):
    def __init__(self, root, message):
        super().__init__(root, width=350, height=70, bg=Color.FOCUS)

        self.nt_frame = tk.Frame(self, width=70, height=70, bg="red", relief="solid", bd=1)
        self.nt_frame.place(x=0,y=0)
        self.ui_frame = tk.Frame(self, width=280, height=70, bg="skyblue", relief="solid", bd=1)
        self.ui_frame.place(x=70,y=0)

        self.name_label = tk.Label(self.ui_frame, text="침팬치", font=("godic",15))
        self.name_label.place(x=5,y=5)

        self.mesagge_label = tk.Label(self.ui_frame, text=message)
        self.mesagge_label.place(x=5,y=35)
        # self.label = tk.Label(self, text=message, bg=Color.FOCUS, fg="white")
        # self.label.grid(row=1,column=1,)


if __name__ == "__main__":
    r = tk.Tk()
    r.geometry("1300x700")
    r.config(bg="white")
    nt = NotificationFrame(r)
    nt.add_notification("123123")
    nt.add_notification("456456")
    nt.add_notification("789789")
    nt.add_notification("112233")
    nt.add_notification("445566")
    nt.add_notification("778899")
    nt.place(x=0, y=0)

    r.mainloop()