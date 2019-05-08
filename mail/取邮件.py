
import poplib

from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

# 输入邮件地址，口令和 POP3 服务器地址
email = "xx@qq.com"
password  = "XX"
# 在对于的邮箱设置的SMTP/POP3里，找到对应的服务地址
pop3_server = "pop.qq.com"
# 连接到POP3服务器:
server = poplib.POP3_SSL(pop3_server, '995')
# 可以打开或关闭调试信息:
server.set_debuglevel(1)
# 可选:打印POP3服务器的欢迎文字:
print("getwelcome  ",server.getwelcome().decode('utf-8'))

# 身份认证
server.user(email)
server.pass_(password)

# stat()返回邮件数量和占用空间:
print('邮件数量: %s. 大小: %s' % server.stat())
# list()返回所有邮件的编号:
print("---验证是否执行3---")
resp, mails, octets = server.list()
# [b'1 9121', b'2 2540', b'3 51773', b'4 63830',
print("---resp1---",resp)
print("---mails2---",mails)
print("---octets3---",octets)

# 获取最新一封邮件, 注意索引号从1开始:
print("---验证是否执行123---")
index = len(mails)
print("---index---", index)
print("---压正是否执行6---")
resp1, lines2, octets3 = server.retr(index)
print("---resp---", resp1)
print("---lines---", lines2)
print("---octets---", octets3)

# lines存储了邮件的原始文本的每一行,
# 可以获得整个邮件的原始文本:
msg_content = b'\r\n'.join(lines2).decode('utf-8')
# 稍后解析出邮件，即完成下载邮件
msg = Parser().parsestr(msg_content)

# 接下来解析文件
def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value

def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset

# indent用于缩进显示:
def print_info(msg, indent=0):
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header=='Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % ('  ' * indent, header, value))
    if (msg.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % ('  ' * indent, n))
            print('%s--------------------' % ('  ' * indent))
            print_info(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type=='text/plain' or content_type=='text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % ('  ' * indent, content + '...'))
        else:
            print('%sAttachment: %s' % ('  ' * indent, content_type))

msg = Parser().parsestr(msg_content)

print_info(msg)
