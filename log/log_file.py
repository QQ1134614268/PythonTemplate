import logging  

def log(mes,filename='D:/bat/log/task3.log'):
    formatter_str='[%(asctime)s][%(filename)s] -- %(message)s'#日志格式
    formatter = logging.Formatter(formatter_str) 
    logger = logging.getLogger('mylogger')   
    logger.setLevel(logging.DEBUG)  
    fh = logging.FileHandler(filename)
    fh.setLevel(logging.DEBUG) 
    fh.setFormatter(formatter)
    logger.addHandler(fh)#添加标准输出
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    logger.info(mes)
    #  添加下面一句，在记录日志之后移除添加的一个句柄
    logger.removeHandler(ch)
    logger.removeHandler(fh)
    
log('D:/bat/log/task2.log') 
log('D:/bat/log/task2.log') 
log('D:/bat/log/task2.log') 