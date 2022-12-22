'''
1、常见的排序算法 
内置函数：sort()
(1)low B三人组:冒泡排序、选择排序、插入排序
(2)排序NB三人组:快速排序、堆排序、归并排序
(3)其他排序：希尔排序、计数排序、基数排序
'''
from re import I
from tempfile import tempdir
import random
import heapq
from turtle import left

def bubble_sort(li):
    '''
    冒泡排序：
        1、列表每相邻的数，如果前面的比后面的大，则交换这两个数
        2、一趟排序之后，则无序区减少一个数，有序区增加一个数,在一趟中最大的数就上去了
        3、总共排了n-1趟
        4、时间复杂度O(n^2) 最好O(n) 空间复杂度O(1) 
        5、优化 如果冒泡排序中的一趟排序没有发生交换，则说明列表已经有序，可以直接结束算法
    '''
    for i in range(len(li)-1):
        exchange = False
        for j in range(len(li)-i-1):
            if li[j]>li[j+1]:
                # temp = li[j]
                # li[j] = li[j+1]
                # li[j+1] = temp
                li[j],li[j+1] = li[j+1],li[j]
                exchange = True
        
        if exchange == False:
            return li


def select_sort(li):
    '''
    选择排序：
        1、记位置
        2、时间复杂度O(n^2) 空间复杂度O(n)
    '''

    for i in range(len(li)-1):
        min_loc = i
        for j in range(i+1,len(li)):
            if li[j]<li[min_loc]:
                min_loc = j

        li[i],li[min_loc] = li[min_loc],li[i]

    return li
            

def insert_sort(li):
    '''
    插入排序：
        1、类似于摸牌
        2、时间复杂度O(n^2) 空间复杂度O(n)
    '''
    for i  in range(1,len(li)):
        tmp = li[i]   # 抓到的牌
        j = i-1       # li[j] 手里最右边的牌
        while j>=0 and li[j]>tmp:
            li[j+1] = li[j]
            j = j -1

        li[j+1] = tmp
    
    return li

###############################################################################################################
###############################################################################################################
#-----------------快速排序------------------#
def partition(li,left,right):
    '''
    将P归位
    '''
    tmp = li[left]

    while left < right:
        while left < right and li[right] >= tmp:       #从右边找比tmp小的数
            right -= 1              # 往左走一步
    
        li[left] = li[right]      #把右边的值写到左边的空位上

        while left < right and li[left] <= tmp:
            left = left + 1

        li[right]  = li[left]  #把左边的值写到右边的空位上

    li[left] = tmp         # 把tmp归位

    return left


def quick_sort(li,left,right):
    '''
    快速排序：
    1、快速排序：快
    2、思路：
        》取一个元素P（第一个元素），使元素归位；                   
        》列表被P分成两部分，左边都比P小，右边都比P大（P归位）
        》递归完成排序
    3、时间复杂度：最好O(nlogn) 最坏O(n^2)
    '''
    if left < right:
        mid = partition(li,left,right)
        quick_sort(li,left,mid-1)         # 快排左边       
        quick_sort(li,mid+1,right)
    



#------------------------堆排序-------------------------#
def sift(li,low,high):
    '''
    向下调整(根节点的左右子树都是堆，而本身不是堆）的目的：把根节点拿出来向下调整到合适位置
    li:列表
    low:堆的根节点位置
    high:堆的最后一个元素的位置，用来防止越界
    '''
    i = low          # 堆的根节点
    j = 2*i + 1      # 根的左孩子节点
    tmp = li[i]

    while j <= high:
        # 从左右子节点中找出最大的
        if j+1 <= high and li[j+1] > li[j]:   # 右孩子节点大且不能超过high
            j = j + 1    #  选中右孩子节点

        # 然后比较根节点是否小于他的最大叶子节点
        if li[j] > tmp:
            li[i] = li[j]  # 把大的数放到根节点
            i = j          # 再向下看一层
            j = 2*i + 1    
        else:
            break

    li[i] = tmp         #最后把tmp放到叶子节点上
         


