from scapy.fields import ByteField, FieldLenField, StrFixedLenField
from scapy.packet import Packet


class XNumberField(FieldLenField):
    __slots__ = ["sep"]  # 否则  self.sep 报错

    def __init__(self, name, default, sep=b"\r\n", length_of=None):
        FieldLenField.__init__(self, name, default, length_of=length_of)
        self.sep = sep

    def i2m(self, pkt, x):
        x = FieldLenField.i2m(self, pkt, x)
        return "%02x" % x
        # return x.to_bytes()

    def m2i(self, pkt, x):
        return int(x, 16)

    def addfield(self, pkt, s, val):
        return s + self.i2m(pkt, val)

    def getfield(self, pkt, s):
        sep = s.find(self.sep)
        return s[sep:], self.m2i(pkt, s[:sep])


class Foo(Packet):
    fields_desc = [
        ByteField("type", 0),
        XNumberField("len", None, b"\r\n", "sep"),
        StrFixedLenField("sep", b"\r\n", 2)
    ]

    def post_build(self, p, pay):
        if self.len is None and pay:
            l = len(pay)
            p = p[:1] + hex(l)[2:] + p[2:]
        return p + pay


if __name__ == '__main__':
    p = Foo() / ("X" * 32)
    p.show2()
