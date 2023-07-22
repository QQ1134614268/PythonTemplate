from scapy.fields import ByteField, StrLenField, \
    XByteField, ByteEnumField, StrField, StrFixedLenField, \
    StrStopField, LenField, FieldLenField, PacketLenField, PacketField, PacketListField, FieldListField, Field, \
    ConditionalField
from scapy.packet import Packet


class MyTestPck(Packet):
    class InnerField(Field):
        def __init__(self, name, default):
            Field.__init__(self, name, default, "B")

    class InnerPkt(Packet):
        fields_desc = [ByteField("name", 0),
                       ByteField("value", 1)]

        def extract_padding(self, s):  # 重要
            # return s, None
            return "", s

    fields_desc = [
        ByteField("ByteField", 0),
        XByteField("XByteField", 0),
        # IntField("IntField", 0),
        # XIntField("XIntField", 0),
        ByteEnumField("byte_enum_field", 4, {1: "REQUEST", 2: "RESPONSE", 3: "SUCCESS", 4: "FAILURE"}),
        # IntEnumField("IntEnumField", 4, {1: "REQUEST", 2: "RESPONSE", 3: "SUCCESS", 4: "FAILURE"}),

        ByteField("len_1", 4),

        StrField("StrField", "StrField", fmt="H", remain=-1),
        StrLenField("StrLenField", b"StrLenField", length_from=lambda pkt: pkt.len_1),
        StrFixedLenField("StrFixedLenField", b"StrFixedLenField", length=None, length_from=lambda pkt: pkt.len_1),
        StrStopField("StrStopField", "abcdStopAAA", stop=b"\x04\x04", additional=3),

        FieldLenField("field_len_2", None, length_of="field_list_2", fmt="B", count_of=None, adjust=lambda pkt, x: x),
        FieldListField("field_list_2", [], InnerField("InnerField", ""), length_from=lambda pck: pck.len_1),

        PacketLenField("packet_len", InnerPkt(), InnerPkt, length_from=lambda pck: pck.len_1),

        PacketField("packet_field", None, InnerPkt),
        PacketListField("packet_list", None, InnerPkt, length_from=lambda pck: pck.len_1),

        ConditionalField(ByteField("reserved", 0), lambda pkt: pkt.byte_enum_field == 4),

        LenField("len_2", 1, fmt='B', adjust=lambda x: x + 1),  # ?? \x04\x04 =1028

    ]
    # UTCTimeField UUIDField MultipleTypeField  MultipleTypeField FlagsField

# LenField : 自动根据payload 计算长度

# FieldLenField 可根据 FieldListField 自动计算长度
# FieldListField 自动组装成list

# PacketField: 自动组装 packet
# PacketListField: 自动组装成 list;  List[Packet]

# PacketLenField

# count_from:
# count_of:
# length_from:
# length_of
# adjust: 自动计算
# fmt: B: 1字节,Byte; H:2字节, I: 4字节

if __name__ == '__main__':
    # MyTestPck(ByteField=16, XByteField=32, ByteEnumField=1, len_1=4, StrField="\04")
    MyTestPck(b"\x04" * 50).show2()
    # OFPTPacketIn(b"A" * 30).show2()
