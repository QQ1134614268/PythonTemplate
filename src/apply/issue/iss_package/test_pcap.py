# -*- coding:utf-8 -*-
"""
@Time: 2023/6/15
@Description:
"""
from unittest import TestCase

from scapy.all import *
from scapy.layers.http import HTTP
from scapy.layers.inet import IP, TCP, ICMP
from scapy.layers.inet import UDP
from scapy.layers.l2 import Ether
from scapy.layers.l2 import Loopback
from scapy.layers.tls.session import TLSSession


class TestPcap(TestCase):
    def test0(self):
        # 构造报文
        ether = Ether(dst='00:0c:29:47:f3:2f', src='c8:3a:35:09:ef:a1', type=0x86dd)
        ip = IP(src="10.0.0.1", dst="example.com", ttl=(1, 30))
        print(hexdump(ip))
        print(raw(ip))
        print(Ether(raw(ip)))
        # pkt.decode_payload_as（） 更改有效负载的解码方式

        p = IP() / TCP() / HTTP() / "AAAA"
        tcp = p[TCP]
        print(tcp.payload)
        print(tcp.underlayer)
        p.show()
        ls(UDP())

        # 发送报文
        # send：发送3层报文（ 如TCP / UDP协议），不接收数据包
        # sendp：发送2层报文(通过mac地址转发)，不接收

        # 2. 发且收
        # sr：发送，接收3层报文，返回有回应的数据包和没有回应的数据包。
        # sr1：发送，只接收1个响应包
        # srp：发送，接收2层报文
        # srp1：发送，只接收1个响应包
        # srploop：循环发送

        send(IP(dst="192.0.2.1") / UDP(dport=53))
        sendp(Ether() / IP(dst="192.0.2.1") / UDP(dport=53))

        srloop(IP(dst="packetlife.net") / ICMP(), count=3)

    # 抓包
    def test_to_file(self):
        package = sniff(iface='WLAN', timeout=10)
        wrpcap("data/test.pcap", package)  # 将抓取的包保存为test.pcap文件

        # 过滤报文
        # sniff(iface='WLAN', timeout=10, filter="tcp port 80", prn=lambda x: x.sprintf("{IP:%IP.src% -> %IP.dst%}"))

        # 除了使用scapy抓包外，也可以使用tcpdump（Linux）和tshark（Windows）进行抓包。
    def test_tls_https_to_file(self):
        load_layer("tls")
        package = sniff(iface='WLAN', timeout=10, filter="dst host www.shipxy.com", session=TLSSession)
        wrpcap("ship.pcap", package)  # 将抓取的包保存为test.pcap文件
        # https://www.cnpython.com/pypi/scapy-ssl_tls

    def test_tls_https(self):
        # todo scapy-ssl_tls
        load_layer('tls')
        pkts = rdpcap('ship.pcap')
        for pkt in pkts:
            pkt.lastlayer()
            print(pkt)

    def test_read_file(self):
        field = 'dst=00:0c:29:d9:98:c7'
        pkts = rdpcap("data/test.pcap")
        for packet in pkts:
            if packet.haslayer('DHCP6_Solicit'):
                packet_text = repr(packet)
                if re.search(field, packet_text, re.IGNORECASE):
                    print("666")
        # 或者
        pkts = sniff(offline='packet_solicit.pcap')

    def test_read_file2(self):
        packets = rdpcap('test-ggok-http.pcap')  # 'example.pcap' 是 pcap 文件名
        pkt0: Ether = packets[0]
        print(isinstance(pkt0, Loopback))  # 可以产生 Loopback 对象, 捕捉WiFi数据??
        print(pkt0.time)
        a1 = pkt0[Ether].dst
        a2 = pkt0[Ether].src
        a3 = pkt0[Ether].type

        # 可以通过 pkt0.show() 打印每个数据包的详细信息
        # 这里演示如何获取数据包的源地址和目标地址
        # if "IP" in packet:
        # if isinstance(pkt0, pcapng.blocks.EnhancedPacket):
        # pkt0.packet_payload
        b1 = pkt0[IP].version
        b2 = pkt0[IP].dst
        b3 = pkt0[IP].src
        c1 = pkt0[TCP].sport
        c2 = pkt0[TCP].dport
        c3 = pkt0[TCP].seq
        c4 = pkt0[TCP].ack
        c5 = pkt0[TCP].dataofs
        c6 = pkt0[TCP].reserved
        c7 = pkt0[TCP].flags
        c8 = pkt0[TCP].window
        c9 = pkt0[TCP].chksum
        c10 = pkt0[TCP].urgptr
        c11 = pkt0[TCP].options[0][1]
        c12 = pkt0[TCP].options[1][1]
        c13 = pkt0[TCP].options[2][1]
        c14 = pkt0[TCP].options[3][1]
        c15 = pkt0[TCP].options[4][1]
