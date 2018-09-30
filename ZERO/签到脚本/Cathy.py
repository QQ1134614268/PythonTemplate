from selenium import webdriver
import xlrd 
import time

def readCell(file,page, row,Colume):#默认page=1,file一般不变
    cell=xlrd.open_workbook(file, 'r').sheet_by_index(page).cell(row, Colume)
    date = cell.value
#     cell  改变颜色re
    return date

def writeCell(file,page, row,Colume): 
#    xlwt
    return "sucess"
         
def ma(url,xpath,inputValue):
    browser = webdriver.Chrome()
    browser.maximize_window() # 窗口最大化
    browser.get('http://www.baidu.com/')#打开网址
#     操作页面,填值,点击
    browser.find_element_by_xpath('//*[@id="kw"]').send_keys('inputValue')
    browser.find_element_by_id("su").click()

def login():
    browser = webdriver.Chrome()

def verifyCode():#验证码
    browser = webdriver.Chrome()


browser=webdriver.Chrome()
browser.maximize_window() # 窗口最大化
