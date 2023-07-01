1. ip 过滤
ip.src == 127.0.0.1
ip.dst == 127.0.0.1

2. 协议过滤
http
sip
udp

3. 端口过滤
tcp.port == 80
tcp.srcport == 127.0.0.1
tcp.dstport == 80
4. 包长度过滤
udp.length == 26 # header + body
tcp.len > 36 
5. 支持的语法(类 Python?)
== > >=  () ! not  and or eq 
6. http 过滤
http.request.method == "GET"
http.request.uri == "/api/hello"
http contains "Host: "
http.content_type




