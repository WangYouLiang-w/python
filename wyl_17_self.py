"""
self: 哪一个对象调用的方法，self就是哪一个对象的引用  tom.drink() tom调用drink方法 drink里的self就是tom的引用


"""

# 小猫 爱吃鱼 小猫 要喝水

class Cat:
    def eat_fish(self):
        print("%s 爱吃鱼" %self.name)
    
    def drink(self):
        print("小猫 要喝水")


tom = Cat()
tom.name = "Tom"  # 可用 .属性 通过赋值语句给对象增加属性 但是不推荐使用

tom.drink()
tom.eat_fish()