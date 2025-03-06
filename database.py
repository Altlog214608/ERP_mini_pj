import pymysql

class Database:
    _instance = None
    _connection = None
    _cursor = None

    def __new__(cls, host, user, password, port, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._connection = pymysql.connect(
                host=host,
                user=user,
                password=password,
                port=port)
            cls._cursor = cls._connection.cursor()
        return cls._instance

    def __del__(self):
        self.close()

    def close(self):
        if self._cursor:
            self._cursor.close()
        if self._connection:
            self._connection.close()
            self._cursor = None
            self._connection = None

    def query(self, query, params=None):
        try:
            print(query)
            self._cursor.execute(query, params)
            self._connection.commit()
            return self._cursor.fetchall()
        except Exception as e:
            print(f"Query failed. Error: {e}")
            return None

    def transaction(self, queries):
        try:
            self._connection.autocommit(False)
            for query, params in queries:
                self._cursor.execute(query, params)
            self._connection.commit()
            return True
        except Exception as e:
            self._connection.rollback()
            print(f"Transaction failed. Error: {e}")
            return False

    # 아래부터 injection에 취약할 수 있음
    def current_db(self):
        return self.query("SELECT DATABASE()")[0][0]

    def db_list(self):
        result = self.query("SHOW DATABASES")
        if result is None:
            return []
        return [i[0] for i in result]

    def create_db(self, db_name):
        return self.query(f"CREATE DATABASE {db_name}") is not None

    def drop_db(self, db_name):
        return self.query(f"DROP DATABASE {db_name}") is not None

    def use_db(self, db_name):
        return self.query(f"USE {db_name}") is not None

    def table_list(self):
        result = self.query("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = DATABASE()")
        if result is None:
            return []
        return [i[0] for i in result]

    def create_table(self, table_name, **kwargs):
        return self.query(
            f"CREATE TABLE {table_name} ({', '.join(f'{k} {' '.join(v)}' for k, v in kwargs.items())})") is not None

    def drop_table(self, table_name):
        return self.query(f"DROP TABLE {table_name}") is not None

    def columns(self, table_name):
        result = self.query(
            f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = '{table_name}'")
        if result is None:
            return []
        return [i[0] for i in result]

    def insert(self, table_name, **kwargs):
        keys = [i[0] for i in kwargs.items()]
        values = [f"'{i[1]}'" if i[1] else "NULL" for i in kwargs.items()]
        return self.query(
            f"INSERT INTO {table_name} ({', '.join(keys)}) VALUES ({', '.join(values)})") is not None

    def delete(self, table_name, condition=None):
        return self.query(f"DELETE FROM {table_name}{f" WHERE {condition}" if condition else ""}") is not None

    def select(self, table_name, *cols, condition=None):
        return self.query(f"SELECT {', '.join(cols)} FROM {table_name}{f" WHERE {condition}" if condition else ""}")

    def join(self, db_name, table1_name, table1_col, table2_name, table2_col, *cols, condition=None):
        return self.query(
            f"SELECT {', '.join(cols)} FROM {db_name}.{table1_name} INNER JOIN {db_name}.{table2_name} ON ({table1_col} = {table2_col}){f" WHERE {condition}" if condition else ""}")