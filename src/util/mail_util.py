# -*- coding:utf-8 -*-
"""
@Time: 2021/11/23
@Description:
"""
import smtplib
import traceback
from email.header import Header
from email.mime.text import MIMEText

from util.log_util import logger as log

MAIL_TO = "1134614268@qq.com"
SERVER_MAIL = "1134614268@qq.com"
SERVER_MAIL_HOST = "smtp.qq.com"
SERVER_MAIL_PASS = "XXX"
PORT = 465


def send_email(mail_content, mail_to, subject="master,your mail"):
    message = MIMEText(mail_content, 'plain', 'utf-8')
    message['To'] = Header("朋友", 'utf-8')
    message['From'] = Header("明宇致和", 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtp_obj = smtplib.SMTP_SSL(SERVER_MAIL_HOST, PORT)
        smtp_obj.login(SERVER_MAIL, SERVER_MAIL_PASS)
        smtp_obj.sendmail(SERVER_MAIL, mail_to, message.as_string())
        log.info("邮件发送成功")
    except smtplib.SMTPException:
        traceback.print_exc()
        # 日志记录异常信息
        message = traceback.format_exc()
        # 邮件服务 发送异常通知邮件  邮件模板
        log.error("Error: 无法发送邮件.[原因]" + message)
    finally:
        smtp_obj.quit()


if __name__ == '__main__':
    send_email("hello world", '1134614268@qq.com', subject="master,your mail")
