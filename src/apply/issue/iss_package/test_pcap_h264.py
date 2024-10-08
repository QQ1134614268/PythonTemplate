# -*- coding:utf-8 -*-
"""
@Time: 2023/6/15
@Description:
"""
import json
from datetime import datetime
from typing import List
from unittest import TestCase

from scapy.fields import BitField, IntField, StrLenField, ShortField, X3BytesField, ByteField, XIntField, \
    ConditionalField, PacketListField, PacketField
from scapy.layers.inet import IP, TCP, UDP
from scapy.layers.l2 import Ether
from scapy.layers.rtp import RTP
from scapy.packet import Packet, Raw
from scapy.utils import PcapReader, rdpcap
from sqlalchemy import Column, Text, JSON, DATETIME
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import declarative_base

from config.db_conf import localhost_test_engine, localhost_test_session

Base = declarative_base()


class Package(Base):
    __tablename__ = 'package'
    # 原始数据
    id = Column(INTEGER, primary_key=True, comment="id")
    raw = Column(Text, comment="原始数据")
    debug_info = Column(JSON, comment="debug info, json, 4bit")
    # 数据链路层
    ether_time = Column(DATETIME, comment="版本, 4bit")
    # ether_type = Column(Text, comment="协议类型, 16bit")
    # 1500 1456 -12 = 1442

    ip_json_data = Column(JSON, comment="ip data")
    udp_json_data = Column(JSON, comment="udp data")
    tcp_json_data = Column(JSON, comment="tcp data")

    # RTP 层
    rtp_version = Column(Text, comment="版本号，固定为2，2bit")
    rtp_padding = Column(Text, comment="填充位，1bit")  # 1，表示此包后面会一定数目的填充比特；
    rtp_extension = Column(Text, comment="扩展位，1bit")  # 1，表示此包固定头部后面会跟着一个扩展头部；
    rtp_numsync = Column(Text, comment="CSRC计数位，4bit")  # 表示固定头部后面CSRC识别符的个数；
    rtp_marker = Column(Text, comment="标示位，1bit")  # 对于视频，标记一帧的结束
    rtp_payload_type = Column(Text, comment="负载类型，7bit")  # 表示具体的负载类型，比如音频、视频、文档等；
    rtp_seq = Column(Text, comment="序列号，16bit")  # 发送方在每发送完一个RTP包后就将该值增加1，接收方可以由该值检测包的丢失及恢复包序列。
    # 比如说一个音频的采样频率为8000Hz，那么我们可以把时间戳单位设为1 / 8000
    # timestamp表示每帧的时间，由于一个帧（如I帧）可能被分成多个RTP包，所以多个相同帧的RTP
    # timestamp相等。（可以通过每帧最后一个RTP的marker标志区别帧，但最可靠的方法是查看相同RTP timestamp包为同一帧。）
    rtp_timestamp = Column(Text, comment="时间戳，32bit")
    rtp_ssrc = Column(Text, comment="同步源标示符，32bit")  # 表示RTP数据包的来源，在同一个RTP会话中不可能存在两个相同的SSRC，SSRC的值是随机选取的；
    rtp_sync = Column(Text, comment="sync，12bit")
    # https://blog.csdn.net/ichenwin/article/details/100086930

    # https://www.rstk.cn/news/901965.html
    # 1.PS流传输格式预览
    #   1、视频关键帧的封装 RTP + PS header + PS system header + PS system Map + PES header +h264 data
    #   2、视频非关键帧的封装 RTP +PS header + PES header + h264 data
    #   3、音频帧的封装: RTP + PES header + G711

    ps_start_code = Column(Text, comment="开始码,32bit,")
    ps_clock1 = Column(Text, comment="包头scr,33bit,")  # 系统时钟基准（SCR-System Clock Reference）的基本部分
    ps_clock2 = Column(Text, comment="包头scr,33bit,")  # 系统时钟基准（SCR-System Clock Reference）的基本部分
    ps_clock3 = Column(Text, comment="包头scr,33bit,")  # 系统时钟基准（SCR-System Clock Reference）的基本部分
    ps_clock_extend = Column(Text, comment="包头scr,33bit,")  # 系统时钟基准（SCR-System Clock Reference）的基本部分
    ps_scr_extend = Column(Text, comment="包头scr 扩展部分,9bit,")
    ps_rate = Column(Text, comment="节目复用速率, 22bit,")
    ps_reserved = Column(Text, comment="节目复用速率, 22bit,")
    ps_options = Column(Text, comment="节目复用速率, 22bit,")

    # ps system header
    pss_start_code = Column(Text, comment="系统头 起始码, 32bit,")
    pss_header_len = Column(Text, comment="系统头 长度, 16bit,")
    pss_reserved = Column(Text, comment="系统头 速率界限, 22bit,")
    pss_options = Column(Text, comment="附加, var bit,")

    # psm Header
    psm_start_code = Column(Text, comment="开始码,32bit,")
    psm_stream_info = Column(Text, comment="info,32bit,")
    psm_stream_map = Column(Text, comment="map,32bit,")

    # pes Data
    pes_json_data = Column(JSON, comment="pes data")

    # h264 层
    # 帧 -- 合并


