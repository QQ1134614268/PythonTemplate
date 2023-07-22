from unittest import TestCase

from scapy.fields import ByteField, FieldLenField, FieldListField, PacketListField, StrLenField, \
    IPField
from scapy.layers.inet import IP
from scapy.packet import Packet


class TestPcap(TestCase):

    def test1(self):
        class TestSLF(Packet):
            fields_desc = [FieldLenField("len", None, length_of="data"),
                           StrLenField("data", b"", length_from=lambda pkt: pkt.len)]

        package = TestSLF(b"\x00\x02ABCDEFGHIJKL")
        package.show2()

    def test2(self):
        class TestPLF(Packet):
            fields_desc = [
                FieldLenField("len", None, count_of="plist"),
                PacketListField("plist", None, IP, count_from=lambda pkt: pkt.len)
                # PacketListField("options", [], IPOption, length_from=lambda p: p.ihl * 4 - 20)]  # HTTP
            ]

        con = IP().__bytes__()
        package = TestPLF(b"\x10\x02" + con * 3 + b"ABCDEFGHIJKL")
        package.show2()

    def test3(self):
        class TestFLF(Packet):
            fields_desc = [
                FieldLenField("len", None, count_of="data"),
                FieldListField("data", ["1.2.3.4"], IPField("", "0.0.0.0"), count_from=lambda pkt: pkt.len)]

        package = TestFLF(b"\x00\x02ABCDEFGHIJKL")
        package.show2()

    def test4(self):
        class TestPLF2(Packet):
            class TestPkt(Packet):
                fields_desc = [ByteField("f1", 1),
                               ByteField("f2", 1)]

                def extract_padding(self, s):  # 重要
                    # return s, None
                    return "", s

            fields_desc = [
                FieldLenField("len1", None, count_of="plist", fmt="B", adjust=lambda pkt, x: x),
                FieldLenField("len2", None, length_of="plist", fmt="H", adjust=lambda pkt, x: x),
                PacketListField("plist", [], TestPkt, length_from=lambda pck: pck.len2)
            ]

        package = TestPLF2(b"\x04\x00\x08ababababxxxx")
        package.show2()
