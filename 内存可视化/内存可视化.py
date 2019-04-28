# 获取,存储,展现增量展现 --扩展-监控多个主机,http查看  下载数据
import pymysql
import time
db = pymysql.connect("127.0.0.1","root","123456","database_student" )
db.autocommit(True)
cur=db.cursor();
def getMem():
    file = open('/proc/meminfo')
    memTotal = int(file.readline().split()[1])
    memFree = int(file.readline().split()[1])
    memBuffer = int(file.readline().split()[1])
    memCache = int(file.readline().split()[1])
    memUse = memTotal - memBuffer - memFree - memCache
    print(memUse / 1024)
    sql="insert into Mem(memUse,times) value (%s,%s)"%(memUse,time.localtime())
    print(sql)
    cur.execute(sql)


def main():
    while True:
        getMem()

if __name__ == '__main__':
    main()
