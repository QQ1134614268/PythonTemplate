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
from sqlalchemy import Column, Text


@dataclass()
class H264:
    # 原始数据

    # 数据链路层
    time: str
    e_: str
    # ip 层
    ip_version = Column(Text, comment="版本, 4bit")
    ip_header_len = Column(Text, comment="首部长度, 4bit")
    ip_ser = Column(Text, comment="区分服务, 4bit")
    ip_total_len = Column(Text, comment="总长度, 4bit")
    ip_flag = Column(Text, comment="标识, 16bit")
    ip_flag2 = Column(Text, comment="标志, 3bit")
    ip_offset = Column(Text, comment="片偏移, 9bit")
    ip_live_time = Column(Text, comment="生存时间, 8bit")
    ip_prop = Column(Text, comment="协议, 8bit")
    ip_check = Column(Text, comment="首部校验和, 16bit")
    ip_src = Column(Text, comment="源地址, 32bit")
    ip_dst = Column(Text, comment="目标地址, 32bit")
    ip_other = Column(Text, comment="可选字段")
    ip_padding = Column(Text, comment="填充")

    # udp 层
    udp_src_port = Column(Text, comment="源端口号, 16bit")
    udp_dst_port = Column(Text, comment="目标端口号, 16bit")
    udp_len = Column(Text, comment="udp 长度, 16bit")
    udp_check = Column(Text, comment="udp 校验和, 16bit")

    # tcp层
    tcp_src_port = Column(Text, comment="源端口号, 16bit")
    tcp_dst_port = Column(Text, comment="目标端口号, 16bit")
    tcp_seq = Column(Text, comment="序号, 32bit")
    tcp_ack = Column(Text, comment="确认号, 32bit")
    tcp_offset = Column(Text,
                        comment="数据偏移, 4bit")  # Offset：报头长度，4位，给出报头中 32bit 字的数目。需要这个值是因为任选字段的长度是可变的。这个字段占 4bit,即TCP 最多有 60（15*4） 字节的首部
    tcp_reserve = Column(Text, comment="保留, 6bit")
    tcp_flag_urg = Column(Text, comment="urg 标识, 1bit")
    tcp_flag_ack = Column(Text, comment="ack 标识, 1bit")
    tcp_flag_psh = Column(Text, comment="psh 标识, 1bit")
    tcp_flag_pst = Column(Text, comment="pst 标识, 1bit")
    tcp_flag_syn = Column(Text, comment="syn 标识, 1bit")
    tcp_flag_fin = Column(Text, comment="fin 标识, 1bit")  # 指示接收方的接收窗口大小，用于流量控制
    tcp_window = Column(Text, comment="窗口, 16bit")
    tcp_check = Column(Text, comment="校验和, 16bit")
    tcp_emergency = Column(Text, comment="紧急指针, 16bit")
    tcp_other = Column(Text, comment="选项, 16bit")
    tcp_padding = Column(Text, comment="选项, 16bit")

    # RTP 层
    rtp_version = Column(Text, comment="版本号，2bit")
    rtp_p_padding = Column(Text, comment="填充位，1bit")  # 置成1，表示此包后面会一定数目的填充比特；
    rtp_x_extend = Column(Text, comment="扩展位，1bit")  # 置成1，表示此包固定头部后面会跟着一个扩展头部；
    rtp_cc = Column(Text, comment="CSRC计数位，4bit")  # 表示固定头部后面CSRC识别符的个数；
    rtp_flag = Column(Text, comment="标示位，1bit")  # 具体含义由特定协议解释；
    rtp_payload_type = Column(Text, comment="负载类型，7bit")  # 表示具体的负载类型，比如音频、视频、文档等；
    rtp_seq = Column(Text, comment="序列号，16bit")  # 发送方在每发送完一个RTP包后就将该值增加1，接收方可以由该值检测包的丢失及恢复包序列。序列号的初始值是随机的；
    rtp_timestamp = Column(Text, comment="时间戳，32bit")  # 表示RTP数据包中第一个字节的采样时间；
    rtp_ssrc = Column(Text, comment="同步源标示符，32bit")  # 表示RTP数据包的来源，在同一个RTP会话中不可能存在两个相同的SSRC，SSRC的值是随机选取的；
    rtp_csrc = Column(Text,
                      comment="贡献源列表，0到15项，每项32bit,")  # 表示此包中负载的所有贡献源。若贡献源多于15个，仅识别15个，CSRC由混合器插入，便于接收端正确识别出会话者的身份。

    # https://blog.csdn.net/ichenwin/article/details/100086930

    # https://www.rstk.cn/news/901965.html
    # 1.PS流传输格式预览
    #   1、视频关键帧的封装 RTP + PS header + PS system header + PS system Map + PES header +h264 data
    #   2、视频非关键帧的封装 RTP +PS header + PES header + h264 data
    #   3、音频帧的封装: RTP + PES header + G711

    # ps 层 PS header + SYS header(I帧)+PSM header(I帧) +PES header+ PES packet n
    # PS包由包头、系统头、PES包3部分构成。包头由PS包起始码、系统时钟基准（SCR-System Clock Reference）的基本部分、SCR的扩展部分和PS复用速率4部分组成。
    # http://www.360doc.com/content/14/0127/08/15166967_348250162.shtml
    ps_start_code = Column(Text, comment="开始码,32bit,")  # 表示此包中负载的所有贡献源。若贡献源多于15个，仅识别15个，CSRC由混合器插入，便于接收端正确识别出会话者的身份。
    ps_scr = Column(Text, comment="包头scr,33bit,")  # 系统时钟基准（SCR-System Clock Reference）的基本部分
    ps_scr_extend = Column(Text, comment="包头scr 扩展部分,9bit,")
    ps_rate = Column(Text, comment="节目复用速率, 22bit,")
    ps_sys_start_code = Column(Text, comment="系统头 起始码, 32bit,")
    ps_sys_len = Column(Text, comment="系统头 长度, 16bit,")
    ps_sys_rate = Column(Text, comment="系统头 速率界限, 22bit,")
    ps_sys_audio_rate = Column(Text, comment="系统头 音频 界限, 6bit,")
    ps_sys_flag_fix = Column(Text, comment="系统头 固定标识, 1bit,")
    ps_sys_flag_csps = Column(Text, comment="系统头 csps标识, 1bit,")
    ps_sys_flag_audio = Column(Text, comment="系统头 系统音频锁定标识, 1bit,")
    ps_sys_flag_video = Column(Text, comment="系统头 系统视频锁定标识, 1bit,")
    ps_sys_video_rate = Column(Text, comment="系统头 视频 界限, 5bit,")
    ps_sys_stream_flag = Column(Text, comment="系统头 流标识, 8bit,")
    ps_sys_std_flag = Column(Text, comment="std缓存器界限标识, 1bit,")
    ps_sys_std_len = Column(Text, comment="std缓存器尺寸标识, 13bit,")
    ps_sys_stream = Column(Text, comment="流识别, 8bit,")
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
