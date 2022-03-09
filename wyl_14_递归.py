"""
递归：
    一个函数 内部 自己 调用自己

代码特点：
    1、函数内部的代码是相同的，只是针对的参数不同，处理的结果不同
    2、当参数满足一个条件时，函数不再执行（函数的出口）

    到达出口，函数会一层层的返回，首先要确定出口，大胆假设

递归在处理不确定的循环条件时，格外有用，例如遍历整个文件目录的结构
"""

# 示例
def sum_number(num):
    print(num)

    # 递归出口，当参数满足某个条件时，不在执行
    if num == 1:
        return

    sum_number(num-1)
    print("完成：%d" % num)

sum_number(3)



# 数字累加的例子
def sum_number(num):

    # 1、出口
    if num == 1:
        return 1

    # 数字累计 num + （1，...num-1） 假设它可以完成1-num-1的累加
    temp = sum_number(num-1)

    return num+temp

result = sum_number(100)
print(result)