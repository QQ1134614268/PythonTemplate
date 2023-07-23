# https://www.jianshu.com/p/88e4df708970

import struct

from scapy.fields import Field, ShortField
from scapy.packet import Packet
from scapy.utils import hexdump


def hexify(buffer):
    """
    Return a hexadecimal string encoding of input buffer
    """
    return ' '.join('%02x' % ord(c) for c in buffer)


class RecordField(Field):
    def __init__(self, name, default):
        Field.__init__(self, name, default)

    def addfield(self, pkt, s, val):
        name = bytearray(val['name']) + bytearray(1)
        height = val['height']
        age = val['age']

        return s + name + struct.pack("I", height) + struct.pack("H", age)

    def getfield(self, pkt, s):
        index = 0
        for b in bytearray(s):
            if b == 0x00:
                break
            else:
                index += 1
        result = {'name': s[:index],
                  'height': struct.unpack("I", s[index + 1:index + 5])[0],
                  'age': struct.unpack("H", s[index + 5:index + 7])[0]}

        return s[index + 7:], result


class MyFrame(Packet):
    name = "MyFrame"
    fields_desc = [
        ShortField("id", 0),
        RecordField("record", None)
    ]


frame = MyFrame(
    id=100,
    record={
        "name": "jobs",
        "height": 180,
        "age": 55
    }
)

frame.show()
print(hexify(str(frame)))
hexdump(frame)
print(frame.fields_desc[1].getfield(frame, str(frame)[2:]))

# addfield是成帧函数，输出一个最终的bytes数组，输入参数如下
#     pkt: 本Field对象所属的Packet对象实例
#     s: Packet已经构建出的bytearray数组，即本Field之前的那些Field组成的bytearray,所以返回值一定是s + 自己的bytearray，如果自己是空，则只返回s
#     val: 定义Packet实例时传给自己的值，类型不确定

# 自定义Field，只需要继承Field类，重写addfield和getfield函数就可以了
# addfield函数是把对象变为bytearray，反过来，getfield即把bytearray变为对象

# 00 64   #id=100
# 6a 6f 62 73 00  #record.name=jobs
# b4 00 00 00     #record.height=180
# 37 00           #record.age=55
