#encoding:utf-8
class Stack:
    def __init__(self,maxSize = 20):
        self.data = []
        self.maxSize = maxSize
    def is_full(self):
        return len(self.data) == self.maxSize
    def push(self, X):
        if self.is_full():
            return False
        else:
            self.data.append(X)
            return True
    def is_empty(self):
        return len(self.data) == 0
    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.data.pop()
    def get_top(self):
        if self.is_empty():
            return None
        else:
            return self.data[-1]

# 二叉树结点
class TNode:
    def __init__(self, data, left=None, right = None):
        self.data = data
        self.left = left
        self.right = right

# 前序遍历，递归
def preOrderTraversal(tree):

    # if not tree:
    #     return None
    # else:
    #     print tree.data,
    #     preOrderTraversal(tree.left)
    #     preOrderTraversal(tree.right)


    if tree:
        print tree.data,
        preOrderTraversal(tree.left)
        preOrderTraversal(tree.right)


def inOrderTraversal(tree):
    if tree: # 递归出口，如果为none什么都不做就出去，也不会进入下一个递归
        inOrderTraversal(tree.left)
        print tree.data,
        inOrderTraversal(tree.right)
def postOrderTraversal(tree):
    if tree:
        postOrderTraversal(tree.left)
        postOrderTraversal(tree.right)
        print tree.data,


#########  非递归遍历，利用堆栈 ############
# http://bookshadow.com/weblog/2015/01/19/binary-tree-post-order-traversal/
# 先进后出的考虑使用堆栈
# https://blog.csdn.net/sgbfblog/article/details/7773103



# 本算法有一个地方要注意的是，每次从栈中pop出结点时，表示该结点以及该的左子树已经访问完了，接下来访问其右子树
def in_iteate(tree):
    s = Stack()
    while tree != None or not s.is_empty(): # 如果tree不为空，或者堆栈不空都应处理
        # 树不空
        if tree != None:
            s.push(tree)
            tree = tree.left
        else: # 栈不空
            top = s.pop()
            print top.data,
            tree = top.right # 转向右支
    print
    return None


# 只是与中序遍历的print位置不一样而已，其他都一样
def pre_iteate(tree):
    s = Stack()
    while tree != None or not s.is_empty(): # 如果tree不为空，或者堆栈不空都应处理
        # 树不空
        if tree != None:
            s.push(tree)
            print tree.data,
            tree = tree.left
        else: # 栈不空
            top = s.pop()
            tree = top.right # 转向右支
    print
    return None

# 法1，如果前序先右后左，那么逆转后就是后序了，因此采用两个堆栈来实现
def post_iteate1(tree):
    s2 = Stack()
    # 先右后左的前序， 入栈
    s = Stack()
    while tree != None or not s.is_empty():
        if tree!=None:
            s.push(tree)
            # print tree.data
            s2.push(tree)
            tree = tree.right
        else:
            top = s.pop()
            tree = top.left
    # 出栈
    while not s2.is_empty():
        print s2.pop().data,
    print
# 后序，需要判断其右子树是否访问过，若访问过才visit，pop该结点，因此需要记录上次访问的结点
# 对栈顶元素需要考虑其上次遍历是否是其右结点
def post_iteate2(tree):
    s = Stack()
    lastVisited = None
    while tree != None or not s.is_empty():
        if tree != None:
            s.push(tree)
            tree = tree.left
        else:
            top = s.get_top() # 栈顶元素 ,需要判断上次访问是否是其右子结点来确定是否访问该结点
            # if top.right != None and top.right != lastVisited:
            #     # 或者如果某个条件描述起来较麻烦的话，不如转向其对立条件，然后 做 非运算
            #     tree = top.right
            # else:
            #     print top.data,
            #     lastVisited = top
            #     s.pop()

            if top.right == None or top.right == lastVisited:
                # top.right == None or top.right == lastVisited与top.right == lastVisited 显然不等价，
                # 只有当lastVisited == none的时候二者等价
                print top.data,
                lastVisited = top
                s.pop()
            else:
                tree = top.right # 其实就是一个新的递归了，只不过是while迭代的形式
    print

# 层序遍历，利用一个队列
# 遍历从根结点开始，首先将根结点入队，然后开始执行循环：结点出队、访问该结点、其左右儿子入队(要想访问下一层的，怎么办？下一层是队头结点的子节点)
def levelOrderTraveral(tree):
    if tree == None:
        return None
    q = Queue()
    q.addQ(tree)
    while not q.is_empty():
        curr = q.deleteQ()
        print curr.data,
        if curr.left:
            q.addQ(curr.left)
        if curr.right:
            q.addQ(curr.right)


# 循环顺序队列
class Queue:
    def __init__(self, maxSize = 10):
        self.front = 0
        self.rear = 0
        self.maxSize = maxSize
        self.data = [None]*maxSize
    def is_empty(self):
        return self.rear == self.front
    def is_full(self):
        return (self.rear+1)%self.maxSize == self.front
    def addQ(self,X):
        if self.is_full():
            return False
        else:
            self.data[(self.rear+1)%self.maxSize] = X
            self.rear += 1
            return True
    def deleteQ(self):
        if self.is_empty():
            return False
        else:
            self.front = (self.front+1)%self.maxSize
            return self.data[self.front] # front指向的是第一个元素前面的位置


###############################
# 遍历二叉树的应用
# 输出树的叶子结点：在遍历结点中检测是否是叶子结点
def preOrderPrintLeaves(tree):
    if tree:
        # visit
        if tree.left==None and tree.right==None:
            print tree.data,
        preOrderPrintLeaves(tree.left)
        preOrderPrintLeaves(tree.right)

# 求二叉树的高度
# 空树为0，其他点 H = max(H_left, H_right) + 1，先左后右再加1，显然是后序遍历
def postOrderGetHeight(tree):
    if tree:
        H_left = postOrderGetHeight(tree.left)
        H_right = postOrderGetHeight(tree.right)
        # visit
        max = H_left if H_left > H_right else H_right
        return max + 1
    else:
        return 0 # 递归出口

#################  test  ##############
A = TNode('A')
B = TNode('B')
C = TNode('C')
D = TNode('D')
E = TNode('E')
F = TNode('F')
G = TNode('G')
H = TNode('H')
I = TNode('I')
G = TNode('G')

A.left = B
A.right = C
B.left = D
B.right= F
F.left = E
C.left = G
C.right = I
G.right = H

tree = A
preOrderTraversal(tree)
print
pre_iteate(tree)
print
inOrderTraversal(tree)
print
in_iteate(tree)
print
postOrderTraversal(tree)
print
post_iteate1(tree)
post_iteate2(tree)
print
levelOrderTraveral(tree)

print
preOrderPrintLeaves(tree)
print
print postOrderGetHeight(tree)

