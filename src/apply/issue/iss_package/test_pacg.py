# -*- coding:utf-8 -*-
"""
@Time: 2023/6/15
@Description:
"""
import csv
from unittest import TestCase

import pcapng
from scapy.all import *


class TestPcap(TestCase):

    def test_run(self):

        packets = rdpcap('example.pcap')  # 'example.pcap' 是 pcap 文件名
        for packet in packets:
            # 可以通过 packet.show() 打印每个数据包的详细信息
            # 这里演示如何获取数据包的源地址和目标地址
            src = packet['IP'].src
            dst = packet['IP'].dst
            print(f'Source IP: {src}, Destination IP: {dst}')

    def test_run(self):

        with open('example.pcap', 'rb') as fp:
            pcap = pcapng.Reader(fp)
            for block in pcap:
                if isinstance(block, pcapng.blocks.EnhancedPacket):
                    print(block.packet_payload)

    def test_run(self):

        packets = rdpcap('sample.pcap')
        print(len(packets))

    def test_run(self):
        packets = rdpcap('sample.pcap')
        for packet in packets:
            if "IP" in packet:
                print(packet["IP"].src, packet["IP"].dst)

    def test_run(self):
        pkts = rdpcap("tcp02.pcap")
        pkt0 = pkts[0]
        dst = pkt0['Ethernet'].dst
        version = pkt0['IPv6'].version
        sport = pkt0['TCP'].sport

    def test_run(self):

        pkts = rdpcap("tcp02.pcap")
        pkt0 = pkts[0]

        headers = ['dst', 'src', 'type', 'version', 'tc', 'f1', 'plen', 'nh', 'hlim', 'IPsrc', 'IPdst', 'sport',
                   'dport',
                   'seq', 'ack',
                   'dataofs', 'reserved', 'flags', 'window', 'chksum', 'urgptr', 'optionsmss', 'optionsNOP0',
                   'optionsWScale',
                   'optionsNOP1', 'optionsNOP2', 'optionsSAckOK']

        a1 = pkt0['Ethernet'].dst
        a2 = pkt0['Ethernet'].src
        a3 = pkt0['Ethernet'].type

        b1 = pkt0['IPv6'].version
        b2 = pkt0['IPv6'].tc
        b3 = pkt0['IPv6'].fl
        b4 = pkt0['IPv6'].plen
        b5 = pkt0['IPv6'].nh
        b6 = pkt0['IPv6'].hlim
        b7 = pkt0['IPv6'].src
        b8 = pkt0['IPv6'].dst
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
        c16 = pkt0['TCP'].options[5][1]

        rows = [a1, a2, a3, b1, b2, b3, b4, b5, b6, b7, b8, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14,
                c15, c16]

        with open('test3.csv', 'w', newline='') as f:
            fcsv = csv.writer(f)
            fcsv.writerow(headers)
            fcsv.writerow(rows)
