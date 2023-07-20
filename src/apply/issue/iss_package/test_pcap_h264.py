# -*- coding:utf-8 -*-
"""
@Time: 2023/6/15
@Description:
"""
import json
import time
from unittest import TestCase

from scapy.fields import BitField, IntField, StrLenField, ShortField, X3BytesField, ByteField, XIntField
from scapy.layers.inet import IP, TCP, UDP
from scapy.layers.l2 import Ether
from scapy.layers.rtp import RTP
from scapy.packet import Packet, Raw
from scapy.utils import PcapReader, rdpcap
from sqlalchemy import Column, Text
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import declarative_base

from config.db_conf import localhost_test_engine, localhost_test_session

Base = declarative_base()


class Package(Base):
    __tablename__ = 'package'
    # 原始数据
    id = Column(INTEGER, primary_key=True, comment="id")
    raw = Column(Text, comment="原始数据")
    debug_info = Column(Text, comment="debug info, json, 4bit")
    # 数据链路层
    ether_time = Column(Text, comment="版本, 4bit")
    # ether_mac_src = Column(Text, comment="目标mac, 48bit")
    # ether_mac_dst = Column(Text, comment="源mac, 48bit")
    # ether_type = Column(Text, comment="协议类型, 16bit")
    # 1500 1456 -12 = 1442

    # ip 层
    ip_version = Column(Text, comment="版本, 4bit")
    ip_header_len = Column(Text, comment="首部长度, 4bit")
    ip_ser = Column(Text, comment="区分服务, 4bit")
    ip_total_len = Column(Text, comment="总长度, 4bit")
    ip_id = Column(Text, comment="标识, 16bit")
    ip_flags = Column(Text, comment="标志, 3bit")
    ip_offset = Column(Text, comment="片偏移, 9bit")
    ip_live_time = Column(Text, comment="生存时间, 8bit")
    ip_prop = Column(Text, comment="payload协议, 8bit")  # 其值为6，则为TCP，其值为17，则为UDP。
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
    rtp_padding = Column(Text, comment="填充位，1bit")  # 置成1，表示此包后面会一定数目的填充比特；
    rtp_extension = Column(Text, comment="扩展位，1bit")  # 置成1，表示此包固定头部后面会跟着一个扩展头部；
    rtp_numsync = Column(Text, comment="CSRC计数位，4bit")  # 表示固定头部后面CSRC识别符的个数；
    rtp_marker = Column(Text, comment="标示位，1bit")  # 具体含义由特定协议解释；
    rtp_payload_type = Column(Text, comment="负载类型，7bit")  # 表示具体的负载类型，比如音频、视频、文档等；
    rtp_seq = Column(Text, comment="序列号，16bit")  # 发送方在每发送完一个RTP包后就将该值增加1，接收方可以由该值检测包的丢失及恢复包序列。序列号的初始值是随机的；
    rtp_timestamp = Column(Text, comment="时间戳，32bit")  # 表示RTP数据包中第一个字节的采样时间；
    rtp_ssrc = Column(Text, comment="同步源标示符，32bit")  # 表示RTP数据包的来源，在同一个RTP会话中不可能存在两个相同的SSRC，SSRC的值是随机选取的；
    rtp_sync = Column(Text, comment="sync，12bit")
    # https://blog.csdn.net/ichenwin/article/details/100086930

    # https://www.rstk.cn/news/901965.html
    # 1.PS流传输格式预览
    #   1、视频关键帧的封装 RTP + PS header + PS system header + PS system Map + PES header +h264 data
    #   2、视频非关键帧的封装 RTP +PS header + PES header + h264 data
    #   3、音频帧的封装: RTP + PES header + G711

    ps_start_code = Column(Text, comment="开始码,32bit,")
    ps_mark_1 = Column(Text, comment="market bit, 2bit")
    ps_scr = Column(Text, comment="包头scr,33bit,")  # 系统时钟基准（SCR-System Clock Reference）的基本部分
    ps_scr_extend = Column(Text, comment="包头scr 扩展部分,9bit,")
    ps_rate = Column(Text, comment="节目复用速率, 22bit,")

    # ps system header
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

    ps_sys_options = Column(Text, comment="附加, 8bit,")
    # psm Header
    psm_start_code = Column(Text, comment="开始码,32bit,")

    # pes Header
    pes_start_code = Column(Text, comment="开始码,32bit,")

    # h264 层
    # 帧 -- 合并