def heap_sort(li):
    '''
    堆排序（这里采用顺序存储方式即用列表存）：
    1、堆：是特殊的完全二叉树（叶子节点只能出现在最下层和次下层，并且最下层的节点都集中在该层的最左边的若干位置的二叉树）
    2、大根堆：根节点比两个子节点都大  小根堆：根节点比两个子节点都小

    第一步：构造堆：从最后的叶子节点对应的子树（子树的左右子树都是堆，而本身不是）依次开始调整，调整为根节点比两个子节点都大（农村包围城市：从最后一级开始调整）
    第二步：出数：选出堆的根节点，与最后一个叶子节点交换（防止浪费内存空间），然后再堆整个堆进行调整，依次执行

    3、时间复杂度: sift:O(logn) (最多走树的高度)  整体则是：O(nlogn)

    4、python 堆的内置模块 (heapq) q->queue 优先队列（小的先出或者大的先出）    heapq.heapify(li) 建堆   heapq.heappop(li) 弹出最小元素
    '''
    n = len(li)

    # 构造堆
    for i in range((n-2)//2,-1,-1):         # 从最后一个根节点开始调整，直到等于0
        sift_small(li,i,n-1)  

    # 出数
    for i in range(n-1,-1,-1):   # i 始终指的是堆的最后一个元素
        # 先交换
        li[0], li[i] = li[i], li[0]
        # 再调整
        sift_small(li,0,i-1)
    

#--------------------------------topk问题-------------------------------#
def sift_small(heap,low,high):
    '''
    小根堆的向下调整
    '''
    i = low
    j = 2*i + 1
    tmp = heap[i]

    while j <= high:
        if j+1 <= high and heap[j+1] < heap[j]:
            j = j + 1

        if heap[j] < tmp:
            heap[i] = heap[j]
            i = j
            j = 2*i + 1
        else:
            break

    heap[i] = tmp


def topk(li,k):
    '''
    topk问题: 现在又n个数，设计算法得到前K大的数。(k<n)
    解决思路：
        1、排序后切片   O(nlogn)
        2、排序lowB三人组  O(Kn)
        3、堆排序思路  O(nlogk)  
            > 取列表的前K个元素建立一个小根堆。堆顶就是目前第K大的数
            > 依次向后遍历原列表，对于列表中的元素，如果小于堆顶，则忽略该元素；如果大于堆顶，则将堆顶更换为该元素，并且对堆进行一次调整
            > 遍历列表所有元素后，倒序弹出堆顶   
    '''
    #1、取出列表的前k个数
    heap = li[0:k]

    # 2、构造小根堆
    for i in range((k-1)//2,-1,-1):
        sift_small(heap,i,k-1)

    # 3、遍历
    for i in range(k,len(li)):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift_small(heap,0,k-1)

    # 4、出数
    for i in range(k-1,-1,-1):
        heap[0],heap[i] = heap[i],heap[0]
        sift_small(heap,0,i-1)

    return heap



#---------------------归并排序------------------------#
'''
> 假设现在的列表两段有序，将两段排成有序的
    > 遍历两段有序，依次比较,把小的拿出来（归并）

> 分解：将列表越分越小，直至分成一个元素。
> 终止条件：一个元素是有序的
> 合并：将两个有序列表并归，列表越来越大

时间复杂度：O(nlogn)  空间复杂度：O(n)
'''
def merge(li,low,mid,high):
    '''
    一次归并，即两边有序在合并
    '''
    i = low
    j = mid + 1
    litmp = []
    while i<= mid and j <= high:
        if li[i] < li[j]:
            litmp.append(li[i])
            i = i + 1
        else:
            litmp.append(li[j])
            j = j + 1

    while i <= mid:
        litmp.append(li[i])
        i += 1

    while j<=high:
        litmp.append(li[j])
        j += 1
    li[low:high+1] = litmp


def merge_sort(li,low,high):
    mid = (low + high)//2
    if low < high:
        merge_sort(li,low,mid)
        merge_sort(li,mid+1,high)
        merge(li,low,mid,high)

'''
NB三人组的总结：
> 一般情况就运行时间而言：快速排序 < 归并排序 < 堆排序
> 三种算法的缺点：
    > 快速排序，极端情况下排序效率低
    > 归并排序：需要额外的内存开销
    > 堆排序：在快的排序算法中相对较慢

> 递归需要系统栈的内存 则快速排序 平均情况O(logn),最坏情况O(n)
> 稳定性：当两个元素一样时，保证他们的相对位置不变
    稳定的(挨着交换) ： 冒泡、直接插入、归并
    非稳定的（跳着交换）：直接选择、快速排序、堆排序
'''


# li = [random.randint(0,10000) for i in range(1000)]  # 列表生成式
li = list(range(100))
random.shuffle(li)
merge_sort(li,0,len(li)-1)
print(li)

