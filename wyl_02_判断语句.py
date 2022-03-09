# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 15:37:52 2021

@author: Administrator
"""

'''
if 语句以及缩进部分看成一个整体

逻辑运算：
    python 只有：与 and、或 or、 非 not三种
    （1）and
    必须两个条件都要成立
    （2）or
    条件有一个成立就可以
    （3）not （不是）

elif：同时判断多个条件，所有的条件都是平级的
    if 条件1：
        CODE
    elif 条件2：
        code

    else：
        以上条件都不满足、


if的嵌套：



'''
age = int(input("请输出年龄："))
# 年龄判断
if age >= 18:
  print("请进happy")
else:
  print("请出去：")


if age >= 0 and age <= 120:
    print("你是个人")
else:
    print("你不是个人")

is_employee = False

if not is_employee:
    print("请勿进入")

# 火车站安检

has_ticket = True

knife_length = 30

if has_ticket:
    print("车票检查通过。准备开始安检：")

    if knife_length > 20:
        print("刀的车度超过 %d，不允许上车" % knife_length)
    else:
        print("允许上车" )

else:
    print("请先买票")