"""
函数参数和返回值的作用：
    组合：
        1、无c,无f
        2、无c，有f
        3、有c，无f
        4、有c，有f
    
    根据实际的功能需求决定的：
        函数内部处理的数据不确定，就可以将外界的数据以参数传到函数内部
        一个函数执行完成后，向外界汇报执行结果，增加返回值
函数返回值：
    利用元组返回多个值，可以不加括号

    接收返回的元组，可以使用多个变量一次接收函数返回的结果,变量个数要保存一致

函数参数：
    在函数内部，针对参数使用的赋值语句，不会影响到外部变量的引用。
    无论传递的参数是可变还是不可变
        只是针对参数使用的赋值语句，会在函数内部修改局部变量的引用，不会影响到外部变量的引用
        
    但是针对传递的参数是可变类型，在函数内部，使用 方法 修改了数据的内容，同样会影响到外部的数据
    注：列表的"+="运算相当于列表的extend方法


缺省参数：
    定义函数时，可以给某个参数指定一个默认值，具有默认值的参数就做缺省参数
    调用函数时，如果没有缺省参数的值，则在函数内部使用定义函数时指定的参数默认值
    函数的缺省参数，将常见的值设置为参数的缺省值，从而简化函数的使用

    在参数使用赋值语句，就可以指定参数的缺省值

缺省参数的注意事项：
    参数的定义位置，必须保证带有默认值参数 在参数列表的尾部 ，否则是错误的
    在调用函数时，如果有多个缺省参数，需要指定参数名


多指参数：
    一个函数 能够能够处理的参数 个数 是不确定的，这个时候，就可以使用 多值参数
    python中的两种多值参数：
        参数名前增加一个*可以接收元组
        参数名前增加两个*可以接收字典

    多值参数的命名，习惯使用下面两个名字：
        *args --存放 元组参数
        **kwargs --存放 字典 参数，前面有两个 *
    
    使用，分隔

元组和字典的拆包：
    在调用带有多值参数的函数时，如果希望：
        将一个 元组变量 ，直接传递给args
        将一个 字典变量 ，直接传递给kwargs
    就可以使用拆包，简化参数的传递，拆包的方式是：
        在元组变量前，增加一个 *
        在字典变量前，增加两个 *

"""

def measure():
    """返回当前的温度"""

    print("开始测量....")

    temp = 39
    wetness = 50
    print("测量结束...")
    # 元组可以包含多个数据
    # 如果函数返回的类型是元组，小括号可以省略
    return temp,wetness

result = measure()

print(result)

# 需要单独的处理温度或者湿度,不方便
print(result[0])
print(result[1])

# 如果函数返回的类型是元组，同时
gl_temp,gl_witness = measure()
print(gl_temp,gl_witness)



################
a = 1
b = 2
print(a,b)
a,b = b,a                 # 可以不使用其他变量交换变量
print(a,b)


####
# 调用方法会对外部变量进行修改
def demo(num):
    num.append(4)
    print("函数内部的序列：",num)


gl_num = [1,2,3]
print(gl_num)
demo(gl_num)
print(gl_num)

###### 缺省参数 ############
gl_list = [6,2,9]
gl_list.sort()

# 如果需要降序排序，需要传递‘reverse'参数
print(gl_list)

def print_info(name,title="",gender=True):
    """
    :param name :班上同学的姓名
    :param gender:性别
    
    """
    gender_text = "男生"

    if not gender:
        gender_text = "女生"

    print("%s 是 %s" %(name,gender_text))


print_info("小明")
print_info("小美",False)


def demo4(num,*nums,**person):
    print(num)
    print(nums)
    print(person)


demo4(1,2,3,4,5,name="小明",age=18)


def sum_nums(*args):
    num = 0
    print(args)

    for n in args:
        num += n
    return num



result = sum_nums(1,2,3)
print(result)


###
def demo5(*args,**kwargs):
    print(args)
    print(kwargs)


# 元组变量/字典变量
gl_num = (1,2,3)
gl_xiaoming = {"name":"xiaoming","age":18}
demo5(gl_num,gl_xiaoming)

# 拆包语法
demo5(*gl_num,**gl_xiaoming)