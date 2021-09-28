import socket

s = socket.socket()

host = socket.gethostname()
print(host)
port = 1234
s.bind((host, port))
# s.bind(("127.0.0.1", port))
s.listen(5) # 最多多少个链接
while True:
    c, addr = s.accept()
    print("got connect from ", addr)
    c.send(b"thinks for connecting")
    c.close()
