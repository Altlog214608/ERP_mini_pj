import tkinter as tk
from itertools import count
from tkinter import ttk


from color import Color
# nt = None

class NotificationFrame(tk.Frame):
    def __init__(self,root, on_delete):
        super().__init__(root, width=350, height=350)
        self.root = root
        self.nt_list=[]
        self.old_nt_list = []
        self.on_delete = on_delete



        self.main_frame = tk.Frame(self, width=350, height=400, bg=Color.WHITE, relief="ridge", bd=2)
        self.main_frame.place(x=0, y=0)

        self.sub_frame= tk.Frame(self, width=350, height=50, bg=Color.VISUALIZE1, relief="ridge", bd=2)
        self.sub_frame.grid(row=0,column=0,sticky="nsew")
        self.nt_frame = tk.Frame(self, width=350, height=350, bg=Color.WHITE, relief="ridge", bd=2)
        self.nt_frame.grid(row=1,column=0,sticky="nsew")

        self.empty_label = tk.Label(self.nt_frame, text="현재 알림이 없습니다.", fg="black", bg=Color.WHITE, font=("Godic", 14,"bold"))
        self.empty_label.place(relx=0.5, rely=0.5, anchor="center")

        self.nt_label = tk.Label(self.sub_frame, text="알림", fg="black", bg=Color.VISUALIZE1,  font=("Arial", 12,"bold"))
        self.nt_label.grid(row=0,column=0)

        self.nt_label = tk.Label(self.sub_frame, text="", fg="black", bg=Color.VISUALIZE1,font=("Arial", 12, "bold"))
        self.nt_label.grid(row=0,column=1)

    def get_nt_len(self):
        sum = len(self.nt_list) + len(self.old_nt_list)
        self.nt_label.config(text=sum)
        if sum > 99:
            return 99
        else:
            return sum

    def add_notification(self,message,userID,userName, notification_frame):
        if len(self.nt_list) >= 5:
            old_nt = self.nt_list.pop(0)
            self.old_nt_list.append(old_nt)

        new_notification = Notification(self.nt_frame, message, userID, userName, notification_frame)
        self.nt_list.append(new_notification)

        self.deployment()

    def delete_nt(self, userID):
        index_to_remove = None
        for i, nt in enumerate(self.nt_list):
            if nt.get_id() == userID:
                index_to_remove = i
                break

        if index_to_remove is not None:
            del self.nt_list[index_to_remove]
            self.deployment()
            self.on_delete()

    def deployment(self):
        for widget in self.nt_frame.winfo_children():
            widget.grid_forget()

        while len(self.nt_list) < 5 and self.old_nt_list:
            restored_nt = self.old_nt_list.pop(0)
            self.nt_list.append(restored_nt)

        if not self.nt_list:
            self.empty_label.place(relx=0.5, rely=0.5, anchor="center")
        else:
            self.empty_label.place_forget()

        for i, item in enumerate(self.nt_list):
            item.grid(row=i, column=0, sticky="ew")

    def recv(self, dict):
        # code = kwargs.get("code")
        # sign = kwargs.get("sign")
        # data = kwargs.get("data")
        code = dict.get("code")
        sign = dict.get("sign")
        data = dict.get("data")
        print(data)
        if sign == 1:
            message = data["message"]
            userID = data["sender_id"]
            userName = data["sender_name"]

            self.add_notification(message,userID,userName,self)
            print(message,userID,userName)

class Notification(tk.Frame):
    def __init__(self, root, message, userID, userName, notification_frame):
        super().__init__(root, width=350, height=70, bg=Color.WHITE )

        self.root = root
        self.userID = userID
        self.mesagge = message
        self.userName = userName
        self.notification_frame = notification_frame

        self.person_img = tk.PhotoImage(file="person.png")

        self.nt_frame = tk.Frame(self, width=70, height=70, bg=Color.WHITE, relief="sunken", bd=1)
        self.nt_frame.place(x=0,y=0)

        self.labelPhoto = tk.Label(self.nt_frame, image=self.person_img, bg=Color.WHITE, width=70,height=70, anchor="center")
        self.labelPhoto.place(x=0,y=0)

        self.ui_frame = tk.Frame(self, width=280, height=70, bg=Color.WHITE, relief="sunken", bd=1)
        self.ui_frame.place(x=70,y=0)
        self.ui_frame.bind("<Button-1>",self.notification_click)
        self.ui_frame.configure(cursor='hand2')

        self.name_label = tk.Label(self.ui_frame, text=userName, bg=Color.WHITE, font=("Consolas",17,"bold"))
        self.name_label.place(x=5,y=5)

        self.mesagge_label = tk.Label(self.ui_frame, text=message, bg=Color.WHITE, font=("Arial"))
        self.mesagge_label.place(x=5,y=38)

    def get_id(self):
        return self.userID

    def get_name(self):
        return self.userName

    def notification_click(self, e):
        print("frame click",self.mesagge,self.userID, self.userName)
        self.notification_frame.delete_nt(self.get_id())

if __name__ == "__main__":
    r = tk.Tk()
    r.geometry("1300x700")
    r.config(bg="white")
    nt = NotificationFrame(r)

    r.mainloop()