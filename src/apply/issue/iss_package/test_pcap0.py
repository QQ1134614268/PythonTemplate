# -*- coding:utf-8 -*-
"""
@Time: 2023/6/15
@Description:
"""
from unittest import TestCase

from scapy.all import *
from scapy.layers.dhcp6 import DHCP6OptIA_PD, DHCP6OptIAPrefix, DHCP6OptIA_NA, DHCP6OptClientId, DHCP6_Solicit
from scapy.layers.inet import UDP
from scapy.layers.inet6 import IPv6
from scapy.layers.l2 import Ether


class TestPcap(TestCase):
    # 抓包
    def test1(self):
        package = sniff(iface='WLAN', timeout=10)
        wrpcap("test.pcap", package)  # 将抓取的包保存为test.pcap文件

        # 过滤报文
        # sniff(iface='WLAN', timeout=10, filter="tcp port 80", prn=lambda x: x.sprintf("{IP:%IP.src% -> %IP.dst%}"))

        # 除了使用scapy抓包外，也可以使用tcpdump（Linux）和tshark（Windows）进行抓包。

    def test2(self):
        pkts = sniff(offline='test.pcap')
        pkts[0].show()

    def test3(self):
        # 构造报文
        ethernet = Ether(dst='00:0c:29:47:f3:2f', src='c8:3a:35:09:ef:a1', type=0x86dd)
        ip = IPv6(src='2001:db8:3333::16', dst='ff02::2')
        udp = UDP(sport=546, dport=547)
        # dhcpv6 = DHCP6(msgtype = 1)
        dhcpv6 = DHCP6_Solicit()
        cid = DHCP6OptClientId()
        iana = DHCP6OptIA_NA()
        iapd_p = DHCP6OptIAPrefix()
        iapd = DHCP6OptIA_PD(iapdopt=[iapd_p])
        packet = ethernet / ip / udp / dhcpv6 / cid / iana / iapd
        packet.show()

        # 发送报文
        # send：发送3层报文（ 如TCP / UDP协议），不接收数据包
        # sendp：发送2层报文(通过mac地址转发)，不接收

        # 2. 发且收
        # sr：发送，接收3层报文，返回有回应的数据包和没有回应的数据包。
        # sr1：发送，只接收1个响应包
        # srp：发送，接收2层报文
        # srloop()：循环发送
        # srp1：发送，只接收1个响应包
        # srploop：循环发送

    def test4(self):
        package = "test.pcap"
        field = 'dst=00:0c:29:d9:98:c7'
        pkts = rdpcap(package)
        for packet in pkts:
            if packet.haslayer('DHCP6_Solicit'):
                packet_text = repr(packet)
                if re.search(field, packet_text, re.IGNORECASE):
                    print("666")
        # 或者
        pkts = sniff(offline='packet_solicit.pcap')
