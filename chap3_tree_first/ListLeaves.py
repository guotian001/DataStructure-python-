#encoding:utf-8
'''

8
1 -
- -
0 -
2 7
- -
- -
5 -
4 6

4 1 5

思路：
    1.buildTree，elem就放下标，静态链表
    2.层序遍历，加上检测是否是叶子结点


'''

def readList():
    desc = raw_input()
    result = desc.strip().split()
    result[0] = toInt(result[0])
    result[1] = toInt(result[1])
    return result

def toInt(c):
    return NULL if c == '-' else int(c)

# left，right 指的是数组下标
class TNode:
    def __init__(self, elem, left, right):
        self.elem = elem
        self.left = left
        self.right = right

# NULL = '-' # 全局变量
# 下标应转为int，为保持一致，需要将'-' 用特殊的int代替，不妨设为-1
NULL = -1
def buildTree():
    N = input() # 结点数
    tree = [None]*N # 新建一个n的数组，python中仅做练习
    check = [0]*N # 每个结点的初始标记为0，当有结点指向他时，改为1，根节点没有别的结点指向，check为0
    for i in range(N):
        node_desc = readList()
        node = TNode(i, node_desc[0],node_desc[1])
        tree[i] = node
        # 在输入遍历的时候就把check确定了
        if node_desc[0] != NULL:
            check[node_desc[0]] = 1
        if node_desc[1] != NULL:
            check[node_desc[1]] = 1
    root = -1
    for i in range(N):
        if check[i] == 0:
            root = i
            break
    return tree, root



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

def main():
    tree, root = buildTree()
    # 层序遍历加上叶子结点检测
    q = Queue(12)
    q.addQ(tree[root])
    while not q.is_empty():
        temp = q.deleteQ()
        # visit
        if temp.left==NULL and temp.right==NULL:
            print temp.elem,
        # 将左右子节点入队
        if temp.left!=NULL:
            q.addQ(tree[temp.left])
        if temp.right!=NULL:
            q.addQ(tree[temp.right])

main()