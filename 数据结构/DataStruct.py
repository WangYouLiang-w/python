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
#%%
'''
》哈希表(又称为散列表）是一种线性表的存储结构。哈希表由一个直接寻址和一个哈希函数组成。哈希函数h(k)将元素关键字k作为自变量，返回元素的存储下标：
    >哈希表一个通过哈希函数来计算数据存储位置的数据结构（很高效的查找的数据结构），通常支持如下操作：
        》insert(key, value): 插入键值对（key, value)
        》get(key): 如果存在键为key的键值对则返回其value，否则返回空值
        》delete(key): 删除键为key的键值对

》 直接寻址表（key为k的元素放在k位置上）：
    当域U(存放键值对的下标何键值对应，通过寻找下标寻找键值对)很大时，需要消耗大量内存，很不实际
    如果域U很大而实际出现的key很少，则大量空间被浪费
    无法处理关键字不是数字的情况

》改进：哈希
    构建大小为m的寻址表T
    key为k的元素放到h(k)的位置上
    h(k)是一个函数，其将域U映射到表T[0,1,...,m-1]

》哈希冲突：
    由于哈希表的大小是有限的，而要存储的值的总数量是无限的，因此对于任何哈希函数，都会出现两个不同元素映射到同一个位置上的情况，这种情况叫做哈希冲突。

》哈希冲突的解决方法：
    开放寻址法：如果哈希函数返回的位置已经有值，则可以向后探查新的位置来存储这个值。
        》线性探查：如果位置i被占用，则探查i+1，i+2，....
        》二次探查：如果位置i被占用，则探查i+1^2,i-1^2,i+2^2,i-i^2....
        》二度哈希：有n个哈希函数，当使用第1个哈希函数h1发生冲突时，则尝试使用h2，h3，....
    
    拉链法（***）：哈希表每个位置都连接一个链表，当冲突发生时，冲突的元素将被加到该位置链表的最后

》常见的哈希函数
    除法哈希法：h(k) = k % m
    乘法哈希法：h(k) = floor(m*(A*key%1)) 向下取整
    全域哈希法:ha,b(k) = ((a*key + b) mod p) mod m a,b=1,2,...p-1

'''
class LinkList:

    class Node:
        def __init__(self, item = None):
            self.item = item
            self.next = None


    def __init__(self, iterable=None) :
        self.head = None
        self.tail = None
        if iterable:
            self.extend(iterable)


    def append(self, obj):
        s = LinkList.Node(obj)
        if not self.head:
            self.head = s
            self.tail = s
        else:
            self.tail.next = s
            self.tail = s
    

    def extend(self, iterable):
        for obj in iterable:
            self.append(obj)

    
    def find(self, obj):
        for n in self:
            if n == obj:
                return True
            else:
                return False
            
    
    def __iter__(self):
        '''迭代器'''
        return self.LinkListIterator(self.head)
    

    def __repr__(self) -> str:
        '''打印时将对象转换成字符串
          1. for example: ','.join('abc'), “将字符串abc中的每个成员以字符','分隔开再拼接成一个字符串”
          2.map() 会根据提供的函数对指定序列做映射。
            第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
        '''
        return "<<"+",".join(map(str, self))+">>"
    

    class LinkListIterator:
        # 迭代器类
        def __init__(self, node) -> None:
            self.node = node

        def __next__(self):
            # 执行迭代时，循环调用 __next__()
            if self.node:
                cur_node = self.node
                self.node = cur_node.next
                return cur_node.item
            
            else:
                raise StopIteration
        
        
        def __iter__(self):
            return self


LK = LinkList([1,2,3,4,5])

#可打印列表
for element in LK:
    print(element)
print(LK)

class HashTable:
    # 类似集合的操作
    def __init__(self, size = 101):
        self.size = size
        self.T = [LinkList() for i in range(self.size)]  


    def h(self,k):
        return k % self.size
    

    def insert(self, k):
        i = self.h(k)
        if self.find(k):
            print("Duplicated Insert")
        else:
            self.T[i].append(k)


    def find(self,k):
        i = self.h(k)
        return self.T[i].find(k)


ht = HashTable()
ht.insert(0)
ht.insert(1)
ht.insert(0)
print(','.join(map(str, ht.T)))
# %%
#---------练习
class LinkList:

    class Node:
        def __init__(self, item):
            self.item = item
            self.next = None

    
    class LinkListIterator:
        def __init__(self, Node=None):
            self.Node = Node


        def __next__(self):
            curNode = self.Node
            if not curNode:
                raise StopIteration
            else:
                self.Node = curNode.next
                return curNode.item
        

        def __iter__(self):
            return self

            
    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        if iterable:
            self.expand(iterable)

    
    def append(self, obj):
        curNode = LinkList.Node(obj)
        if not self.head:
            self.head = curNode
            self.tail = curNode
        else:
            self.tail.next = curNode
            self.tail = curNode

    
    def expand(self, iterable):
        for element in iterable:
            self.append(element)


    def find(self, obj):
        for n in self:
            if n == obj:
                return True
            else:
                return False
            

    def __iter__(self):
        return self.LinkListIterator(self.head)
    

    def __repr__(self) -> str:
        return '<<' + ','.join(map(str, self)) + '>>'


