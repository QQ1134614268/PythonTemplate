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


class TestHTTP(Packet):
    name = "HTTP 1"
    fields_desc = []
    show_indent = 0

    @classmethod
    def dispatch_hook(cls, _pkt=None, *args, **kargs):
        if _pkt and len(_pkt) >= 9:
            from scapy.contrib.http2 import _HTTP2_types, H2Frame
            # To detect a valid HTTP2, we check that the type is correct
            # that the Reserved bit is set and length makes sense.
            while _pkt:
                if len(_pkt) < 9:
                    # Invalid total length
                    return cls
                if ord(_pkt[3:4]) not in _HTTP2_types:
                    # Invalid type
                    return cls
                length = struct.unpack("!I", b"\0" + _pkt[:3])[0] + 9
                if length > len(_pkt):
                    # Invalid length
                    return cls
                sid = struct.unpack("!I", _pkt[5:9])[0]
                if sid >> 31 != 0:
                    # Invalid Reserved bit
                    return cls
                _pkt = _pkt[length:]
            return H2Frame
        return cls

    # tcp_reassemble is used by TCPSession in session.py
    @classmethod
    def tcp_reassemble(cls, data, metadata, _):
        detect_end = metadata.get("detect_end", None)
        is_unknown = metadata.get("detect_unknown", True)
        if not detect_end or is_unknown:
            metadata["detect_unknown"] = False
            http_packet = HTTP(data)
            # Detect packing method
            if not isinstance(http_packet.payload, _HTTPContent):
                return http_packet
            length = http_packet.Content_Length
            if length is not None:
                # The packet provides a Content-Length attribute: let's
                # use it. When the total size of the frags is high enough,
                # we have the packet
                length = int(length)
                # Subtract the length of the "HTTP*" layer
                if http_packet.payload.payload or length == 0:
                    http_length = len(data) - len(http_packet.payload.payload)
                    detect_end = lambda dat: len(dat) - http_length >= length
                else:
                    # The HTTP layer isn't fully received.
                    detect_end = lambda dat: False
                    metadata["detect_unknown"] = True
            else:
                # It's not Content-Length based. It could be chunked
                encodings = http_packet[HTTP].payload._get_encodings()
                chunked = ("chunked" in encodings)
                is_response = isinstance(http_packet.payload, HTTPResponse)
                if chunked:
                    detect_end = lambda dat: dat.endswith(b"0\r\n\r\n")
                # HTTP Requests that do not have any content,
                # end with a double CRLF
                elif isinstance(http_packet.payload, HTTPRequest):
                    detect_end = lambda dat: dat.endswith(b"\r\n\r\n")
                    # In case we are handling a HTTP Request,
                    # we want to continue assessing the data,
                    # to handle requests with a body (POST)
                    metadata["detect_unknown"] = True
                elif is_response and http_packet.Status_Code == b"101":
                    # If it's an upgrade response, it may also hold a
                    # different protocol data.
                    # make sure all headers are present
                    detect_end = lambda dat: dat.find(b"\r\n\r\n")
                else:
                    # If neither Content-Length nor chunked is specified,
                    # it means it's the TCP packet that contains the data,
                    # or that the information hasn't been given yet.
                    detect_end = lambda dat: metadata.get("tcp_end", False)
                    metadata["detect_unknown"] = True
            metadata["detect_end"] = detect_end
            if detect_end(data):
                return http_packet
        else:
            if detect_end(data):
                http_packet = HTTP(data)
                return http_packet

    def guess_payload_class(self, payload):
        """Decides if the payload is an HTTP Request or Response, or
        something else.
        """
        try:
            prog = re.compile(
                br"^(?:OPTIONS|GET|HEAD|POST|PUT|DELETE|TRACE|CONNECT) "
                br"(?:.+?) "
                br"HTTP/\d\.\d$"
            )
            crlfIndex = payload.index(b"\r\n")
            req = payload[:crlfIndex]
            result = prog.match(req)
            if result:
                return HTTPRequest
            else:
                prog = re.compile(br"^HTTP/\d\.\d \d\d\d .*$")
                result = prog.match(req)
                if result:
                    return HTTPResponse
        except ValueError:
            # Anything that isn't HTTP but on port 80
            pass
        return Raw


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
