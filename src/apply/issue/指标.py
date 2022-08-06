import json
from unittest import TestCase


class TestAutoCode(TestCase):
    def test_run(self):
        with open("指标.txt", encoding="utf-8", mode='r') as f:
            for line in f.readlines():
                menu_list = json.loads(line)
                print(menu_list)

