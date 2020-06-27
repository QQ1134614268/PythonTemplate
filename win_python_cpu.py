# -*- coding:utf-8 -*-
import psutil
import os
import time
import logging


def KillProcess():
    os.kill(pid, 2)


def ProcessLog():
    LOG_FORMAT = "%(asctime)s %(name)s %(levelname)s %(pathname)s %(message)s "
    DATE_FORMAT = '%Y-%m-%d  %H:%M:%S %a '
    logging.basicConfig(level=logging.INFO,
                        format=LOG_FORMAT,
                        datefmt=DATE_FORMAT,
                        filename=r"D:\jiaoben\Process.log"
                        )

    logging.info('%s The end of this process has been!!!', FilePath)


#####################################################################################################
if __name__ == '__main__':
    pl = psutil.pids()
    r = []
    for pid in pl:
        try:
            p = psutil.Process(pid)
            r.append((pid, p.name(), p.cpu_percent()))
            FilePath = p.username()
            CpuPercent = p.cpu_percent(interval=0.2)
            if (p.name() == 'w3wp.exe') and (CpuPercent >= 400):
                KillProcess()
                ProcessLog()
        except:
            pass
