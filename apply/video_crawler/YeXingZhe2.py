# -*- coding:utf-8 -*-
"""
@Time: 2020/9/16
@Description: 
"""
import os

import requests
import time

file = []
b = os.listdir("data")
for i in b:
    path = os.path.join('data', i)
    size = os.path.getsize(path)
    if size == 0:
        file.append(i)
url = "https://www.zhuticlub.com:65/20190619/A1pB3p4f/2000kb/hls/JQ3F2776000.ts"


def get_video(video_url, name):
    res = retry_get(video_url, timeout=200, headers={
        "Referer": "https://jx.123ku.com/123kudpbfq/?url=https://www.zhuticlub.com:65/20190619/A1pB3p4f/index.m3u8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    })
    try:
        with open(name, 'ab') as f:
            f.write(res.content)
            f.flush()
    except Exception:
        print(video_url)


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


for i in file:
    new_url = url[:-len(i)] + i
    time.sleep(2)
    get_video(new_url, i)
