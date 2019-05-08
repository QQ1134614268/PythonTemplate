import logging  
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys 


def log(mes, filename='D:/bat/log/zhong.log'):
    logger = logging.getLogger('mylogger')   
    logger.setLevel(logging.DEBUG)  
    fh = logging.FileHandler(filename)
    fh.setLevel(logging.DEBUG) 
    formatter_str = '[%(asctime)s][%(filename)s] -- %(message)s'
    formatter = logging.Formatter(formatter_str)  
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    logger.info(mes)
    
    
browser = webdriver.Chrome()
browser.maximize_window()  # 窗口最大化 
 
browser.get('http://fund.eastmoney.com/001677.html')  
time.sleep(3)
price = browser.find_element_by_xpath('//*[@id="gz_gsz"]').text
message = "中银战略新兴 价格: " + price
log(message, 'D:/桌面文件夹/news.txt')
time.sleep(10)
browser.quit()