LK = LinkList([1,2,3,4,5])

for element in LK:
    print(element)

print(LK)
        

class HashTable:
    def __init__(self, size=101):
        self.size = size
        self.T = [LinkList() for n in range(size)]

    def h(self, k):
        return k % self.size
    

    def insert(self, obj):
        i = self.h(obj)
        if not self.find(obj):
            self.T[i].append(obj)

            
    def find(self, obj):
        i = self.h(obj)
        if self.T[i].find(obj):
            print("Doupulict Insert")
            return True
        else:
            return False


ht = HashTable()

ht.insert(0)
ht.insert(1)
ht.insert(0)        
print(','.join(map(str,ht.T)))   

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
'''
E（A（L_C（B，D），G（L_F））
二叉树的遍历方式（递归）：
》前序遍历：EACBDGF 
    如果二叉树不为空：先访问自己，再访问左子树，再访问右子树
》中序遍历：ABCDEGF
    如果二叉树不为空：先访问左子树，再访问自己，最后访问右子树
》后序遍历：BDCAFGE
    如果二叉树不为空：先访问左子树，再访问右子树，最后访问自己
》层次遍历：EAGCFBD
    采用队列，先进根节点进队，出队之后，将孩子节点进队，依次进行，直到队列为空
'''
class BiTreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.rchild = None
        self.lchild = None

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


def pre_order(root):
    '''
    前序遍历
    '''
    if root:
        print(root.data, end=',')
        pre_order(root.lchild)
        pre_order(root.rchild)


def in_order(root):
    '''
    中序遍历
    '''
    if root:
        in_order(root.lchild)
        print(root.data, end=",")
        in_order(root.rchild)


def post_order(root):
    '''后序遍历'''
    if root:
        post_order(root.lchild)
        post_order(root.rchild)
        print(root.data, end=",")


from collections import deque
def level_order(root):
    Tree_queue = deque()
    Tree_queue.append(root)
    while len(Tree_queue) != 0:
        node = Tree_queue.popleft()
        print(node.data, end= ", ")

        if node.lchild:
            Tree_queue.append(node.lchild)
        
        if node.rchild:
            Tree_queue.append(node.rchild)


level_order(root)
# in_order(root)
# post_order(root)

# %%
'''
二叉搜索树（banary search tree, BST):设x是二叉树的一个节点，如果y是x左子树的一个节点，那么y.key<=x.key; 
                                如果y是x右子树的一个节点，那么y.key >= x.key

二叉搜素树的查询、插入和删除

****二叉搜索树的中序序列是有序的
删除：
（1）如果删除的节点是叶子节点，直接删除
（2）如果删除的节点只有一个孩子，将此节点的父亲与孩子连接，然后删除
（3）如果删除的节点有两个孩子，将其右子树的最小节点替换当前节点并（该节点最多有一个右孩子**）删除。（寻找最小节点的
    方法是往左走到头）
'''
class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
        self.parent = None


