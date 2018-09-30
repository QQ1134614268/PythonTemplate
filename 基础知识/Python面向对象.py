class Employee2:
    '所有员工的基类'
    empCount = 0
 
    def __init__(self, name, salary):
            self.name = name
            self.salary = salary
            Employee2.empCount += 1
    
    def displayCount(self):
        print( "Total Employee2 %d" % Employee2.empCount)
 
    def displayEmployee2(self):
            print ("Name : ", self.name,  ", Salary: ", self.salary)
 
print ("Employee2.__doc__:", Employee2.__doc__)
print ("Employee2.__name__:", Employee2.__name__)
print ("Employee2.__module__:", Employee2.__module__)
print ("Employee2.__bases__:", Employee2.__bases__)
print ("Employee2.__dict__:", Employee2.__dict__)
# emp1.displayEmployee2()
# emp2.displayEmployee2()
print ("Total Employee2 %d" % Employee2.empCount     )
 
class Parent:              # 定义父类
    parentAttr = 100
    def __init__(self):
            print ("调用父类构造函数")
 
    def parentMethod(self):
            print ('调用父类方法')
 
    def setAttr(self, attr):
            Parent.parentAttr = attr
 
    def getAttr(self):
            print ("父类属性 :", Parent.parentAttr)
 
class Child(Parent): # 定义子类
    def __init__(self):
            print ("调用子类构造方法")
 
    def childMethod(self):
            print ('调用子类方法')
 
c = Child()                 # 实例化子类
c.childMethod()            # 调用子类的方法
c.parentMethod()        # 调用父类方法
c.setAttr(200)             # 再次调用父类的方法 - 设置属性值
c.getAttr()                 # 再次调用父类的方法 - 获取属性值  

 