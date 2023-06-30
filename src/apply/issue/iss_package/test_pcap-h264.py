# -*- coding:utf-8 -*-
"""
@Time: 2023/6/15
@Description:
"""
from dataclasses import dataclass
from unittest import TestCase

from scapy.fields import BitField, BitFieldLenField
from scapy.layers.http import HTTP
from scapy.layers.inet import IP, UDP, TCP
from scapy.layers.l2 import Ether
from scapy.layers.rtp import RTP
from scapy.packet import Packet


@dataclass()
class H264:
    # 原始数据

    # 数据链路层
    time: str
    e_: str

    # ip 层

    # udp 层
    # tcp层

    # ps 层

    # RTP 层

    # h264 层

    # 帧 -- 合并


class PS(Packet):
    # eg: HTTP:

    # GB28181 对RTP 传输的数据负载类型有规定（参考GB28181 附录B），负载类型中96-127
    # RFC2250 建议96 表示PS 封装，建议97 为MPEG-4，建议98 为H264

    # [PSH][PS system header][PSM][PES header][ES] 关键帧
    # [PSH][PES header][ES][PES header][ES]

    # 若PTS_DTS_flags == ‘10’，则说明只有PTS，起始码为0010；若PTS_DTS_flags == ‘11’，则PTS和DTS都存在，PTS的起始码为0011，DTS的起始码为0001；(PTS的起始码后2个bit与flag相同)
    # PTS = （PTS1 & 0x0e) << 29 + (PTS2 & 0xfffe) << 14 + (PTS3 & 0xfffe ) >> 1
    # DTS规则与PTS一致，一般PES header data length是10+填充位，其他可选字段大都不存在，解封装的时候，先计算PES长度，再计算PES header data长度，最后计算出ES的长度及起始位置，计算工时如下：
    # ESlen = PESlen-2-1-pes_header_data_length
    # PES包头之后，紧跟着就是原始的视频帧数据(ES)或者音频数据

    # pack_start_code:起始码，占位32bit，标识PS包的开始，固定为0x000001BA
    #
    # ‘01’字段：占位2bit
    #
    # SCR字段：占位46bit，其中包含42bit的SCR值和4个bit的marker_bit值；其中SCR值由system_clock_reference_base和system_clock_reference_extension两部分组成,字节顺序依次是：
    #
    # (1) system_clock_reference_base [32…30]：占位3bit
    #
    # (2) marker_bit：占位1bit
    #
    # (3) system_clock_reference_base [29…15]：占位15bit
    #
    # (4) marker_bit：占位1bit
    #
    # (5) system_clock_reference_base [14…0]：占位15bit
    #
    # (6) marker_bit：占位1bit
    #
    # (7) system_clock_reference_extension：占位9bit
    #
    # (8) marker_bit：占位1bit
    #
    # program_mux_rate字段：速率值字段，占位22bit，正整数，表示P-STD接收此字段所在包的PS流的速率；这个值以每秒50字节作为单位；禁止0值；
    #
    # Marker_bit：标记字段，占位1bit，固定为’1’；
    #
    # Marker_bit：标记字段，占位1bit，固定为’1’；
    #
    # Reserved字段：保留字段，占位5bit；
    #
    # pack_stuffing_length字段：长度字段，占位3bit；规定了此字段之后填充字段的长度；
    #
    # stuffing_byte：填充字段，固定为0xFF；长度由前一字段确定

    name = "PS"
    fields_desc = [BitField('start_code', 2, 2),  # 起始码，占位4bit; 000001BA/000001BB/000001BC/000001E0 | 000001BA/000001E0
                   BitField('PTS', 0, 1),  # PTS[32…30]：占位3bit；
                   BitField('marker_bit', 0, 1),  # 占位1bit；
                   BitFieldLenField('PTS', None, 4, count_of='sync'),  # 占位15bit；
                   BitField('marker_bit', 0, 1),  # 占位1bit；
                   BitFieldLenField('PTS', None, 4, count_of='sync'),  # 占位15bit；
                   BitField('marker_bit', 0, 1),  # 占位1bit；
                   ]  # noqa: E501


class TestPcap(TestCase):
    def test1(self):
        # 过滤

        # 解析,
        pck = Ether()
        ip_pck: IP = pck.getlayer(1)
        udp_pck: UDP = ip_pck.getlayer(1)
        rtp_pck: RTP = udp_pck.getlayer(1)
        ps_pck: PS = rtp_pck.getlayer(1)
        h264_pck: H264 = rtp_pck.getlayer(1)

        # 结果

        # 过滤组合, 保存文件

    def test_http(self):
        # 过滤

        # 解析,
        pck = Ether()
        ip_pck: IP = pck.getlayer(1)
        tcp_pck: TCP = ip_pck.getlayer(1)
        http_pck: HTTP = tcp_pck.getlayer(1)
