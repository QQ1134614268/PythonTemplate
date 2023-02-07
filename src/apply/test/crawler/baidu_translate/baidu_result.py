# coding: utf-8
from bs4 import BeautifulSoup
from urllib import request
from urllib.parse import quote
import string

# 输入关键词,查找结果
question_word = "吃货 程序员"
url = "http://www.baidu.com/s?wd=" + question_word
url = quote(url, safe=string.printable)  # safe表示可以忽略的字符  编码中文
response = request.urlopen(url)
htmlpage = response.read().decode('utf-8')
# print(htmlpage)
soup = BeautifulSoup(htmlpage, 'lxml')
count = 0
for div in soup.findAll("div", {"class": "result c-container "}):
    count = count + 1
    a_click = div.find("a")  # 第一个a标签
    print("第", count, "个结果")
    print("----标题----" + str(a_click.text))  # 标题
    # print("-----标题----" + str(a_click.renderContents(), 'utf-8'))  # 标题
    print("----链接----" + str(a_click.get("href")))  # 链接
    print("----描述----" + str(div.find("div", {"class": "c-abstract"}).text))  # 描述
