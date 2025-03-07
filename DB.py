import threading
import pymysql
from tkinter import messagebox
lock = threading.Lock()


##DB table만들어지기 전까진 password 와 database 수정 후 사용
class ConnectDB:
    def connection_DB(self):
        try:
            self.connection = pymysql.connect(
                    host='localhost',
                    user = 'root',
                    password = '0000',      #바꿔서쓰셈
                    database = 'sakila',  #바꿔서쓰셈
                    port = 3306
                )
            self.cursor = self.connection.cursor()
            print('DB연결 성공')
        except pymysql.MySQLError as e:
            messagebox.showerror("DB 연결 오류", str(e))


    def query(self,sql):
        #sql 처리
        self.tablist=[]
        try:
            # 작업이 끝나기 전까지 다른 쓰레드가 공유 데이터 접근 금지
            lock.acquire()
            print('--1')
            self.cursor.execute(sql)
            self.connection.commit()
            self.result = self.cursor.fetchall()
            for i in self.result:
                self.tablist.append(list(i))
            print('test', self.tablist)


            # if ('select' in sql or 'SELECT' in sql):
            #     print('--select')
            #     self.cursor.execute(sql)
            #     self.result = self.cursor.fetchall()
            #     for i in self.result:
            #         self.tablist.append(list(i))
            #     print('test',self.tablist)
            #     return self.tablist
            #
            # elif ('insert' in sql or 'INSERT' in sql):
            #     print('--insert')
            #     self.cursor.execute(sql)
            #     self.connection.commit()
            #     self.result = self.cursor.fetchall()
            #     return self.result
            #
            # elif ('update' in sql or 'UPDATE' in sql):
            #     print('--update')
            #     self.cursor.execute(sql)
            #     self.connection.commit()
            #     self.result = self.cursor.fetchall()
            #     return self.result
            #
            # elif ('delete' in sql or 'DELETE' in sql):
            #     print('--delete')
            #     self.cursor.execute(sql)
            #     self.connection.commit()
            #     self.result = self.cursor.fetchall()
            #     return self.result
            # elif ('create' in sql or 'CREATE' in sql):
            #     print('--Create')
            #     # self.cursor.execute(sql)
            #     # self.connection.commit()
            #     # self.result = self.cursor.fetchall()
            #     # return self.result
            # else:
            #     print('--another')
            #     self.cursor.execute(sql)
            #     self.result = self.cursor.fetchall()
            #     for i in self.result:
            #         self.tablist.append(list(i))
            #     print('test',self.tablist)
            #     return self.tablist

            #lock 해제
            lock.release()
            return self.tablist
        except pymysql.MySQLError as e:
            messagebox.showerror("SQL 오류", str(e))
            lock.release()
            return None

    def close(self):
        self.cursor.close()
        self.connection.close()


