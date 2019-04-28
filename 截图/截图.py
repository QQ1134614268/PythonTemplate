import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.maximize_window() # 窗口最大化 

pat="D:/bat/screenshot/"+"qiandao"+str(time.time())+".png"
print(pat)
time.sleep(2)
# driver.get('www.baidu.com')  
driver.get('http://www.baidu.com') 
driver.get_screenshot_as_file(pat)
driver.save_screenshot(str(3)+'.png')
driver.get('http://stock.eastmoney.com')
driver.get_screenshot_as_file(pat)
  
time.sleep(3)
driver.quit()