class PES(Packet):  # https://blog.csdn.net/marcosun_sw/article/details/86495509/
    name = "PES"
    fields_desc = [
        X3BytesField('pes_start_code', 0x000001),  # 起始码是(0x000001)
        ByteField('pes_stream_id', 0xe0),  # stream_id
        BitField('pes_pck_len', 0, 16),
        # PES包的长度, 指定在这个字段后的字节数，可以为零，如果这个字段为零的话，这个包可以是任意的长度，并且只有当这个 PES 包携带的是视频数据的时候，这个字段才可以为零
        BitField('pes_flag', b'\x01\x00', 2),  # 固定 '10'
        BitField('pes_scrambling_control', 0, 2),  # 加扰控制
        BitField('pes_priority', 1, 1),  # 优先级
        BitField('pes_data_alignment_indicator', 1, 1),  # 数据定位指示符
        BitField('pes_copyright', 0, 1),  # 是否版权
        BitField('pes_original_or_copy', 0, 1),  # 原始的或复制的
        BitField('pes_pts_flag', 1, 1),
        # 2位字段。当值为’10’时，PTS字段应出现在PES分组标题中；当值为’11’时，PTS字段和DTS字段都应出现在PES分组标题中；当值为’00’时，PTS字段和DTS字段都不出现在PES分组标题中。值’01’是不允许的。
        BitField('pes_dts_flag', 1, 1),
        BitField('pes_escr_flag', 0, 1),
        BitField('pes_es_rate_flag', 0, 1),
        BitField('pes_dsm_trick_mode_flag', 0, 1),
        BitField('pes_additional_copy_info_flag', 0, 1),
        BitField('pes_CRC_flag', 0, 1),
        BitField('pes_extension_flag', 0, 1),
        BitField('pes_header_data_length', 10, 8),  # 8位字段。指出包含在PES分组标题中的可选字段和任何填充字节所占用的总字节数。该字段之前的字节指出了有无可选字段。

        ConditionalField(BitField('pes_pts_start', 3, 4), lambda pkt: pkt.pes_pts_flag),
        ConditionalField(BitField('pes_pts_pts1', 0, 3), lambda pkt: pkt.pes_pts_flag),
        ConditionalField(BitField('pes_pts_mark1', 0, 1), lambda pkt: pkt.pes_pts_flag),
        ConditionalField(BitField('pes_pts_pts2', 0, 15), lambda pkt: pkt.pes_pts_flag),
        ConditionalField(BitField('pes_pts_mark2', 0, 1), lambda pkt: pkt.pes_pts_flag),
        ConditionalField(BitField('pes_pts_pts3', 0, 15), lambda pkt: pkt.pes_pts_flag),
        ConditionalField(BitField('pes_pts_mark3', 0, 1), lambda pkt: pkt.pes_pts_flag),

        ConditionalField(BitField('pes_dts_start', 3, 4), lambda pkt: pkt.pes_dts_flag),
        ConditionalField(BitField('pes_dts_dts1', 0, 3), lambda pkt: pkt.pes_dts_flag),
        ConditionalField(BitField('pes_dts_mark1', 0, 1), lambda pkt: pkt.pes_dts_flag),
        ConditionalField(BitField('pes_dts_dts2', 0, 15), lambda pkt: pkt.pes_dts_flag),
        ConditionalField(BitField('pes_dts_mark2', 0, 1), lambda pkt: pkt.pes_dts_flag),
        ConditionalField(BitField('pes_dts_dts3', 0, 15), lambda pkt: pkt.pes_dts_flag),
        ConditionalField(BitField('pes_dts_mark3', 0, 1), lambda pkt: pkt.pes_dts_flag),

        StrLenField("pes_header_data", b"",
                    length_from=lambda pkt: pkt.pes_header_data_length - (pkt.pes_pts_flag and 5) - (
                            pkt.pes_dts_flag and 5)),

        StrLenField("pes_payload", b"", length_from=lambda pkt: pkt.pes_pck_len - 3 - pkt.pes_header_data_length),
    ]

    def extract_padding(self, pkt):
        return "", pkt


