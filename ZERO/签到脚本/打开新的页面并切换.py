'''
Created on 2018年6月7日

@author: Administrator
'''
import time
from selenium import webdriver

browser=webdriver.Chrome()
browser.maximize_window() # 窗口最大化 

browser.get('https://www.baidu.com') # 在当前浏览器中访问百度
 
# 新开一个窗口，通过执行js来新开一个窗口
js='window.open("https://www.sogou.com");'
browser.execute_script(js)
time.sleep(10)
print ("百度   句柄  ",browser.current_window_handle) # 输出当前窗口句柄（百度）
handles = browser.window_handles # 获取当前窗口句柄集合（列表类型）
print (handles) # 输出句柄集合
time.sleep(10)
for handle in handles:# 切换窗口（切换到搜狗）
    if handle!=browser.current_window_handle:
        print ('switch to ',handle)
        browser.switch_to_window(handle)
        print (browser.current_window_handle) # 输出当前窗口句柄（搜狗）
        break


browser.close() #关闭当前窗口（搜狗）.
time.sleep(10)
browser.switch_to_window(handles[0]) #切换回百度窗口
time.sleep(10)

time.sleep(10)
print(123)
browser.quit()