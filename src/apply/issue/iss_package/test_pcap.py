# -*- coding:utf-8 -*-
"""
@Time: 2023/6/15
@Description:
"""
import csv
from unittest import TestCase

import pcapng
from scapy.all import *
from scapy.layers.inet import IP, TCP, UDP, ICMP
from scapy.layers.inet6 import IPv6
from scapy.layers.l2 import Loopback, Ether


class TestPcap(TestCase):
    def test1(self):
        ip = IP(src="10.0.0.1")
        ip.dst = "10.0.0.2"
        l3: IP = IP() / TCP()
        l2: Ether = Ether() / l3
        l4: IP = l2.getlayer(1)
        l5: TCP = l2.getlayer(2)

        IP(dst=RandIP())
        IP(dst="example.com")
        Ether(dst=RandMAC())
        IP(ttl=(1, 30))

        send(IP(dst="192.0.2.1") / UDP(dport=53))
        sendp(Ether() / IP(dst="192.0.2.1") / UDP(dport=53))

        ls(UDP())
        (Ether() / IPv6()).show()

        srloop(IP(dst="packetlife.net") / ICMP(), count=3)

        eth_packet = Ether()
        # 使用IP()方法生成一个网络层数据包
        ip_packet = IP()
        ipv6 = IPv6()
        # 使用TCP()方法生成一个tcp数据包
        tcp_packet = TCP()
        # 使用UDP()方法生成一个udp数据包
        udp_packet = UDP()
        # 使用ICMP()方法生成一个udp数据包
        icmp_packet = ICMP()

    def test_run(self):
        with open('test.h264.export.fenxi.video.pcapng', 'rb') as fp:
            pcap = pcapng.Reader(fp)
            for block in pcap:
                if isinstance(block, pcapng.blocks.EnhancedPacket):
                    print(block.packet_payload)

    def test_run4(self):
        packets = rdpcap('test-ggok-http.pcap')  # 'example.pcap' 是 pcap 文件名
        pkt0: Ether = packets[0]
        print(isinstance(pkt0, Loopback))  # 可以产生 Loopback 对象, 捕捉WiFi数据??
        print(pkt0.time)
        a1 = pkt0['Ethernet'].dst
        a2 = pkt0['Ethernet'].src
        a3 = pkt0['Ethernet'].type

        # 可以通过 pkt0.show() 打印每个数据包的详细信息
        # 这里演示如何获取数据包的源地址和目标地址
        # if "IP" in packet:
        # if isinstance(pkt0, pcapng.blocks.EnhancedPacket):
        # pkt0.packet_payload
        b1 = pkt0['IP'].version
        b2 = pkt0['IP'].dst
        b3 = pkt0['IP'].src

        # b1 = pkt0['IPv6'].version
        # b2 = pkt0['IPv6'].tc
        # b3 = pkt0['IPv6'].fl
        # b4 = pkt0['IPv6'].plen
        # b5 = pkt0['IPv6'].nh
        # b6 = pkt0['IPv6'].hlim
        # b7 = pkt0['IPv6'].src
        # b8 = pkt0['IPv6'].dst
        c1 = pkt0['TCP'].sport
        c2 = pkt0['TCP'].dport
        c3 = pkt0['TCP'].seq
        c4 = pkt0['TCP'].ack
        c5 = pkt0['TCP'].dataofs
        c6 = pkt0['TCP'].reserved
        c7 = pkt0['TCP'].flags
        c8 = pkt0['TCP'].window
        c9 = pkt0['TCP'].chksum
        c10 = pkt0['TCP'].urgptr
        c11 = pkt0['TCP'].options[0][1]
        c12 = pkt0['TCP'].options[1][1]
        c13 = pkt0['TCP'].options[2][1]
        c14 = pkt0['TCP'].options[3][1]
        c15 = pkt0['TCP'].options[4][1]


# https://www.cntofu.com/book/33/6.md 添加高级协议
class Disney(Packet):
    name = "DisneyPacket "
    fields_desc = [ShortField("mickey", 5),
                   XByteField("minnie", 3),
                   IntEnumField("donald", 1, {1: "happy", 2: "cool", 3: "angry"})]
