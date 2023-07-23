from scapy.fields import ByteField, StrLenField, \
    XByteField, ByteEnumField, StrField, StrFixedLenField, \
    StrStopField, LenField, FieldLenField, PacketLenField, PacketField, PacketListField, FieldListField, \
    ConditionalField, MultipleTypeField, IntField
from scapy.packet import Packet


class MyTestPck(Packet):
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
        FieldListField("field_list_2", [], ByteField("innerField", None), length_from=lambda pck: pck.len_1),

        # BitFieldLenField('numsync', None, 4, count_of='sync'),
        # FieldListField('sync', [], IntField("id", 0), count_from=lambda pkt: pkt.numsync),

        PacketLenField("packet_len", InnerPkt(), InnerPkt, length_from=lambda pck: pck.len_1),

        PacketField("packet_field", None, InnerPkt),
        PacketListField("packet_list", None, InnerPkt, count_from=None, length_from=lambda pck: pck.len_1),

        ConditionalField(ByteField("reserved", 0), lambda pkt: pkt.byte_enum_field == 4),
        MultipleTypeField(
            [
                (ByteField("b", None), lambda pkt: pkt.len_1 == 1),
                (IntField("b", None), lambda pkt: pkt.len_1 != 1)
            ],
            ByteField("b", None)),  # 根据 lambda 构造类型, 参数有默认值
        LenField("len_2", 1, fmt='B', adjust=lambda x: x + 1),  # ?? \x04\x04 =1028

    ]


# ConditionalField: 根据 lambda 构造类型
# MultipleTypeField: list中字段, 根据 lambda 构造类型

# LenField : 自动根据payload 计算长度

# FieldLenField 可根据 字段(eg: FieldListField) 自动计算长度(length_from), 个数(count_of)
# FieldListField 自动组装成list, 一般用 IntField 列表

# PacketField: 自动组装 packet
# PacketListField: 自动组装成 list;  List[Packet]

# PacketLenField: 根据字段(PacketField, PacketListField) 自动计算长度(length_from), 个数(count_of)

# count_from:  从个数 eg: RTP
# count_of: 列表的个数
# length_from: 从长度
# length_of: 列表的长度
# adjust: 自动计算
# fmt: B: 1字节,Byte; H:2字节, I: 4字节

if __name__ == '__main__':
    # MyTestPck(ByteField=16, XByteField=32, ByteEnumField=1, len_1=4, StrField="\04")
    MyTestPck(b"\x04" * 50).show2()
    # OFPTPacketIn(b"A" * 30).show2()
