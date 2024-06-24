# -*- coding:utf-8 -*-
# 参考网址: https://www.jianshu.com/p/491d6590b2a0
import json

import requests

if __name__ == '__main__':
    # 1.  Get请求
    res = requests.get("http://httpbin.org/get")
    print(res.text)  # 自动按默认utf-8解码
    # 1.2 HTTPS,GET请求,带中文参数
    res = requests.get("https://httpbin.org/get?name=张三&age=12")  # 自动编码
    print(res.text)  # 自动按默认utf-8解码

    # 2. Post x-www-form-urlencoded传统表单请求
    # POST http://httpbin.org/post 请求数据: name=张三&age=12
    data = {"name": "张三", "age": 12}
    res = requests.post("http://httpbin.org/post", data=data)  # 自动编码
    print(res.text)

    # 3. Post application/json请求
    # POST http://httpbin.org/post 请求数据: {"name": "张三","age": 12}
    data = {"name": "张三", "age": 12}
    res = requests.post("http://httpbin.org/post", json=data)
    print(res.json())  # 转为字典格式

    # 3.2 Post application/json请求
    data = {"name": "张三", "age": 12}
    headers = {"Content-Type": "application/json"}
    res = requests.post("http://httpbin.org/post", data=json.dumps(data), headers=headers)
    print(res.json())  # 转为字典格式
