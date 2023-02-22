'''
>python数据结构:是指互相之间存在着一种或多种关系的数据元素的集合和该集合中数据元素之间的关系组成
>简单来说，数据结构就是设计数据以何种方式组织并存储在计算机中
>比如：列表、集合与字典等都是一种数据结构
>N.Wirth: 程序 = 数据结构 + 算法

'''

#----------------------------------列表---------------------------------#
'''
列表：
(1)怎么存储：顺序存储
(2) 数组
    > 查找是O(1),因为存储是按照地址存储，知道首地址，存储的类型（例如，int是32位占4个字节），就可根据数在列表的位置直接查找
    > 数组和列表的区别：（1）数组的元素类型一定要相同，因为数组存储的是元素 （2）数组长度固定
（3）列表查找、删除、插入、等基本操作原理 
    > 列表的元素类型可以不同
        > 列表存储的是元素的地址，长度一样（64位的电脑就是8个字节） 
    > 列表的长度可以不固定(不够就补)
    > 查找是O(1)，类似于数组，先查找地址、在从地址中取出元素
    > 插入和删除是O（n)
'''

#--------------------------------栈----------------------------#
'''
栈：是一个数据集合，可以理解为只能在一端进行插入或者删除操作的'列表'
> 栈的特点：先进后出LIFO
> 栈的概念：栈顶、栈底
> 栈的基本操作：
    进栈：push
    出栈:pop
    取栈顶：gettop

> 使用一般的列表结构即可实现栈
    > 进栈：li.append
    > 出栈：li.pop
    > 取栈顶：li[-1]
    
'''

'''
括号匹配问题
（1）取出元素判断是不是左括号,将括号字符串的元素依次进栈
（2）取下一个元素， 若是右括号与栈顶元素进行匹配（栈不为空），如果匹配就将栈顶元素出栈，否则报错
（3）重复1-2
（4）如果字符串遍历完，栈也为空则符号匹配成功，否则不成功
'''
class stact:
    def __init__(self):
        self.li = []

    def is_empty(self):
        if len(self.li) == 0:
            return True
        else:
            return False

    def push(self,a):
        self.li.append(a)


    def pop(self):
        self.li.pop()

    
    def gettop(self):
        return self.li[-1]


def brace_match(s):
    brace_stact = stact()
    match_dict = {'}':'{',')':'(',']':'['}
    for brace in s:
        if brace == '{' or brace == '[' or brace == '(':
            brace_stact.push(brace)

        elif brace_stact.is_empty() == False and match_dict[brace] == brace_stact.gettop():
            brace_stact.pop()
        else:
            return False
    
    if brace_stact.is_empty() == True:
        return True
    else:
        return False
        
    
S = '['
print(brace_match(S))



#--------------------------------队列----------------------------#
'''
》队列（Queue）是一个数据集合，仅允许在列表的一端进行插入，另一端进行删除
》进行插入的一端称为队尾（rear），插入动作称为进队或入队
》进行删除的一端称为对头（front),删除动作称为出队
》队列的性质是：先进先出


## 环形队列:（front or rear = Maxsize + 1时，再前进一个位置就自动到0)
    >front(指向队列头部)前进1：front = （front + 1）%MaxSize
    >rear (指向队列尾部)前进1：rear = (rear + 1）%MaxSize
    >队为空的条件：front  == rear
    >队满的条件：（rear+1)%Maxsize == front
'''
class Queue:
    def __init__(self,size) -> None:
        self.queue = [0 for _ in range(size)]
        self.rear = 0   # 指向队尾元素
        self.front = 0  # +1 之后指向队首元素
        self.size = size

    def push(self,element):
        if not self.is_filled():
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = element
        else:
            raise IndexError("Queue is filled")

    
    def pop(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]
        else:
            raise IndexError("Queue is empty")

    
    def is_empty(self):
        return self.rear==self.front


    def is_filled(self):
        return (self.rear + 1) % self.size == self.front


    def getrear(self):
        return self.queue[self.rear]
    

    def getfront(self):
        return self.queue[self.front+1]

# q = Queue(10)

# for i in range(11):
#     q.push(i)

# print(q.getfront())

'''
双向队列的两端都支持进队和出队操作

双向队列的基本操作：
（1）队首进队
（2）队首出队
（3）队尾进队
（4）队尾出队


注：queue模块是来保证线程安全的

'''
from collections import deque
q = deque([1,2,3,4,5],5)
# 单向队列
q.append(6) #队尾进队  6进队的时候，队已满 1自动出队，队首就是2
print(q.popleft()) # 队首出队

# 双向队列
# q.appendleft(1) #队首进队
# q.pop()         #队尾出队

def tail(n):
    '''
    利用队列实现，输出文件的后五行
    '''
    with open('./数据结构/test.txt','r') as f:
        q = deque(f,n)         #队满就会出队
    return q


for line in tail(5):
    print(line,end='')




#--------------------------栈和队列的应用-----------------------------------#

