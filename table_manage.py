# GUI + DB MTSQL 연습문제
# GUI 프로그램을 통해 MYSQL 서버의 데이터베이스 생성 및 수정 관리를 할 수 있도록 구현
# GUI를 통한 DB의 CRUD 작업
# 1 DB생성, 테이블 생성 데이터 USE설정
# 2 특정 테이블의 데이터 삽임
# 3 특정 테이블의 데이터 검색 결과 조회 (데이터가 SQL 문법에 적합한지 검사하는 함수)
# 4 특정 테이블의 데이터 검색 결과 조회 (select 기능인데 전체열 or 특정열)
# 5 테이블 삭제 (어떤 테이블 삭제할건지 지정)

import pymysql
import tkinter as tk
from tkinter import ttk, messagebox

DB_NAME = ""  # 현재 사용 중인 데이터베이스


def use_database(sql):
    try:
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='0731',
            port=3306,
            database=DB_NAME if DB_NAME else None  # DB_NAME이 없을 경우 None
        )
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        cursor.close()
        connection.close()
    except pymysql.MySQLError as e:
        messagebox.showerror("DB 오류", str(e))


# 데이터 조회
def query_data():
    selected_table = table_combobox.get()
    query = query_entry.get().strip()

    if not selected_table:
        messagebox.showwarning("조회 오류", "테이블을 선택하세요.")
        return

    if not query:
        query = f"SELECT * FROM {selected_table}"

    try:
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='0731',
            port=3306,
            database=DB_NAME
        )
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        columns = []
        for i in cursor.description:
            print(i)
            columns.append(i[0])
            print(columns)
        cursor.close()
        connection.close()

        # Treeview
        update_treeview(columns, result)

    except pymysql.MySQLError as e:
        messagebox.showerror("조회 오류", str(e))


# Treeview
def update_treeview(columns, data):
    tree["columns"] = columns
    tree.delete(*tree.get_children())  # 기존 데이터 삭제

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=120, anchor="center")

    for row in data:
        tree.insert("", "end", values=row)


# 데이터베이스 선택
def select_db_action(e=None):
    global DB_NAME
    DB_NAME = db_combobox.get()

    if DB_NAME:
        use_database(f"USE {DB_NAME}")
        messagebox.showinfo("데이터베이스 선택", f"{DB_NAME} 사용 중")
        load_tables(e)
    else:
        messagebox.showwarning("선택 오류", "데이터베이스를 선택하세요.")


# DB 생성
def create_db():
    new_db_name = db_name.get().strip()
    if not new_db_name:
        messagebox.showwarning("입력 오류", "DB 이름을 입력하세요.")
        return
    try:
        use_database(f"CREATE DATABASE {new_db_name}")
        messagebox.showinfo("DB 생성 완료", f"데이터베이스 '{new_db_name}' 생성됨.")
        load_databases()
    except pymysql.MySQLError as e:
        messagebox.showerror("DB 오류", str(e))


# DB 목록 불러오기
def load_databases():
    try:
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='0731',
            port=3306
        )
        cursor = connection.cursor()
        cursor.execute("SHOW DATABASES")
        databases = cursor.fetchall()
        db = []
        for i in databases:
            db.append(i[0])
        db_combobox["values"] = db
        cursor.close()
        connection.close()
    except pymysql.MySQLError as e:
        messagebox.showerror("DB 오류", str(e))


# 테이블 목록 불러오기
def load_tables(e=None):
    if not DB_NAME:
        messagebox.showwarning("DB 선택 오류", "먼저 데이터베이스를 선택하세요.")
        return
    try:
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='0731',
            port=3306,
            database=DB_NAME
        )
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        tb = []
        for i in tables:
            tb.append(i[0])
        table_combobox["values"] = tb
        cursor.close()
        connection.close()
    except pymysql.MySQLError as e:
        messagebox.showerror("DB 오류", str(e))


# 테이블 생성
def create_table():
    new_table_name = table_name.get().strip()
    if not new_table_name:
        messagebox.showwarning("입력 오류", "테이블 이름을 입력하세요.")
        return
    try:
        use_database(f"CREATE TABLE {new_table_name} (id INT AUTO_INCREMENT PRIMARY KEY, data TEXT)")
        messagebox.showinfo("테이블 생성 완료", f"테이블 '{new_table_name}' 생성됨.")
        load_tables()
    except pymysql.MySQLError as e:
        messagebox.showerror("테이블 오류", str(e))


