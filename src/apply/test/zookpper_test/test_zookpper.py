import time

from kazoo.client import KazooClient

# todo 1.远程服务器 2.测试监听数据
#
from conf.config import ZOOKEEPER_HOST


def connection():
    zk = KazooClient(ZOOKEEPER_HOST)
    zk.start()
    # print(zk.connected)
    if zk.connected:
        kk = "success"
    else:
        kk = "failed"
    print(kk)
    return zk.connected


def Utime(f):
    def timechange(*args, **kwargs):
        start_time = time.time()
        f(*args, **kwargs)
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000
        return execution_time

    return timechange


# 增
@Utime
def create(hosts, path, data):
    zk = KazooClient(hosts)
    zk.start()
    value = data.encode()
    zk.create(path, value, makepath=True)
    zk.stop()


# 删
@Utime
def delete(hosts, path):
    zk1 = KazooClient(hosts)
    zk1.start()
    zk1.delete(path)
    zk1.stop()


# 查
@Utime
def get(hosts, path):
    zk2 = KazooClient(hosts)
    zk2.start()
    zk2.get(path)
    zk2.stop()


#   return data

# 改
@Utime
def set_data(hosts, path, data):
    zk3 = KazooClient(hosts)
    zk3.start()
    value = data.encode()
    zk3.set(path, value)
    zk3.stop()


# 递归删
def delete_all(hosts, path):
    zk4 = KazooClient(hosts)
    zk4.start(timeout=10)
    zk4.delete(path, recursive=True)
    zk4.stop()


# watch
def node_watch(host, path):
    zk = KazooClient(host)
    zk.start()

    @zk.DataWatch(path)
    def my_change(data, stat):
        time.sleep(3)
        # print("Data is %s" % data)
        # print("Version is %s" % stat.version)
        # print("Event is %s" % event)

    while True:
        time.sleep(3)
        # print("OK")


if __name__ == '__main__':
    connection()
