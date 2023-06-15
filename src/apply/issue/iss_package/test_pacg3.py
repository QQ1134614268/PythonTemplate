#!/usr/bin/python
#-*- coding:utf8 -*-

from scapy.all import *
import collections
import os
import re
import sys
import zlib

# 指定保存图片的目录和pcap文件的路径
OUTDIR = '/home/kali/D/pictures'
PCAPS = '/home/kali/D'
# Response命名元组，数据包头header，载荷payload
Response = collections.namedtuple('Response',['header','payload'])

# 获取数据包头（读取原始HTTP流量，将数据头单独切出来）
def get_header(payload):
    try:
        # 从数据包开头往下找两个连续的\r\n，把这整段数据切出来
        header_raw = payload[:payload.index(b'\r\n\r\n')+2]
    except ValueError:
        # 如果不存在就报异常，并输出符号“-”
        sys.stdout.write('-')
        sys.stdout.flush()
        return None
    # 如果没发生异常，就将HTTP头中的每一行以冒号分割，冒号左边是字段名，右边是字段值，然后存储在header字典中
    # 这里由于运行报错的原因（utf-8编码报错），使用了ISO-8859-1编码
    header = dict(re.findall(r'(?P<name>.*?): (?P<value>.*?)\r\n', header_raw.decode('ISO-8859-1')))
    # 如果HTTP头中没有名为Content-Type的字段，就返回None
    if 'Content-Type' not in header:
        return None
    return header

# 提取数据包内容，image是我们想提取的数据类型的名字
def extract_content(Response, content_name = 'image'):
    content, content_type = None, None
    # 含有图片的响应包，数据头的Content-Type会有image标识
    if content_name in Response.header['Content-Type']:
        # 将数据头中指定的实际数据类型保存下来
        content_type = Response.header['Content-Type'].split('/')[1]
        # 将HTTP头之后的全部数据保存下来
        content = Response.payload[Response.payload.index(b'\r\n\r\n')+4:]
        # 如果数据被gzip或deflate之类的工具压缩过，就调用zlib来解压
        # 这里使用Content-Encoding报错，因此使用Accept-Encoding
        if 'Accept-Encoding' in Response.header:
            # if Response.header['Content-Encoding'] == 'gzip':
            if Response.header['Accept-Encoding'] == 'gzip':
                content = zlib.decompress(Response.payload, zlib.MAX_WBITS | 32)
            elif Response.header['Accept-Encoding'] == 'deflate':
                content = zlib.decompress(Response.payload)
    return content, content_type

# 重构在数据包中出现过的图片
class Recapper:
    # 将要读取的pcap文件路径传给它
    def __init__(self,fname):
        pcap = rdpcap(fname)
        # TCP数据流保存到字典里
        self.sessions = pcap.sessions()
        self.responses = list()

    # get_responses的作用是从pcap文件中遍历读取响应数据
    def get_responses(self):
        # 遍历整个sessions字典中的每个会话
        for session in self.sessions:
            payload = b' '
            # 遍历每个会话中的每个数据包
            for packet in self.sessions[session]:
                try:
                    # 过滤数据，只处理发往80或者从80端口接收的数据
                    if packet[TCP].dport == 80 or packet[TCP].sport == 80:
                        # 把所有读取到的数据载荷做拼接
                        # 相当于wireshark中右键单击一个数据包，点击“Follow TCP Stream”
                        payload += bytes(packet[TCP].payload)
                except IndexError:
                    # 如果报错就打印一个“x”
                    sys.stdout.write('x')
                    sys.stdout.flush()
            # 如果payload有数据，就将其交给get_header函数解析
            if payload:
                header = get_header(payload)
                if header is None:
                    continue
                # 把构造出的response对象附加到responses列表中
                self.responses.append(Response(header=header,payload=payload))

    # write的作用是把在响应数据中找到的图片写入到输出目录里
    def write(self,content_name):
        # 遍历所有responses响应
        for i,response in enumerate(self.responses):
            # 提取响应中的内容
            content, content_type = extract_content(response,content_name)
            if content and content_type:
                fname = os.path.join(OUTDIR, f'ex_{i}.{content_type}')
                print(f'Writing {fname}')
                # 将内容写到一个文件里
                with open(fname, 'wb') as f:
                    f.write(content)

if __name__ == '__main__':
    pfile = os.path.join(PCAPS, 'test.pcap')
    recapper = Recapper(pfile)
    recapper.get_responses()
    recapper.write('image')
