import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as msgbox

test_columns = ["입고번호","거래처코드","거래처명","입고 담당자","거래처명","거래처명","거래처명","거래처명","거래처명","거래처명","거래처명","거래처명","거래처명","거래처명","거래처명","거래처명"]


class Receiving(tk.Frame):
    def __init__(self, root):
        super().__init__(root, width=1300, height=700)
        self.root = root

        self.frame1 = tk.LabelFrame(self, text="입력 필드",width=950, height=350, bg="lightgrey")  # 왼쪽 위 구역
        self.frame2 = tk.LabelFrame(self,text="조회 필드",width=350, height=350, bg="lightgrey")  # 오른쪽 위 구역
        # self.frame3 = tk.Frame(self, width=950, height=350, bg="green")  # 왼쪽 아래 구역
        # self.frame4 = tk.Frame(self, width=350, height=350, bg="blue")  # 오른쪽 아래 구역
        # (frame 3, 4가 하나라면 아래와 같이 사용)
        self.frame3 = tk.Frame(self, width=1300, height=350, bg="white")  # 아래 구역
        # self.label=tk.Label(self.frame_top,text="123")
        # self.label= self.label.pack()

        self.testframe = tk.Frame(self.frame2,width=250,height=350, bg="lightgrey")
        self.testframe2 = tk.Frame(self.frame2,width=100,height=350, bg="lightgrey")
        # self.testlabelframe = tk.LabelFrame(self.frame1,width=)
        # frame 크기 자동 축소 방지 (pack/grid)
        self.frame1.grid_propagate(False)
        self.frame1.pack_propagate(False)
        self.frame2.grid_propagate(False)
        self.frame2.pack_propagate(False)
        self.frame3.grid_propagate(False)
        self.frame3.pack_propagate(False)
        # self.frame4.grid_propagate(False)
        # self.frame4.pack_propagate(False)

        # frame 배치
        self.frame1.grid(row=0, column=0)
        self.frame2.grid(row=0, column=1)
        # self.frame3.grid(row=1, column=0)
        # self.frame4.grid(row=1, column=1)
        # (frame 3, 4가 하나라면 아래와 같이 사용)
        self.frame3.grid(row=1, column=0, columnspan=2)

        self.testframe.grid(row=0, column=0)
        self.testframe.place(x=0,y=0)
        self.testframe2.grid(row=0, column=1)
        self.testframe2.place(x=250,y=0)

        #생성, 신규 필드 테스트용 엔트리
        self.label1 = ttk.Label(self.frame1, text="테스트용 라벨")
        self.entry1 = ttk.Entry(self.frame1)

        self.label2 = ttk.Label(self.frame1, text="테스트용 라벨")
        self.entry2 = ttk.Entry(self.frame1)

        self.label3 = ttk.Label(self.frame1, text="테스트용 라벨")
        self.entry3 = ttk.Entry(self.frame1)

        self.label4 = ttk.Label(self.frame1, text="테스트용 라벨")
        self.entry4 = ttk.Entry(self.frame1)

        self.label5 = ttk.Label(self.frame1, text="테스트용 라벨")
        self.entry5 = ttk.Entry(self.frame1)

        self.label6 = ttk.Label(self.frame1, text="테스트용 라벨")
        self.entry6 = ttk.Entry(self.frame1)

        self.label7 = ttk.Label(self.frame1, text="테스트용 라벨")
        self.entry7 = ttk.Entry(self.frame1)

        self.label8 = ttk.Label(self.frame1, text="테스트용 라벨")
        self.entry8 = ttk.Entry(self.frame1)

        self.label9 = ttk.Label(self.frame1, text="테스트용 라벨")
        self.entry9 = ttk.Entry(self.frame1)

        self.label10 = ttk.Label(self.frame1, text="테스트용 라벨")
        self.entry10 = ttk.Entry(self.frame1)

        self.label11 = ttk.Label(self.frame1, text="테스트용 라벨")
        self.entry11 = ttk.Entry(self.frame1)

        # 조회 필드 테스트용 엔트리
        self.tlabel1 = ttk.Label(self.testframe, text="테스트용 라벨")
        self.tentry1 = ttk.Entry(self.testframe)

        self.tlabel2 = ttk.Label(self.testframe, text="테스트용 라벨")
        self.tentry2 = ttk.Entry(self.testframe)

        self.tlabel3 = ttk.Label(self.testframe, text="테스트용 라벨")
        self.tentry3 = ttk.Entry(self.testframe)

        self.tlabel4 = ttk.Label(self.testframe, text="테스트용 라벨")
        self.tentry4 = ttk.Entry(self.testframe)

        self.tlabel5 = ttk.Label(self.testframe, text="테스트용 라벨")
        self.tentry5 = ttk.Entry(self.testframe)

        #생성, 신규 필드 테스트용 엔트리 배치
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        self.entry1.grid(row=0, column=1, padx=10, pady=10)

        self.label2.grid(row=1, column=0, padx=10, pady=10)
        self.entry2.grid(row=1, column=1, padx=10, pady=10)

        self.label3.grid(row=2, column=0, padx=10, pady=10)
        self.entry3.grid(row=2, column=1, padx=10, pady=10)

        self.label4.grid(row=3, column=0, padx=10, pady=10)
        self.entry4.grid(row=3, column=1, padx=10, pady=10)

        self.label5.grid(row=4, column=0, padx=10, pady=10)
        self.entry5.grid(row=4, column=1, padx=10, pady=10)

        self.label6.grid(row=5, column=0, padx=10, pady=10)
        self.entry6.grid(row=5, column=1, padx=10, pady=10)

        self.label7.grid(row=6, column=0, padx=10, pady=10)
        self.entry7.grid(row=6, column=1, padx=10, pady=10)

        self.label8.grid(row=7, column=0, padx=10, pady=10)
        self.entry8.grid(row=7, column=1, padx=10, pady=10)

        self.label9.grid(row=0, column=2, padx=10, pady=10)
        self.entry9.grid(row=0, column=3, padx=10, pady=10)

        self.label10.grid(row=1, column=2, padx=10, pady=10)
        self.entry10.grid(row=1, column=3, padx=10, pady=10)

        self.label11.grid(row=2, column=2, padx=10, pady=10)
        self.entry11.grid(row=2, column=3, padx=10, pady=10)

        #조회 필드 테스트용 엔트리 배치
        self.tlabel1.grid(row=0, column=0, padx=5, pady=5)
        self.tentry1.grid(row=0, column=1, padx=5, pady=5)

        self.tlabel2.grid(row=1, column=0, padx=5, pady=5)
        self.tentry2.grid(row=1, column=1, padx=5, pady=5)

        self.tlabel3.grid(row=2, column=0, padx=5, pady=5)
        self.tentry3.grid(row=2, column=1, padx=5, pady=5)

        self.tlabel4.grid(row=3, column=0, padx=5, pady=5)
        self.tentry4.grid(row=3, column=1, padx=5, pady=5)

        self.tlabel5.grid(row=4, column=0, padx=5, pady=5)
        self.tentry5.grid(row=4, column=1, padx=5, pady=5)


        # CRUD 버튼
        self.test_button = ttk.Button(self.testframe2, text= "조회")
        self.test_button.grid(row=0, column=1,pady=5)
        # self.test_button.place(y=5)

        self.test_button2 = ttk.Button(self.testframe2, text= "신규")
        self.test_button2.grid(row=1, column=1,pady=5)
        # self.test_button2.place(x=10,y=60)

        self.test_button3 = ttk.Button(self.testframe2, text= "생성")
        self.test_button3.grid(row=2, column=1,pady=5)
        # self.test_button3.place(x=10,y=100)
        
        self.test_button3 = ttk.Button(self.testframe2, text= "저장")
        self.test_button3.grid(row=3, column=1,pady=5)
        # self.test_button3.place(x=10,y=140)
        #
        # self.test_treeview = ttk.Treeview(self.frame3, columns=test_columns,displaycolumns=test_columns)
        # self.test_treeview.grid(row=0, column=0)
        #
        # self.test_treeview.column("입고번호", width=1000, anchor="center")
        # self.test_treeview.heading("입고번호", text="입고번호", anchor="center")
        #
        # self.scrollbar = ttk.Scrollbar(self.frame3, orient="horizontal", command=self.test_treeview.xview())
        # self.scrollbar.pack(side="bottom", fill="x")
        # self.test_treeview.configure(xscrollcommand=self.scrollbar.set)
    #
    # def


if __name__ == "__main__":
    r = tk.Tk()
    r.geometry("1300x700")
    r.config(bg="white")
    fr = Receiving(r)
    fr.place(x=0, y=0)
    r.mainloop()