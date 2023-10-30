import json
from unittest import TestCase


class TestIndex(TestCase):
    def test_run(self):
        with open("data.txt", encoding="utf-8", mode='r') as f:
            for line in f.readlines():
                menu_list = json.loads(line)
                print(json.dumps(menu_list, ensure_ascii=False))
