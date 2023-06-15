#!/usr/bin/env python
# -*- coding:UTF-8 -*-

# 一、协议组成：pcap协议、IP协议、MAC协议、UDP协议

from __future__ import division

import struct
import sys
from collections import OrderedDict

pcap_header = OrderedDict([
    # 4字节 pcap文件的magic num 目前为0xD4C3B2A1
    ('magic', ['unsigned int', 1]),
    # 2字节 主版本号 #define PCAP_VERSION_MAJOR 2
    ('version_major', ['unsigned short', 1]),
    # 2字节 次版本号 #define PCAP_VERSION_MINOR 4
    ('version_minor', ['unsigned short', 1]),
    # 4字节 时区修正 未使用，目前全为0
    ('this_zone', ['unsigned int', 1]),
    # 4字节 精确时间戳 未使用，目前全为0
    ('sig_figs', ['unsigned int', 1]),
    # 4字节 抓包最大长度 如果要抓全，设为0x0000ffff（65535）,tcpdump -s 0就是设置这个参数，缺省为68字节
    ('snap_len', ['unsigned int', 1]),
    # 4字节 链路类型 一般都是1：ethernet
    ('link_type', ['unsigned int', 1])
])

# 数据包头 16字节
packet_header = OrderedDict([
    # struct timeval ts 8字节 抓包时间 4字节表示秒数，4字节表示微秒数
    ('time_ms', ['unsigned int', 1]),
    ('time_ns', ['unsigned int', 1]),
    # 4字节 保存下来的包长度（最多是snap_len，比如68字节）
    ('cap_len', ['unsigned int', 1]),
    # 4字节 数据包的真实长度，如果文件中保存的不是完整数据包，可能比cap_len大
    ('len', ['unsigned int', 1]),
])

# mac报文头：14字节
mac_header = OrderedDict([
    ('dst_mac', ['char[]', 6]),
    ('src_mac', ['char[]', 6]),
    ('eth_type', ['unsigned short', 1])
])
# IP报文头：20字节
ip_header = OrderedDict([
    ('ver_h_len', ['unsigned char', 1]),
    ('tos', ['unsigned char', 1]),
    ('tot_len', ['unsigned short', 1]),
    ('id', ['unsigned short', 1]),
    ('frag_off', ['unsigned short', 1]),
    ('ttl', ['unsigned char', 1]),
    ('protocol', ['unsigned char', 1]),
    ('ip_chk_sum', ['unsigned short', 1]),
    ('src_add_r', ['char[]', 4]),
    ('dst_add_r', ['char[]', 4])
])
# UDP报文头：8字节
udp_header = OrderedDict([
    ('src_port', ['unsigned short', 1]),
    ('dst_port', ['unsigned short', 1]),
    ('uhl', ['unsigned short', 1]),
    ('chk_sum', ['unsigned short', 1])
])
# 7、TCP报文头
tcp_header = OrderedDict([
    ('src_port', ['unsigned short', 1]),
    ('det_port', ['unsigned short', 1]),
    ('seq_num', ['unsigned int', 1]),
    ('ack_num', ['unsigned int', 1]),
    ('data_off', ['char', 1]),
    ('reserved_urg_ack', ['char[]', 2]),
    ('PSH_RST_SYN_FIN', ['char[]', 1]),
    ('window', ['unsigned short', 1]),
    ('chk_sum', ['unsigned short', 1]),
    ('urp', ['unsigned short', 1]),
])
# struct库解析C语言结构体格式
c_type = OrderedDict([
    ('pad byte', 'x'),
    ('char', 'c'),
    ('signed char', 'b'),
    ('unsigned char', 'B'),
    ('_bool', '?'),
    ('short', 'h'),
    ('unsigned short', 'H'),
    ('int', 'i'),
    ('unsigned int', 'I'),
    ('long', 'l'),
    ('unsigned long', 'L'),
    ('long long', 'q'),
    ('unsigned long long', 'Q'),
    ('float', 'f'),
    ('double', 'd'),
    ('char[]', 's'),  # ('char[]', 'p'),
    ('void *', 'P'),
])


