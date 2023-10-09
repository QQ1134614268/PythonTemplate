# -*- coding:utf-8 -*-
import signal
import os
import time


def receiveSignal(signalNumber, frame):
    with open("out.log", "a") as f:
        f.write(f"Received: {signalNumber}\r\n")
    print('Received:', signalNumber)
    return


if __name__ == '__main__':  # register the signals to be caught

    signal.signal(signal.SIGHUP, receiveSignal)  # win 不支持

    signal.signal(signal.SIGINT, receiveSignal)

    # signal.signal(signal.SIGQUIT, receiveSignal)  # win 不支持

    signal.signal(signal.SIGILL, receiveSignal)

    # signal.signal(signal.SIGTRAP, receiveSignal)  # win 不支持

    signal.signal(signal.SIGABRT, receiveSignal)

    # signal.signal(signal.SIGBUS, receiveSignal) # win 不支持

    signal.signal(signal.SIGFPE, receiveSignal)

    # signal.signal(signal.SIGKILL, receiveSignal) # 不能捕捉

    # signal.signal(signal.SIGUSR1, receiveSignal) # win 不支持

    # signal.signal(signal.SIGSEGV, receiveSignal) # win 不支持

    # signal.signal(signal.SIGUSR2, receiveSignal) # win 不支持

    # signal.signal(signal.SIGPIPE, receiveSignal) # win 不支持

    # signal.signal(signal.SIGALRM, receiveSignal) # win 不支持

    signal.signal(signal.SIGTERM, receiveSignal)

    print('My PID is:', os.getpid())  # wait in an endless loop for signals

    while True:
        print('Waiting...')
        time.sleep(3)
