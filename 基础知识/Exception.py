try:
    fh = open("testfiles", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
    print("here")
except IOError as ioerr :
    print ("Error: 没有找到文件或读取文件失败"+ioerr)
else:
    print( "内容写入文件成功33")
    fh.close()
finally:
    print ("Error: 没有找到文件或读取文件失败")    

# 定义函数
def temp_convert(var):
    try:
        return int(var)
    except ValueError as Argument:
        print ("参数没有包含数字\n", Argument)
 
# 调用函数
temp_convert("xyz");

def functionName( level ):
    if level < 1:
        raise Exception("Invalid level!", level)
    
# 定义函数
def mye( level ):
    if level < 1:
        raise Exception("Invalid level!", level)
        # 触发异常后，后面的代码就不会再执行

try:
    mye(0)              #    触发异常
except "Invalid level!":
    print (1)
else:
    print (2)
    
#自定义异常   
class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg
        
try:
    raise Networkerror("Bad hostname")
except Networkerror as e:
    print (e.args)
