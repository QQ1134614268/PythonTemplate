import random
import time
from selenium import webdriver

time.sleep(random.randint(0, 1))
browser = webdriver.Chrome()
browser.maximize_window()  # 窗口最大化
browser.get('http://xx.com')
time.sleep(1.5)
browser.find_element_by_xpath('//*[@id="username"]').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="username"]').send_keys('xx')
time.sleep(1)
browser.find_element_by_xpath('//*[@id="password_input"]').send_keys('xx')
time.sleep(1)
browser.find_element_by_xpath('//*[@id="login_button"]').click()  # 登录
