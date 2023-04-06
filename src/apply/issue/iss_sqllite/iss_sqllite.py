import sqlite3
from unittest import TestCase


class TestSqlLite(TestCase):

    def test_run(self):
        conn = sqlite3.connect('test.db')

        print("数据库打开成功")
        c = conn.cursor()
        c.execute('''CREATE TABLE COMPANY
               (ID INT PRIMARY KEY     NOT NULL,
               NAME           TEXT    NOT NULL,
               AGE            INT     NOT NULL,
               ADDRESS        CHAR(50),
               SALARY         REAL);''')
        print("数据表创建成功")
        conn.commit()
        conn.close()

    def test_run2(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        print("数据库打开成功")

        c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
              VALUES (1, 'Paul', 32, 'California', 20000.00 )")

        c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
              VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")

        conn.commit()
        print("数据插入成功")

        c.execute("UPDATE COMPANY set SALARY = 25000.00 where ID=1")
        conn.commit()
        print("Total number of rows updated :", conn.total_changes)

        cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")
        for row in cursor:
            print("ID = ", row[0], "NAME = ", row[1], "ADDRESS = ", row[2], "SALARY = ", row[3], "\n")

        print("数据操作成功")

        c.execute("DELETE from COMPANY where ID=2;")
        conn.commit()
        print("Total number of rows deleted :", conn.total_changes)

        cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")
        for row in cursor:
            print("ID = ", row[0], "NAME = ", row[1], "ADDRESS = ", row[2], "SALARY = ", row[3], "\n")

        print("数据操作成功")
        conn.close()

    def test_select(self):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        print("数据库打开成功")

        cursor = c.execute("SELECT id, name, address, salary  from COMPANY")
        for row in cursor:
            print("ID = ", row[0], "NAME = ", row[1], "ADDRESS = ", row[2], "SALARY = ", row[3], "\n")

        print("数据操作成功")
        conn.close()