class PSS(Packet):
    name = "PSS"
    fields_desc = [
        XIntField('pss_start_code', 1),  # 固定为0x000001BB，标志系统首部的开始
        ShortField('pss_header_len', 1),  # 表示此字段之后的系统首部字节长度
        BitField('pss_mark_1', 1, 1),  # 固定值为1
        BitField('pss_rate_bound', 50000, 22),  # 为一个大于或等于PS流所有PS包中的最大program_mux_rate值的整数；可以被解码器用来判断是否可以对整个流进行解码；
        BitField('pss_mark_2', 1, 1),
        BitField('pss_audio_bound', 1, 6),  # 取值范围0到32间整数, 大于或等于同时进行解码处理的PS流中的音频流的最大数目；
        BitField('pss_fixed_flag', 0, 1),  # 置位1表示固定比特率操作，置位0则为可变比特率操作；
        BitField('pss_csps_flag', 1, 1),  # 置位1表示此PS流满足标准的限制；
        BitField('pss_audio_lock_flag', 1, 1),  # 表示音频采样率和STD的system_clock_frequency之间有一特定常数比例关系
        BitField('pss_video_lock_flag', 1, 1),  # 表示在系统目标解码器system_clock_frequency和视频帧速率之间存在一特定常数比例关系；
        BitField('pss_mark_3', 1, 1),
        BitField('pss_video_bound', 1, 5),  # 取值范围0到16；大于或等于同时进行解码处理的PS流中的视频流的最大数目
        BitField('pss_restriction_flag', 1, 1),  # 分组速率限制标志字段 若CSPS_flag == 1，则此字段表示哪种限制适用于分组速率；若CSPS_flag == 0，则此字段无意义；
        BitField('pss_reserved', 0x7F, 7),  # 保留字段，占位7bit，固定为’1111111’；
        StrLenField("pss_options", b"", length_from=lambda pkt: pkt.pss_header_len - 6),
        # BitField('pss_audio_stream_id', 0xC0, 8),
        # BitField('pss_audio_mark', 3, 2),
        # BitField('pss_audio_pstd_buffer_bound_scale', 0, 1),
        # BitField('pss_audio_pstd_buffer_size_bound', 512, 13),
        #
        # BitField('pss_video_stream_id', 0xE0, 8),
        # BitField('pss_video_mark', 3, 2),
        # BitField('pss_video_pstd_buffer_bound_scale', 1, 1),
        # BitField('pss_video_pstd_buffer_size_bound', 2048, 13),

    ]

    def extract_padding(self, pkt):
        return "", pkt


