lsc() 命令：列出scapy通用的操作方法，常用的函数包括：

arpcachepoison（用于arp毒化攻击，也叫arp欺骗攻击）
arping（用于构造一个ARP的who-has包）
send：发送3层报文（ 如TCP/UDP 协议），不接收数据包
sendp：发送2层报文(通过mac地址转发)，不接收
sniff：用于网络嗅探，类似Wireshark和tcpdump抓包
sr：发送，接收3层报文，返回有回应的数据包和没有回应的数据包。
sr1：发送，只接收1个响应包
srp：发送，接收2层报文
srp1：发送，只接收1个响应包

ls()：查看支持的协议

