# -*- coding:utf-8 -*-
import json
from urllib import request

import time

date = time.strftime('%Y%m%d', time.localtime(time.time()))
url = "http://api.goseek.cn/Tools/holiday?date=" + date
req = request.Request(url)
res = request.urlopen(req)
data = res.read()
data = str(data, encoding="utf-8")
print(data)
# data= json.dumps(data)
data = json.loads(data)
code = data['code']
data = data['data']
holiday = -1
if code == 10000:
    holiday = data
    print(holiday)
else:
    holiday = "err"
