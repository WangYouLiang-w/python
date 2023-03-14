# %%
'''
贪心算法：在对问题求解时，总是做出在“当前”看来是最好的选择。也就是说，不从整体最优上加以考虑，他所做出的是在
某种意义上的局部最优解

贪心算法并不能保证会得到最优解，但是在“某些问题”上贪心算法的解就是最优解。《要会判断一个问题能否用贪心算法来计算》

'''

'''
@ 找零问题
题目：假设商店老板需要找零n元钱，钱币的面额有100元、50元、20元、5元、1元，如何找零使得所需钱币的数量最少？？？
'''
t = [100,50,20,5,1]
def change(t, n):
    m = [0 for _ in range(len(t))]

    for i, maneny in enumerate(t):
        m[i] = n // maneny
        n = n % maneny
    return m, n

print(change(t, 376))
# %%
'''
@ 背包问题
》一个小偷在某个商店发现有n个商品，第i个商品价值Vi元， 重Wi千克。他希望拿走的价值尽量高，但他的背包只能容纳W千克的东西。他应该拿走那些商品？

》0-1背包：对于一个商品，小偷要么把它完整拿走，要么留下。不能只拿走一部分，或把一个商品拿走多次。（商品为金条）（不是最优）

》分数背包：对于一个商品，小偷可以拿走其中的任意一部分。（商品为金砂）（一定可以得到最优解）
'''
goods = [(60, 10), (100, 20), (120, 30)]
goods.sort(key= lambda x: x[0]/x[1], reverse=True)

def fractional_backpack(goods, w):
    m = [0 for _ in range(len(goods))]

    for i, (prize, weight) in enumerate(goods):
        if w >= weight:
            m[i] = 1
            w -= weight
        else:
            m[i] = w/weight
            w = 0
            break
    return m
print(fractional_backpack(goods, 50))
# %%
'''
@拼接最大数字问题
》 有n个非负整数， 将其按照字符串拼接的方式拼接成为一个整数。如何拼接可以使得得到最大的整数
 
》例：32，94，128，1286，6，71可以拼接除的最大整数为94716321286128
'''
from functools import cmp_to_key
li = [32, 94, 128, 1286, 6, 71]

def cmp_xy(x, y):
    if x+y < y+x:
        return 1
    elif x+y > y+x:
        return -1
    else:
        return 0

def number_com(li):
    li = list(map(str, li))
    li.sort(key=cmp_to_key(cmp_xy))
    return "".join(li)


print(number_com(li))
# %%
'''
@活动选择问题：

》假设有n个活动，这些活动要占用同一片场地，而场地在某时刻只能供一个活动使用

》每个活动都有一个开始时间Si 和结束时间fi（题目中时间以整数表示）表示活动在[Si,fi)区间占用场地

》问安排那些活动能够使该场地举办的活动的个数最多？
i : 1  2  3  4  5  6  7  8  9  10 11
Si: 1  3  0  5  3  5  6  8  8  2  12
fi: 4  5  6  7  9  9  10 11 12 14 16

**贪心结论：“最先结束”的活动的一定是最优解的一部分
证明： 假设a是所有活动中最先结束的活动，b是最优解中最先结束的活动
    》如果a=b，结论成立
    》如果a!=b,则b结束的时间一定晚于a的结束时间，则此时用a替换掉最优解中的b，a一定不与最优解中的其他活动时间
    重叠，因此被替换后的解也是最优解
'''
activities = [(1,4), (3,5), (0,6), (5,7), (3,9), (5,9), (6,10), (8,11), (8,12), (2,14), (12,16)]

# 保证活动是按照活动结束的时间排好序
activities.sort(key=lambda x:x[1])

def activities_selection(a):
    res = [a[0]]

    for i in range(1, len(a)):
        if a[i][0] > res[-1][1]: # 当前活动的开始时间小于等于最后一个入选活动的结束时间
            res.append(a[i])
    
    return res

print(activities_selection(activities))

# %%
