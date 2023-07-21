from scapy.fields import ByteField, FieldLenField, FieldListField, PacketListField, StrLenField, \
    ShortField, IPField
from scapy.layers.inet import IP
from scapy.packet import Packet


class TestSLF(Packet):
    fields_desc = [FieldLenField("len", None, length_of="data"),
                   StrLenField("data", "", length_from=lambda pkt: pkt.len)]


class TestPLF(Packet):
    fields_desc = [FieldLenField("len", None, count_of="plist"),
                   PacketListField("plist", None, IP, count_from=lambda pkt: pkt.len)]


class TestFLF(Packet):
    fields_desc = [
        FieldLenField("the_lenfield", None, count_of="the_varfield"),
        FieldListField("the_varfield", ["1.2.3.4"], IPField("", "0.0.0.0"),
                       count_from=lambda pkt: pkt.the_lenfield)]


class TestPLF2(Packet):
    class TestPkt(Packet):
        fields_desc = [ByteField("f1", 65),
                       ShortField("f2", 0x4244)]

        def extract_padding(self, p):
            return "", p

    fields_desc = [
        FieldLenField("len1", None, count_of="plist", fmt="H", adjust=lambda pkt, x: x + 2),
        FieldLenField("len2", None, length_of="plist", fmt="I", adjust=lambda pkt, x: (x + 1) / 2),
        PacketListField("plist", None, TestPkt, length_from=lambda x: (x.len2 * 2) / 3 * 3)
    ]


# ByteField
# IntField
# StrField(name, default, fmt="H", remain=0, shift=0) # remain todo

if __name__ == '__main__':
    package = TestSLF(b"\x00\x02ABCDEFGHIJKL")
    package.show2()

    con = IP().__bytes__()
    package = TestPLF(b"\x10\x02" + con * 3 + b"ABCDEFGHIJKL")
    package.show2()

    package = TestFLF(b"\x00\x02ABCDEFGHIJKL")
    package.show2()

    pkt = TestPLF2(b"\x00\x02\x00\x03ABC")
    pkt.show2()