class BST:
    def __init__(self, li=None):
        self.root = None

        if li:
            for val in li:
                # self.root = self.insert_rec(self.root, val)
                self.insert_no_rec(val)


    def insert_rec(self, Node, val):
        '''插入的递归方法'''
        if not Node:
            Node = BiTreeNode(val)
        
        elif val < Node.data:
            Node.lchild = self.insert_rec(Node.lchild, val)
            Node.lchild.parent = Node
        
        elif val > Node.data:
            Node.rchild = self.insert_rec(Node.rchild, val)
            Node.rchild.parent = Node

        return Node
    

    def insert_no_rec(self, val):
        '''插入的非递归方法'''
        p = self.root
        if not p:
            self.root = BiTreeNode(val)
            return
        while True:
            if val < p.data:
                if not p.lchild:
                    p.lchild = BiTreeNode(val)
                    p.lchild.parent = p
                    return
                else:
                    p = p.lchild
        
            elif val > p.data:
                if not p.rchild:
                    p.rchild = BiTreeNode(val)
                    p.rchild.parent = p
                    return
                else:
                    p = p.rchild
            else:
                return
    

    def search_rec(self, node, val):
        '''查找的递归方法'''
        if not node:     # 如果为空
            return None
        else:
            if val < node.data:
                return self.search_rec(node.lchild, val)
            elif val > node.data:
                return self.search_rec(node.rchild, val)
            else:
                return node
            
    
    def search_no_rec(self,val):
        '''查找的非递归方法'''
        p = self.root
        while p:
            if val < p.data:
                p = p.lchild
            elif val > p.data:
                p = p.rchild
            else:
                return p
        return None
    
      
    def __remove_node_1(self, node):
        '''删除的节点是叶子节点'''
        if not node.parent: # 是根节点
            self.root = None
        if node == node.parent.lchild:
            node.parent.lchild = None
        else:
            node.parent.rchild = None

    def __remove_node_21(self, node):
        '''删除的节点只有一个左孩子'''
        if not node.parent:
            self.root = node.lchild
            node.lchild.parent = None

        elif node == node.parent.lchild:
            node.parent.lchild = node.lchild
            node.lchild.parent = node.parent
        else:
            node.parent.rchild = node.lchild
            node.lchild.parent = node.parent
        

    def __remove_node_22(self, node):
        '''删除的节点只有一个右孩子'''
        if not node.parent:
            self.root = node.rchild
            node.rchild.parent = None

        elif node == node.parent.rchild: # 删除的节点是它父亲的右孩子
            node.parent.rchild = node.rchild
            node.rchild.parent = node.parent
        
        else:
            node.parent.lchild = node.rchild
            node.rchild.parent = node.parent


    
    def delete(self, val):
        '''删除节点'''
        if self.root: # 不是空树
            node = self.search_no_rec(val)
            if not node: # 不存在
                return False
            
            if not node.lchild  and not node.rchild:
                self.__remove_node_1(node)
            elif node.lchild == None:
                self.__remove_node_22(node)
            elif node.rchild == None:
                self.__remove_node_21(node)
            else:
                #有两个孩子节点
                min_node = node.rchild
                while min_node.lchild:
                    min_node = min_node.lchild
                node.data = min_node.data
                # 删除min_node
                if not min_node.rchild:
                    # 右子树最小的节点没有右孩子
                    self.__remove_node_1(min_node)
                else:
                    self.__remove_node_22(min_node)


    def pre_order(self, root):
        '''
        前序遍历
        '''
        if root:
            print(root.data, end=',')
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)


    def in_order(self, root):
        '''
        中序遍历
        '''
        if root:
            self.in_order(root.lchild)
            print(root.data, end=",")
            self.in_order(root.rchild)


    def post_order(self,root):
        '''后序遍历'''
        if root:
            self.post_order(root.lchild)
            self.post_order(root.rchild)
            print(root.data, end=",")

            
b_s_t = BST([1,3,4,5,6,9,2,7,10,8])

# print(b_s_t.root)
# b_s_t.pre_order(b_s_t.root)
# print("")
b_s_t.in_order(b_s_t.root)
print("")
# b_s_t.post_order(b_s_t.root)
b_s_t.delete(4)
b_s_t.in_order(b_s_t.root)


# %%
'''
平衡二叉树：AVL树

问题：
    二叉树的平均情况下进行搜索的时间是O(lgn)
    最坏情况下，树比较倾斜，查找效率是O（n）

解决的方法：
    随机化插入
    AVL树：是一棵自平衡的二叉搜索树

AVL树的性质：
    根的左右子树的高度之差的绝对值不能超过1 （balance factor：右子树的高度 - 左子树的高度）
    根的左右子树都是平衡二叉树

AVL树的插入：
    》插入一个节点可能会破坏AVL树的平衡，可以通过《旋转》操作来进行修正
    》插入一个节点后，只有从插入节点到根节点的路径上的节点的平衡可能被改变。我们需要找出第一个破坏了平衡条件的节点，称之为k。k的两颗子树的高度差为2
    》不平衡的出现可能有4种情况：
        》对K的右孩子的右子树插入导致的不平衡:左旋（从上左旋）
        》对K的左孩子的左子树插入导致的不平衡:右旋（从下右旋）
        》对K的右孩子的左子树插入导致的不平衡：先右旋，再左旋
        》对K的左孩子的右子树插入导致的不平衡：先左旋，再右旋
'''

class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
        self.parent = None

class BST:
    def __init__(self):
        self.root = None


    def pre_order(self, root):
        '''
        前序遍历
        '''
        if root:
            print(root.data, end=',')
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)


    def in_order(self, root):
        '''
        中序遍历
        '''
        if root:
            self.in_order(root.lchild)
            print(root.data, end=",")
            self.in_order(root.rchild)


    def post_order(self,root):
        '''后序遍历'''
        if root:
            self.post_order(root.lchild)
            self.post_order(root.rchild)
            print(root.data, end=",")

            
