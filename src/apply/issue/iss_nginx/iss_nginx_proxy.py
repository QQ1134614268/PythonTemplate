import os
from unittest import TestCase

import requests


class TestNginxProxy(TestCase):
    """
      测试nginx proxy_pass 代理转发
    """

    def test_main(self):
        a1 = ["/", "/proxy", "/proxy/"]
        a2 = ["", "/", "/api", "/api/"]
        req_url = 'http://localhost:20080/proxy/abc'
        # conf_path = r'D:/dev/nginx-1.22.0/conf/nginx.conf'
        nginx_dir = r'D:/dev/nginx-1.17.7'
        conf_path = os.path.join(nginx_dir, 'conf/test.conf')

        for proxy in a1:
            for to in a2:
                tpl = f'server {{ listen 20080; location {proxy} {{ proxy_pass http://127.0.0.1:20090{to}; }} }}'
                with open(conf_path, encoding="utf-8", mode="w") as f:
                    f.write(tpl)
                os.system(f'D: && cd {nginx_dir} && nginx -s reload')
                res = requests.get(req_url)
                print(proxy, f'http://127.0.0.1:20090{to}', f'http://127.0.0.1:20090{res.text}')
