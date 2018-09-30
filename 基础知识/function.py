#   *vartuple 不定参数  指定默认值
def printinfo3(arg="moren", arg1="moren2", *vartuple ):
    "打印任何传入的参数"
    print ("输出: ",arg)
    print ("输出: ",arg1)
    for var in vartuple:
        print (var)
    return;
 
# 调用printinfo 函数
printinfo3( arg1=10 );
printinfo3( 70, 60, 50,63,"666" );

''' python 使用 lambda 来创建匿名函数。
lambda只是一个表达式，函数体比def简单很多。
lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。
虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。'''

sumq = lambda arg1, arg2: arg1 + arg2;
# 调用sum函数
print ("相加后的值为 : ", sumq( 10, 20 ))
print ("相加后的值为 : ", sumq( 20, 20 ))
