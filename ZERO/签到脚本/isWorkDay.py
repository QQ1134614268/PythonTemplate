import json
import time
from urllib import request


def isWorkDay():  # 代理
    date = time.strftime('%Y%m%d', time.localtime())
    url = "http://api.goseek.cn/Tools/holiday?date=" + date
    proxy = request.ProxyHandler({'http': "http://web-proxy.tencent.com:8080"})  # 设置代理
    opener = request.build_opener(proxy, request.HTTPHandler)
    request.install_opener(opener)
    data = request.urlopen(url).read().decode('utf-8') 
#     data= json.dumps(data)
    data = json.loads(data)
    if(data['code'] == 10000 and data['data'] == 0):
        return True
    else:
        return False


print(isWorkDay())
