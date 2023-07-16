# -*- coding:utf-8 -*-
"""
@Time: 2023/6/15
@Description:
"""
from unittest import TestCase

from scapy.fields import BitField
from scapy.layers.inet import IP, TCP, UDP
from scapy.layers.l2 import Ether
from scapy.layers.rtp import RTP
from scapy.packet import Packet, Raw
from scapy.utils import PcapReader, rdpcap
from sqlalchemy import BLOB
from sqlalchemy import Column, Text
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import declarative_base

from config.db_conf import localhost_test_engine, localhost_test_session

Base = declarative_base()


class Package(Base):
    __tablename__ = 'package'
    # 原始数据
    id = Column(INTEGER, primary_key=True, comment="id")
    raw = Column(BLOB, comment="原始数据")

    # 其值为6，则为TCP，其值为17，则为UDP。

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
    # Offset：报头长度，4位，给出报头中 32bit 字的数目。
    # 需要这个值是因为任选字段的长度是可变的。这个字段占 4bit,即TCP 最多有 60（15*4） 字节的首部
    tcp_offset = Column(Text, comment="数据偏移, 4bit")
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
    ps_h_start_code = Column(Text, comment="开始码,32bit,")
    ps_h_mark_1 = Column(Text, comment="market bit, 2bit")
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
    p
    s_sys_std_flag = Column(Text, comment="std缓存器界限标识, 1bit,")
    ps_sys_std_len = Column(Text, comment="std缓存器尺寸标识, 13bit,")
    ps_sys_stream = Column(Text, comment="流识别, 8bit,")
    # h264 层
    # 帧 -- 合并


class PS(Packet):
    # eg: HTTP:
    name = "PS"
    fields_desc = [
        BitField('ps_h_start_code', 32, 2),  # 起始码，占位4bit; 000001BA/000001BB/000001BC/000001E0 | 000001BA/000001E0
        BitField('ps_h_mark_1', 2, 1),  # PTS[32…30]：占位3bit；
        BitField('ps_h_scr', 3, 1),  # System clock
        BitField('ps_h_mark_2', 1, 1),
        BitField('ps_h_scr2', 15, 1),  # System clock
        BitField('ps_h_mark_3', 1, 1),
        BitField('ps_h_scr2', 15, 1),  # System clock
        BitField('ps_h_mark_3', 1, 1),
        BitField('ps_h_scr_extend', 9, 1),
        BitField('ps_h_mark_4', 1, 1),
        BitField('ps_h_rate', 22, 1),
        BitField('ps_h_reserved', 5, 1),
        BitField('ps_h_stuffing_length', 3, 1),

        #
        BitField('ps_sys_start_code', 32, 1),
        BitField('ps_sys_hdr_len', 16, 1),
        BitField('ps_sys_mark_1', 1, 1),
        BitField('ps_sys_rate_bound', 22, 50000),
        BitField('ps_sys_mark_2', 1, 1),
        BitField('ps_sys_audio_bound', 6, 1),
        BitField('ps_sys_fixed_flag', 1, 0),
        BitField('ps_sys_csps_flag', 1, 1),
        BitField('ps_sys_audio_lock_flag', 1, 1),
        BitField('ps_sys_video_lock_flag', 1, 1),
        BitField('ps_sys_mark_3', 1, 1),
        BitField('ps_sys_video_bound', 1, 1),
        BitField('ps_sys_dif_mpeg1', 1, 1),
        BitField('ps_sys_reserver', 7, 0x7F),

        BitField('ps_sys_audio_stream_id', 7, 0xC0),
        BitField('ps_sys_audio_mark', 2, 3),
        BitField('ps_sys_audio_size_bound', 1, 0),
        BitField('ps_sys_audio_size_bound', 13, 512),

        BitField('ps_sys_video_stream_id', 7, 0xE0),
        BitField('ps_sys_video_mark', 2, 3),
        BitField('ps_sys_video_size_bound', 1, 1),
        BitField('ps_sys_video_size_bound', 13, 2048),

        # psm 记录了媒体信息，比如音视频的编码格式
        BitField('ps_m_start_code', 24, 0x000001),
        BitField('ps_m_stream_id', 8, 0xBC),
        BitField('ps_m_len', 16, 16),
        BitField('ps_m_next_indicator', 1, 1),
        BitField('ps_m_reserved', 2, 3),
        BitField('ps_m_version', 5, 0),
        BitField('ps_m_reserved2', 7, 0x7F),
        BitField('ps_m_mark_1', 1, 1),
        BitField('ps_m_stream_info_len', 16, 0),
        BitField('ps_m_stream_map_len', 16, 8),

        BitField('ps_m_video_stream_type', 8, 0x1B),  # 视频编码格式H264
        BitField('ps_m_video_elementary_stream_id', 8, 0xE0),
        BitField('ps_m_video_elementary_stream_info_length', 16, 0),

        #     /*audio*/

        BitField('ps_m_audio_stream_type', 8, 0x90),  # 音频编码格式G711
        BitField('ps_m_audio_elementary_stream_id', 8, 0xC0),
        BitField('ps_m_audio_elementary_stream_info_length', 16, 0),

        #     /*crc*/
        BitField('ps_m_crc_1', 8, 0x45),
        BitField('ps_m_crc_2', 8, 0xBD),
        BitField('ps_m_crc_3', 8, 0xDC),

        # PES
        BitField('ps_pes_start_code', 24, 0x000001),
        BitField('ps_pes_stream_id', 8, 0x000001),
        BitField('ps_pes_payload_len', 16, 0),
        BitField('ps_pes_f1', 2, 10),
        BitField('ps_pes_scrambling_control', 2, 0),
        BitField('ps_pes_priority', 1, 1),
        BitField('ps_pes_data_alignment_indicator', 1, 1),
        BitField('ps_pes_copyright', 1, 0),
        BitField('ps_pes_original_or_copy', 1, 0),
        BitField('ps_pes_pts_flag', 1, 1),
        BitField('ps_pes_dts_flag', 1, 1),
        BitField('ps_pes_escr_flag', 1, 0),
        BitField('ps_pes_es_rate_flag', 1, 0),
        BitField('ps_pes_dsm_trick_mode_flag', 1, 0),
        BitField('ps_pes_additional_copy_info_flag', 1, 0),
        BitField('ps_pes_PES_CRC_flag', 1, 0),
        BitField('ps_pes_PES_extension_flag', 1, 0),
        BitField('ps_pes_header_data_length', 8, 10),
        #     /*PTS,DTS*/
        BitField('ps_pes_pts', 4, 3),
        BitField('ps_pes_PTS', 3, 3),
        BitField('ps_pes_mark_1', 1, 1),
        BitField('ps_pes_pts_2', 15, 0),
        BitField('ps_pes_mark_2', 1, 1),
        BitField('ps_pes_pts_3', 15, 1),
        BitField('ps_pes_mark_3', 1, 1),
        BitField('ps_pes_pts_4', 4, 1),
        BitField('ps_pes_dts_1', 3, 1),
        BitField('ps_pes_dts_mark_1', 1, 1),
        BitField('ps_pes_dts_2', 4, 1),
        BitField('ps_pes_dts_3', 3, 1),
        BitField('ps_pes_dts_mark_2', 1, 1),
        BitField('ps_pes_dts_4', 15, 1),
        BitField('ps_pes_dts_mark_3', 1, 1),
        BitField('ps_pes_dts_5', 15, 1),
        BitField('ps_pes_dts_mark_5', 1, 1),
        BitField('ps_pes_dts_6', 15, 1),
        BitField('ps_pes_dts_mark_6', 1, 1),
    ]


