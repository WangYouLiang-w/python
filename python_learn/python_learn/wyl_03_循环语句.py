'''
1、break 和 continue
    break 退出循环
    continue：某一个条件满足时，不执行后续重复的代码


2、 转义字符 "\"
（1）\t 在控制台输出一个制表符，协助在输出文本时 垂直方向 保持对齐
（2）\n 在控制台输出一个 换行符
'''

print("1\t2\t3\t")
print("10\t20\t30\t")
i = 1
while True:
    print(i)
    if i == 3:
        break
    i = i + 1
   
    