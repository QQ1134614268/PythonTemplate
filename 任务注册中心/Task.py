'''
Created on 2018年6月20日

@author: Administrator
'''


class Task:
    time = 0
    note = '注释'
    id = -1


task = Task()
task.id = 1
task.note = '健身签到任务'
task.time = '11:00'  # 检查任务执行完成时间 每天

task2 = Task()
task2.id = 2
task2.note = '上班签到'
task2.time = '9:20'  # 检查任务执行完成时间
