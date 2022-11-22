import os
import threading

import time


def test_loop():
    while True:
        time.sleep(1)


def test1():
    test_loop()


def test2():
    test_loop()


if __name__ == '__main__':
    print(os.getpid())
    t1 = threading.Thread(target=test1, args=())
    t2 = threading.Thread(target=test2, args=())
    t1.start()
    t2.start()
    time.sleep(12345)

# pstree -apl 7954
# ps -Lf 7954
# pstack 510
