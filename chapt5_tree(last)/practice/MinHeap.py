# encoding:utf-8
# 最小堆
# maxSize = 1000
minData = -10001
class minHeap:
    def __init__(self, maxSize):
        self.capacity = maxSize
        self.size=0
        self.elements = [None]*(maxSize+1)
        self.elements[0]=minData

    def isFull(self):
        return self.size==self.capacity
    def insert(self, x):
        if self.isFull():
            return False
        self.size+=1
        i = self.size
        while x<self.elements[i/2]: # 一定小于elements[0]，即i>=1肯定成立
            self.elements[i]=self.elements[i/2]
            i/=2
        self.elements[i]=x
        return True

    # 打印从i结点到根节点路径上的元素的值
    def printPath(self, i):
        while i/2>=0:
            if i==0:
                break
            else:
                print self.elements[i],
                i/=2

        # print self.elements[i],
        # while i/2>=1:
        #     i/=2
        #     print self.elements[i],


############################
'''
5 3
46 23 26 24 10
5 4 3

24 23 10
46 23 10
26 10
'''

def readList():
    desc = raw_input()
    return map(int,  desc.strip().split())

def test():
    maxSize = 1000
    desc = readList()
    N = desc[0]
    M = desc[1]
    h = minHeap(maxSize)
    heap_list = readList()
    # 构建最小堆
    for i in range(len(heap_list)):
        h.insert(heap_list[i])
    # 打印
    M_list = readList()
    for i in range(M):
        h.printPath(M_list[i])
        print

test()
