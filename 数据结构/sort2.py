import random
#-------------------------其他排序-----------------------------------#
#####################################################################
#####################################################################
#-------------希尔排序-------------#
def insert_sort(li):
    for i in range(1,len(li)):
        tmp = li[i]   # 摸到的牌
        j = i - 1     # 手里的牌
        while j >= 0 and li[j] > tmp:
            li[j+1] = li[j]  # 把牌往前放一位
            j -= 1
        li[j+1] = tmp


def insert_sort_gap(li,gap):
    for i in range(gap,len(li)):
        tmp = li[i]
        j = i - gap
        while j >= 0 and li[j] > tmp:
            li[j+gap] = li[j]
            j = j - gap
        li[j+gap] = tmp


def shell_sort(li):
    '''
    > 希尔排序是一种分组插入排序算法
    > 首先取一个整数 d1=n/2 ,将元素分为d1个组，每组相邻两元素之间的距离为d1，在各组内进行直接插入排序；
    > 取第二个整数d2 = d1/2,重复上述分组排序的过程，直到di = 1，即所有的元素在同一个组内进行直接插入排序
    > 希尔排序每趟并不使某些元素有序，而是使整体数据越来越接近有序；最后一趟排序使得所有数据有序
    '''
    d = (len(li))//2
    while d>=1 :
        insert_sort_gap(li,d)
        d = d//2


#------------------------------计数排序------------------------#
def count_sort(li,max_count = 100):
    '''
    已知列表的数的范围都在0：100之内，知道列表中的数的范围我们知道
    '''
    count = [0 for _ in range(max_count+1)]
    for val in li:
        count[val] += 1
    li.clear()
    for ind,val in enumerate(count):
        for i in range(val):
            li.append(ind)

#-------------------------------桶排序------------------------------#

'''
在计数排序中，如果元素的范围比较大（比如在1到一亿之间）？？？
1、桶排序（Bucket sort)：首先将元素分在不同的桶中，在对每个桶的元素排序，创建n个桶，并维持每个桶是有序的
    >平均时间复杂度：O(n+k)
    >最坏情况的时间复杂度：O(n^2k)
    >空间复杂度：O(nk)
'''
def Bucket_sort(li,Bucket_nums=100,MaxNum=1000000):
    Buckets = [[] for _ in range(Bucket_nums)]
    for val in li:
         Bucket_index = min(val//(MaxNum//Bucket_nums),Bucket_nums-1)
         Buckets[Bucket_index].append(val)
         for i in range(len(Buckets[Bucket_index])-1,0,-1):
            if Buckets[Bucket_index][i] < Buckets[Bucket_index][i-1]:
                Buckets[Bucket_index][i], Buckets[Bucket_index][i-1] = Buckets[Bucket_index][i-1],Buckets[Bucket_index][i]
            else:
                break
    BucketSorted = []
    for Bucket in Buckets:
        BucketSorted.extend(Bucket)
    return BucketSorted
            


#---------------------------------基数排序----------------------------#
'''
基数排序(多关键字排序)：假如现在有个员工表,要求按照薪资排序，薪资相同的按照员工的年龄排序
    》则先按照年龄进行排序，再按照薪资进行‘稳定’的排序

》例如对32、13、94、52、17、54、93排序，可对个位和十位数按照多关键字进行排序,
    >先将个位数进行装桶输出
    >再将十位数进行装桶输出
  多位数同理，依次从个位数进行装桶输出，位数不够前面补零
  注意：比较字符串，从前取，后面补零

》时间复杂度：O(kn)  (一定情况下，基数排序会快于快速排序，因为k=log(10,K),快排的log(n)=log(2,n),但是K过于大就会慢下来)
》空间复杂度：O(k+n)
'''
import numpy as np
def radix_sort(li):
    max_num = max(li)
    it = 0
    while 10**it <= max_num:
        Buckets = [[] for _ in range(10)]
        for var in li:
            # 987 it = 1 987%10=7   987//10->98 98%10=8 
            i = (var // 10**it) % 10
            Buckets[i].append(var)
        
        li.clear()
        for bucket in Buckets:
            li.extend(bucket)

        it = it + 1
            
li = list(range(10000))
random.shuffle(li)
print(li)
# li = [random.randint(0,10000) for _ in range(10000)]
# li = list(range(100))
# random.shuffle(li)
radix_sort(li)
print(li)