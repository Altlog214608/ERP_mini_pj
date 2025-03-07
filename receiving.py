import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as msgbox
import dbManager
from tablewidget import TableWidget
from color import Color


host = "localhost"
user = "root"
password = "0000"
port = 3306
test_columns = ["입고번호","거래처코드","거래처명","입고 담당자","단가","수량","단위","발주번호","생산지시서 코드","자재명","자재코드"]

class Receiving(tk.Frame):
    dbm = dbManager.DBManager(host,user,password,port)

    def __init__(self, root):
        super().__init__(root, width=1300, height=700)
        self.root = root

        self.frame1 = tk.Frame(self, width=950, height=350, bg=Color.GRAY)  # 왼쪽 위 구역
        self.frame2 = tk.LabelFrame(self,text="조회 필드",width=350, height=350, bg=Color.GRAY)  # 오른쪽 위 구역
        # (frame 3, 4가 하나라면 아래와 같이 사용)
        self.frame3 = tk.Frame(self, width=1300, height=350, bg=Color.WHITE)  # 아래 구역

        # self.frame2 = tk.Frame(self.frame2, width=250, height=350, bg="lightgrey")
        # self.testframe2 = tk.Frame(self.frame2,width=100,height=350, bg="lightgrey")
        # frame 크기 자동 축소 방지 (pack/grid)
        self.frame1.grid_propagate(False)
        self.frame1.pack_propagate(False)
        self.frame2.grid_propagate(False)
        self.frame2.pack_propagate(False)
        self.frame3.grid_propagate(False)
        self.frame3.pack_propagate(False)

        # frame 배치
        self.frame1.grid(row=0, column=0)
        self.frame2.grid(row=0, column=1)
        self.frame3.grid(row=1, column=0, columnspan=2)

        # self.frame2.grid(row=0, column=0)
        # self.frame2.place(x=0, y=0)
        # self.testframe2.grid(row=0, column=1)
        # self.testframe2.place(x=250,y=0)

        self.makeDB()
        self.maintable_columns = self.columnDB()
        print(self.maintable_columns)

        self.maindata = []
        self.subdata = []

        self.maindata = [[f"Data {r + 1}{chr(65 + c)}" for c in range(6)] for r in range(15)]  # 임의의 데이터

        maintable = TableWidget(self.frame3,
                           data=self.maindata,
                           col_name=self.maintable_columns,  # 열 이름(순서대로, 데이터 열 개수와 맞게)
                           # col_width=[325, 325, 325, 325],  # 열 너비(순서대로, 데이터 열 개수와 맞게)
                           width=1300,  # 테이블 그려질 너비
                           height=350)  # 테이블 그려질 높이
        # col_width 생략 시 크기에 맞게 분배
        # col_name 생략 시 Col1, Col2, ... 지정

        maintable.grid(row=0, column=0, columnspan=2, sticky="nsew")

        self.subdata = [[f"" for _ in range(6)] for _ in range(15)]  # 임의의 데이터

        subtable = TableWidget(self.frame1,
                                data=self.subdata,
                                col_name=self.maintable_columns,  # 열 이름(순서대로, 데이터 열 개수와 맞게)
                                # col_width=[325, 325, 325, 325],  # 열 너비(순서대로, 데이터 열 개수와 맞게)
                                width=950,  # 테이블 그려질 너비
                                height=350)  # 테이블 그려질 높이
        # col_width 생략 시 크기에 맞게 분배
        # col_name 생략 시 Col1, Col2, ... 지정

        subtable.grid(row=0, column=0, columnspan=2, sticky="nsew")


        # 조회 필드 테스트용 엔트리
        self.tlabel1 = ttk.Label(self.frame2, text="입고 번호")
        self.tentry1 = ttk.Entry(self.frame2)

        self.tlabel2 = ttk.Label(self.frame2, text="거래처 코드")
        self.tentry2 = ttk.Entry(self.frame2)

        self.tlabel3 = ttk.Label(self.frame2, text="자재 코드")
        self.tentry3 = ttk.Entry(self.frame2)

        self.tlabel4 = ttk.Label(self.frame2, text="발주 번호")
        self.tentry4 = ttk.Entry(self.frame2)

        self.tlabel5 = ttk.Label(self.frame2, text="품목명")
        self.tentry5 = ttk.Entry(self.frame2)

        self.tlabel1.grid(row=0, column=0, padx=5, pady=10)
        self.tentry1.grid(row=0, column=1, padx=5, pady=10)
        self.tlabel2.grid(row=1, column=0, padx=5, pady=10)
        self.tentry2.grid(row=1, column=1, padx=5, pady=10)
        self.tlabel3.grid(row=2, column=0, padx=5, pady=10)
        self.tentry3.grid(row=2, column=1, padx=5, pady=10)
        self.tlabel4.grid(row=3, column=0, padx=5, pady=10)
        self.tentry4.grid(row=3, column=1, padx=5, pady=10)
        self.tlabel5.grid(row=4, column=0, padx=5, pady=10)
        self.tentry5.grid(row=4, column=1, padx=5, pady=10)

        self.test_button = ttk.Button(self.frame2, text="조회", command=self.check_data)
        self.test_button.grid(row=0, column=2, pady=5)
        self.test_button2 = ttk.Button(self.frame2, text="입고")
        self.test_button2.grid(row=1, column=2, pady=5)
        self.test_button3 = ttk.Button(self.frame2, text="생성")
        self.test_button3.grid(row=2, column=2, pady=5)
        self.test_button3 = ttk.Button(self.frame2, text="저장")
        self.test_button3.grid(row=3, column=2, pady=5)
        self.test_button4 = ttk.Button(self.frame2, text="수정")
        self.test_button4.grid(row=4, column=2, pady=5)


    def check_data(self): #데이터 조회 버튼
        print(self.tentry1.get())
        self.tentry1.delete(0,tk.END)

    def makeDB(self):
        self.dbm.query("use test")
        self.dbm.query(
            """
            create table IF NOT EXISTS testReceiving(
            receiving_code INT NOT NULL AUTO_INCREMENT,
            production_order char(10) NOT NULL,
            quantity int(10) NOT NULL,
            unit char(10) NOT NULL,
            PRIMARY KEY (receiving_code)
            )"""
        )
        print(self.dbm.query("SHOW TABLES"))
        self.add_column(tableName="testreceiving",type="char",size=50,name="material_code",null="NOT")
        self.add_column(tableName="testreceiving",type="char",size=50,name="material_name",null="NOT")
        print("생성됨")

    def columnDB(self):
        print("컬럼뽑기")
        self.dbm.query("USE test;")
        columnlist = []
        result = self.dbm.query("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS where TABLE_SCHEMA = 'test' AND TABLE_NAME  = 'testreceiving';")
        for i in result:
            columnlist.append(i[0])
        return columnlist

    def add_column(self,tableName,name,type,size,null=None):
        check_column = self.dbm.query(f"""
        
        SELECT COUNT(*)
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_SCHEMA = 'test' 
        AND TABLE_NAME = '{tableName}' 
        AND COLUMN_NAME = '{name}';
        """
                                      )
        print("---에드컬럼 체크")
        print(check_column)
        print("---에드컬럼 체크")
        if check_column[0][0] == 0:
            if "NOT" in null:
                self.dbm.query(f"ALTER TABLE {tableName} ADD COLUMN {name} {type}({size}) NOT NULL")
                print(f"낫 널 {name}컬럼 추가")
            else:
                self.dbm.query(f"ALTER TABLE {tableName} ADD COLUMN {name} {type}({size})")
                print(f"{name}컬럼 추가")
        else:
            print("이미 존재하는 컬럼")






if __name__ == "__main__":
    r = tk.Tk()
    r.geometry("1300x700")
    r.config(bg="white")
    fr = Receiving(r)
    fr.place(x=0, y=0)

    r.mainloop()