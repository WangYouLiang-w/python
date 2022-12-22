from turtle import left, right

def linear_search(li,val):
    '''
    顺序查找
    内置函数:index()
    '''
    for ind,v in enumerate(li):
        if v == val:
            return ind
    
    else:
        return None




def binary_search(li,val):
    '''
    二分查找(列表必须是有序列表)
    '''
    left = 0
    right = len(li)-1
    while left<=right:                   # 说明候选区有值
        mid = (left + right)//2          # //代表整除

        if val < li[mid]:
            left = left
            right = mid-1

        elif val > li[mid]:
            left = mid+1
            right = right

        else:
            return mid


li = [1,2,3,4,5,6,7,8,9]

print(binary_search(li,3))