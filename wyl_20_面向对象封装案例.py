"""
首先进行需求分析：将属性和方法封装到一个抽象的类中
外界使用类创建对象，然后让对象调用方法
对象方法的细节都被封装在类的内部


在对象的方法内部，是可以 直接访问对象的属性的
同一个类 创建的 多个对象之间，属性 互不干扰


一个对象的属性 可以是 另外一个类 创建的对象
 哪一个类要被使用到，先开发哪个类

 定义没有初始值的属性
 在定义属性时，如果 不知道设置什么初始值，可以设置为 None
    ·None 关键字 表示 什么都没有
    ·表示一个 空对象，没有方法和属性，是一个特殊的常量
    ·可以将None赋值给任何一个变量


身份运算符：判断None应该用is
    身份运算符用于 比较 两个对象的 内存地址 是否一致 --是否对同一个对象的引用
    ·在python中针对 None 比较时，建议使用 is 判断

    is      is是判断两个标识符是不是引用同一个对象    x is y  类似id(x) == id(y)
    is not  is not是判断两个标识符是不是引用不同对象  x is not y，类似id(a) != id(b) 

is 与 == 的区别：
    is 用于判断 两个变量引用对象 是否为同一个
    == 用于判断 引用变量值 是否相等

"""

"""
需求：
1、小明 体重 75.0公斤
2、每次 跑步 会减肥 0.5公斤
3、每次 吃东西 体重会增加1公斤
"""

from typing import Counter


class Person:
    def __init__(self,name,weight) -> None:
        # self.属性 = 形参
        self.name = name
        self.weight = weight

    def __str__(self) -> str:
        return "我的名字是%s，体重是%.2f公斤"%(self.name,self.weight)

    def run(self):
        print("%s爱跑步，跑步锻炼身体"%self.name)
        self.weight -= 0.5

    def eat(self):
        pass


xiaoming = Person("小明",75)
print(xiaoming)
xiaoming.run()
print(xiaoming)



"""
摆放家具：
1、房子 有户型、总面积和家具名称列表
    新房子没有任何的家具
2、家具有名字和占地面积，其中
    ·席梦思占地 4平米
    ·衣柜占地 2平米
    ·餐桌占地1.5平米

3、将以上三件餐具 添加 到 房子 中
4、打印房子时，要求输出：户型、总面积、剩余面积、家具名称列表

"""



class HouseItem:

    def __init__(self,name,area) -> None:
        self.name = name
        self.area = area

    def __str__(self) -> str:
        return "[%s] 占地 %.2f" %(self.name,self.area)


class House:
    def __init__(self,house_type,area) -> None:
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []

    def __str__(self) -> str:
        return ("户型：%s\n总面积：%.2f[剩余：%.2f]\n家具：%s"
                %(self.house_type,self.area,self.free_area,self.item_list))

    def add_item(self,item):
        print("要添加 %s"%item)
        # 1、判断家具的面积
        if self.free_area < item.area:
            print("无法将 %s 添加到房子中"%item.name)
            return
        
        # 2、将家具的名称添加到列表中
        self.item_list.append(item.name)

        # 3、计算剩余面积
        self.free_area -= item.area


bed = HouseItem("席梦思",40)

chest = HouseItem("衣柜 ",2)

table = HouseItem("桌子",20)



my_home = House("两室一厅",60)

print(my_home)

my_home.add_item(bed)
print(my_home)
my_home.add_item(chest)
print(my_home)
my_home.add_item(table)




"""



"""


class Gun:
    def __init__(self,model) -> None:
        # 1、枪的型号
        self.model = model

        # 2、子弹的数量
        self.bullet_count = 0


    def add_bullet(self,count):
        self.bullet_count += count
             

    def shoot(self):
        if self.bullet_count <= 0:
            print("[%s]没有子弹了..."%self.model)
            return

        # 2. 发射子弹，-1
        self.bullet_count -= 1

        # 3. 提示发射信息
        print("[%s] 突突突...[%d]"%(self.model,self.bullet_count))

    
class Soldier:
    def __init__(self,name):
        # 1、姓名
        self.name = name

        # 2、枪-新兵没有枪
        self.gun = None

    def fire(self):
        # 1. 判断士兵是否有枪
        if self.gun is None:
            print("[%s]还没有枪....."%self.name)

            return
        # 2.高喊口号
        print("冲啊...[%s]"%self.name)

        # 3. 让枪装填子弹
        self.gun.add_bullet(50)

        # 4、让枪发射子弹
        self.gun.shoot()


# 1、创建枪对象
ak47 = Gun("AK47")

# ak47.add_bullet(50)
# ak47.shoot()

# 2、创建许三多
xusanduo = Soldier("许三多")

xusanduo.gun = ak47
xusanduo.fire()
print(xusanduo.gun)