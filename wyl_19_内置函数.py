"""
内置方法和属性
    __del__  方法  对象被从内存中销毁前，会被自动调用
    __str__  方法  返回对象的描述信息，print函数输出使用

应用场景：
    __del__ 如果希望在对象被销毁前，在做一些事情，可以考虑一下 __del__方法

生命周期：
    一个对象从调用类(),可以让创建对象更加灵活
    一个对象的__del__方法一旦被调用，生命周期结束
    在对象的生命周期内，可以访问对象的属性，或者让对象调用方法


__str__方法：
    ·再python中，使用print输出对象变量，默认情况下，会输出这个变量 引用的对象 是 由哪一个类创建的对象，以及 在内存中的地址(十六进制表示)
    ·如果在开发中，希望使用print输出 对象变量 时，能够打印 自定义的内容 ，就可以利用__str__这个内置方法
    __str__方法必须返回的是个字符串


"""

class Cat:
    def __init__(self,new_name) -> None:
        self.name = new_name

        print("%s 来了"%self.name)
    

    def __str__(self) -> str:
        return "我是小猫%s" %self.name

    def __del__(self):                           # 在对象被销毁之前 自动被调用  可以在对象销毁前再做一些事情
        print("%s 我去了"%self.name)

    

# tom是个全局变量
tom = Cat("Tom")
print(tom)                    # 可以利用__str__返回自定义的内容
print(tom.name)
print("-"*50)

del tom                # 会自动调用__del__方法
print("-"*50)



