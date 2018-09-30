class student:
    __id__=0
    _name_="Tom"
    def __init__(self,studentId,name):
        self.__id__= studentId
        self.studentId=studentId
        self.name=name
    def toString(self):
        print(self.__id__,self._name_,self.studentId,self.name)
        
        
a= student(999,"999")
a.toString()

print(a.__id__)

# 0 Tom 999 999
# 0