class PSM(Packet):  # https://blog.csdn.net/marcosun_sw/article/details/86495509/
    name = "PSM"
    fields_desc = [
        # psm 记录了媒体信息，比如音视频的编码格式
        X3BytesField('psm_start_code', 0x000001),  # 包头起始码，固定为0x000001，占位24bit；与后面的字段map_stream_id一起组成分组开始码，标志着分组的开始；
        ByteField('psm_stream_id', 0xBC),  # 类型字段，标志此分组是什么类型，占位8bit；如果此值为0xBC，则说明此PES包为PSM；
        ShortField('psm_pck_len', 16),  # 表示此字段之后PSM的总长度，最大值为1018(0x3FA)；
        BitField('psm_next_indicator', 1, 1),  # 置位1表示当前PSM是可用的，置位0则表示当前PSM不可以，下一个可用；
        BitField('psm_reserved', 3, 2),
        BitField('psm_version', 0, 5),
        # 表示PSM的版本号，取值范围1到32，随着PSM定义的改变循环累加；若current_next_indicator == 1，表示当前PSM的版本号，若current_next_indicator == 0，表示下一个PSM的版本号
        BitField('psm_reserved2', 0x7F, 7),
        BitField('psm_mark_1', 1, 1),
        BitField('psm_stream_info_len', 0, 16),
        StrLenField("psm_stream_info", b"", length_from=lambda pkt: pkt.psm_stream_info_len),
        BitField('psm_stream_map_len', 8, 16),
        # 表示在这个PSM中所有ES流信息的总长度；包括stream_type,elementary_stream_id, elementary_stream_info_length的长度，即N*32bit；是不包括具体ES流描述信息descriptor的长度的；
        StrLenField("psm_stream_map", b"", length_from=lambda pkt: pkt.psm_stream_map_len),
        # #     /*video*/
        # BitField('psm_video_stream_type', 0x1B, 8),  # 视频编码格式H264
        # BitField('psm_video_elementary_stream_id', 0xE0, 8),
        # BitField('psm_video_elementary_stream_info_length', 0, 16),
        # #     /*audio*/
        # BitField('psm_audio_stream_type', 0x90, 8),  # 音频编码格式G711
        # BitField('psm_audio_elementary_stream_id', 0xC0, 8),
        # BitField('psm_audio_elementary_stream_info_length', 0, 16),

        #     /*crc*/
        BitField('psm_crc_32', 0x45, 32),
        StrLenField("psm_options", b"",
                    length_from=lambda pkt: pkt.psm_pck_len - 10 - pkt.psm_stream_info_len - pkt.psm_stream_map_len),

    ]

    def extract_padding(self, pkt):
        return "", pkt


class PS(Packet):
    name = "PS"
    # https://blog.csdn.net/ichenwin/article/details/100086930
    fields_desc = [
        # 0~3字节: 为0x 00 00 01 ba，表示当前为PSH头部 #I帧附加信息:20~23: 为0x 00 00 01 bb,表示当前为I帧附件信息
        # 当前为I帧或P帧的第一个NALU则需加PSH头部。若当前为I帧的第一个NALU还需要加PSM头部。
        # 每个NALU分为若干段，每段前需加PES头部, 每段数据与PES头部组成PES包。
        IntField('ps_start_code', 0x000001BA),  # 起始码，标识PS包的开始，固定为 0x000001BA
        BitField('ps_mark_1', 1, 2),
        BitField('ps_clock1', 1, 3),
        BitField('ps_mark_2', 1, 1),
        BitField('ps_clock2', 1, 15),
        BitField('ps_mark_3', 1, 1),
        BitField('ps_clock3', 1, 15),
        BitField('ps_mark_4', 1, 1),
        BitField('ps_clock_extend', 1, 9),
        BitField('ps_mark_5', 1, 1),
        BitField('ps_rate', 1, 22),  # 按协议的说法是以50字节50字节/秒为单位节目流的速率，可以理解为是码流。比如我们用海康的摄像头来验证，因为海康的摄像头是节目流出流的
        BitField('ps_mark_6', 0x11, 2),  # 固定 '11'
        BitField('ps_reserved', 0x1f, 5),
        BitField('ps_stuffing_length', 0, 3),
        StrLenField("ps_options", b"", length_from=lambda pkt: pkt.ps_stuffing_length),
        # PacketListField("ppp", None, ConditionalField),
        ConditionalField(PacketField("pss", None, PSS),
                         lambda pkt: pkt.original[pkt.ps_stuffing_length + 14:pkt.ps_stuffing_length + 18] == pss_bb),
        ConditionalField(PacketField("psm", None, PSM), lambda pkt: pkt.pss),
        PacketListField("pes", [], PES),
    ]