'''
迷宫问题：

》》栈----深度优先搜索（DFS) (通俗讲就是一条道走到黑，不行就往回走)---回溯法

    》思路：从一个节点开始，任意找下一个能走的点，当找不到能走的点，退回上一个点，寻找是否有其他方向的点

    》用栈存储当前路径


》》队列------广度优先搜索（还可以找到最短路径）
    》 从一个节点开始，寻找所有接下来能继续走的点，继续不断的寻找，直到直到出口
    
    》使用队列存储当前正在考虑的节点

    需要创建一个列表存储出队的元素是谁让其进的队,这样就可以从出口往回找到整个路径

'''
maze = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,0,0,1,1,0,0,1],
    [1,0,1,1,1,0,0,0,0,1],
    [1,0,0,0,1,0,0,0,0,1],
    [1,0,1,0,0,0,1,0,0,1],
    [1,0,1,1,1,0,1,1,0,1],
    [1,1,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
]

dirs = [
    lambda x,y:(x+1,y),
    lambda x,y:(x,y+1),
    lambda x,y:(x-1,y),
    lambda x,y:(x,y-1)
]


def maze_path(x1,y1,x2,y2):
    stact = []
    stact.append((x1, y1))
    while(len(stact)>0):
        curNode = stact[-1] # 获取栈顶元素
        if curNode[0] == x2 and curNode[1] == y2:
            for p in stact:
                print(p)
            return True
        
        for dir in dirs:
            # 寻找四个方向有没有路
            nextNode = dir(curNode[0], curNode[1])
            if maze[nextNode[0]][nextNode[1]] == 0:
                stact.append(nextNode)
                maze[nextNode[0]][nextNode[1]] = 2 # 标记当前节点已经走过
                break
        
        else:
            maze[curNode[0]][curNode[1]] = 2
            stact.pop() # 出栈
            
    else:
        print('没有路')
        return False


maze_path(1,1,8,8)

maze = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,0,0,1,1,0,0,1],
    [1,0,1,1,1,0,0,0,0,1],
    [1,0,0,0,1,0,0,0,0,1],
    [1,0,1,0,0,0,1,0,0,1],
    [1,0,1,1,1,0,1,1,0,1],
    [1,1,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
]

def print_r(path):
    curNode = path[-1]
    realpath = []

    while curNode[2] != -1:
        realpath.append(curNode[0:2])
        curNode = path[curNode[2]]
    
    realpath.append(curNode[0:2])  # 起点
    realpath.reverse()
    for node in realpath:
        print(node)


def maze_path_queue(x1,y1,x2,y2):
    queue = deque()
    queue.append((x1,y1,-1))
    path = []
    while len(queue) > 0:
        curNode = queue.popleft()  # 队首出队
        path.append(curNode)
        if curNode[0] == x2 and curNode[1] == y2:
            print_r(path)
            return True
        for dir in dirs:
            # 看下一个节点能不能走
            nextNode = dir(curNode[0],curNode[1])
            if maze[nextNode[0]][nextNode[1]] == 0:
                queue.append((nextNode[0], nextNode[1], len(path)-1))  # 存放下一步可以走的节点，以及把其带进去的节点的下标，curNode 在path的最后
                maze[nextNode[0]][nextNode[1]] = 2 # 标记已经走过
    else:
        print('没有路')
        return False            
        

maze_path_queue(1,1,8,8)




#----------------------------------链表-------------------------------------------#
'''
列表：是由一系列节点组成的元素集合。每个节点包含两部分，数据域item和指向下一个节点的指针next。
通过节点之间的相互连接，最终串联成一个链表。

单向列表： head——》[86][]——》[19][]——》[4][]——》|||

》》创建列表：
    》头插法：head
    》尾插法：head、tail
    
》》链表的遍历：

》》链表的插入和删除：
    》插入： P.next = curNode.next
            curNode.next = P

    》删除： P = curNode.next
            curNode.next = P.next
            del P
'''   

class Node:
    def __init__(self,item) -> None:
        self.item = item
        self.next = None


def create_linklist_head(li):
    '''头插法'''
    head = Node(li[0])
    for element in li[1:]:
        newNode = Node(element)
        newNode.next = head
        head = newNode

    return head

def create_linklist_tail(li):
    '''尾插法'''
    head = Node(li[0])
    tail = head
    for element in li[1:]:
        newNode = Node(element)
        tail.next = newNode
        tail = newNode

    return head


def print_linklist(head):
    '''链表的遍历'''
    while head!= None:
        print(head.item,end=',')
        head = head.next
    

def linklist_insert(head,i,element):
    '''
      在链表的第i个位置后插入element
    '''
    curNode = head
    if i == 0:
        P = Node(element)
        P.next = head
        head = P
        return head

    for j in range(i-1):        # 寻找第i-1个节点
        curNode = curNode.next

    if curNode == None:
        raise TypeError('err!!!')

    else:
        P = Node(element)
        P.next = curNode.next
        curNode.next = P
        return head


def linklist_delete(head,i):
    '''
      在链表的第i个位置后插入element
    '''
    curNode = head
    if i == 1:
        head = curNode.next
        return head
    
    for j in range(i-2):        # 寻找第i-1个节点
        curNode = curNode.next

    if curNode == None:
        raise TypeError('err!!!')
    else:
        P = curNode.next
        curNode.next = P.next
        del P
        return head



