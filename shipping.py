import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as msgbox
import dbManager
import naviframe
from tablewidget import TableWidget
from color import Color


host = "localhost"
user = "root"
password = "0000"
port = 3306
shipping_columns = {
    "출고 번호": "shipping_code",
    "생산지시서 코드": "production_order",
    "발주 코드": "order_code",
    "거래처 코드": "client_code",
    "거래처 명": "client_name",
    "수량": "quantity",
    "단위": "unit",
    "판매 가격": "selling_amount",
    "부가세액": "vat_amount",
    "판매 가격 단위": "selling_price_unit",
    "총액": "total_amount",
    "자재 코드": "material_code",
    "자재 명": "material_name",
    "출고 구분": "delivery_category",
    "납품 장소": "delivery_location",
    "출고 담당자": "shipping_responsibility",
    "날짜": "date",
    "창고": "warehouse",
    "판매 코드": "sales_order_number"
}
receiving_columns = {
    "입고 번호": "receiving_code",
    "생산지시서 코드": "production_order",
    "거래처 코드": "client_code",
    "거래처 명": "client_name",
    "수량": "quantity",
    "단위": "unit",
    "자재 코드": "material_code",
    "자재 명": "material_name",
    "발주 코드": "order_code",
    "날짜": "date",
    "입고 창고": "receiving_warehouse",
    "입고 담당자": "receiving_responsibility",
    "입고 구분": "receiving_classification"
}