class PS(Packet):
    name = "PS"
    # https://blog.csdn.net/ichenwin/article/details/100086930
    fields_desc = [
        # 0~3字节: 为0x 00 00 01 ba，表示当前为PSH头部 #I帧附加信息:20~23: 为0x 00 00 01 bb,表示当前为I帧附件信息
        # 当前为I帧或P帧的第一个NALU则需加PSH头部。若当前为I帧的第一个NALU还需要加PSM头部。
        # 每个NALU分为若干段，每段前需加PES头部, 每段数据与PES头部组成PES包。
        IntField('ps_start_code', 0x000001BB),  # 起始码，占位4bit; 000001BA/000001BB/000001BC/000001E0 | 000001BA/000001E0
        BitField('ps_mark_1', 1, 2),
        BitField('ps_scr', 1, 3),
        BitField('ps_mark_2', 1, 1),
        BitField('ps_scr2', 1, 15),
        BitField('ps_mark_3', 1, 1),
        BitField('ps_scr22', 1, 15),
        BitField('ps_mark_33', 1, 1),
        BitField('ps_scr_extend', 1, 9),
        BitField('ps_mark_4', 1, 1),
        BitField('ps_rate', 1, 22),
        BitField('ps_mark_5', 3, 2),
        BitField('ps_reserved', 3, 5),
        BitField('ps_stuffing_length', 0, 3),
        StrLenField("ps_options", b"", length_from=lambda pkt: pkt.ps_stuffing_length)
    ]


class PSSYS(Packet):
    name = "PSSYS"
    fields_desc = [
        XIntField('ps_sys_start_code', 1),
        ShortField('ps_sys_header_len', 1),
        BitField('ps_sys_mark_1', 1, 1),
        BitField('ps_sys_rate_bound', 50000, 22),
        BitField('ps_sys_mark_2', 1, 1),
        BitField('ps_sys_audio_bound', 1, 6),
        BitField('ps_sys_fixed_flag', 0, 1),
        BitField('ps_sys_csps_flag', 1, 1),
        BitField('ps_sys_audio_lock_flag', 1, 1),
        BitField('ps_sys_video_lock_flag', 1, 1),
        BitField('ps_sys_mark_3', 1, 1),
        BitField('ps_sys_video_bound', 1, 5),
        BitField('ps_sys_restriction_flag', 1, 1),
        BitField('ps_sys_reserved', 0x7F, 7),

        StrLenField("ps_sys_options", b"", length_from=lambda pkt: pkt.ps_sys_header_len - 6),

        # BitField('ps_sys_audio_stream_id', 0xC0, 8),
        # BitField('ps_sys_audio_mark', 3, 2),
        # BitField('ps_sys_audio_pstd_buffer_bound_scale', 0, 1),
        # BitField('ps_sys_audio_pstd_buffer_size_bound', 512, 13),
        #
        # BitField('ps_sys_video_stream_id', 0xE0, 8),
        # BitField('ps_sys_video_mark', 3, 2),
        # BitField('ps_sys_video_pstd_buffer_bound_scale', 1, 1),
        # BitField('ps_sys_video_pstd_buffer_size_bound', 2048, 13),

    ]


