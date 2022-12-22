"""
python内置函数：
    len(item)
    max(item)   对于 字典 只找最大的key
    min(item)
    del(item)
    cmp(item1,itme2)   python3.x 取消了cmp函数 使用运算符比较   符合 "0"<"A"<"a"

运算符：
    元组和列表和字符串 都可以使用 * 重复 ，+ 拼接   字典不可以
    in 3 in（1，2，3） True
    not in  4 not in(1,2,4) True   
    in 和 not in 是成员运算符  列表 元组 字典 字符串  字典只使用key


完整的for循环语法：

    for 变量 in 集合

        循环体代码
    else：
        没有通过 break 退出循环，循环结束，会执行的代码
        通过break退出循环，else 不会执行

     
"""
# 
for num in [1,2,3]:
    print(num)
    if num == 2:
       break    # else不会被执行
else:
    print("会执行嘛")

# 
student = [
    {"name":"阿土"},
    {"name":"小美"}
]

find_name = "阿1"
for stu_dict in student:
    print(stu_dict)

    if stu_dict["name"] == find_name:
        print("找到了 %s" % find_name)
        break
else:
    print("找不到")