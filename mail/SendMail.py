from email.header import Header
from email.mime.text import MIMEText
import smtplib


def sendEmail(mail_content, mail_to, subject="master,your mail"):
    # 第三方 SMTP 服务 修改mail_sender mail_pass参数
    mail_host = "smtp.qq.com"  # 设置服务器
    mail_sender = "xxx@qq.com"  # 用户名
    mail_pass = "XX"  # 口令
    
    message = MIMEText(mail_content, 'plain', 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')
    message['From'] = Header("明宇致和", 'utf-8')
    message['To'] = Header("朋友", 'utf-8')
    
#     # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
#     with open('''D:\\py\\www\\img\\android-icon.png''', 'rb') as f:
#         # 设置附件的MIME和文件名，这里是png类型:
#         mime = MIMEBase('image', 'png', filename='android-icon.png')
#         # 加上必要的头信息:
#         mime.add_header('Content-Disposition', 'attachment', filename='android-icon.png')
#         mime.add_header('Content-ID', '<0>')
#         mime.add_header('X-Attachment-Id', '0')
#         # 把附件的内容读进来:
#         
#         mime.set_payload(f.read())
#         # 用Base64编码:
#         encoders.encode_base64(mime)
#         # 添加到MIMEMultipart:
#         message.attach(mime)
    
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465) 
        smtpObj.set_debuglevel(1)
        smtpObj.login(mail_sender, mail_pass)
        smtpObj.sendmail(mail_sender, mail_to, message.as_string())
        print ("邮件发送成功")
    except smtplib.SMTPException:
        print ("Error: 无法发送邮件")
    finally:
        smtpObj.quit() 

        
sendEmail("hello world", '1134614268@qq.com')


def sendEmail2(sendMail, token_password, receiveMail, host, port, message, subject, nickname, frinds_nickname, slave):
    mail = MIMEText(message, 'plain', 'utf-8')
    mail['Subject'] = Header(subject, 'utf-8')
    mail['From'] = Header(nickname, 'utf-8')
    mail['To'] = Header(frinds_nickname, 'utf-8') 
    try:
        smtpObj = smtplib.SMTP_SSL(host, port) 
        smtpObj.login(sendMail, token_password)
        smtpObj.sendmail(sendMail, receiveMail, mail.as_string())
        print ("邮件发送成功")
    except smtplib.SMTPException:
        print ("Error: 无法发送邮件")
    finally:
        smtpObj.quit() 
        
# #推荐使用html格式的正文内容，这样比较灵活，可以附加图片地址，调整格式等
# with open('abc.html','r') as f:
# content = f.read()
# #设置html格式参数
# part1 = MIMEText(content,'html','utf-8')
# 
# basename = os.path.basename("report.txt")
# #添加一个txt文本附件
# with open('report.txt','r')as h:
# content2 = h.read()
# #设置txt参数
# part2 = MIMEText(content2,'plain','utf-8')
# 
# #附件设置内容类型，方便起见，设置为二进制流
# part2['Content-Type'] = 'application/octet-stream'
# #设置附件头，添加文件名
# part2['Content-Disposition'] = 'attachment;filename=%s' % basename
# 
# #解决中文附件名乱码问题 
# # part2.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', basename))
# 
# #添加照片附件
# with open('1.png','rb')as fp:
# picture = MIMEImage(fp.read())
# #与txt文件设置相似
# picture['Content-Type'] = 'application/octet-stream'
# picture['Content-Disposition'] = 'attachment;filename="1.png"'
# #将内容附加到邮件主体中
# message.attach(part1)
# message.attach(part2)
# message.attach(picture)
