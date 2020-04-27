# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
import os

import pandas as pd


def getCsv(dicPath="data"):
    file_list = os.listdir(dicPath)
    return [os.path.join(dicPath, i) for i in file_list]


from mysql import connector


def connectMysql():
    # config = {'host': '127.0.0.1',  # 默认127.0.0.1
    #           'user': 'root',
    #           'password': 'hao123',
    #           'port': 3306,  # 默认即为3306
    #           'database': 'learn',
    #           'charset': 'utf8'  # 默认即为utf8
    #           }
    # db = connector.connect(**config)  # 连接数据库
    db = connector.connect(host="127.0.0.1", port=3306, user="root", passwd="1234556", db="vx_cost_db")  # 连接数据库
    # cursor = db.cursor()
    # cursor.close()
    # db.close()
    return db


def insert_data():
    '''

    '''
    pass


def readCsv():
    file_path = getCsv()
    for i in file_path:
        data = pd.read_csv(i)


if __name__ == '__main__':
    db = connector.connect(host="127.0.0.1", port=3306, user="root", passwd="123456", db="zero_db")  # 连接数据库
    table_header = ["trading_time", "trading_type", "trading_people", "goods", "cost", "money", "pay_type",
                    "trading_status", "trading_number", "trading_people_account", "note"]
    sql = "CREATE TABLE IF NOT EXISTS `person_cost` (`id` int(11)  NOT NULL AUTO_INCREMENT PRIMARY KEY ,`{}` datetime \
    DEFAULT NULL,`{}` varchar(255) DEFAULT NULL,`{}` varchar(255) DEFAULT NULL,`{}` varchar(255) DEFAULT NULL,\
    `{}` varchar(255) DEFAULT NULL,`{}` float DEFAULT NULL,`{}` varchar(255) DEFAULT NULL,`{}` varchar(255) DEFAULT NULL,\
    `{}` varchar(255) DEFAULT NULL,`{}` varchar(255) DEFAULT NULL,`{}` varchar(255) DEFAULT NULL) ENGINE=InnoDB DEFAULT\
     CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;".format(*table_header)
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    file_path = getCsv()
    insert_header = ','.join(table_header)
    value_sql = ('"{}", ' * 11)[0:-2]
    sql = 'insert into person_cost ({})values({})'.format(insert_header, value_sql)
    for i in file_path:
        print(i)
        data = pd.read_csv(i)
        data["金额(元)"] = pd.Series([i.replace("¥", "") for i in data["金额(元)"].values])
        for index, row in data.iterrows():
            # print(*row.values)
            exc_sql = sql.format(*row.values)
            print(exc_sql)
            cursor.execute(exc_sql)
            db.commit()
    db.commit()
    db.close()
