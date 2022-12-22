"""
列表：
    专门用于存储一串信息
    列表用[]定义，数据之间使用，分隔
    列表的索引从0开始
        索引：就是数据在列表中的位置编号，索引又可以被标为下标

列表的常用操作：
    在ipyton3中定义一个列表，例如：name_list = []
    输入name_list. 按下TAB键，ipython会提示列表能够使用的方法
    增加：.insert(index,date) 在指定位置插入数据
         .append (date)  在末尾加数据
         .extend（列表2） 将列表2追加到列表

    修改：list[index] = date

    删除：del list[index]  删除指定索引的数据
        .remove（） 删除第一个出现的指定数据
        .pop             删除末尾数据
        .clear            清空列表

    统计：len(list)
        .count（date)   数据在列表中出现的次数

    排序:.reverse()        逆序，翻转
        .sort（）         升序排序 
        .sort（reverse=True）    降序排序 
               
        .copy            
        .index
        
"""


name_list = ["wangwu","zhangsan","lisi"]

print(name_list[0])