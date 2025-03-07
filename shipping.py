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

        self.frame1 = tk.Frame(self, width=950, height=350, bg=Color.GRAY)  # 왼쪽 위 구역
        self.frame2 = tk.LabelFrame(self,text="조회 필드",width=350, height=350, bg=Color.GRAY)  # 오른쪽 위 구역
        self.frame3 = tk.Frame(self, width=1300, height=350, bg=Color.WHITE)  # 아래 구역

        self.frame1.grid_propagate(False)
        self.frame1.pack_propagate(False)
        self.frame2.grid_propagate(False)
        self.frame2.pack_propagate(False)
        self.frame3.grid_propagate(False)
        self.frame3.pack_propagate(False)

        self.frame1.grid(row=0, column=0)
        self.frame2.grid(row=0, column=1)
        self.frame3.grid(row=1, column=0, columnspan=2)

        self.make_table() #table생성
        self.main_table_columns = self.get_columns("shipping") #테이블 이름에 맞는 컬럼명 추출
        self.sub_table_columns = self.get_columns("purchase_orders")
        self.main_datalist = self.get_all_data("shipping") #테이블 이름에 맞는 데이터 추출
        self.sub_datalist = self.get_all_data("purchase_orders")
        print(self.main_table_columns)
        self.main_data = []
        self.sub_data = []
        # 메인 데이터 담기
        self.main_data = [[f"{c}" for c in self.main_datalist[r]] for r in range(len(self.main_datalist))]

        #메인 프레임
        self.main_table = TableWidget(self.frame3,
                                      data=self.main_data,
                                      col_name=self.main_table_columns,
                                      col_width=[130 for _ in range(len(self.main_table_columns))],  # 열 너비(순서대로, 데이터 열 개수와 맞게)
                                      width=1300,
                                      height=350)
        self.main_table.grid(row=0, column=0, columnspan=2, sticky="nsew")

        self.main_scrollbar = ttk.Scrollbar(self.frame3, orient="horizontal", command=self.main_table.canvas.xview)
        self.main_scrollbar.pack(side="bottom",fill="x")
        self.main_table.canvas.configure(xscrollcommand=self.main_scrollbar.set)

        # 서브 데이터 담기
        # self.sub_data = [[f"{c}" for c in self.sub_datalist[r]] for r in range(len(self.sub_datalist))]
        # self.sub_data = [[f"" for c in range(len(self.sub_table_columns))] for r in range(len(self.sub_datalist))]
        self.sub_data = [[f"" for c in range(len(self.sub_table_columns))] for r in range(1)]
        # 서브 프레임
        self.sub_table = TableWidget(self.frame1,
                                     data=self.sub_data,
                                     col_name=self.sub_table_columns,
                                     col_width=[130 for _ in range(len(self.sub_table_columns))],
                                     width=950,
                                     height=350)
        self.sub_table.grid(row=0, column=0, columnspan=2, sticky="nsew")

        self.sub_scrollbar = ttk.Scrollbar(self.frame1, orient="horizontal", command=self.sub_table.canvas.xview)
        self.sub_scrollbar.pack(side="bottom", fill="x")
        self.sub_table.canvas.configure(xscrollcommand=self.sub_scrollbar.set)
        #조회 필드 위젯
        self.tlabel1 = ttk.Label(self.frame2, text="발주 코드")
        self.tentry1 = ttk.Entry(self.frame2)
        self.tlabel2 = ttk.Label(self.frame2, text="거래처 코드")
        self.tentry2 = ttk.Entry(self.frame2)
        self.tlabel3 = ttk.Label(self.frame2, text="자재 코드")
        self.tentry3 = ttk.Entry(self.frame2)
        self.tlabel4 = ttk.Label(self.frame2, text="출고 번호")
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
        # self.main_table.draw_table()
        # target = self.tentry1.get()
        # self.tentry1.delete(0, tk.END)
        # self.main_datalist = self.dbm.query(f"SELECT * FROM shipping where purchase_order_code = '{target}'")
        # self.main_data = [[f"{c}" for c in self.main_datalist[r]] for r in range(len(self.main_datalist))]
        # self.main_table_columns = self.get_columns("shipping")
        # self.main_table.from_data(data=self.main_data, col_name=self.main_table_columns,col_width=[130 for _ in range(len(self.sub_table_columns))])  # 데이터 갱신
        # self.main_table.draw_table()

        self.sub_table.draw_table()
        target = self.tentry1.get()
        self.tentry1.delete(0, tk.END)
        self.sub_datalist = self.dbm.query(f"SELECT * FROM purchase_orders where purchase_order_code = '{target}'")
        self.sub_data = [[f"{c}" for c in self.sub_datalist[r]] for r in range(len(self.sub_datalist))]
        self.sub_table_columns = self.get_columns("purchase_orders")
        self.sub_table.from_data(data=self.sub_data, col_name=self.sub_table_columns,col_width=[130 for _ in range(len(self.sub_table_columns))])  # 데이터 갱신
        self.sub_table.draw_table()

    def make_table(self):
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

    def get_all_data(self, tablename):
        result = self.dbm.query(f"SELECT * FROM {tablename}")
        return list(result)

    def get_columns(self, tablename):
        # self.dbm.query("USE test;")
        columnlist = []
        result = self.dbm.query(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS where TABLE_SCHEMA = 'sakila' AND TABLE_NAME  = '{tablename}' ORDER BY ORDINAL_POSITION;")
        print(result)
        for i in result:
            columnlist.append(i[0])
        # columnlist.sort()
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

    def test(self):
        print(f"data: {self.main_table.data}")  # 저장된 데이터
        print(f"rows cols: {self.main_table.rows} {self.main_table.cols}")  # 행 열 개수
        print(f"selected: {self.main_table.selected_row} {self.main_table.selected_col}")  # 선택된 행 열 index
        print(f"changed {self.main_table.changed}")  # 원본 대비 변경된 데이터

if __name__ == "__main__":
    r = tk.Tk()
    r.geometry("1300x700")
    r.config(bg="white")
    fr = Shipping(r)
    fr.place(x=0, y=0)

    r.bind("<F5>", lambda e: Shipping.test(fr))

    r.mainloop()
