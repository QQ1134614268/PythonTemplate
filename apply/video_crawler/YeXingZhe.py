# -*- coding:utf-8 -*-

import requests
import time
from requests.adapters import HTTPAdapter


def getVideo():
    m3u6_url = "https://www.zhuticlub.com:65/20190619/A1pB3p4f/2000kb/hls/index.m3u8"
    count = 0
    session = requests.Session()
    session.mount('http://', HTTPAdapter(max_retries=5))
    session.mount('https://', HTTPAdapter(max_retries=5))
    send_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "Connection": "keep-alive",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8"}

    all_content = session.get(m3u6_url, timeout=30, headers=send_headers).text
    file_lines = all_content.split("\n")
    for line in file_lines:
        if not line.endswith(r"ts"):
            continue
        video_url = m3u6_url.replace("index.m3u8", line.split("/")[-1])
        time.sleep(2)
        res = retry_get(video_url, timeout=200, headers={
            "Referer": "https://jx.123ku.com/123kudpbfq/?url=https://www.zhuticlub.com:65/20190619/A1pB3p4f/index.m3u8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        })
        try:
            with open("{}.ts".format(count), 'ab') as f:
                f.write(res.content)
                f.flush()
        except Exception:
            print(video_url)
        count += 1


def retry_get(url, timeout, headers, retry_count=3):
    print(url)
    if retry_count <= 0:
        return Exception("获取失败", url)
    try:
        res = requests.get(url, timeout=10, headers=headers)
        if res.status_code == 200:
            return res
        else:
            print(url, "  重试 ", retry_count, )
            return retry_get(url, timeout, headers, retry_count - 1)
    except Exception:
        print(url, "  重试 ", retry_count - 1, )
        return retry_get(url, timeout, headers, retry_count - 1)


if __name__ == '__main__':
    getVideo()
