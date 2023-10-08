# 语法: tcpdump option [ expression ]
#    expression(proto dir type):
#      option: -i -w 等
#      proto: 协议 ip tcp udp 等, 不支持应用协议 http sip
#      dir: 方向 src dst
#      type: 类型 host net port

1. 根据ip/网段
tcpdump -i enp0s20f0u1 -s 0 -w out.pcap src host 44.39.52.214
2. 根据端口

3. 根据协议
tcpdump -i enp0s20f0u1 -s 0 -w out.pcap

# 其他 过滤
tcp.stream == 5
tcp.options.sack
tcp.analysis.out_of_order
tcp.analysis.retransmission
tcp.flags.reset == 1

# 时间过滤
frame.time >= "2023-01-00 10:10:10"

# 长度过滤
ip.len == 100 # 除了以太网头固定长度14，从IP Header到IP payload的总长度
frame.len == 119 # 整个数据包长度，从ethernet层开始到最后


tcpdump host 44.39.52.214 -i any -s 0 -vv -w 0612-1.pcap
tcpdump src net 44.39.52.0/24 -i any -s 0 -w rtp_port.pcap
tcpdump \( src net 44.39.52.0/24 or port 5060 \) and udp -i any -s 0 -vv -w test_01.pcap

# 运算符 and or not && || ! ()

# tcpdump 过滤
tcpdump -i eth0 -s 0 -w out.pcap     #监听网络接口字节为0保存到out.pcap文件中
tcpdump -r out.pcap                  #来读取a.cap文件内容
tcpdump -A -r out.pcap #以ASCII格式打印出所有的分组并且读取此文件
tcpdump -X -r out.pcap #以十六进制格式打印出所有的分组并且读取此文件
tcpdump -i eth0 tcp port 22 # 只抓TCP,22端口的包,这里我们用nc来连一下另一台虚拟机的22端口

tcpdump port 53 -r out.pcap #50端口
tcpdump -n -r out.pcap | awk '{print $3}'| sort -u #-n 是不对域名做解析,只以IP地址的形式来显示;awk '{print $3}'显示第三列的内容;sort -u 筛选掉重复的内容
tcpdump -n src host 145.254.160.237 -r out.pcap # 只有数据包的来源IP(源)145.254.160.237是这个的才提取
tcpdump -n dst host 145.254.160.237 -r out.pcap #只有数据包是这个目标地址145.254.160.237才显示出来
tcpdump -n port 53 -r out.pcap #50端口
tcpdump -nX port 80 -r out.pcap #16进制显示80端口的信息
tcpdump -A -n 'tcp[13]=24' -r out.pcap #ascll码 只显示tcp13位为24的

tcpdump -i eth0 'port 1111' -c 3 -r out.pcap # 即可进行流量回放;

# 参数:

-i any # 指定网络接口, 不指定为第一个网络接口 eth0, any 任意
-s 0 # 指定包大小, 0 不限制大小
-vv 输出详细的报文信息
-r 从指定的文件中读取包, 这些包一般通过-w选项产生


参数:
    -A 以ASCII格式打印出所有分组,并将链路层的头最小化;
    -c 在收到指定的数量的分组后,tcpdump就会停止;
    -C 在将一个原始分组写入文件之前,检查文件当前的大小是否超过了参数file_size 中指定的大小; 如果超过了指定大小,则关闭当前文件,然后在打开一个新的文件; 参数 file_size 的单位是兆字节(是1,000,000字节,而不是1,048,576字节);
    -d 将匹配信息包的代码以人们能够理解的汇编格式给出;
    -dd 将匹配信息包的代码以c语言程序段的格式给出;
    -ddd 将匹配信息包的代码以十进制的形式给出;
    -D 打印出系统中所有可以用tcpdump截包的网络接口;
    -e 在输出行打印出数据链路层的头部信息;
    -E 用spi@ipaddr algo:secret解密那些以addr作为地址,并且包含了安全参数索引值spi的IPsec ESP分组;
    -f 将外部的Internet地址以数字的形式打印出来;
    -F 从指定的文件中读取表达式,忽略命令行中给出的表达式;
    -i 指定监听的网络接口;
    -l 使标准输出变为缓冲行形式,可以把数据导出到文件;
    -L 列出网络接口的已知数据链路;
    -m 从文件module中导入SMI MIB模块定义; 该参数可以被使用多次,以导入多个MIB模块;
    -M 如果tcp报文中存在TCP-MD5选项,则需要用secret作为共享的验证码用于验证TCP-MD5选选项摘要(详情可参考RFC 2385);
    -b 在数据-链路层上选择协议,包括ip,arp,rarp,ipx都是这一层的;
    -n 不把网络地址转换成名字;
    -nn 不进行端口名称的转换;
    -N 不输出主机名中的域名部分; 例如,'nic.ddn.mil'只输出'nic';
    -t 在输出的每一行不打印时间戳;
    -O 不运行分组分组匹配(packet-matching)代码优化程序;
    -P 不将网络接口设置成混杂模式;
    -q 快速输出; 只输出较少的协议信息;
    -r 从指定的文件中读取包(这些包一般通过-w选项产生);
    -S 将tcp的序列号以绝对值形式输出,而不是相对值;
    -s 从每个分组中读取最开始的snaplen个字节,而不是默认的68个字节;
    -T 将监听到的包直接解释为指定的类型的报文,常见的类型有rpc远程过程调用)和snmp(简单网络管理协议;);
    -t 不在每一行中输出时间戳;
    -tt 在每一行中输出非格式化的时间戳;
    -ttt 输出本行和前面一行之间的时间差;
    -tttt 在每一行中输出由date处理的默认格式的时间戳;
    -u 输出未解码的NFS句柄;
    -v 输出一个稍微详细的信息,例如在ip包中可以包括ttl和服务类型的信息;
    -vv 输出详细的报文信息;
    -w 直接将分组写入文件中,而不是不分析并打印出来;


tcpdump version 4.9.2
libpcap version 1.5.3
OpenSSL 1.0.2k-fips  26 Jan 2017
Usage: tcpdump [-aAbdDefhHIJKlLnNOpqStuUvxX#] [ -B size ] [ -c count ]
                [ -C file_size ] [ -E algo:secret ] [ -F file ] [ -G seconds ]
                [ -i interface ] [ -j tstamptype ] [ -M secret ] [ --number ]
                [ -Q|-P in|out|inout ]
                [ -r file ] [ -s snaplen ] [ --time-stamp-precision precision ]
                [ --immediate-mode ] [ -T type ] [ --version ] [ -V file ]
                [ -w file ] [ -W filecount ] [ -y datalinktype ] [ -z postrotate-command ]
                [ -Z user ] [ expression ]
