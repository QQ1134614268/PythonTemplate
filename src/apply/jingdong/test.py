# -*- coding: utf-8 -*-
from appium import webdriver
from time import sleep


def login():
    try:
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = 'Galaxy S6'
        desired_caps['appPackage'] = 'dji.go.v4'
        desired_caps['appActivity'] = 'dji.pilot.main.activity.DJILauncherActivity'
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

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
    if (True == login()):
        print("该条用例执行成功")
    else:
        print("该条用例执行失败")