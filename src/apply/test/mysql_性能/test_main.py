import datetime
import random
from unittest import TestCase

from apply.test.mysql_性能.models import User, Base, Order, OrderInfo, Goods
from apply.test.mysql_性能.util import get_id
from conf.config import localhost_test_engine, localhost_test_session


# 根据model 生成存储过程,根据类型生成字段
# 根据model 生成数据, model批量插入

# todo
# TPCC 它模拟了一个仓储物流的业务场景，包括新建订单、付款、发货、订单查询、库存查询五个事务操作

#   1. 注册用户 1千万条
#   2. 订单表 1百万数据 包含 交易完成90%,退单50%,发货2%,付款2%,下单1% (平均分布1000天内, 用户正态分布)
#   3. 订单详情表: 1个订单1-3中商品,1-10数量, 约2百万数据

# 性能: 存储过程拼接 > 程序批量(500秒 1千万,无网络io) > 存储过程插入(43818.561) > 程序单条?
# 批量与单条 87倍性能差距?
class TestMysql(TestCase):

    def test_init_table(self):
        Base.metadata.create_all(localhost_test_engine)

    def test_drop_table(self):
        # Base.metadata.drop_all(engine)
        ...

    def test_insert_user(self):
        num = get_id(1)
        now = datetime.datetime.now()
        for i in range(100):
            create_time = now - datetime.timedelta(days=(1000 - i))
            vos = []
            for j in range(100000):
                row = next(num)
                vos.append(User(**{
                    "name": "name_"+row,
                    "sex": random.randint(0, 2),
                    "id": row,
                    "create_time": create_time,
                    "update_time": create_time,
                    "create_by": row,
                    "update_by": row,
                }))
            localhost_test_session.add_all(vos)
            localhost_test_session.commit()

    def test_insert_goods(self):
        num = get_id(1)
        vos = []
        for j in range(1000):
            row = next(num)
            vos.append(Goods(**{
                "num": 10000,
                "goods_name": "goods_name_" + str(row),
                "id": row,
            }))
        localhost_test_session.add_all(vos)
        localhost_test_session.commit()

    def test_insert_order(self):
        num = get_id(1)
        now = datetime.datetime.now()
        for i in range(10):
            create_time = now - datetime.timedelta(days=(1000 - i))
            vos = []
            for j in range(100000):
                row = next(num)
                user_id = random.randint(1000, 10000)
                vos.append(Order(**{
                    "user_id": user_id,
                    "status": random.randint(0, 6),

                    "id": row,
                    "create_time": create_time,
                    "update_time": create_time,
                    "create_by": user_id,
                    "update_by": user_id,
                }))
            localhost_test_session.add_all(vos)
            localhost_test_session.commit()

    def test_insert_order_info(self):
        num = get_id(1)
        order_id_func = get_id(1)
        now = datetime.datetime.now()
        for i in range(10):
            create_time = now - datetime.timedelta(days=(1000 - i))
            vos = []
            for j in range(100000):
                order_id = next(order_id_func)
                for x in range(random.randint(1, 3)):
                    row = next(num)
                    goods_ids = [random.randint(1, 300), random.randint(300, 600), random.randint(600, 1000), ]
                    vos.append(OrderInfo(**{
                        "order_id": order_id,
                        "goods_id": goods_ids[x],
                        "goods_name": "goods_name_" + str(goods_ids[x]),

                        "id": row,
                        "create_time": create_time,
                        "update_time": create_time,
                        "create_by": row,
                        "update_by": row,
                    }))
            localhost_test_session.add_all(vos)
            localhost_test_session.commit()

    def test_insert_user_proc(self):
        connection = localhost_test_engine.raw_connection()
        cursor = connection.cursor()
        cursor.callproc('insert_performance_user_t', (10000000,))
        connection.commit()

    def _table_arg(self, _id=None, create_time=None, create_by=None):
        return {
            "id": _id,
            "create_time": create_time,
            "update_time": create_time,
            "create_by": create_by,
            "update_by": create_by,
        }
