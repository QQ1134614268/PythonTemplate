# -*- coding: utf-8 -*-
"""
# @Time    : 2019/10/3 21:14
"""

# https://www.cnblogs.com/weiququ/p/9471844.html
import time
from datetime import datetime, timedelta

# 1. time.time()输出当前时间戳
# 2. 获取当前时间，时间元组的形式localtime()
# 3. 最简单的获取可读的时间形式asctime():
# 4. 格式化日期
# ----------------------------------------
# 1. 获取当前时间和日期
# 2. 获取指定日期
# 3. datetime转换为timestamp
# 4. timestamp转换为datetime
# 5. str转换为datetime
# 6. datetime转换为str
# 7. datetime加减

ticks = time.time()
print("时间戳: ", ticks)
localtime_struct_time = time.localtime()  # localtime(seconds=None)
print("时间元组的形式: ", localtime_struct_time)
localtime = time.asctime()  # asctime(p_tuple=None)
print("简单可读时间: ", localtime)
format_time = time.strftime("%Y-%m-%d %H:%M:%S")  # strftime(format, p_tuple=None)
print("格式化: ", format_time)

# 1. 获取当前时间和日期
now = datetime.now()
print("当前时间: ", now)
# 2. 获取指定日期
dt = datetime(2015, 4, 19, 12, 20)  # 用指定日期时间创建datetime
print("指定日期: ", dt)
# 3. datetime转换为timestamp
ts = dt.timestamp()  # dt.time() 获取时间部分
print("datetime转时间戳: ", dt)
# 4. timestamp转换为datetime
dt = datetime.fromtimestamp(ts)
print("时间戳转datetime: ", dt)
# 5. str转换为datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print("字符串转datetime: ", dt)
# 6. datetime转换为str
dt = now.strftime('%a, %b %d %H:%M')
print("datetime转换为str: ", dt)
# 7. datetime加减
add_time = datetime.now() + timedelta(days=2, hours=12)
print("时间加减: ", add_time)
