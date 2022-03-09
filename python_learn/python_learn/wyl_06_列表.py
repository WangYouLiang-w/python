"""
列表：
    专门用于存储一串信息
    列表用[]定义，数据之间使用，分隔
    列表的索引从0开始
        索引：就是数据在列表中的位置编号，索引又可以被标为下标

列表常用方法查询：
    (1)在ipython建立一个列表例如name_list=[]
    (2)输入name_list. 按下tab键

    增加：.insert(index,date) 在指定位置插入数据
        .append(date)         在列表末尾添加数据
        .extend(list2)        将list2的数据追加到列表
    修改：list[index] = date  修改指定索引的数据
    删除：del list[index]     删除指定索引的数据
        .remove[data]         删除第一个出现的指定数据
        .pop                  删除末尾数据
        .pop(index)           删除指定索引的数据
        .clear                清除列表
    
    统计：len(list)            列表长度
        .count(date)          数据在列表出现的次数

    排序：.sort()             升序排序
         .sort(reverse = True)降序排序
         .reverse()           逆序、反转
          
         .index(date)         获得数据在列表中的索引


关键字、函数和方法：
    关键字是python内置的，具有特殊意义的标识符
    查看ipython
        import keyword
        print(keyword.kwlist)
    关键字使用不需要括号

    函数 函数名需要死记硬背 函数(参数) 封装了独立功能，可以直接调用

    方法：需要通过对象来调用， 表示针对这个 对象 要做的操作
        对象.方法(参数)



列表的应用场景：
    列表中可以存储不同类型的数据，一般都是存储相同类型的
    使用迭代遍历，针对列表中的每一个元素，执行相同的操作
"""


name_list = ["wangwu","zhangsan","lisi"]


# 1、取值和索引
print(name_list[0])
print(name_list)

# del 关键字的本质是用来将一个变量从内存中删除的
# 如果使用del将变量删除了，后续的代码就不能使用这个变量了
del name_list[1]  
print(name_list)

# 排序
num_list = [1,5,2,8,4]
# num_list.sort()
num_list.sort(reverse=True)
print(num_list)


# 列表的循环编历
# for 循环内部使用的变量 in 列表
for name in name_list:
    print(name)