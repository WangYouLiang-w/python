'''
私有属性：就是对象不想公开的属性
私有方法：就是对象不希望公开的方法

定义私有属性或方法时，在属性名或者方法前 增加两个下划线，定义的就是私有属性或方法
'''
class Women:
    def __init__(self,name):
        self.name = name
        self.__age = 18

    def secret(self):
        print("{}的年龄时{}".format(self.name,self.__age))



xiaofang = Women("xiaofang")

# print(xiaofang.__age) # 无法实现
xiaofang.secret()