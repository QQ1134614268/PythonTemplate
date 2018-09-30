import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import logging  

def log(mes,filename='D:/bat/log/task3.log'):
    formatter_str='[%(asctime)s][%(filename)s] -- %(message)s'#日志格式
    formatter = logging.Formatter(formatter_str) 
    logger = logging.getLogger('mylogger')   
    logger.setLevel(logging.DEBUG)  
    fh = logging.FileHandler(filename)
    fh.setLevel(logging.DEBUG) 
    fh.setFormatter(formatter)
    logger.addHandler(fh)#添加标准输出
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    logger.info(mes)
    #  添加下面一句，在记录日志之后移除添加的一个句柄
    logger.removeHandler(ch)
    logger.removeHandler(fh)
    
import smtplib
from email.mime.text import MIMEText
from email.header import Header
def sendEmail(mail_content,mail_to,subject="master,your mail"):
    # 第三方 SMTP 服务
    mail_host="smtp.qq.com"  #设置服务器
    mail_sender="839238852@qq.com"    #用户名
    mail_pass="ypeiornvjkjxbedc"   #口令 
    
    message = MIMEText(mail_content, 'plain', 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')
    message['From'] = Header("明宇致和", 'utf-8')
    message['To'] =  Header("天任", 'utf-8') 
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465) 
        smtpObj.set_debuglevel(1)
        smtpObj.login(mail_sender,mail_pass)
        smtpObj.sendmail(mail_sender, mail_to, message.as_string())
        log ("邮件发送成功")
    except smtplib.SMTPException:
        log ("Error: 无法发送邮件")
    finally:
        smtpObj.quit()  
        
import random   
time.sleep(random.randint(0,90))
    
browser=webdriver.Chrome()
browser.maximize_window() # 窗口最大化 
 
browser.get('http://club.oa.com/club/#/topic/input/0')  
time.sleep(3)
browser.find_element_by_xpath('//*[@id="btn_smartlogin"]').click() 
time.sleep(2)
browser.get('http://club.oa.com/club/#/topic/input/0') # 在当前浏览器中访问百度
time.sleep(2)
browser.find_element_by_xpath('//*[@id="txtTitle"]').send_keys('签到贴')
time.sleep(2)
browser.find_element_by_xpath('//input[@class="form-control border-radius-sm  datachooser ng-valid"]').send_keys('健身班')
time.sleep(1)
browser.find_element_by_xpath('''//a[@ tabindex="-1" and @class="ng-binding"]''').click()
time.sleep(2)
in_text='''发帖需选择协会，若无该协会选项，请先加入协会；
发帖子，每天第一个帖+1分，被管理员加精+10分，被赞超50个+30分，删帖将扣除相应分数；
由于需要计算积分的原因，提交后将不能修改相关协会。--这是一个快乐的小尾巴'''
a = browser.find_element_by_xpath('//*[@id="txtContent_ifr"]')
browser.switch_to.frame(a)
time.sleep(2)
browser.find_element_by_xpath('//*[@id="tinymce"]').send_keys(in_text)
time.sleep(2)
browser.switch_to.default_content()
js="var q=document.documentElement.scrollTop=100000"  
browser.execute_script(js)
time.sleep(1)
browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/div/div[2]/form/div[4]/div/button[2]').click()
time.sleep(2)
path="D:/bat/screenshot/"+"qiandao"+str(time.time())+".png"
browser.get_screenshot_as_file(path) 
log("健身签到完成")
sendEmail("健身签到成功", "1134614268@qq.com", "your mail, master")
browser.quit()