class TestPcap(TestCase):
    def test_pre(self):
        ...
        Base.metadata.drop_all(localhost_test_engine)
        Base.metadata.create_all(localhost_test_engine)

    def test1(self):
        packets = rdpcap('test_out_export_h264.pcapng')
        for pck in packets[0:1000]:
            package = Package()
            pck.raw = pck
            print(pck, pck.time, isinstance(pck, Ether), isinstance(pck, IP), isinstance(pck, Raw))
            if pck.haslayer(Ether):
                ether: Ether = pck[Ether]
                package.time = ether.time
            if pck.haslayer(IP):
                ip: IP = pck[IP]
                package.ip_version = ip.version
                package.ip_header_len = ip.ihl
                package.ip_ser = ip.tos
                package.ip_total_len = ip.len
                package.ip_flag = ip.id
                package.ip_flag2 = ip.flags.value  # ["MF", "DF", "evil"]
                package.ip_offset = ip.frag
                package.ip_live_time = ip.ttl
                package.ip_prop = ip.proto
                package.ip_check = ip.chksum
                package.ip_src = ip.src
                package.ip_dst = ip.dst
                package.ip_other = str(ip.options)
            if pck.haslayer(UDP):
                udp: UDP = pck[UDP]
                package.udp_src_port = udp.sport
                package.udp_dst_port = udp.dport
                package.udp_len = udp.len
                package.udp_check = udp.chksum
            if pck.haslayer(TCP):
                tcp: TCP = pck[TCP]
                package.tcp_src_port = tcp.sport
                package.tcp_dst_port = tcp.dport
                package.tcp_seq = tcp.seq
                package.tcp_ack = tcp.ack
                package.tcp_offset = tcp.dataofs
                package.tcp_reserve = tcp.reserved
                package.tcp_flag_urg = tcp.flags.value
                package.tcp_flag_ack = tcp.flags.value
                package.tcp_flag_psh = tcp.flags.value
                package.tcp_flag_pst = tcp.flags.value
                package.tcp_flag_syn = tcp.flags.value
                package.tcp_flag_fin = tcp.flags.value
                package.tcp_window = tcp.window
                package.tcp_check = tcp.chksum
                package.tcp_emergency = tcp.urgptr
                package.tcp_other = str(tcp.options)

            if pck.haslayer(RTP):
                rtp: RTP = pck[RTP]
                package.rtp_version = rtp.version
                package.rtp_p_padding = rtp.padding
                package.rtp_x_extend = rtp.extension
                package.rtp_cc = rtp.numsync
                package.rtp_flag = rtp.marker
                package.rtp_payload_type = rtp.payload_type
                package.rtp_seq = rtp.sequence
                package.rtp_timestamp = rtp.timestamp
                package.rtp_ssrc = rtp.sourcesync
                package.rtp_csrc = rtp.sync

            if pck.haslayer("PS"):
                ps: PS = pck["PS"]
                package.ps_start_code = ip.chksum

            if pck.haslayer("H264"):
                ps: PS = pck["H264"]
                package.ps_start_code = ip.chksum
            print(package)
            localhost_test_session.add(package)
            localhost_test_session.commit()

    def test2(self):
        with PcapReader("test_out_export_h264.pcapng") as reader:
            for pck in reader:
                print(pck, pck.time, isinstance(pck, Ether), isinstance(pck, IP), isinstance(pck, Raw))
                pck.show()
                # str(pck).encode("HEX")
                # pck.add_payload()
                # pck.build_ps()
                # pck.haslayer()
                # pck.add_underlayer()
                # pck.payload_guess
                # pck.layers()
                # print(pck)
