# -*- coding:utf-8 -*-
import datetime
import random
import string
import threading
import time

import requests


# timer = threading.Timer(2.0, hello, ["Hawk"])
def getUtcTimeStr():
    default_time_str = '%Y_%m_%d_%H_%M_%S_%f'
    return datetime.datetime.utcnow().strftime(default_time_str)


def create_data(datatype, length):
    if datatype == "String" or datatype == "string":
        return ''.join(random.sample(string.ascii_letters + string.digits, length))
    if datatype == "Time" or datatype == "time":
        return getUtcTimeStr()
    if datatype == "Int" or datatype == "int":
        return random.randint(10 ** (length - 1), 10 ** length - 1)
    if datatype == "Float" or datatype == "float":
        return float(random.randint(10 ** (length - 1), 10 ** length - 1) / 100)


def register(data):
    host = "http://ggok.top"
    url = '/api/user_api/register'
    start_time = time.time()
    res = requests.post(host + url, json=data)
    end_time = time.time()
    exec_time = end_time - start_time
    print({"开始时间": start_time, "执行时间:": exec_time, "  执行结果:": res.text})


if __name__ == '__main__':
    result = []
    request_per = 10
    last_time = 60
    total = request_per * last_time
    data = [{
        "email": create_data("string", 10),
        "password": "123456",
        "username": create_data("string", 6),
    } for i in range(request_per * last_time)]
    request = []

    for i in range(request_per):
        arg = data[random.randint(0, total)]
        request.append(threading.Thread(target=register, args=(arg,)))

    for i in request:
        i.start()
