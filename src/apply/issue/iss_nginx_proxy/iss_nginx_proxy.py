import os
from unittest import TestCase

import requests


class TestNginxProxy(TestCase):
    """
      测试nginx proxy_pass 代理转发
    """

    def test_main(self):
        a1 = ["/proxy", "/proxy/"]
        a2 = ["", "/", "/api", "/api/"]
        req_url = 'http://localhost:20080/proxy/abc'
        conf_path = r'D:/dev/nginx-1.22.0/conf/nginx.conf'
        row1 = 97
        row2 = 98
        with open(conf_path, encoding="utf-8", mode="r") as f:
            lines = f.readlines()

        for proxy in a1:
            lines[row1 - 1] = f'\t\tlocation {proxy} {{\n'
            for to in a2:
                lines[row2 - 1] = f'\t\t\tproxy_pass http://127.0.0.1:20090{to};\n'
                with open(conf_path, encoding="utf-8", mode="w") as f:
                    f.writelines(lines)
                os.system(r'D: && cd D:\dev\nginx-1.22.0\ && nginx -s reload')
                res = requests.get(req_url)
                print(proxy, f'http://127.0.0.1:20090{to}', f'http://127.0.0.1:20090{res.text}')
