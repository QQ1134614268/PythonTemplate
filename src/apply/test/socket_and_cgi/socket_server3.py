import socket

import select

s = socket.socket()

host = socket.gethostname()
print(host)
port = 1234
s.bind((host, port))
fdamp = {s.fileno(): s}
# s.bind(("127.0.0.1", port))
s.listen(5)  # 最多多少个链接
p = select.poll()
p.regeist(s)
while True:
    events = p.poll()
    for fd, event in events:
        if fd in fdamp:
            c, addr = s.accept()
            print('connect ', addr)
            p.regeist(c)
            fdamp[c.fileno()] = c
        elif event & select.POLLIN:
            data = fdamp[fd].recv(1024)
            if not data:
                print(fdamp[fd].getpeername(), "disconnect")
                p.unregeist(fd)
                del fdamp[fd]
            else:
                print(data)
