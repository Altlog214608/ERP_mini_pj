# `account_name` VARCHAR(45) NULL DEFAULT NULL, 과목
# `jr_dr` VARCHAR(14) NULL DEFAULT '0', 차변
# `jr_cr` VARCHAR(14) NULL DEFAULT '0', 대변
# 빈데이터가 왔을때의 처리 ,그냥 조회만 눌렀을때 처리  1,2번 파일
# 두개 코드 합치기 send_data하나만 보내주기

# 계정과목 테이블(accountsubject)에서 account_type컬럼 값이 자산,부채 자본인 account_name을 가져온다.
# 분개 테이블(accountbook)에서 설정날짜 기간안에 전표승인이(bk_approval_state) 승인처리 되어있는 전표아이디(bk_id) 조회
# 전표 테이블(journalizingbook)에서 전표아이디(bk_id)를 조회하여 account_name(과목별로group by) , 차변(jr_cr) 대변(jr_dr)


# 조회된 분개들을 계정과목별 총 합계를 구함 ( dr 합계(차변), cr합계(대변) )
# 분개 테이블 조회하기 전에 accountbook과 accountsubject를
#

# 재무상태표 : 자산(왼쪽), 부채 자본 (오른쪽)
# 손익계산서 : 비용(왼쪽), 수익(오른쪽)

# import pymysql
import tkinter as tk
from tkcalendar import Calendar
from tablewidget import TableWidget, ColName
from color import Color
import datetime
# import dbManager
import json
import math


class Financial_statement(tk.Frame):  # 재무제표
    def __init__(self, root):
        super().__init__(root, width=1300, height=700)
        self.root = root
        self.cal = None
        self.table_data = []  # 조회 데이터 담을 리스트
        self.select = None

        # self.db_data = None #전표 승인 조회

        # frame 생성
        self.frame1 = tk.Frame(self, width=950, height=700, )
        self.frame2 = tk.Frame(self, width=350, height=350, )
        self.frame4 = tk.Frame(self, width=350, height=350, )

        # frame 크기 자동 축소 방지 (pack/grid)
        self.frame1.grid_propagate(False)
        self.frame1.pack_propagate(False)
        self.frame2.grid_propagate(False)
        self.frame2.pack_propagate(False)
        self.frame4.grid_propagate(False)
        self.frame4.pack_propagate(False)

        # frame 배치
        self.frame1.grid(row=0, column=0, rowspan=2)
        self.frame2.grid(row=0, column=1)
        self.frame4.grid(row=1, column=1)

        # 초기 테이블
        self.create_table()

        # frame2에 들어갈 위젯들
        self.test_label1 = tk.Label(self.frame2, text="기준일자")
        self.test_label1.place(x=0, y=0)

        self.test_ent1 = tk.Entry(self.frame2, width=10)
        self.test_ent1.place(x=60, y=0)

        self.test_btn1 = tk.Button(self.frame2, text="조회하기", command=self.on_click, bg=Color.BUTTON)
        self.test_btn1.place(x=280, y=0)

        self.test_ent1.bind("<Button-1>", self.on_date_select)

    def after_init(self):
        pass

    def create_table(self, current_range="당기", prev_range="전기"):

        if hasattr(self, "table"):  # 테이블이 있으면 지우기
            self.table.destroy()

        # 새로운 열 이름 설정 (당기, 전기 옆에 날짜 추가)
        col_name = ColName()
        col_name.add("과목", 0, 0, rowspan=2)
        col_name.add(f"{current_range}", 0, 1, colspan=2)
        col_name.add(f"{prev_range}", 0, 3, colspan=2)
        col_name.add("금액", 1, 1, colspan=2)
        col_name.add("금액", 1, 3, colspan=2)

        # 새 테이블 생성
        self.table = TableWidget(
            self.frame1,
            data=None,  # 해당하는 당기,전기 데이터 가져오기
            cols=5,
            new_row=False,
            has_checkbox=False,
            col_name=col_name,  # 업데이트된 열 제목 적용
            col_width=[85, 200, 200, 200, 200],
            col_align=["center", "right", "right", "right", "right"],
            editable=[False, False, False, False, False],
            width=950,
            height=700,
            padding=10,
            relief="solid", bd=1,
        )
        self.table.grid(row=0, column=0)

    def on_date_select(self, event):  # 캘린더 생성
        self.cal = Calendar(self.frame2, firstweekday="sunday", locale="ko_KR", showweeknumbers=False)
        self.cal.place(x=60, y=20)
        self.cal.bind("<<CalendarSelected>>", self.select_date)

    def select_date(self, event):  # 선택된 날짜를 엔트리에 입력
        self.test_ent1.delete(0, tk.END)
        self.test_ent1.insert(0, self.cal.selection_get())
        self.cal.destroy()  # 캘린더 닫기

    def on_click(self):  # 조회하기 버튼
        self.select = self.test_ent1.get().strip()  # 사용자가 선택한 날짜 가져오기

        if not self.select:  # 날짜를 선택하지 않은 경우
            print("no date")
            return  # 함수 종료

        try:
            select_date = datetime.datetime.strptime(self.select, "%Y-%m-%d")
        except ValueError:
            print("date error")  # 날짜 형식이 맞지 않을 경우 처리
            return

        # 당기: 선택년도 1월 1일 ~ 선택 날짜
        current_year = select_date.year
        current_start = datetime.datetime(current_year, 1, 1)
        current_end = select_date

        # 전기: 작년 1월 1일 ~ 선택 날짜
        prev_year = current_year - 1
        prev_start = datetime.datetime(prev_year, 1, 1)
        prev_end = datetime.datetime(prev_year, 12, 31)

        # 날짜 문자열 생성
        current_range = [current_start.strftime('%Y-%m-%d'), current_end.strftime('%Y-%m-%d')]
        prev_range = f"전기[{prev_start.strftime('%Y-%m-%d')} ~ {prev_end.strftime('%Y-%m-%d')}]"

        print(f"당기: {current_range}")
        print(f"전기: {prev_range}")

        self.create_table(f"당기{current_range[0]}~{current_range[1]}", prev_range)  # 컬럼에 들어가는 날짜

        send_data = {"code": 40401, "args": {"기준일자": current_range}}
        self.send_(send_data)

        # 클라 >> 서버

    def send_(self, data):
        self.root.send_(json.dumps(data, ensure_ascii=False))

    # 자동호출
    def recv(self, **kwargs):

        code = kwargs.get('code')
        sign = kwargs.get('sign')
        data = kwargs.get('data')

        if code == 40401:  # 불러오기
            if sign == 1:
                print("f40401 success")
                print("sign:", kwargs.get("sign"))
                print("data:", kwargs.get("data"))

                self.table_data.clear()
                send_data_list = []  # send_data2리스트

                for i in data:
                    account_name, jr_dr, jr_cr, account_type = i
                    # 자산인 경우
                    if account_type == "자산":
                        self.table_data.append([account_name, format(math.floor(jr_dr), ","), None, None, None])
                    # 부채 또는 자본인 경우
                    elif account_type in ("부채", "자본"):
                        self.table_data.append([account_name, None, format(math.floor(jr_cr), ","), None, None])

                    # send_data_list에 데이터 추가
                    send_data_list.append((account_name, jr_dr, jr_cr))

                self.table.refresh(self.table_data)

                send_data2 = {"code": 40402, "args": {"insert": send_data_list}}
                self.send_(send_data2)


            else:
                print("f40401 fail")

                print("sign:", kwargs.get("sign"))
                print("data:", kwargs.get("data"))

        if code == 40402:  # 인서트
            if sign == 1:
                print("f40402 sucess")

                print("sign:", kwargs.get("sign"))
                print("data:", kwargs.get("data"))
            else:
                print("f40402 fail")

                print("sign:", kwargs.get("sign"))
                print("data:", kwargs.get("data"))


