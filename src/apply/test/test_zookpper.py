from unittest import TestCase

import time
from kazoo.client import KazooClient

from config.conf import GGOK_ZOOKEEPER_HOST


class TestZookeeper(TestCase):

    def setUp(self):
        self.zk = KazooClient(GGOK_ZOOKEEPER_HOST)
        self.zk.start()
        self.path = "/root"

    def test_create(self):
        if self.zk.exists(self.path):
            print("节点已经存在")
            return
        self.zk.create(self.path, b'this is byte', makepath=True)

    def test_get(self):
        print(self.zk.get(self.path))

    def test_update(self):
        self.zk.set(self.path, b"this is byte after update")

    def test_watch(self):
        @self.zk.DataWatch(self.path)
        def my_change(num1, num2):
            time.sleep(3)
            print(num1, num2)

        while True:
            time.sleep(3)
            my_change(1, 2)

    def test_delete(self):
        self.zk.delete(self.path, recursive=True)  # 递归删
