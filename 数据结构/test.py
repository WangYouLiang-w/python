import random
#------------查找方法-------------#
def liner_search(li,num):
    for i in range(len(li)):
        if li[i] == num:
            return i
    else:    
        return None


def binary_search(li,val):
    left = 0
    right = len(li) - 1
    mid = (left+right)//2
    while left <= right:
        if li[mid] >val:
            right = mid
        elif li[mid] < val:
            left = mid + 1
        else:
            return mid
        mid = (left+right)//2


# li = [1,2,3,4,5,6,7]

# print(liner_search(li,7))
# print(binary_search(li,7))


#------------冒泡排序-------------# 
def bulle_sort(li):
    for i in range(len(li)):
        for j in range(len(li)-i-1):
            if li[j]>li[j+1]:
                li[j+1],li[j] = li[j],li[j+1]
                


#------------选择排序-------------# 
def select_sort(li):
    for i in range(len(li)-1):
        for j in range(i+1,len(li)):
            if li[j]<li[i]:
                li[j],li[i] = li[i],li[j]


#------------插入排序-------------# 
def serter_sort(li):
    for i in range(len(li)):
        tmp = li[i]
        j = i - 1
        while j>=0:
            if li[j] > li[j+1]:
                li[j+1] = li[j]
                i = j
                j = j-1
            else:
                break
            li[i] = tmp
        li[i] = tmp


#------------快速排序-------------# 
def position(li,left,right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] > tmp:
            right = right - 1
        li[left] = li[right]

        while left < right and li[left] < tmp:
            left  = left + 1
        li[right] = li[left]

    li[left] = tmp
    return left


def fast_sort(li,left,right):
    if left < right:
        mid  = position(li,left,right)
        fast_sort(li,left,mid-1)
        fast_sort(li,mid+1,right)



#------------------堆排序-------------------#
def heap_down(heap,low,high):
    i = low  # 根节点
    j = 2*i + 1  # 左孩子节点
    while j <= high:
        # 从左右孩子中找出大的
        # 如果右孩子比较大
        if j+1<=high and heap[j+1] >= heap[j]:
            j = j + 1

        if heap[j] >= heap[i]:
            heap[j],heap[i]= heap[i],heap[j]
            i = j                           # 继续往下调整
            j = 2*i + 1                    
        else:
            break
    

def heap_sort(heap):
    # 先建堆
    n = len(heap)-1
    for i in range((n-1)//2,-1,-1):
        heap_down(heap,i,n)

    # 调整堆
    for i in range(n):
        heap[n-i],heap[0] = heap[0],heap[n-i]
        heap_down(heap,0,n-i-1)




#----------------------归并排序---------------------#
def merge(li,low,mid,high):
    it_list = []
    i = low
    j = mid + 1
    while i <= mid and j <= high:
        if li[i] <= li[j]:
            it_list.append(li[i])
            i = i + 1
        else:
            it_list.append(li[j])
            j = j + 1

    while i <=mid:
        it_list.append(li[i])
        i = i + 1

    while j <= high:
        it_list.append(li[j])
        j = j + 1
    li[low:high+1] = it_list

def merge_sort(li,low,high):
    mid = (low + high)//2
    if low < high:
        merge_sort(li,low,mid)
        merge_sort(li,mid+1,high)
        merge(li,low,mid,high)



#-------------------------------练习2----------------------------#

#---------------快速排序---------------------#
def position1(li,left,right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] > tmp:
            right = right - 1
        li[left] = li[right]

        while left < right and li[left] < tmp:
            left = left + 1
        li[right] = li[left]

    li[left] = tmp
    return left

def quick_sort(li,left,right):
    if left < right:
        mid = position1(li,left,right)
        quick_sort(li,left,mid-1)
        quick_sort(li,mid+1,right)




#--------------------堆排序-----------------------------#


def heap_down1(li,low,high):
    i = low  # 根节点位置
    j = 2*i + 1  # 左叶子节点

    tmp = li[low] # 根节点的值

    while j<= high:
        # 从孩子节点中找出最大的
        # 先比较左右孩子节点谁大
        if j+1 <= high and li[j+1] > li[j]:
            j = j + 1
        if li[j] > tmp:
            # 最大的叶子节点赋予根节点
            li[i] = li[j] 
            i = j
            j = j*2 + 1
        else:
            break
    
    li[i] = tmp


def heap_sort1(li,left,high):
    # 先构造堆
    n = high
    for i in range((n-2)//2,-1,-1):
        #从最后一个根节点开始调整
        heap_down1(li,i,n-1)
    # 排序
    for i in range(n-1):
        li[0],li[n-1-i] = li[n-1-i],li[0]
        heap_down1(li,0,n-i-2)



#----------------归并排序------------------------#
def merge1(li,low,mid,high):
    i = low
    j = mid+1
    litmp = []
    while i <= mid and j<= high:
        if li[i] <= li[j]:
            litmp.append(li[i])
            i = i + 1
        else:
            litmp.append(li[j])
            j = j + 1

    while i <= mid:
        litmp.append(li[i])
        i = i + 1

    while j <= high:
        litmp.append(li[j])
        j = j + 1

    li[low:high+1] = litmp


def merge_sort1(li,low,high):
    if low < high:
        mid = (low + high)//2
        merge_sort1(li,low,mid)
        merge_sort1(li,mid+1,high)
        merge1(li,low,mid,high)




#-----------------------希尔排序---------------------#
def insert_sort1(li,gap):
    for i in range(gap,len(li)):
        tmp = li[i]
        j = i - gap
        while j >= 0 and li[j]>tmp:
            li[j+gap] = li[j]
            j = j - gap
        li[j+gap] = tmp


def shell_sort(li):
    #先将一组数据分为d组 n/2
    d = (len(li))//2
    while d>=1:
        insert_sort1(li,d)
        d = d//2


li = list(range(100))
random.shuffle(li)
print(li)
shell_sort(li)
print(li)