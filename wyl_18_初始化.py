"""
初始化方法：
    对象包含的属性，应该封装在类的内部
    1、当使用类名（）创建对象时，会 自动 执行一下操作:
        1 为对象在内存中 分配空间 --创建对象
        2 为对象的属性 设置初始值 --初始化方法(init)
    这个初始化方法 就是 __init__方法，__init__是对象的内置方法
   *** __init__方法就是专门来定义一个类 具有哪些属性的方法！！！


初始化方法的改造：
    在开发中，如果希望在 创建对象的同时，就设置对象的属性，可以对__init__方法进行 改造
    1、把希望设置的属性值，定义成__init__方法的参数
    2、在方法内部使用self.属性 = 形参 接收外部传递的参数
    3、在创建对象时，使用类名(属性1，属性2...)调用


"""


# 小猫 爱吃鱼 小猫 要喝水

class Cat:
    def __init__(self,new_name) -> None:          # 会被自动调用
        print("这是一个初始化方法")
        # self.name = "Tom"
        self.name = new_name

    def eat_fish(self):
        print("%s 爱吃鱼" %self.name)
    
    def drink(self):
        print("%s 要喝水" %self.name)


# 创建对象会自动调用初始化方法
tom = Cat("Tom")

print(tom.name)

lazy_cat = Cat("dalanmao")
lazy_cat.drink()