class AVLNode(BiTreeNode):
    def __init__(self, data):
        super().__init__(data)
        self.bf = 0


class AVLTree(BST):
    def __init__(self, li=None):
        BST.__init__(self)
        if li:
            for val in li:
                self.insert_no_rec(val)

    def rotate_left(self, p, c):
        '''左旋'''
        s2 = c.lchild 
        p.rchild = s2
        if s2:
            s2.parent = p
        
        c.lchild = p
        p.parent = c

        # 更新bf
        c.bf = 0
        g.bf = 0
        return c
    
    
    def rotate_right(self, p, c):
        '''右旋'''
        s2 = c.rchild
        p.lchild = s2
        if s2:
            s2.parent = p
        c.rchild = p
        p.parent = c

        c.bf = 0
        p.bf = 0
        return c

    
    def rotate_right_left(self, p, c):
        '''先右旋再左旋'''
        g = c.lchild
        s3 = g.rchild
        c.lchild = s3
        if s3:
            s3.parent = c
        g.rchild = c
        c.parent = g

        s2 = g.lchild
        p.rchild = s2
        if s2:
            s2.parent = p
        g.lchild = p
        p.parent = g

        #更新bf
        if g.bf < 0 : #左边沉
            c.bf = 1
            p.bf = 0
        else:
            c.bf = 0
            p.bf = -1

        g.bf =0
        
        return g

    
    def rotate_left_right(self, p, c):
        '''先右旋再左旋'''
        g = c.rchild
        s2 = g.lchild
        c.rchild = s2
        if s2:
            s2.parent = c
        g.lchild = c
        c.parent = g

        s3 = g.rchild
        p.lchild = s3
        if s3:
            s3.parent = p
        g.rchild = p
        p.parent = g

        #更新bf
        if g.bf < 0 : #左边沉
            c.bf = 0
            p.bf = 1
        else:
            c.bf = -1
            p.bf = 0

        g.bf = 0
        return g

    
    def insert_no_rec(self, val):
        '''插入的非递归方法'''
        p = self.root
        if not p:
            self.root = AVLNode(val)
            return
        while True:
            if val < p.data:
                if not p.lchild:
                    p.lchild = AVLNode(val)
                    p.lchild.parent = p
                    node = p.lchild  # 插入的节点
                    break
                else:
                    p = p.lchild
        
            elif val > p.data:
                if not p.rchild:
                    p.rchild = AVLNode(val)
                    p.rchild.parent = p
                    node = p.rchild
                    break
                else:
                    p = p.rchild
            else:
                break
        
        # 更新 balance factor
        # 在插入节点后，若从某个节点的左子树插入，bf-1，从父亲节点开始往上传递bf的变化，如果有一个节点的bf=0，更新结束
        # 如果有一个节点变成2或-2就不平衡了，然后调节子树（又要分4种情况）
        while node.parent:   # node.parent 不为空
            if node.parent.lchild == node: # r如果是从左子树来的，左子树更沉了
                # 更新node.parent的bf -= 1  
                # node.parent的bf可能是 -1，0，1
                if node.parent.bf < 0: # 原来的node.parent.bf == -1,更新后变成-2
                    # 做旋转
                    g = node.parent.parent # 为了连接旋转之后的子树
                    x = node.parent # 旋转前子树的根
                    if node.bf > 0:
                        n = self.rotate_left_right(node.parent, node)
                    else:
                        n = self.rotate_right(node.parent, node)
                    # 记得将n和g 连起来
                elif node.parent.bf > 0:
                    node.parent.bf = 0
                    break
                else:
                    node.parent.bf = -1
                    node = node.parent
                    continue

            else: # 如果是从右子树来的，右子树更沉了
                # 更新node.parent的bf += 1  
                # node.parent的bf可能是 -1，0，1
                if node.parent.bf > 0: # 原来的node.parent.bf == 1,更新后变成2
                    # 做旋转
                    g = node.parent.parent # 为了连接旋转之后的子树
                    x = node.parent # 旋转前子树的根
                    if node.bf < 0:
                        n = self.rotate_right_left(node.parent, node)
                    else:
                        n = self.rotate_left(node.parent, node)
                    # 记得将n和g 连起来
                elif node.parent.bf < 0:
                    node.parent.bf = 0
                    break
                else:
                    node.parent.bf = 1
                    node = node.parent
                    continue
            
            # 连接旋转后的子树
            n.parent = g
            if g:
                if x == g.lchild:
                    g.lchild = n
                else:
                    g.rchild = n
                break
            else: #调整的是根节点
                self.root = n
                break


tree = AVLTree([9,8,7,6,5,4,3,2,1])

tree.pre_order(tree.root)
print("")
tree.in_order(tree.root)


# %%
