"""

通常用来描述一个物体的特征

和列表的区别：
    列表是有序的对象集合
    字典是无序的对象集合
    key          value
    name        zhangsan
    age         18
    gender      True
    height      1.75

字典是用{}定义
字典使用的 键值对 存储数据，键值对之间使用 ， 分隔
    键key是索引
    值value是数据
    键和值之间使用：分隔
    键必须是唯一的
    值可以取任意类型 ， 但键只能使用 字符串、数字或元组
    xiaoming = {"name":"xiaoming","age":18,"gender":True,"height":1.75}

字典的常用操作：
    取值：xiaoming["name"]    

    增加/修改：
        xiaoming["weight"] = 75
        xiaoming["name"] = "xiaoxiaoming"
    
    删除：
        xiaoming.pop("name")
    
    统计键值对的数量： len(xiaoming)

    合并字典：xiaoming.update(temp_dict)   如果合并的字典中含有已经存在的键值对，会覆盖原有的键值对

    清空：xiaoming.clear

列表和字典的应用场景：
    将多个字典放在一个列表中,再进行遍历
    stu_list = [{"name":"xiaoming",
                "age":18,
                "gender":True},
                {"name":"xiaohong",
                "age":18,
                "gender":False},]
"""
xiaoming = {"name":"xiaoming",
            "age":18,
            "gender":True,
            "height":1.75}

# 如果key不存在会新增键值对，存在则更改
xiaoming["weight"] = 75
print(xiaoming)


# 删除
xiaoming.pop("name")
print(xiaoming)

# 合并
xiaohong = {"name":"xiaohong",
            "age":18,
            "gender":True,
            "height":1.75}

xiaoming.update(xiaohong)

print(xiaoming)

string_dict = {"name":"xiaoming",
                "qq":"1233"}
# 遍历 k是每次循环从字典中拿到的key
for k in string_dict:
    print("%s - %s" % (k,string_dict[k]))

# 列表和字典的应用
stu_list = [{"name":"xiaoming",
            "age":18,
            "gender":True},
            {"name":"xiaohong",
            "age":18,
            "gender":False}]


for stu_info in stu_list:
    print(stu_info)