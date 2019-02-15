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

