from email.header import Header
from email.mime.text import MIMEText
import json
import logging  
import random   
import smtplib
import time
from urllib import request

from selenium import webdriver


def log(mes, filename='D:/bat/log/task3.log'):
    formatter_str = '[%(asctime)s][%(filename)s] -- %(message)s'  # 日志格式
    formatter = logging.Formatter(formatter_str) 
    logger = logging.getLogger('mylogger')   
    logger.setLevel(logging.DEBUG)  
    fh = logging.FileHandler(filename)
    fh.setLevel(logging.DEBUG) 
    fh.setFormatter(formatter)
    logger.addHandler(fh)  # 添加标准输出
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    logger.info(mes)
    #  添加下面一句，在记录日志之后移除添加的一个句柄
    logger.removeHandler(ch)
    logger.removeHandler(fh)

    
def sendEmail(mail_content, mail_to, subject="master,your mail"):
    # 第三方 SMTP 服务
    mail_host = "smtp.qq.com"  # 设置服务器
    mail_sender = "1134614268@qq.com"  # 用户名
    mail_pass = "ragrmyytlnsuibih"  # 口令 
    
    message = MIMEText(mail_content, 'plain', 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')
    message['From'] = Header("明宇致和", 'utf-8')
    message['To'] = Header("天任", 'utf-8') 
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465) 
        smtpObj.set_debuglevel(1)
        smtpObj.login(mail_sender, mail_pass)
        smtpObj.sendmail(mail_sender, mail_to, message.as_string())
        log ("邮件发送成功")
    except smtplib.SMTPException:
        log ("Error: 无法发送邮件")
    finally:
        smtpObj.quit()  


def isWorkDay():
    date = time.strftime('%Y%m%d', time.localtime())
    url = "http://api.goseek.cn/Tools/holiday?date=" + date
    proxy = request.ProxyHandler({'http': "http://web-proxy.tencent.com:8080"})  # 设置代理
    opener = request.build_opener(proxy, request.HTTPHandler)
    request.install_opener(opener)
    data = request.urlopen(url).read().decode('utf-8') 
    # data= json.dumps(data)
    data = json.loads(data)
    if(data['code'] == 10000 and data['data'] == 0):
        return True
    else:
        return False 

           
def main():
    if not isWorkDay():
        return 
    try:
        time.sleep(random.randint(0, 1)) 
        browser = webdriver.Chrome()
        browser.maximize_window()  # 窗口最大化
        browser.get('http://om.tencent.com/attendances/check_out/5575965?from=TAPD') 
        time.sleep(1.5)
        browser.find_element_by_xpath('//*[@id="username"]').click() 
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="username"]').send_keys('v_xranhuang')
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="password_input"]').send_keys('Apple666')
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="login_button"]').click()  #   登录
        browser.get('http://om.tencent.com/attendances/check_out/5575965?from=TAPD')  
        
        localtime = time.localtime()
        m = time.strftime("%p", localtime)
        mybool = "没有验证码"
        if m == "AM":  # 上午签到
            browser.find_element_by_xpath('//*[@id="checkin_btn"]').click()
            time.sleep(2)
            try:
                browser.find_element_by_xpath('//*[@id="code_input"]')
                mybool = "快去签到----------有验证码----------0.0"
            except:
                browser.find_element_by_xpath('//*[@id="tdialog-buttonwrap"]/a[1]/span').click() 
                time.sleep(1)
                path = "D:/bat/screenshot/" + "zaoshang" + str(time.time()) + ".png"
                browser.get_screenshot_as_file(path)
                time.sleep(5)
        elif m == "PM":  # 下午签出
            browser.find_element_by_xpath('//*[@id="checkout_btn"]').click()
            time.sleep(2)
            try:
                browser.find_element_by_xpath('//*[@id="code_input"]')
                mybool = "快去签到----------有验证码----------0.0"
            except:
                browser.find_element_by_xpath('//*[@id="tdialog-buttonwrap"]/a[1]/span').click()
                time.sleep(1)
                path = "D:/bat/screenshot/" + "xiawu" + str(time.time()) + ".png"
                browser.get_screenshot_as_file(path)
                time.sleep(5)
        else:
            log("this is time error,search time error")
        log(mybool + " " + m + " 签到", 'D:/bat/log/task3.log')  # 'D:/bat/log/task3.log' 路径必须存在,否则报错
        sendEmail(mybool + " " + m + " 签到" + " " + "sucess", "1134614268@qq.com", "your mail, master")
        browser.quit()
    except:
        sendEmail("----error---bug---", "1134614268@qq.com", "your mail, master")


main()