dbm = dbManager.DBManager(host,user,password,port)

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
        self.main_table_columns = self.get_columns("shipping")#테이블 이름에 맞는 컬럼명 추출
        # test = []
        # for i in shipping_columns.keys():
        #     test.append(i)
        # self.main_table_columns = test
        self.sub_table_columns = self.get_columns("order_form")
        self.main_datalist = self.get_all_data("shipping") #테이블 이름에 맞는 데이터 추출
        self.sub_datalist = self.get_all_data("order_form")
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
        self.tentry1 = ttk.Entry(self.frame2, textvariable=shipping_columns.get("발주 코드"))
        self.tlabel2 = ttk.Label(self.frame2, text="거래처 코드")
        self.tentry2 = ttk.Entry(self.frame2, textvariable=shipping_columns.get("거래처 코드"))
        self.tentry2.bind("<F2>",lambda e:self.onkey())
        self.tlabel3 = ttk.Label(self.frame2, text="자재 코드")
        self.tentry3 = ttk.Entry(self.frame2, textvariable=shipping_columns.get("자재 코드"))
        self.tlabel4 = ttk.Label(self.frame2, text="출고 번호")
        self.tentry4 = ttk.Entry(self.frame2, textvariable=shipping_columns.get("출고 번호"))
        self.tlabel5 = ttk.Label(self.frame2, text="생산지시서 코드")
        self.tentry5 = ttk.Entry(self.frame2, textvariable=shipping_columns.get("생산지시서 코드"))

        self.entry_list = [self.tentry1,self.tentry2,self.tentry3,self.tentry4]

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
        self.test_button2 = ttk.Button(self.frame2, text= "출고", command=self.shipping_process)
        self.test_button2.grid(row=1, column=2,pady=5)
        self.test_button3 = ttk.Button(self.frame2, text= "생성")
        self.test_button3.grid(row=2, column=2,pady=5)
        self.test_button3 = ttk.Button(self.frame2, text= "저장")
        self.test_button3.grid(row=3, column=2,pady=5)
        self.test_button4 = ttk.Button(self.frame2, text= "수정")
        self.test_button4.grid(row=4, column=2,pady=5)

    def onkey(self):

        # 테이블에 들어갈 데이터 // db에서 데이터를 불러와 [[],[],[]] 이중배열로 가공해서 넣기
        data = [['00001', '(주)이상한과자가게전천당', '123-12-45678', '성진하'],
                ['00002', '이상한과자가게전천당', '123-12-45678', '성진하'],
                ['00003', '(주)아크라시아사탕가게', '457-34-44587', '박미나니'],
                ['00025', '엘가시아과자가게', '942-34-47898', '김니나브'],
                ['00284', '신창섭의극극극성비가게', '766-56-10957', '신창섭'],
                ['09876', '만능고물상', '186-78-05957', '몽땅따']
                ]

        # 테이블 위젯을 만들때 필요한 정보
        naviData = {"검색유형": ['거래처코드', '거래처명'],  # 검색기준 설정 []안의 내용만 바꾸면 됨, 단 col_name에 있는 것이어야함.
                    "data": data,  # 위에서 불러온 데이터
                    "col_name": ['거래처코드', '거래처명', '사업자등록번호', '대표자 성명'],  # 컬럼 이름
                    "col_width": [80, 220, 125, 101],  # 컬럼별 사이즈
                    "col_align": ['center', 'left', 'center', 'center']  # 컬럼별 정렬 기준
                    }

        # 생성자
        fr = naviframe.NaviFrame(self.root,  # 최상위 프레임
                                 naviData,  # 위에서 작성한 테이블 위젯 생성시에 필요한 정보
                                 {
                                     # 1:1 대응 // self.bkClientEnt 위치에는 '거래처코드' 값이 들어가고, self.bkClientContent 위치에는 '거래처명'이 들어감
                                     "entry": [self.tentry2],  # 테이블 행 선택시 정보가 들어갈 엔트리박스 변수명
                                     "key": ["거래처코드"]},  # 선택한 테이블 행의 데이터중 얻을 값 ( 컬럼 이름 적으면 됨 )
                                 x=100,  # 코드 검색창 뜰 위치 좌표 X값 // 미입력시 디폴트값 x=700
                                 y=180,  # 코드 검색창 뜰 위치 좌표 Y값 // 미입력시 디폴트값 y=180
                                 width=602)  # 코드 검색창 가로사이즈 ( 세로사이즈는 고정임 ) // 미입력시 디폴트값 width=602
        # 배치
        fr.place(x=500, y=300)

    def check_data(self): #데이터 조회 버튼
        text_list = []

        if self.tentry1.get() or self.tentry2.get() or self.tentry3.get() or self.tentry4.get() or self.tentry5.get():
            if self.tentry1.get():
                self.sub_table.draw_table()
                target = self.tentry1.get()
                self.tentry1.delete(0, tk.END)
                send_dict = {"order_code":target}
                recv_dict = f20701(dict=send_dict)
                key, value = recv_dict.items()
                print(key)
                print(value)
                self.sub_datalist = value[1]
                self.sub_data = [[f"{c}" for c in self.sub_datalist[r]] for r in range(len(self.sub_datalist))]
                self.sub_table_columns = self.get_columns("order_form")
                self.sub_table.from_data(data=self.sub_data, col_name=self.sub_table_columns,
                                         col_width=[130 for _ in range(len(self.sub_table_columns))])  # 데이터 갱신
                self.sub_table.draw_table()

            elif self.tentry2.get():
                self.main_table.draw_table()
                target = self.tentry2.get()
                self.tentry2.delete(0, tk.END)
                send_dict = {self.tentry2.cget("textvariable"): target}
                recv_dict = f20701(dict=send_dict)
                key, value = recv_dict.items()
                # self.main_datalist = self.dbm.query(f"SELECT * FROM shipping where client_code = '{target}'")
                self.main_datalist = value[1]
                self.main_data = [[f"{c}" for c in self.main_datalist[r]] for r in range(len(self.main_datalist))]
                self.main_table_columns = self.get_columns("shipping")
                self.main_table.from_data(data=self.main_data, col_name=self.main_table_columns,col_width=[130 for _ in range(len(self.main_table_columns))])
                self.main_table.draw_table()

            elif self.tentry3.get():
                self.main_table.draw_table()
                target = self.tentry3.get()
                self.tentry3.delete(0, tk.END)
                send_dict = {self.tentry3.cget("textvariable"): target}
                recv_dict = f20701(dict=send_dict)
                key, value = recv_dict.items()
                self.main_datalist = value[1]
                # self.main_datalist = self.dbm.query(f"SELECT * FROM shipping where material_code = '{target}'")
                self.main_data = [[f"{c}" for c in self.main_datalist[r]] for r in range(len(self.main_datalist))]
                self.main_table_columns = self.get_columns("shipping")
                self.main_table.from_data(data=self.main_data, col_name=self.main_table_columns,col_width=[130 for _ in range(len(self.main_table_columns))])
                self.main_table.draw_table()

            elif self.tentry4.get():
                self.main_table.draw_table()
                target = self.tentry4.get()
                self.tentry4.delete(0, tk.END)
                send_dict = {self.tentry4.cget("textvariable"): target}
                recv_dict = f20701(dict=send_dict)
                key, value = recv_dict.items()
                self.main_datalist = value[1]
                self.main_data = [[f"{c}" for c in self.main_datalist[r]] for r in range(len(self.main_datalist))]
                self.main_table_columns = self.get_columns("shipping")
                self.main_table.from_data(data=self.main_data, col_name=self.main_table_columns,col_width=[130 for _ in range(len(self.main_table_columns))])
                self.main_table.draw_table()

            elif self.tentry5.get():
                self.main_table.draw_table()
                target = self.tentry5.get()
                self.tentry5.delete(0, tk.END)
                send_dict = {self.tentry5.cget("textvariable"): target}
                recv_dict = f20701(dict=send_dict)
                key, value = recv_dict.items()
                self.main_datalist = value[1]
                self.main_data = [[f"{c}" for c in self.main_datalist[r]] for r in range(len(self.main_datalist))]
                self.main_table_columns = self.get_columns("shipping")
                self.main_table.from_data(data=self.main_data, col_name=self.main_table_columns,col_width=[130 for _ in range(len(self.main_table_columns))])
                self.main_table.draw_table()
            else:
                print("선택값 없음")

    def make_table(self):
        self.dbm.query("use test")
        # self.dbm.query(
        #     """
        #     create table IF NOT EXISTS testShipping(
        #     shipping_code INT NOT NULL AUTO_INCREMENT,
        #     production_order char(10) NOT NULL,
        #     quantity int(10) NOT NULL,
        #     unit char(10) NOT NULL,
        #     PRIMARY KEY (shipping_code)
        #     )""")
        print(self.dbm.query("SHOW TABLES"))
        # self.add_column(tableName="testshipping",type="char",size=50,name="material_code",null="NOT")
        # self.add_column(tableName="testshipping",type="char",size=50,name="material_name",null="NOT")
        print("생성됨")

    def get_all_data(self, tablename):
        result = self.dbm.query(f"SELECT * FROM {tablename}")
        return list(result)

    def get_columns(self, tablename):
        self.dbm.query("USE test;")
        columnlist = []
        result = self.dbm.query(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS where TABLE_SCHEMA = 'test' AND TABLE_NAME  = '{tablename}' ORDER BY ORDINAL_POSITION;")
        print(result)
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

    def shipping_process(self):
        a = self.dbm.query(f"""
                SELECT 
                o.order_code,        -- 발주 코드
                o.order_id,          -- order_id
                m.mo_code,           -- 생산지시서 코드
                s.shipping_code,       -- 출고 번호
                s.quantity,          -- 수량
                t.material_Code,     -- 자재 코드
                t.material_Name,     -- 자재 명
                t.unit,              -- 단위
                t.price,             -- 가격
                CURDATE() AS order_date  -- 오늘 날짜
                FROM order_form o
                LEFT JOIN mo m ON o.order_code = m.order_code        -- 생산지시서 조인
                LEFT JOIN shipping s ON o.order_code = s.order_code  -- 출고 정보 조인
                LEFT JOIN materialTable t ON s.material_Code = t.material_Code  -- 자재 정보 조인
                WHERE o.order_code = 'ord003';  -- 특정 발주 코드 조회
        """)
        print(a)
        # print(self.check_main_data())
        # print(self.check_sub_data())

    def check_main_data(self):
        print(f"data: {self.main_table.data}")  # 저장된 데이터
        print(f"rows cols: {self.main_table.rows} {self.main_table.cols}")  # 행 열 개수
        print(f"selected: {self.main_table.selected_row} {self.main_table.selected_col}")  # 선택된 행 열 index
        print(f"changed {self.main_table.changed}")

    def check_sub_data(self):
        print(f"data: {self.sub_table.data}")  # 저장된 데이터
        print(f"rows cols: {self.sub_table.rows} {self.sub_table.cols}")  # 행 열 개수
        print(f"selected: {self.sub_table.selected_row} {self.sub_table.selected_col}")  # 선택된 행 열 index
        print(f"changed {self.sub_table.changed}")  # 원본 대비 변경된 데이터

def f20701(**kwargs):
    result_dict = {}
    data_dict= kwargs.get("dict")

    for key, value in data_dict.items():
        if key == "order_code":
            result = dbm.query(f"SELECT * FROM order_form where {key} = '{value}';")
        else:
            result = dbm.query(f"SELECT * FROM shipping where {key} = '{value}';")

    if result:
        result_dict = {"sign": 1, "data": list(result)}
    else:
        result_dict = {"sign": 0, "data": None}

    return result_dict

if __name__ == "__main__":
    r = tk.Tk()
    r.geometry("1300x700")
    r.config(bg="white")
    fr = Shipping(r)
    fr.place(x=0, y=0)

    r.bind("<F5>", lambda e: Shipping.check_main_data(fr))
    r.bind("<F6>", lambda e: Shipping.check_sub_data(fr))

    r.mainloop()
