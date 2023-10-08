import signal
import os
import time

data = {
    "end": True
}


def receiveSignal(signalNumber, frame):
    print('Received:', signalNumber)
    if signalNumber == signal.SIGKILL:
        print("end SIGKILL")
        data["end"] = False
    return


if __name__ == '__main__':  # register the signals to be caught

    signal.signal(signal.SIGHUP, receiveSignal)

    signal.signal(signal.SIGINT, receiveSignal)

    signal.signal(signal.SIGQUIT, receiveSignal)

    signal.signal(signal.SIGILL, receiveSignal)

    signal.signal(signal.SIGTRAP, receiveSignal)

    signal.signal(signal.SIGABRT, receiveSignal)

    signal.signal(signal.SIGBUS, receiveSignal)

    signal.signal(signal.SIGFPE, receiveSignal)

    signal.signal(signal.SIGKILL, receiveSignal)

    signal.signal(signal.SIGUSR1, receiveSignal)

    signal.signal(signal.SIGSEGV, receiveSignal)

    signal.signal(signal.SIGUSR2, receiveSignal)

    signal.signal(signal.SIGPIPE, receiveSignal)

    signal.signal(signal.SIGALRM, receiveSignal)

    signal.signal(signal.SIGTERM, receiveSignal)

    print('My PID is:', os.getpid())  # wait in an endless loop for signals

    while data["end"]:
        print('Waiting...')
        time.sleep(3)
