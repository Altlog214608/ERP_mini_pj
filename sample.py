import tkinter as tk
import tkinter.messagebox as msgbox

class SampleFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root, width=1300, height=700)
        self.root = root
        
        # frame 생성
        self.frame1 = tk.Frame(self, width=950, height=350, bg="red") # 왼쪽 위 구역
        self.frame2 = tk.Frame(self, width=350, height=350, bg="yellow") # 오른쪽 위 구역
        self.frame3 = tk.Frame(self, width=950, height=350, bg="green") # 왼쪽 아래 구역
        self.frame4 = tk.Frame(self, width=350, height=350, bg="blue") # 오른쪽 아래 구역
        # (frame 3, 4가 하나라면 아래와 같이 사용)
        # self.frame3 = tk.Frame(self, width=1300, height=350, bg="green")  # 아래 구역

        # frame 크기 자동 축소 방지 (pack/grid)
        self.frame1.grid_propagate(False)
        self.frame1.pack_propagate(False)
        self.frame2.grid_propagate(False)
        self.frame2.pack_propagate(False)
        self.frame3.grid_propagate(False)
        self.frame3.pack_propagate(False)
        self.frame4.grid_propagate(False)
        self.frame4.pack_propagate(False)

        # frame 배치
        self.frame1.grid(row=0, column=0)
        self.frame2.grid(row=0, column=1)
        self.frame3.grid(row=1, column=0)
        self.frame4.grid(row=1, column=1)
        # (frame 3, 4가 하나라면 아래와 같이 사용)
        # self.frame3.grid(row=1, column=0, columnspan=2)

        # frame1에 들어갈 것들
        self.test_label1 = tk.Label(self.frame1, text="test1")
        self.test_label1.grid(row=0)

        self.test_entry = tk.Entry(self.frame1)
        self.test_entry.grid(row=1)
        self.test_entry.bind("<Return>", self.test_function)
        
        # frame2에 들어갈 것들
        self.test_label2 = tk.Label(self.frame2, text="test2")
        self.test_label2.place(x=50, y=50)

        # frame3에 들어갈 것들
        self.test_label3 = tk.Label(self.frame3, text="test3")
        self.test_label3.pack()

        # frame4에 들어갈 것들
        self.test_label4 = tk.Label(self.frame4, text="test4")
        self.test_label4.pack()

        self.test_entry2 = tk.Entry(self.frame4)
        self.test_entry2.pack()

    def test_function(self, e):
        msgbox.showinfo("제목", self.test_entry.get())


# 테스트용 코드
if __name__ == "__main__":
    r = tk.Tk()
    r.geometry("1600x900")
    r.config(bg="white")
    fr = SampleFrame(r)
    fr.place(x=300, y=130)
    r.mainloop()