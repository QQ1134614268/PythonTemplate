同步 异步
并行与并发

进程 线程 携程


multiprocessing 多进程模块 
    使用多核CPU
threading 多线程
    
asyncio
    asyncio.run()
    asyncio.gather()
    asyncio.create_task()
    await asyncio.wait()



IO耗时  输入输出,执行函数时间
异步 
    遇到await后执行异步任务
    遇到await,就执行内嵌的异步,得到结果后在执行await后代码
    asyncio.create_task task任务并行的 并且与添加顺序有关
# asyncio.run 运行一个异步函数
# asyncio.gather 与 asyncio.create_task 运行多个异步函数