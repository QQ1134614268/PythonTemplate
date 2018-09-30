import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import logging  
import random   
browser=webdriver.Chrome()
browser.maximize_window() # 窗口最大化 file:///D:/%E6%A1%8C%E9%9D%A2%E6%96%87%E4%BB%B6%E5%A4%B9/test.html
path='file:///E:/Java/python/web2/SelenuimTest.html'
browser.get(path)


 
# 1.串联寻找
print ('查找 B  div  '+browser.find_element_by_id('B').find_element_by_tag_name('div').text)

# 2.xpath父子关系寻找
print ('''查找//div[@id='B']/div  '''+browser.find_element_by_xpath("//div[@id='B']/div").text)

# 3.css selector父子关系寻找
print ('查找div#B>div  '+browser.find_element_by_css_selector('div#B>div').text)

# 4.css selector nth-child
print ('查找div#B div:nth-child(1)  '+browser.find_element_by_css_selector('div#B div:nth-child(1)').text)

# 5.css selector nth-of-type
print ('查找div#B div:nth-of-type(1)  '+browser.find_element_by_css_selector('div#B div:nth-of-type(1)').text)

# 6.xpath轴 child
print ('''查找//div[@id='B']/child::div  '''+browser.find_element_by_xpath("//div[@id='B']/child::div").text)

'''=========子节点找父节点============'''
# 1.xpath: `.`代表当前节点; '..'代表父节点
print ('''查找//div[@id='C']/../..  '''+browser.find_element_by_xpath("//div[@id='C']/../..").text)

# 2.xpath轴 parent
print ('查找parent /parent::*/parent::div '+browser.find_element_by_xpath("//div[@id='C']/parent::*/parent::div").text)

# 1.xpath,通过父节点获取其哥哥节点
print ('查找/../div[1]  '+browser.find_element_by_xpath("//div[@id='D']/../div[1]").text)

# 2.xpath轴 preceding-sibling
print ('查找/preceding-sibling::div[1]  '+browser.find_element_by_xpath("//div[@id='D']/preceding-sibling::div[1]").text)

# 1.xpath，通过父节点获取其弟弟节点
print ('查找/../div[3]  '+browser.find_element_by_xpath("//div[@id='D']/../div[3]").text)

# 2.xpath轴 following-sibling
print ('查找/following-sibling::div[1]  '+browser.find_element_by_xpath("//div[@id='D']/following-sibling::div[1]").text)

# 3.xpath轴 following
print ('查找/following::*  '+browser.find_element_by_xpath("//div[@id='D']/following::*").text)
'================兄弟节点====================='
# 4.css selector +
print ('查找div#D + div  '+browser.find_element_by_css_selector('div#D + div').text)

# 5.css selector ~

print ('查找div#D ~ div  '+browser.find_element_by_css_selector('div#D ~ div').text)
'============================================='
time.sleep(5)
print ('通过 id  '+ browser.find_element_by_id("D").text)
print ('通过 classname  '+browser.find_element_by_class_name("classname").text)
print ('标签为div  '+browser.find_element_by_tag_name("div").text)#list集合
print ('查找name属性   '+browser.find_element_by_name("name").text)
print ('通过css_selector  '+browser.find_element_by_css_selector("div#D").text)
print ('通过css_selector  '+browser.find_element_by_css_selector(".classname").text)
print ('通过css_selector  '+browser.find_element_by_css_selector("[name='name']").text)
print ('通过css_selector  '+browser.find_element_by_css_selector("div>div.classname").text)
print ('通过css_selector  '+browser.find_element_by_css_selector("div[name='name'][class='classname']").text)
# print (browser.find_element_by_link_text("this is D").text)#  通过文本找  报错
# print (browser.find_element_by_partial_link_text("s ").text)#  通过文本找  报错

browser.quit()
