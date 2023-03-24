# coding: utf-8
from time import sleep

from appium import webdriver

desired_caps = {'platformName': 'Android',
                'deviceName': '127.0.0.1:52001',
                'platformVersion': '23',
                'appPackage': 'com.jingdong.app.mall',
                'appActivity': 'com.jingdong.app.mall.main.MainActivity',
                'unicodeKeyboard': True,
                'resetKeyboard': True
                }
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
#
# driver.delete_all_cookies()
# driver.get_cookies()
# driver.get_cookie()
# driver.add_cookie()  #  cookie
# driver.reset() 重置应用,清除应用数据
# hide_keyboard
# driver.context隐藏键盘 dr.keyevent(‘4’)发送按键码  driver.current_url
# driver.current_activity
# driver.get("/wd/hub/session/:sessionId?/cookie")
# print(driver.current_url())


driver.get_cookies()
sleep(10)
print(111)
driver.add_cookie({'name': 'foo', 'value': 'bar'})
print("f all ")
driver.get_cookies()
print(str(driver.get_cookies()))
driver.add_cookie({'name': 'BAIDUID', 'value': 'AAAA:FG=1'})
print("add   BAIDUID ")
print(str(driver.get_cookie("BAIDUID")))
print("f add all ")
print(str(driver.get_cookies()))
print("f delete_all_cookies all ")
driver.delete_all_cookies()
print(str(driver.get_cookies()))

buttons = driver.find_element_by_name(u"我的")
driver.get_screenshot_as_file('E:/login2.png')
buttons.click()
try:
    buttons = driver.find_element_by_name(u"登录/注册")  # 点击登录
    buttons.click()
    sleep(5)
    print(driver.page_source)  # 打印当前页面 xml
    # 登录
    # buttons = driver.find_element_by_name(u"账号密码登录").click()
    buttons = driver.find_element_by_id(u"com.jd.lib.login:id/pe").send_keys("188XXX7398")
    sleep(3)
    buttons = driver.find_element_by_id(u"com.jd.lib.login:id/pg").send_keys("XXX")
    sleep(3)
    buttons = driver.find_element_by_name(u"登录").click()
except Exception as e:
    print(e)
sleep(3)
buttons = driver.find_element_by_id("com.jingdong.app.mall:id/bik").click()
# 搜索
buttons = driver.find_element_by_id("com.jingdong.app.mall:id/a4_")
buttons.click()
sleep(3)
buttons = driver.find_element_by_id("com.jd.lib.search:id/xs").send_keys("运动鞋")
sleep(3)
buttons = driver.find_element_by_id("com.jd.lib.search:id/ah0")
#  点击第一个结果
buttons = buttons.find_element_by_class_name("android.widget.LinearLayout")
sleep(3)
buttons.click()
