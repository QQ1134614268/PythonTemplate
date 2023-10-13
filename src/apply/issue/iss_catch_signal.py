# -*- coding:utf-8 -*-
import signal
import os
import time


def receive_signal(signal_number, frame):
    with open("out.log", "a") as f:
        f.write(f"Received: {signal_number}\r\n")
    print('Received:', signal_number)
    return


if __name__ == '__main__':  # register the signals to be caught
    # linux strace更好追踪进程接收的信号
    signalList = [
        signal.SIGHUP,  # win 不支持
        signal.SIGINT,
        signal.SIGQUIT,  # win 不支持
        signal.SIGILL,
        signal.SIGTRAP,  # win 不支持
        signal.SIGABRT,
        signal.SIGBUS,  # win 不支持
        signal.SIGFPE,
        # signal.SIGKILL # 不能捕捉
        signal.SIGUSR1,  # win 不支持
        signal.SIGSEGV,  # win 不支持
        signal.SIGUSR2,  # win 不支持
        signal.SIGPIPE,  # win 不支持
        signal.SIGALRM,  # win 不支持
        signal.SIGTERM,
    ]

    for sig in signalList:
        signal.signal(sig, receive_signal)
    print('My PID is:', os.getpid())  # wait in an endless loop for signals

    while True:
        print('Waiting...')
        time.sleep(3)
