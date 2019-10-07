# !usr/bin/python import urllib.request
# 88********************************************  ecplise 导入urllib 直接run,AttributeError: module 'urllib' has no attribute 'request'
# ecplise 导入 urllib.request  ,或者导入urllib debug  运行OK
# pycharm  OK
import urllib

# import urllib.request
response = urllib.request
response2 = response.urlopen("http://www.baidu.com");
# urllib.request.urlopen
print(response2.read().decode('utf-8'));


def foo(a, b, c, d):
    print(a)
    print(b)
    print(c)
    print(d)


foo(**{"b": 2, "a": 3, "c": 4, "d": 5})  # 按名称  传值
