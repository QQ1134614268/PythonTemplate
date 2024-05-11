#    接口的复用 todo:
#         继承,
#         组合,
#         巨量参数:
#               原因: 统一参数,  数十参数, 难以理解; 拓展接口,导致字段增多;
#               使用: 每个参数都查看一下, 类似表,每个字段都要考虑; 相关字段; 如果不能知道表字段, 熟悉度*0.5, 困难度直接*2, 时间*2
#         理解:
#             对象- 领域, 具体化参数
#             场景:
#                 用户来源:  自建用户, 第三方用户, 数据字段不一样;
#                 被禁账号:
#                 男性用户, 女性用户,
#                 早起v1注册用户,v2注册用户
#                 导致字段不一样;
#
#                 排除思想, 期望数据字段统一, 树形结构, 离散数据, 线性数据;  特别注意离散字段
#
#         解决办法: 核心方法-复用(全面的参数, 默认简化的参数)
#         eg:统计按小时,天,周,月,季度,年, 总计, 预测,日期补全,标签补全,翻译, 折线图多个, 数据结构, 其他, top3 top10, 字段, Python demo

# 24中设计模式, 面向大工程, 组装模式 ; mapReduce 是否可以映射成表,组装查询; mysql的视图功能, 手动落库实现视图;
# 根据领域, 一个对象(表) 只拥有有限字段(权重大的), 或表字段只做展示,不影响其他属性; 表通过对象

data = []


def gen_data():
    for i in range(10):
        obj = {
            "id": i,
            "name": "张三" + str(i),
            "createTime": ""
        }
        data.append(obj)


#         eg:拓展-- 统计按小时,天,周,月,季度,年, 总计, 预测,日期补全,标签补全,翻译, 折线图多个, 数据结构, 其他, top3 top10, 字段, Python demo

# 补充标签 原地补充,还是计算返回

# 分页
def page(start, end):
    return data[start:end]


def fill_label(label_id, label_name):  # 外围循环
    data2 = {}
    return data2.get(label_id)


def fill_label_v2(obj):  # 更不容易理解?? 对象参数更多,不知做什么用; 外围循环
    data2 = {}
    obj.label_value = data2.get(obj.label_id)


def fill_label_v3(list_obj):  # lambda??
    for obj in list_obj:
        data2 = {}
        obj.label_value = data2.get(obj.label_id)


def group_by_day(start, end):
    new_data = filter(lambda a: start < a.createTime < end, data)
    pass


def group_by_day_v1(near7day):
    start = 1
    end = 2
    group_by_day(start, end)


def group_by_day_v3(near7day, start, end):
    if near7day:
        return group_by_day_v1(near7day)
    if start:
        return group_by_day(start, end)

# 季度 不是从0开始, 使用-1 /3 计算
# 时间 从0开始, /4 计算
# 循环次数  可认为从0开始, /10, 向上取整, 保证余数也能处理
