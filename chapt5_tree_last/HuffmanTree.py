# encoding:utf-8
'''
    哈夫曼树的构建：
        1.选取最小的两个结点构成一个树，树的权重为两个结点权重的和
        2.将树当做一个结点放进序列中，重复上述过程
    ps ： 选择的过程中利用最小堆来实现下
'''
'''
除第一合并减少两个结点外，每次合并都能减少一个结点，
如果某次合并减少了两个结点，说明这两个结点生成了一颗新的树，还要将该树合到与原先构建的树上，
因此还是要多做一次合并，与每次合并减少一个结点效果一样

故共需合并n-1次
'''

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# 堆中存放Node结点，这样delete出来的就是一个结点,保证树结构
# 顺便实现下最小堆
# 堆中存放的不在直接是数据，而是对象，进行比较的key是对象的一个属性
minData = float('-inf')
class MinHeap:
    def __init__(self, maxSize):
        self.elements = [None]*(maxSize+1)
        self.size=0
        self.capacity = maxSize
        self.elements[0]=Node(minData)
    def isFull(self):
        return self.size==self.capacity

    def insert(self, item):
        if self.isFull():
            print '最小堆已满'
            return False
        # 开始插入
        self.size+=1
        i = self.size
        while item.data < self.elements[i/2].data: # 0位置存放的是极小值，因此不用考虑超过边界的问题
            self.elements[i] = self.elements[i/2]
            i/=2
        self.elements[i]=item
        return True

    def isEmpty(self):
        return self.size == 0

    def delete(self):
        if self.isEmpty():
            print '最小堆已空'
            return None
        # 开始删除
        temp = self.elements[self.size]
        self.size-=1
        min = self.elements[1]
        parent=1
        while 2*parent<=self.size:
            # 找到最小子结点
            child = 2*parent
            if child!=self.size and self.elements[child].data > self.elements[child+1].data:
                child+=1
            # 上浮
            if self.elements[child].data < temp.data:
                self.elements[parent] = self.elements[child]
                parent = child
            else:
                break
        self.elements[parent] = temp
        return min

    # 调整第i个结点的位置，它的左右子树都是最小堆
    def adjust(self, i):
        temp = self.elements[i]
        parent = i
        while 2*parent<=self.size:
            child=2*parent
            if child!=self.size and self.elements[child].data>self.elements[child+1].data:
                child+=1
            if self.elements[child].data<temp.data:
                self.elements[parent] = self.elements[child]
                parent = child
            else:
                break
        self.elements[parent] = temp


    def buildTree(self, list):
        self.elements[1:] = list
        self.size = len(list)
        # 开始递归调整
        for i in range(len(list)/2, 0,-1):
            self.adjust(i)

def huffman(heap): # 此处的heap是最小堆
    # 做n-1次合并
    for i in range(heap.size-1):
        node = Node()
        node.left = heap.delete()
        node.right = heap.delete()
        node.data = node.left.data+node.right.data
        heap.insert(node)
    # 最后堆中剩下的元素就是Huffman树
    return heap.delete()

# 递归：解方程的思想总能使问题简便化
# 递归求wpl
# 递归 闪烁着智慧的光芒
# 根节点的长度=0
def wpl(tree, length=0):
    # 如果是叶子结点，直求，如果不是，返回其左树的+右树的,每递归一层，长度+1，根节点的长度=0
    if not tree:
        return 0
    else:
        if tree.left==None and tree.right==None:
            return tree.data*length
        else:
            return wpl(tree.left,length+1)+wpl(tree.right,length+1)



################  test  ##########################


dataList = [1,2,3,4,5]
def huffmanWithList():
    list = [Node(i) for i in dataList]
    h = MinHeap(10)
    h.buildTree(list)
    huffTree = huffman(h)
    return huffTree
    # print wpl(huffTree)

test()


##############  哈夫曼编码  ########################
'''
    对给定的字符串，如何对其中的字符进行编码（字符出现频率不同），使得整个字符串的存储成本最低？
    等长编码：给每个字符一个固定的位数，这个给定的位数可以表示所有出现的字符
    可以进一步改进，已知字符出现的频率，经常出现的字符要远远小于所有的字符数，因此对这些经常出现的位数可以采用较少位数表示，
    而那些不经常出现的字符用较多位数表示；再极端点，对每个不同频率的字符都采用可能不同的编码，不等长编码
    不等长编码：可以使得出现频率高的位数小，而出现频率低的位数高（因为等长的较小的位数不能完全表示所有的字符），进而使得总的存储成本降低
    
    问题： ① 二义性 如何避免：每个字符都不是其他字符的前缀码；解决方法，使用二叉树（左分支0，右分支1，从根结点到该结点的字符表示其编码），让每个字符都位于叶节点上，这样就不会有字符是其他字符的前缀码的情况
                         （如果某个字符是其他字符的前缀码，那么她肯定是其他字符的祖先结点，即它就不是叶子结点）
          ② 总成本最小
    
    方法： 哈夫曼树，根据每个字符出现的频率
    
'''