class PSM(Packet):
    name = "PSM"
    fields_desc = [
        # psm 记录了媒体信息，比如音视频的编码格式
        X3BytesField('psm_start_code', 0x000001),
        ByteField('psm_stream_id', 0xBC),
        ShortField('psm_len', 16),
        BitField('psm_next_indicator', 1, 1),
        BitField('psm_reserved', 3, 2),
        BitField('psm_version', 0, 5),
        BitField('psm_reserved2', 0x7F, 7),
        BitField('psm_mark_1', 1, 1),
        BitField('psm_stream_info_len', 0, 16),
        StrLenField("psm_stream_info", b"", length_from=lambda pkt: pkt.psm_stream_info_len),
        BitField('psm_stream_map_len', 8, 16),
        StrLenField("psm_stream_map", b"", length_from=lambda pkt: pkt.psm_stream_map_len),
        # #     /*video*/
        # BitField('psm_video_stream_type', 0x1B, 8),  # 视频编码格式H264
        # BitField('psm_video_elementary_stream_id', 0xE0, 8),
        # BitField('psm_video_elementary_stream_info_length', 0, 16),
        # #     /*audio*/
        # BitField('psm_audio_stream_type', 0x90, 8),  # 音频编码格式G711
        # BitField('psm_audio_elementary_stream_id', 0xC0, 8),
        # BitField('psm_audio_elementary_stream_info_length', 0, 16),

        #
        #     /*crc*/
        BitField('psm_crc_1', 0x45, 8),
        BitField('psm_crc_2', 0xBD, 8),
        BitField('psm_crc_3', 0xDC, 8),
        BitField('psm_crc_4', 0xDC, 8),
        StrLenField("psm_options", b"",
                    length_from=lambda pkt: pkt.psm_len - 10 - pkt.psm_stream_info_len - pkt.psm_stream_map_len),

    ]


class PES(Packet):
    name = "PES"
    fields_desc = [
        # PES
        X3BytesField('pes_start_code', 0x000001),
        ByteField('pes_stream_id', 0x000001),
        BitField('pes_payload_len', 0, 16),
        BitField('pes_f1', 10, 2),
        BitField('pes_scrambling_control', 0, 2),
        BitField('pes_priority', 1, 1),
        BitField('pes_data_alignment_indicator', 1, 1),
        BitField('pes_copyright', 0, 1),
        BitField('pes_original_or_copy', 0, 1),
        BitField('pes_pts_flag', 1, 1),
        BitField('pes_dts_flag', 1, 1),
        BitField('pes_escr_flag', 0, 1),
        BitField('pes_es_rate_flag', 0, 1),
        BitField('pes_dsm_trick_mode_flag', 0, 1),
        BitField('pes_additional_copy_info_flag', 0, 1),
        BitField('pes_PES_CRC_flag', 0, 1),
        BitField('pes_PES_extension_flag', 0, 1),
        BitField('pes_header_data_length', 10, 8),
        #     /*PTS,DTS*/
        BitField('pes_pts', 3, 4),
        BitField('pes_PTS', 3, 3),
        BitField('pes_mark_1', 1, 1),
        BitField('pes_pts_2', 0, 15),
        BitField('pes_mark_2', 1, 1),
        BitField('pes_pts_3', 1, 15),
        BitField('pes_mark_3', 1, 1),
        BitField('pes_pts_4', 1, 4),
        BitField('pes_dts_1', 1, 3),
        BitField('pes_dts_mark_1', 1, 1),
        BitField('pes_dts_2', 1, 4),
        BitField('pes_dts_3', 1, 3),
        BitField('pes_dts_mark_2', 1, 1),
        BitField('pes_dts_4', 1, 15),
        BitField('pes_dts_mark_3', 1, 1),
        BitField('pes_dts_5', 1, 15),
        BitField('pes_dts_mark_5', 1, 1),
        BitField('pes_dts_6', 1, 15),
        BitField('pes_dts_mark_6', 1, 1),
    ]


class H264(Packet):
    # 标准 H.264 流以 0x00 00 00 01 起始码为标志分割成若干单元，称之为 Network Abstraction Layer
    ...


