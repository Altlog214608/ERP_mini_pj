import tkinter as tk
from itertools import count
from tkinter import ttk


from color import Color
# nt = None

class NotificationFrame(tk.Frame):
    def __init__(self,root):
        super().__init__(root, width=350, height=350)
        self.root = root
        self.nt_list=[]
        self.old_nt_list = []
        self.mainframe = tk.Frame(self, width=350, height=350, bg=Color.GRAY)
        self.mainframe.place(x=0,y=0)

        self.empty_label = tk.Label(self.mainframe, text="현재 알림이 없습니다.", fg="black", bg=Color.GRAY, font=("Arial", 12))
        self.empty_label.place(relx=0.5, rely=0.5, anchor="center")

    def get_nt_len(self):
        sum = len(self.nt_list) + len(self.old_nt_list)
        if sum > 99:
            return 99
        else:
            return sum

    def add_notification(self,message,userID,userName, notification_frame):
        if len(self.nt_list) >= 5:
            old_nt = self.nt_list.pop(0)
            self.old_nt_list.append(old_nt)

        new_notification = Notification(self.mainframe, message, userID, userName, notification_frame)
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

    def deployment(self):
        for widget in self.mainframe.winfo_children():
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

    def hideframe(self):
        # nt.place_forget()
        test = {"code": 00000, "sign": 1, "data": {"message": "안녕하세요", "sender_id": "id1", "sender_name": "박미놘"}}
        self.recv(test)
        print(test)

    def hideframe2(self):
        # nt.place_forget()
        test = {"code": 00000, "sign": 1, "data": {"message": "안녕하세요", "sender_id": "id2", "sender_name": "성진하이"}}
        self.recv(test)
        print(test)

    # def send_(self,dict):
    #     self.root.send_(json.dumps(dict, ensure_ascii=False))

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
        super().__init__(root, width=350, height=70, bg=Color.GRAY )

        self.root = root
        self.userID = userID
        self.mesagge = message
        self.userName = userName
        self.notification_frame = notification_frame

        self.nt_frame = tk.Frame(self, width=70, height=70, bg=Color.GRAY, relief="solid", bd=1)
        self.nt_frame.place(x=0,y=0)
        self.ui_frame = tk.Frame(self, width=280, height=70, bg=Color.GRAY, relief="solid", bd=1)
        self.ui_frame.place(x=70,y=0)
        self.ui_frame.bind("<Button-1>",self.notification_click)
        self.ui_frame.configure(cursor='hand2')

        self.name_label = tk.Label(self.ui_frame, text=userName, font=("godic",15))
        self.name_label.place(x=5,y=5)

        self.mesagge_label = tk.Label(self.ui_frame, text=message)
        self.mesagge_label.place(x=5,y=38)

    def get_id(self):
        return self.userID

    def get_name(self):
        return self.userName

    def notification_click(self,e):
        print("frame click",self.mesagge,self.userID, self.userName)
        self.notification_frame.delete_nt(self.get_id())

if __name__ == "__main__":
    r = tk.Tk()
    r.geometry("1300x700")
    r.config(bg="white")
    nt = NotificationFrame(r)

    def openframe():
        nt.deployment()
        nt.place(x=0, y=0)

    def testdata():
        nt.add_notification("123123", "김동현", "id1")
        nt.add_notification("456456", "성진하", "id2")
        nt.add_notification("789789", "박민환", "id3")
        nt.add_notification("112233", "양승준", "id4")
        nt.add_notification("445566", "최정윤", "id5")
        nt.add_notification("778899", "김태연", "id6")

    def testdata2():
        nt.add_notification("87987", "이윤서", "id7")
        nt.add_notification("523987", "송기윤", "id8")

    def hideframe():
        nt.place_forget()

    test_button = tk.Button(r,text="테스트",command=openframe)
    test_button.pack()
    test_button2 = tk.Button(r,text="데이터추가",command=testdata)
    test_button2.pack()
    test_button3 = tk.Button(r,text="데이터추가2",command=testdata2)
    test_button3.pack()
    test_button4 = tk.Button(r,text="새로고침",command=nt.deployment)
    test_button4.pack()
    test_button5 = tk.Button(r,text="숨기기",command=nt.hideframe)
    test_button5.pack()
    test_button6 = tk.Button(r,text="숨기기",command=nt.hideframe2)
    test_button6.pack()

    r.mainloop()
