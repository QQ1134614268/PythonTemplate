# coding:utf-8
# 常量值不变,常量名大写


class TestConst:
    class ConstError(TypeError):
        pass

    class ConstCaseError(ConstError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("can't change value %s" % name)
        if not name.isupper():
            raise self.ConstCaseError('value name "%s" is not all uppercase' % name)
        self.__dict__[name] = value


const = TestConst()
const.PI = 3.14
const.MY_CONST = 'my_const'
const.LOGFILE = 'D:/bat/log/task.log'
