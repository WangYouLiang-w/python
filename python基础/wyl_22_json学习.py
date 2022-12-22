"""
json.dumps()是把python对象转换成json对象的一个过程,生成的是字符串。
json.dump()是把python对象转换成json对象生成一个fp的文件流,和文件相关。

json.loads(recv_msg)   # 将字符串格式转成字典形式
json.load(f)    # 读入Json文件：f 将f转成字典形式
"""


from fileinput import filename
import json
from textwrap import indent
wyl = {'name':'wyl','age':18}
numbers = [1,2,3,5,5]

filename = './python基础/number.json'
wyl['numbers'] = numbers

# with open(filename,'w') as f:
#     json.dump(wyl,f,indent=2)

with open(filename) as f:
    names = json.load(f)
print(names)
print(type(names))  # 字典格式
# x = json.dumps(wyl,indent=2)
# print(x)
# print(type(x))
