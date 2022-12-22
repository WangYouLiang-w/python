from threading import Thread

#%% 创建一个类 包括属性和类
class Car:
    '''一次模拟汽车的简单尝试'''
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odomoter_reading = 0


    def get_descriptive_name(self):
        long_name = f"{self.make} {self.make} {self.year}"
        return long_name

me_tesla = Car('tesla','model s',2019)
print(me_tesla.get_descriptive_name())


#%% 创建一个子类 继承父类
class ElectricCar(Car):
    '''电动车的独特之处'''
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 75


    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car1 has a {}--kWh battery".format(self.battery_size))


me_tesla = ElectricCar('tesla','model s',2019)
print(me_tesla.get_descriptive_name())
me_tesla.describe_battery()

#%% 创建一个类使其实例作为另一个类属性
class Battery:
    """电池"""
    def __init__(self,battery_size) -> None:
        self.battery_size = battery_size


    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car2 has a {}--kWh battery".format(self.battery_size))

class ElectricCar1(Car):
    '''电动车的独特之处'''
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery(75)   # 创建一个Battery实例作为ElectricCar1的属性

me_tesla = ElectricCar1('tesla','model s',2019)
print(me_tesla.get_descriptive_name())
me_tesla.battery.describe_battery()