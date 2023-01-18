import time


def main():
    for i in range(3):
        print("开始打印%s次" % i)
        time.sleep(2)


if __name__ == '__main__':
    main()
    print("执行完毕")
