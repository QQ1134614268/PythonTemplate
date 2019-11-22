import random


def get_nums():
    num_list = []
    for i in range(4):
        num_list.append(random.randint(1, 13))
    return num_list


def yunsuan(a, b, a_str, b_str):
    adding = a + b
    adding_str = '({}+{})'.format(a_str, b_str)
    dividing = a - b
    dividing_str = '({}-{})'.format(a_str, b_str)
    multiplying = a * b
    multiplying_str = '({}*{})'.format(a_str, b_str)
    subtracting = a / b
    subtracting_str = '({}÷{})'.format(a_str, b_str)
    return [{"num": adding, "num_str": adding_str},
            {"num": dividing, "num_str": dividing_str},
            {"num": multiplying, "num_str": multiplying_str},
            {"num": subtracting, "num_str": subtracting_str}, ]


def main():
    num_list = get_nums();
    print("获得四个数字: ", num_list)
    # 列出所有可能情况
    #     取出第一个,
    #     取出第二个,
    #       四种运算
    #     取出第三个
    #       第三个与上一个运算或者与最后一个运算
    #     得到两个数字运算
    result_data = yunsuan(num_list[0], num_list[1], num_list[0], num_list[1], )
    # case 1:
    for i in result_data:
        result_data2 = yunsuan(i["num"], num_list[3], i["num_str"], num_list[3])
        for j in result_data2:
            result_data3 = yunsuan(j["num"], num_list[3], j["num_str"], num_list[3])
            for k in result_data3:
                print('{}={}'.format(k["num_str"][1:-1], k["num"]))
                # if k["num"] == 24:
                #     print('{}={}'.format(k["num_str"][1:-1], k["num"]))
                #     return
    # case 2:
    result_data2_eg2 = yunsuan(num_list[2], num_list[3], num_list[2], num_list[3])
    for i in result_data:
        for j in result_data2_eg2:
            result_data3_eg3 = yunsuan(i["num"], j["num"], i["num_str"], j["num_str"], )
            for k in result_data3_eg3:
                print('{}={}'.format(k["num_str"][1:-1], k["num"]))
                # if k["num"] == 24:
                #     print('{}={}'.format(k["num_str"][1:-1], k["num"]))
                #     return


if __name__ == '__main__':
    main()
