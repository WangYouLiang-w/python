"""
字符串就是一串字符，是编程语言中表示文本的数据类型
在python中可以使用一对双引号 或者 一对单引号 定义一个字符串
可以使用 索引 获取一个字符串中 指定位置的字符，索引计数从 0 开始
也可以使用for 遍历循环字符串中的每一个字符

字符串的常用方法：
    len(str)  str的长度
    str.count(str1) 小字符串在大字符串中出现的次数
    str.index(str1) 小字符串在大字符串中第一次出现的次数

字符串的方法总结：
    str.isspace 不仅可以判断字符串是否含有空格 还可以判断 \t \n \r 回车 输出True or False   is开头输出都是True
    
字符串的切片：
    切片方法适用于字符串、列表、元组
    切片使用索引值来限定范围，从一个大的字符串中切出小的字符串
    列表和元组都是有序的集合，都能够通过索引值获取到对应的数据
    字典是一个无序的集合，是使用键值对保存数据

    字符串[开始索引:结束索引:步长]  不包括结束索引对应的元素  正序：0-n  倒序：-1-（-n）


"""

str1 = "hello world"
str2 = '我的外号是\"xxx\"'

print(str2[0])

for char in str2:
    print(char)


num_str = "\u00b2"  # 平方的上标
print(num_str)
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())

# 字符串查找和替换
str1 = "hello world"
print(str1.startswith("hello"))  # 判断字符串是不是以hello开始的

print(str1.endswith("world"))  # 判断字符串是不是以world结尾的

print(str1.find("llo"))     # 查找字符串出现的位置

print(str1.replace("world","python"))  # 返回一个新的字符串，不会修改原有的字符串
print(str1)


# 文本对齐
str2 = [" hello world",
        "hello",
        "hello world hollo world"]

for poem_str in str2:
    print("|%s|" % poem_str.center(10," "))

# 去除空白字符
"""
str.lstrip()  截掉string左边的空白字符
str.rstrip()  截掉string右边的空白字符
str.strip()   截掉string左右两边的空白字符

"""

# 拆分和连接
"""
str.split(str="",num)  以str为分隔符拆分string，如果num有指定值，则仅分隔num+1个子字符串，str默认包含"\r','\n','\t'"和空格
str.join(seq)  以string作为分隔符，将seq中所有的元素（的字符串表示）合并为一个新的字符串


"""

# 字符串的切片
num_str = "0123456789"

# 截取2-5
print(num_str[2:6])
# 截取2-9
print(num_str[2:])
# 截取0-5
print(num_str[:6])
# 截取0-9
print(num_str[:])
# 每隔2截取一个
print(num_str[::2])
# 倒序
print(num_str[-1])
# 倒数2个字符
print(num_str[-2:])

# 倒序
print(num_str[-1::-1])  # 最后一个字符 步长是负1



