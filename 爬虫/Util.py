import time


#  覆盖写入
def writeToFile(fileName, contenct):
        file_name = time.strftime("%Y-%m-%d_%H-%M-%S")
        with open("%s_%s.txt" % (fileName, file_name), "w", encoding='utf-8') as file:
            file.writelines(contenct)


if __name__ == "__main__":
    print(8888888)
    writeToFile("test", "123")