# python16进制转十进制数据
def intToHex(message):
    message_type = dict(zip([str(_) for _ in range(10)] + ['a', 'b', 'c', 'd', 'e', 'f'], range(16)))
    total = 0
    message = '0' * (4 - len(hex(message)[2:])) + hex(message)[2:]
    for _ in range(len(message)):
        if _ % 2 == 0:
            total += message_type[message[_]] * 16 ** (_ + 1)
        else:
            total += message_type[message[_]] * 16 ** (_ - 1)
    return total


# /根据struct库以及相关报文结构解析数据
def analysis_message(message_kv, message):
    soft_struct = '=' + ' '.join([str(_[1]) + c_type[_[0]] for _ in message_kv.values()])
    analysis_soft = lambda x: struct.unpack(soft_struct, x)
    return dict(zip(message_kv.keys(), analysis_soft(message)))


# 读取pcap包函数：以目的IP为键，将UDP数据以列表形式插入字典中。
def read_pcap(file):
    with open(file, 'rb') as f:
        message = f.read()
    start = 24
    __message = OrderedDict([('dst_mac', '= 6B'), ('src_mac', '= 6B'), ('src_add_r', '= 4B'), ('dst_add_r', '= 4B')])
    message_kv = OrderedDict((k, v) for _ in [packet_header, mac_header, ip_header, udp_header] for k, v in _.items())
    all_message = OrderedDict()
    m_len = len(message)
    while True:
        r_message = analysis_message(message_kv, message[start: start + 58])
        if r_message['protocol'] == 17:
            [r_message.update({k: '.'.join(
                [str(_) for _ in struct.unpack(v, r_message[k])])}) for k, v in __message.items()]
            r_message['dst_port'] = intToHex(r_message['dst_port'])
            r_message['src_port'] = intToHex(r_message['src_port'])
            r_message['uhl'] = intToHex(r_message['uhl'])
            r_message.update({'udp_message': message[start + 58: start + r_message['uhl']]})
            start += r_message['uhl'] + 50
            topic[r_message['dst_port'] % 10000] += 1
            if r_message['dst_add_r'] not in all_message.keys():
                all_message.update({r_message['dst_add_r']: [r_message]})
            else:
                all_message[r_message['dst_add_r']].append(r_message)
        if m_len - start <= 20:
            break
    return all_message


# 根据mac头，IP头，UDP头以及UDP数据进行对比解析数据的正确性
def compareMsg(ot_dict, ot1_dict, key):
    all_dst_ip = [_ for _ in ot_dict.keys() if _ in ot1_dict.keys()]
    all_list = [[ot_dict[_], ot1_dict[_]] for _ in all_dst_ip]
    if type(key) is list:
        total = [False not in [k[0][i][_] == k[1][i][_] for _ in key]
                 for k in all_list for i in range(min(len(k[0]), len(k[1])))]
    else:
        total = [k[0][i] == k[1][i] for k in all_list for i in range(min(len(k[0]), len(k[1])))]
    success = [_ for _ in range(len(total)) if total[_]]
    error = [_ for _ in range(len(total)) if not total[_]]
    print('start to compare pcap data'.center(50, '='))
    print('The packets num of  first: %s packets' % sum([len(_) for _ in hy_dict.values()]))
    print('The packets num of second: %s packets' % sum([len(_) for _ in ot_dict.values()]))
    print('The packets num of   same: %s packets' % len(total))
    print('start'.center(50, '='))
    print('success num: %s packets' % len(success))
    print('  error num: %s packets' % len(error))
    print('end'.center(50, '='))


if __name__ == '__main__':
    if len(sys.argv) == 3:
        hy_message = read_pcap(sys.argv[1])
        ot_message = read_pcap(sys.argv[2])
        compare_key = list(mac_header.keys()) + list(ip_header.keys()) + list(udp_header.keys()) + ['udp_message']
        compareMsg(hy_message, ot_message, key=compare_key)
    else:
        print('Need 2 parameters: first pcap, second pcap')
