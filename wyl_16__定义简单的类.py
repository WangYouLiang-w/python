"""
定义只包含方法的类：
    class 类名：
        def 方法1(self,参数列表):
            pass

        def 方法2(self,参数列表):
            pass


    1、第一个参数必须是self,

创建对象：
    对象变量 = 类名()

引用的概念：
    在面向对象开发中，引用的概念同意适用
    1、在使用类创建了对象后，tom变量中仍然记录的是 对象在内存中的地址
    2、tom变量 引用了 新建的猫对象
    3、使用print 输出对象变量，默认情况下，是能够输出这个变量 引用的对象 是 由哪一个类创建的对象，以及 在内存中的地址（十六进制表示）
    提示：在计算机中，通常使用十六进制表示内存地址
        十进制和十六进制都是用来表达数字的，只是表示的方式不一样
        十进制和十六进制的数字之间可以来回转换
        %d 可以以10进制 输出数字
        %x 可以以16进制 输出数字
"""


# 小猫 爱吃鱼 小猫 要喝水

class Cat:
    def eat_fish(self):
        print("小猫 爱吃鱼")
    
    def drink(self):
        print("小猫 要喝水")


tom = Cat()

tom.eat_fish()
tom.drink()
print(tom)

addr = id(tom)
print("%d" % addr)
print("%x" % addr)



# 再创建一个猫对象

lazy_cat = Cat()
lazy_cat.eat_fish()
lazy_cat.drink()

print(tom)
print(lazy_cat)