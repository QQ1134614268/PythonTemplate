from email.header import Header
from email.mime.text import MIMEText
import smtplib

# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "839238852@qq.com"  # 用户名
mail_pass = "ypeiornvjkjxbedc"  # 口令 

content = '''  三春巧画新时代
四海高歌大浪潮''' 
subject = '生日快乐'
 
sender = '839238852@qq.com'
receivers = ['1134614268@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
message = MIMEText(content, 'plain', 'utf-8')
message['Subject'] = Header(subject, 'utf-8')
message['From'] = Header("明宇致和", 'utf-8')
message['To'] = Header("天任", 'utf-8') 

try:
    smtpObj = smtplib.SMTP_SSL(mail_host, 465) 
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print ("邮件发送成功")
except smtplib.SMTPException:
    print ("Error: 无法发送邮件")
finally:
    smtpObj.quit()    
