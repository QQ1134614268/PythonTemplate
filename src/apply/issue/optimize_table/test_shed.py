import sched
import time

from conf.sw_config import shenwan_session


def print_event():
    sql = "alter table securities_score ENGINE=InnoDB"
    shenwan_session.execute(sql, {})
    shenwan_session.commit()


if __name__ == '__main__':
    # 生成调度器
    scheduler = sched.scheduler(time.time, time.sleep)
    # 分别设置在执行后2秒、3秒之后执行调用函数
    scheduler.enter(1 * 3600, 1, print_event)
    # 运行调度器
    scheduler.run()
    print("over")
