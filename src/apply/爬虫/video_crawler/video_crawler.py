# -*- coding:utf-8 -*-
import os

import requests
from requests.adapters import HTTPAdapter

from util import log_util

logger = log_util.create_logger("F:/log/video_crawler_log.json")


def getSeries(url_file, series_name, series_path):
    # if os.path.exists(series_path):  # 判断文件夹是否存在, 删除所有文件
    #     shutil.rmtree(series_path)
    if not os.path.exists(series_path):
        os.makedirs(series_path)

    with open(url_file) as f:
        url_list = f.readlines()
        count = 0
        for url in url_list:
            count += 1
            url = url.replace("\n", "")
            if not url.endswith("m3u8") or not url.startswith("http"):
                continue
            videoPath = os.path.join(series_path, series_name + "_" + str(count) + ".ts")
            getVideo(url, videoPath)


def getVideo(m3u6_url, file_path):
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
        video_url = m3u6_url.replace("index.m3u8", line)
        res = retry_get(video_url, timeout=20, headers=send_headers)
        with open(file_path, 'ab') as f:
            f.write(res.content)
            f.flush()


def retry_get(url, timeout, headers, retry_count=3):
    logger.info(url)
    if retry_count <= 0:
        return Exception("获取失败", url)
    # noinspection PyBroadException
    try:
        res = requests.get(url, timeout=10, headers=headers)
        if res.status_code == 200:
            return res
        else:
            logger.info(url, "  重试 ", retry_count, )
            return retry_get(url, timeout, headers, retry_count - 1)
    except Exception:
        logger.info(url, "  重试 ", retry_count - 1, )
        return retry_get(url, timeout, headers, retry_count - 1)


if __name__ == '__main__':
    getSeries("url_list.txt", "蜗居", "F:/series")
    # series_path="F:/series"
    # if os.path.exists(series_path):  # 判断文件夹是否存在
    #     shutil.rmtree(series_path)
    # if not os.path.exists(series_path):
    #     os.makedirs(series_path)
    # #
    # with open("F:/series\\a.txt", 'ab') as f:
    #     f.write(b'222')
    #     f.flush()
