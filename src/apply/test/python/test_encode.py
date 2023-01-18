# -*- coding:utf-8 -*-
"""
@Time: 2021/8/19
@Description: 测试字符串编码,及编码展示解析
"""
res = "中".encode("utf-16")  # b'\xff\xfe-N'
# \x: 接下来两个字符以16进制解析
# \xff\xfe utf-16编码标识
# e-N: 中的utf-16编码

# eg: "a".encode("utf-16")  b'\xff\xfea\x00'  同: \xff\xfe  a\x00
#     "aa".encode("utf-16") b'\xff\xfea\x00a\x00' 同: \xff\xfe a\x00 a\x00

# 单字节: 'a' = 97 = 0x61 = b'a'
# 双字节: b'a\x00' 或者  b'\x00a' (little or big)

# 0x用于16进制数字 "\x"用于内部串来表示一个字符

# doc: ord('a')  chr(65) hex(97) (97).to_bytes(2, byteorder='big') (97).to_bytes(2, byteorder='little')

# 同理: 文件内部如此存储,查看字节,使用notepad++,hex view

print(res)

res = b'\xff\xfe-N'.decode("utf-16")  # 解码时忽略 b'\xff\xfe'
print(res)

# file.readline 就是根据 \n换行; 使用utf-16 会把 b'\n\x00'("\n".encode("utf-16")==b'\n\x00') 拆成两行,转字符时自行处理

# 推,同理: utf-8, utf-8-bom, utf-16(utf-16-le), utf-16-be
# 推,同理: GBK, gb2312

# 应用: 超大文件读取最后若干行 (自带的文本编辑器打不开)
with open(r'utf-16-le_demo.txt', 'rb') as f:
    f.seek(-50000, 2)
    lines = f.readlines()
    for line in lines:
        if line.startswith(b"\x00"):
            line = line[1:]
        if line.endswith(b"\n"):
            line = line + b"\x00"
        print(str(line.decode('utf-16')))
