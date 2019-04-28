'''
Created on 2018年2月25日

@author: Administrator
'''
#!/usr/bin/python3
 
import pymysql
 
# 打开数据库连接
db = pymysql.connect("127.0.0.1", "root", "123456", "database_student")
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
# 使用 execute()  方法执行 SQL 查询 
SQL = "SELECT VERSION()"
cursor.execute(SQL) 
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
 
print ("Database version : %s " % data)

sql = "select count(*) from teacher"
try:
    # 执行sql语句
    data1 = cursor.execute(sql)
    data1 = cursor.fetchone()
    print(data1)
    # 执行sql语句
    db.commit()
except:
    # 发生错误时回滚
    db.rollback() 
 
# 关闭数据库连接
db.close()

'''
import pymysql
 
# 打开数据库连接
db = pymysql.connect("localhost","testuser","test123","TESTDB" )
 
# 使用cursor()方法获取操作游标 
cursor = db.cursor()
 
# SQL 插入语句
sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
       ('Mac', 'Mohan', 20, 'M', 2000)
try:
   # 执行sql语句
   cursor.execute(sql)
   # 执行sql语句
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()
 
# 关闭数据库连接
db.close()
'''