linklist = create_linklist_head([1,2,3])
# linklist = create_linklist_tail([1,2,3])
print_linklist(linklist_insert(linklist,0,1))

    

'''
》》双链表：每个节点有两个指针：一个指向后一个节点，另一个指向前一个节点

    》创建双链表和遍历
    》插入节点： P.next = curNode.next
                curNode.next.prior = P
                P.prior = curNode
                curNode.next = P

    》删除节点： P = curNode.next
                curNode.next = P.next
                P.next.prior = curNode
                del P


'''

class Node2:
    def __init__(self,item) -> None:
        self.item = item
        self.next = None
        self.prior = None


def create_double_linklist_head(li):
    head = Node2(li[0])
    for element in li[1:]:
        newNode = Node2(element)
        newNode.next = head
        head.prior = newNode
        head = newNode
    return head


def create_double_linklist_tail(li):
    head = Node2(li[0])
    tail = head
    for element in li[1:]:
        newNode = Node2(element)
        tail.next = newNode
        newNode.prior = tail
        tail = newNode
    return head


def double_linklist_insert(head,i,element):
    '''
      在链表的第i个位置后插入element
    '''
    curNode = head
    if i == 0:
        P = Node2(element)
        P.next = head
        head.prior = P
        head = P
        return head

    for j in range(i-1):        # 寻找第i-1个节点
        curNode = curNode.next

    if curNode == None:
        raise TypeError('err!!!')

    else:
        P = Node2(element)
        if curNode.next == None:
            curNode.next = P
            P.prior = curNode
            return head
        
        P.next = curNode.next
        curNode.next.prior = P
        P.prior = curNode
        curNode.next = P
        return head


def double_linklist_delete(head,i):
    '''
      删除链表的第i个位置element
    '''
    curNode = head
    if i == 1:
        head = curNode.next
        head.prior = None
        return head
    
    for j in range(i-2):        # 寻找第i-1个节点
        curNode = curNode.next

    if curNode == None:
        raise TypeError('err!!!')
    else:
        P = curNode.next
        curNode.next = P.next
        P.prior = curNode
        del P
        return head



doublelinklist = create_double_linklist_head([4,5,6])
print_linklist(double_linklist_insert(doublelinklist,3,0))

'''
链表总结分析：

》》复杂度分析：
    》顺序表（列表和数组） 1 与 链表 2 谁简单：
        》按元素值查找： 都是O(n)
        》按下标查找： 1:O(1) 2:O(n)
        》在某个元素后插入: 1:O(n) 2:O(1) 
        》删除某个元素： 1:O(n) 2:O(1) 

    》 链表在插入和删除的操作上明显快于顺序表
    》 链表的内存分配可以更加灵活
        》 试利用链表重新实现栈和队列
    》 链表这种链式存储的数据结构对树和图的结构有很大的启发性
'''


# %%


'''
树：
树是一种数据结构 ：比如目录结构

树是一种可以递归定义的数据结构(链式存储的方式)

树是由n个节点组成的集合
    如果n = 0 这是一个空树
    如果n>0,那么存在1个节点作为树的根节点，其她节点可以分为m个集合，每个集合本身又是一棵树

'''

class Node:
    def __init__(self, name, type = 'dir'):
        self.name = name
        self.type = type

        self.children = []
        self.parent = Node


    def __repr__(self):
        return self.name

    
class FileSyetemTree:
    def __init__(self):
        self.root = Node("/")
        self.now = self.root

    def mkdir(self, name):
        # 尽量以“/'结尾

        if name[-1] != "/":
            name += "/"

        node = Node(name)
        self.now.children.append(node)

        node.parent = self.now

    def ls(self):
        return self.now.children


    def cd(self,name):
        if name[-1] != "/":
            name += "/"

        if name == "../":
            # 返回上一级
            self.now = self.now.parent
            return

        for child in self.now.children:
            #  寻找相对路径
            if child.name == name:
                self.now = child
                return
        raise ValueError("Invaild dir")


tree = FileSyetemTree()
tree.mkdir("var/")
tree.mkdir("bin/")
tree.mkdir("usr/")

tree.cd("bin/")
tree.mkdir("python/")


tree.cd("../")
print(tree.ls())
# %%
'''
二叉树：

    二叉树的链式存储方式： 将二叉树的节点定义为一个对象，节点之间通过类似链表的链接方式来链接

'''

class BiTreeNode:
    def __init__(self,data):
        self.data = data
        self.lchild = None # 左孩子
        self.rchild = None # 右孩子


a = BiTreeNode("A")
b = BiTreeNode("B")
c = BiTreeNode("C")
d = BiTreeNode("D")
e = BiTreeNode("E")
f = BiTreeNode("F")
g = BiTreeNode("G")

e.lchild = a
e.rchild = g
a.rchild = c
c.lchild = b
c.rchild = d
g.rchild = f

root = e
# 寻找c
print(root.lchild.rchild.data)


# %%
