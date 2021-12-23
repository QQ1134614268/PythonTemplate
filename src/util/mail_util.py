# -*- coding:utf-8 -*-
"""
@Time: 2021/11/23
@Description:
"""
import smtplib
from email.header import Header
from email.mime.text import MIMEText

from util.log_util import logger as log

MAIL_TO = "1134614268@qq.com"
SERVER_MAIL = "1134614268@qq.com"
SERVER_MAIL_HOST = "smtp.qq.com"
SERVER_MAIL_PASS = "XXX"
SERVER_MAIL_PORT = 465


def send_email(mail_content, mail_to, subject="master,your mail"):
    message = MIMEText(mail_content, 'plain', 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')
    message['From'] = Header("明宇致和", 'utf-8')
    message['To'] = Header("朋友", 'utf-8')

    with smtplib.SMTP_SSL(SERVER_MAIL_HOST, SERVER_MAIL_PORT) as smtp_obj:
        # smtp_obj.set_debuglevel(1)
        smtp_obj.login(SERVER_MAIL, SERVER_MAIL_PASS)
        smtp_obj.sendmail(SERVER_MAIL, mail_to, message.as_string())
        log.info("邮件发送成功")


if __name__ == '__main__':
    send_email("hello world", '1134614268@qq.com', subject="master,your mail")