# 테이블 삭제
def delete_table():
    selected_table = table_combobox.get()

    if not selected_table:
        messagebox.showwarning("삭제 오류", "삭제할 테이블을 선택하세요.")
        return

    try:
        use_database(f"DROP TABLE {selected_table}")
        messagebox.showinfo("삭제 완료", f"테이블 '{selected_table}' 삭제됨.")
        load_tables()
    except pymysql.MySQLError as e:
        messagebox.showerror("삭제 오류", str(e))


# 데이터 삽입
def insert_data(data_value, insert_window):
    selected_table = table_combobox.get()

    if not selected_table:
        messagebox.showwarning("입력 오류", "먼저 테이블을 선택하세요.")
        return

    if not data_value:
        messagebox.showwarning("입력 오류", "데이터를 입력하세요.")
        return

    try:
        use_database(f"INSERT INTO {selected_table} (data) VALUES ('{data_value}')")
        messagebox.showinfo("삽입 완료", f"데이터 '{data_value}'가 '{selected_table}' 테이블에 삽입됨.")
        insert_window.destroy()  # 창 닫기
    except pymysql.MySQLError as e:
        messagebox.showerror("삽입 오류", str(e))


# 데이터 입력 창 열기
def open_insert_data_window():
    insert_window = tk.Toplevel()
    insert_window.title('데이터 삽입')
    insert_window.geometry('300x150')

    tk.Label(insert_window, text='데이터 입력:').pack(pady=5)
    data_entry = tk.Entry(insert_window)
    data_entry.pack(pady=5)

    insert_button = tk.Button(
        insert_window,
        text='입력',
        command=lambda: insert_data(data_entry.get().strip(), insert_window)
    )
    insert_button.pack(pady=5)


root = tk.Tk()

root.title("MYSQL GUI Assemble")
root.geometry("800x500")

# 프레임 구성
frame_top = tk.Frame(root)
frame_top.pack(pady=10)
frame_mid = tk.Frame(root)
frame_mid.pack(pady=10)
frame_bottom = tk.Frame(root)
frame_bottom.pack(pady=10)

# 데이터베이스 선택
tk.Label(frame_top, text="데이터베이스 선택:").grid(row=0, column=0)
db_combobox = ttk.Combobox(frame_top, state="readonly")
db_combobox.grid(row=0, column=1)
db_combobox.bind("<<ComboboxSelected>>", select_db_action)

# DB 생성
tk.Label(frame_top, text="새 DB 이름:").grid(row=0, column=2)
db_name = tk.Entry(frame_top)
db_name.grid(row=0, column=3)
tk.Button(frame_top, text="DB 생성", command=create_db).grid(row=0, column=4)

# 테이블 선택
tk.Label(frame_mid, text="테이블 선택:").grid(row=0, column=0)
table_combobox = ttk.Combobox(frame_mid, state="readonly")
table_combobox.grid(row=0, column=1)
table_combobox.bind("<<ComboboxSelected>>", load_tables)

# 테이블 생성
tk.Label(frame_mid, text="새 테이블 이름:").grid(row=0, column=2)
table_name = tk.Entry(frame_mid)
table_name.grid(row=0, column=3)
tk.Button(frame_mid, text="테이블 생성", command=create_table).grid(row=0, column=4)

# 데이터 삽입
tk.Label(frame_mid, text="데이터 입력:").grid(row=1, column=0)
tk.Button(frame_mid, text="데이터 삽입", command=open_insert_data_window).grid(row=1, column=1)

# 테이블 삭제
tk.Button(frame_mid, text="테이블 삭제", command=delete_table).grid(row=1, column=4)

# 데이터 조회
tk.Label(frame_mid, text="조회할 SQL 문:").grid(row=2, column=0)
query_entry = tk.Entry(frame_mid, width=40)
query_entry.grid(row=2, column=1)
tk.Button(frame_mid, text="조회 실행", command=query_data).grid(row=2, column=2)

# 결과 출력창
tree = ttk.Treeview(frame_bottom, columns=(1, 2, 3), show="headings")
tree.pack(side='left')

scrollbar = ttk.Scrollbar(frame_bottom, orient="vertical", command=tree.yview)
scrollbar.pack(side="right", fill="y")
tree.configure(yscrollcommand=scrollbar.set)

# 프로그램 시작 시 DB 목록 불러오기
load_databases()

root.mainloop()