class TestPcap(TestCase):
    def test_pre(self):
        ...
        Base.metadata.drop_all(localhost_test_engine)
        Base.metadata.create_all(localhost_test_engine)

    def test1(self):
        self.test_pre()
        packets = rdpcap('rtp.pcapng')
        for pck in packets:
            package = Package()
            # print(pck, pck.time, isinstance(pck, Ether), isinstance(pck, IP), isinstance(pck, Raw))
            if pck.haslayer(Ether):
                ether: Ether = pck[Ether]
                package.time = time.localtime(ether.time.real.__int__())
            if pck.haslayer(IP):
                ip: IP = pck[IP]
                package.ip_version = ip.version
                package.ip_header_len = ip.ihl
                package.ip_ser = ip.tos
                package.ip_total_len = ip.len
                package.ip_id = ip.id
                package.ip_flags = ip.flags.value  # ["MF", "DF", "evil"]
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
                # udp.payload.decode_payload_as(RTP)
                udp.add_payload(RTP(udp.payload.__bytes__()))
                if pck.haslayer(RTP):
                    rtp: RTP = pck[RTP]
                    package.rtp_version = rtp.version
                    package.rtp_padding = rtp.padding
                    package.rtp_extension = rtp.extension
                    package.rtp_numsync = rtp.numsync
                    package.rtp_marker = rtp.marker
                    package.rtp_payload_type = rtp.payload_type
                    package.rtp_seq = rtp.sequence
                    package.rtp_timestamp = rtp.timestamp
                    package.rtp_ssrc = rtp.sourcesync
                    package.rtp_sync = json.dumps(rtp.sync)

                    ps_ba = b'\x00\x00\x01\xba'
                    pss_bb = b'\x00\x00\x01\xbb'
                    psm_bc = b'\x00\x00\x01\xbc'
                    pes_e0 = b'\x00\x00\x01\xe0'
                    bytes__ = rtp.payload.__bytes__()
                    package.debug_info = f"{ps_ba in bytes__}-{pss_bb in bytes__}-{psm_bc in bytes__}-{pes_e0 in bytes__}"
                    if bytes__.startswith(ps_ba):
                        # rtp.payload.decode_payload_as(PS)
                        rtp.add_payload(PS(rtp.payload.__bytes__()))
                        if pck.haslayer(PS):
                            ps: PS = pck[PS]
                            package.ps_start_code = ps.ps_start_code

                            if ps.payload.__bytes__().startswith(pss_bb):
                                # ps.payload.decode_payload_as(PSSYS)
                                ps.add_payload(PSSYS(ps.payload.__bytes__()))
                                pss: PSSYS = pck[PSSYS]
                                package.ps_sys_start_code = pss.ps_sys_start_code
                                package.ps_sys_options = pss.ps_sys_options

                                if pss.payload.__bytes__().startswith(psm_bc):
                                    # pss.payload.decode_payload_as(PSM)
                                    pss.add_payload(PSM(pss.payload.__bytes__()))
                                    psm: PSM = pss[PSM]
                                    package.psm_start_code = psm.psm_start_code

                                    if psm.payload.__bytes__().startswith(pes_e0):
                                        # pss.payload.decode_payload_as(PES)
                                        psm.add_payload(PES(psm.payload.__bytes__()))
                                        pes: PES = psm[PES]
                                        package.pes_start_code = pes.pes_start_code

                                        package.raw = pes.payload.__bytes__().hex()
                            if ps.payload.__bytes__().startswith(pes_e0):
                                # ps.payload.decode_payload_as(PES)
                                ps.add_payload(PES(ps.payload.__bytes__()))
                                pes: PES = ps[PES]
                                package.pes_start_code = pes.pes_start_code

                                package.raw = pes.payload.__bytes__().hex()
                    else:
                        package.raw = bytes__.hex()

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
