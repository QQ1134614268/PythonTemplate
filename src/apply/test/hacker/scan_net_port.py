import os
import socket
import unittest

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

domain_name = ""


class TestHacker(unittest.TestCase):

    # 获取http指纹
    @staticmethod
    def test_get_headers_by_domain_name():
        # domain_name = input('请输入目标域名：')
        url = f"http://{domain_name}"
        r = requests.get(url, headers=headers)
        print(r.headers)

    # 判断有无robots.txt
    @staticmethod
    def test_robots():
        robots_url = f"http://{domain_name}/robots.txt"

        gf = requests.get(robots_url, headers=headers, timeout=8)
        if gf.status_code == 200:
            print('robots.txt存在')
            print('[+]该站存在robots.txt', robots_url)
        else:
            print('[-]没有robots.txt')

    # 目录扫描
    @staticmethod
    def test_scan_web_directory():
        with open('build.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                try:
                    net_path = f"http://{domain_name}{line}"
                    rvc = requests.get(net_path, headers=headers, timeout=8)
                    if rvc.status_code == 200:
                        print('[*]', net_path)
                except Exception as e:
                    print('[-]远程主机强迫关闭了一个现有的连接',e)

    # 端口扫描
    @staticmethod
    def test_scan_port():
        s = socket.gethostbyname(domain_name)
        o = os.system('nmap {} program'.format(s))
        print(o)

    # whois查询
    @staticmethod
    def test_whois():
        whois_url = f"http://site.ip138.com/{domain_name}/whois.htm"
        rvt = requests.get(whois_url, headers=headers)
        bv = BeautifulSoup(rvt.content, "html.parser")
        for line in bv.find_all('p'):
            link = line.get_text()
            print(link)

    # IP反查域名
    @staticmethod
    def test_get_domain_name_by_ip():
        wu = socket.gethostbyname(domain_name)
        rks = "http://site.ip138.com/{}/".format(wu)
        sjk = requests.get(rks, headers=headers)
        liverou = BeautifulSoup(sjk.content, 'html.parser')
        for low in liverou.find_all('li'):
            bc = low.get_text()
            print(bc)
