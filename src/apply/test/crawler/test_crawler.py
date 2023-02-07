import json
import time
import unittest
from urllib import request


class TestCrawler(unittest.TestCase):

    def test_main(self):

        url = f"http://api.goseek.cn/Tools/holiday?date={time.strftime('%Y%m%d', time.localtime(time.time()))}"
        res = request.urlopen(url)
        data = res.read()
        data = str(data, encoding="utf-8")
        data = json.loads(data)
        if data['code'] == 10000:
            print(data)
        else:
            print("请求失败")
