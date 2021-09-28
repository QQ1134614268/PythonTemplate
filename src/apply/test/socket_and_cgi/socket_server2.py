import select
import socket

s = socket.socket()

host = socket.gethostname()
port = 1234
s.bind((host, port))
s.listen(5)  # 最多多少个链接
inputs = [s]
while True:
    rs, ws, es = select.select(inputs, [], [])
    for r in rs:
        if r is s:
            c, addr = s.accept()
            print("connect ", addr)
            inputs.append(c)
    else:
        try:
            data = r.recv(1024)
            disconnect = not data
        except socket.error:
            disconnect = True
        if disconnect:
            print(r.getpeername(), "disconnect")
            inputs.remove(r)
        else:
            print(data)