'''
@staticmethod
# #서버 >>클라
def f40401(**kwargs):

    standard_code1 = kwargs.get("기준일자")

    if standard_code1 is None:
        return {"sign": 0, "data": None}

    start = standard_code1[0]
    end = standard_code1[1]  # '2025-03-25'예시

    # accountsubject 테이블에서 account_name과 account_type 조회
    account_data = dbm.query(
        "SELECT account_name, account_type FROM accountsubject WHERE account_type IN ('자산','부채','자본')"
    )

    if not account_data:
        return {"sign": 0, "data": None}

    # account_name, account_type딕셔너리
    account_dict = {i: j for i,j in account_data}

    # 승인된 전표 bk_id
    data = dbm.query(
        "SELECT bk_id FROM accountbook WHERE (bk_date BETWEEN %(id1)s AND %(id2)s) AND bk_approval_state = '승인'",
        {"id1": start, "id2": end}
    )

    if not data:
        return {"sign": 0, "data": None}

    bk_id_list = [i[0] for i in data]  # 전표 id리스트

    # journalizingbook 테이블에서 account_name별로 차변 대변 합계
    a = dbm.query("SELECT account_name, SUM(jr_dr), SUM(jr_cr) FROM journalizingbook WHERE bk_id IN %(id)s AND account_name IN %(id1)s GROUP BY account_name",
        {"id": tuple(bk_id_list), "id1": tuple(account_dict.keys())}
    )

    if not a:
        return {"sign": 0, "data": None}

    # account_type 정보 추가
    data1 = []
    for i in a:
        account_name = i[0]  # account_name
        jr_dr = i[1]  #  SUM(jr_dr)
        jr_cr = i[2]  # SUM(jr_cr)
        account_type = account_dict.get(account_name, None) #과목별 (name) 자산,부채,자본

        data1.append((account_name, jr_dr, jr_cr, account_type))

    return {"sign": 1, "data": data1}



@staticmethod
# #서버 >>클라
def f40402(**kwargs):
    standard_code2 = kwargs.get("insert")
    if standard_code2 is not None:
        data2 = []
        for i in standard_code2:
            b = dbm.query("INSERT INTO financial_report (subject,dr_cost, cr_cost) VALUES (%(id1)s, %(id2)s, %(id3)s)",
                          {
                              "id1": i[0], "id2": i[1], "id3": i[2]
                          })
            if b is not None:              
                data2.append(b)
        if data2:
            return {"sign": 1, "data": data2}
        else:
            return {"sign": 0, "data": None}
    else:
        return {"sign": 0, "data": None}
'''

# 테스트용 코드
if __name__ == "__main__":
    # dbm = dbManager.DBManager(host="localhost", user="root", password="0000", port=3306)
    r = tk.Tk()
    r.geometry("1600x900")
    r.config(bg="white")
    fr = Financial_statement(r)
    fr.place(x=300, y=130)
    r.mainloop()