class H264(Packet):
    # 标准 H.264 流以 0x00 00 00 01 起始码为标志分割成若干单元，称之为 Network Abstraction Layer
    ...


ps_ba = b'\x00\x00\x01\xba'
pss_bb = b'\x00\x00\x01\xbb'
psm_bc = b'\x00\x00\x01\xbc'
pes_e0 = b'\x00\x00\x01\xe0'


class TestPcap(TestCase):
    def test_pre(self):
        ...
        Base.metadata.drop_all(localhost_test_engine)
        Base.metadata.create_all(localhost_test_engine)

    def test_to_db(self):
        # 合并psm pss, hex表示 str
        self.test_pre()
        packets = rdpcap('rtp.pcapng')
        for pck in packets:
            package = Package()

            package.debug_info = {
                "ps_ba": pck.original.count(ps_ba),
                "pss_bb": pck.original.count(pss_bb),
                "psm_bc": pck.original.count(psm_bc),
                "pes_e0": pck.original.count(pes_e0),
            }

            if not pck.haslayer(RTP) \
                    and isinstance(pck.lastlayer(), Raw) \
                    and isinstance(pck.lastlayer().underlayer, (UDP, TCP)):
                pck.lastlayer().underlayer.decode_payload_as(RTP)
                rtp: RTP = pck[RTP]
                if rtp.payload_type != 96:  # rtp.version ==
                    pck.lastlayer().underlayer.decode_payload_as(Raw)
            if pck.haslayer(RTP) and pck[RTP].payload.__bytes__().startswith(ps_ba):
                pck[RTP].decode_payload_as(PS)
            if pck.haslayer(Ether):
                ether: Ether = pck[Ether]
                package.ether_time = datetime.fromtimestamp(ether.time.real.__int__())
            if pck.haslayer(IP):
                ip: IP = pck[IP]
                package.ip_json_data = {"ip_version": ip.version, "ip_header_len": ip.ihl, "ip_ser": ip.tos,
                                        "ip_total_len": ip.len, "ip_id": ip.id, "ip_flags": ip.flags.value,
                                        "ip_offset": ip.frag, "ip_live_time": ip.ttl, "ip_prop": ip.proto,
                                        "ip_check": ip.chksum, "ip_src": ip.src, "ip_dst": ip.dst,
                                        "ip_other": str(ip.options)}
            if pck.haslayer(UDP):
                udp: UDP = pck[UDP]
                package.udp_json_data = {"udp_src_port": udp.sport, "udp_dst_port": udp.dport, "udp_len": udp.len,
                                         "udp_check": udp.chksum}
            if pck.haslayer(TCP):
                tcp: TCP = pck[TCP]
                package.tcp_json_data = {"tcp_sport": tcp.sport, "tcp_dport": tcp.dport, "tcp_seq": tcp.seq,
                                         "tcp_ack": tcp.ack,
                                         "tcp_offset": tcp.dataofs, "tcp_reserve": tcp.reserved,
                                         "tcp_flags": str(bin(tcp.flags.value)), "tcp_window": tcp.window,
                                         "tcp_check": tcp.chksum, "tcp_emergency": tcp.urgptr,
                                         "tcp_other": json.dumps(list(map(lambda x: hex(x), tcp.options)))}
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
                package.rtp_ssrc = hex(rtp.sourcesync).upper()
                package.rtp_sync = json.dumps(list(map(lambda x: hex(x), rtp.sync)))
            if pck.haslayer(PS):
                ps: PS = pck[PS]
                package.ps_start_code = ps.ps_start_code
                package.ps_clock1 = ps.ps_clock1
                package.ps_clock2 = ps.ps_clock2
                package.ps_clock3 = ps.ps_clock3
                package.ps_clock_extend = ps.ps_clock_extend
                package.ps_rate = ps.ps_rate
                package.ps_reserved = ps.ps_reserved
                assert ps.ps_mark_6 == 3, "校验"
                package.ps_options = ps.ps_options

                if ps.pss:
                    pss: PSS = ps.pss
                    package.pss_start_code = pss.pss_start_code
                    package.pss_header_len = pss.pss_header_len
                    assert pss.pss_reserved == 127, "校验 固定值"
                    package.pss_reserved = pss.pss_reserved
                    package.pss_options = pss.pss_options
                if ps.psm:
                    psm: PSM = ps.psm
                    package.psm_start_code = psm.psm_start_code
                    assert psm.psm_start_code == 1, "校验 固定值"
                    package.psm_stream_id = psm.psm_stream_id
                    assert psm.psm_stream_id == 0xbc, "校验"
                    package.psm_stream_info = psm.psm_stream_info.hex()
                    package.psm_stream_map = psm.psm_stream_map.hex()
                if ps.pes:
                    pes_list: List[PES] = ps.pes

                    data = []
                    for pes in pes_list:
                        assert pes.pes_flag == 2, "校验"
                        assert pes.pes_start_code == 1, "校验"
                        data.append({
                            "pes_start_code": pes.pes_start_code,
                            "pes_stream_id": pes.pes_stream_id,
                            "pes_pck_len": pes.pes_pck_len,
                            "pes_flag": pes.pes_flag,
                            "pes_pts_flag": pes.pes_pts_flag,
                            "pes_dts_flag": pes.pes_dts_flag,

                            "pes_pts_start": pes.pes_pts_start,
                            "pes_pts_pts1": pes.pes_pts_pts1,
                            "pes_pts_pts2": pes.pes_pts_pts2,
                            "pes_pts_pts3": pes.pes_pts_pts3,

                            "pes_dts_start": pes.pes_dts_start,
                            "pes_dts_dts1": pes.pes_dts_dts1,
                            "pes_dts_dts2": pes.pes_dts_dts2,
                            "pes_dts_dts3": pes.pes_dts_dts3,

                            "pes_header_data": pes.pes_header_data.hex(),
                            "pes_payload": pes.pes_payload.hex(),
                        })
                    package.pes_json_data = data
            if isinstance(pck.lastlayer(), Raw):
                package.raw = pck.lastlayer().original.hex()  # pck.lastlayer().__bytes__().hex()

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

    def test_mp4(self):
        # 转MP4
        vos = localhost_test_session.query(Package).filter(
            Package.psm_start_code.isnot(None)
        ).all()
        vos2 = localhost_test_session.query(Package).filter(
            Package.id < vos[1].id
        ).all()
        # vos2 = localhost_test_session.query(Package).all()
        with open('2.raw', mode='wb') as f:
            for vo2 in vos2:
                if vo2.pes_json_data:
                    for pes in vo2.pes_json_data:
                        f.write(bytearray.fromhex(pes["pes_payload"]))
                if vo2.raw:
                    f.write(bytearray.fromhex(vo2.raw))
                # if vo2.rtp_marker == 1:
                #     break

    def test_assert(self):
        # assert "", 关键帧， # ps_bb bc ==1, e0==4,pes_json_data, 两个关键帧之间 25帧
        # 关键帧 转 rpg
        # 关键帧 真实时间
        # 关键帧 时间戳
        ...
