# -*- coding: utf-8 -*-
from time import sleep

from appium import webdriver


def login():
    desired_caps = {'platformName': 'Android', 'platformVersion': '6.0.1', 'deviceName': 'Galaxy S6',
                    'appPackage': 'dji.go.v4', 'appActivity': 'dji.pilot.main.activity.DJILauncherActivity'}
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    try:
        driver.find_element_by_name('我').click()
        driver.find_element_by_name('登录').click()
        driver.find_element_by_name('请输入注册邮箱').send_keys('account')
        driver.find_element_by_id('dji.go.v4:id/cw1').send_keys('password')
        driver.find_element_by_name('登录').click()
        sleep(3)

        driver.find_element_by_name('设置').click()
        driver.find_element_by_name('退出DJI帐号').click()
        driver.find_element_by_name('确定').click()
        sleep(1)
        driver.quit()
    except Exception as e:
        print(e)
        driver.get_screenshot_as_file("failed.jpg")
        return False
    return True


if __name__ == '__main__':
    if login():
        print("该条用例执行成功")
    else:
        print("该条用例执行失败")
