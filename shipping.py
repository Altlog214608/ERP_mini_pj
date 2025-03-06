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
test_columns = ["출고번호","거래처코드","거래처명","출고 담당자","단가","수량","단위","발주번호","생산지시서 코드","자재명","자재코드"]

class Shipping(tk.Frame):
    dbm = dbManager.DBManager(host,user,password,port)

    def __init__(self, root):
        super().__init__(root, width=1300, height=700)
        self.root = root
        self.name = None

        self.frame1 = tk.Frame(self, width=950, height=350, bg="lightgrey")  # 왼쪽 위 구역
        self.frame2 = tk.LabelFrame(self,text="조회 필드",width=350, height=350, bg="lightgrey")  # 오른쪽 위 구역
        self.frame3 = tk.Frame(self, width=1300, height=350, bg="white")  # 아래 구역

        self.frame1.grid_propagate(False)
        self.frame1.pack_propagate(False)
        self.frame2.grid_propagate(False)
        self.frame2.pack_propagate(False)
        self.frame3.grid_propagate(False)
        self.frame3.pack_propagate(False)

        self.frame1.grid(row=0, column=0)
        self.frame2.grid(row=0, column=1)
        self.frame3.grid(row=1, column=0, columnspan=2)

        self.makeDB()
        self.maintable_columns = self.columnDB()
        self.datalist = self.dataDB()
        print(self.maintable_columns)

        # test_data = [[f"Data {r + 1}{chr(65 + c)}" for c in range(len(self.maintable_columns))] for r in range(15)]
        test_data = [[f"{c}" for c in self.datalist[r]] for r in range(len(self.datalist))]

        maintable = TableWidget(self.frame3,
                           data=test_data,
                           col_name=self.maintable_columns,
                           width=1300,
                           height=350)
        maintable.grid(row=0, column=0, columnspan=2, sticky="nsew")

        subtable = TableWidget(self.frame1,
                                data=test_data,
                                col_name=self.maintable_columns,
                                width=950,
                                height=350)
        subtable.grid(row=0, column=0, columnspan=2, sticky="nsew")

        self.tlabel1 = ttk.Label(self.frame2, text="출고 번호")
        self.tentry1 = ttk.Entry(self.frame2)
        self.tlabel2 = ttk.Label(self.frame2, text="거래처 코드")
        self.tentry2 = ttk.Entry(self.frame2)
        self.tlabel3 = ttk.Label(self.frame2, text="자재 코드")
        self.tentry3 = ttk.Entry(self.frame2)
        self.tlabel4 = ttk.Label(self.frame2, text="발주 코드")
        self.tentry4 = ttk.Entry(self.frame2)
        self.tlabel5 = ttk.Label(self.frame2, text="생산지시서코드")
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

        self.test_button = ttk.Button(self.frame2, text= "조회", command=self.check_data)
        self.test_button.grid(row=0, column=2,pady=5)
        self.test_button2 = ttk.Button(self.frame2, text= "출고")
        self.test_button2.grid(row=1, column=2,pady=5)
        self.test_button3 = ttk.Button(self.frame2, text= "생성")
        self.test_button3.grid(row=2, column=2,pady=5)
        self.test_button3 = ttk.Button(self.frame2, text= "저장")
        self.test_button3.grid(row=3, column=2,pady=5)
        self.test_button4 = ttk.Button(self.frame2, text= "수정")
        self.test_button4.grid(row=4, column=2,pady=5)

    def check_data(self): #데이터 조회 버튼
        # frame1 내부에서 row/column 크기 조정 가능하도록 설정
        self.frame1.grid_rowconfigure(0, weight=1)  # 행이 늘어나면 Treeview도 늘어남
        self.frame1.grid_columnconfigure(0, weight=1)  # 열이 늘어나면 Treeview도 늘어남

    def makeDB(self):
        self.dbm.query("use sakila")
        self.dbm.query(
            """
            create table IF NOT EXISTS testShipping(
            shipping_code INT NOT NULL AUTO_INCREMENT,
            production_order char(10) NOT NULL,
            quantity int(10) NOT NULL,
            unit char(10) NOT NULL,
            PRIMARY KEY (shipping_code)
            )""")
        print(self.dbm.query("SHOW TABLES"))
        self.add_column(tableName="testshipping",type="char",size=50,name="material_code",null="NOT")
        self.add_column(tableName="testshipping",type="char",size=50,name="material_name",null="NOT")
        print("생성됨")

    def dataDB(self):
        result = self.dbm.query("SELECT * FROM actor")
        for i in result:
            print(i)
        print(list(result))
        return list(result)
    def columnDB(self):
        # self.dbm.query("USE test;")
        columnlist = []
        result = self.dbm.query("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS where TABLE_SCHEMA = 'sakila' AND TABLE_NAME  = 'actor';")
        for i in result:
            columnlist.append(i[0])
        return columnlist

    def add_column(self, tableName, name, type, size, null=None):
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
    fr = Shipping(r)
    fr.place(x=0, y=0)

    r.mainloop()
