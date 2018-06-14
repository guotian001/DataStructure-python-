#encoding:utf-8
'''
六度空间

E = 33*N,
(存储成本的界限是133  V^2,  V+E)
(遍历 V^2, V+E)
则当N<17时的时候邻接矩阵的存储成本优于邻接矩阵
E< 33*N时，临界值<17 ，不过当小于17的时候，存储成本也不会很大，只有N很大的时候才会有时间复杂度瓶颈问题，
故采用邻接表

'''


class Node:
    def __init__(self, elem, next_=None):
        self._elem = elem
        self._next = next_

class LQueue:
    def __init__(self, maxSize = 8):
        self._front = None
        self._rear = None
        self._maxSize = maxSize
    def is_empty(self):
        return self._front == None
    def deleteQ(self):
        if self.is_empty():
            print '队列为空'
            return None
        else:
            # 不带空头结点
            temp = self._front
            if self._front == self._rear:
                self._front = self._rear = None
            else:
                self._front  = temp._next
            return temp._elem
    def len(self):
        i = 0
        curr = self._front
        while curr:
            curr = curr._next
            i+=1
        return i

    def is_full(self):
        return self.len() == self._maxSize

    def push(self,X):
        if self.is_full():
            print '队列达到最大值'
            return False
        else:
            # 不带空头结点
            temp = Node(X)
            if self._front:# 队列不为空
                self._rear._next = temp
                self._rear = temp
            else:
                self._front = self._rear = temp
            return True



class AdjvNode:
    def __init__(self, adjV=0, next_=None):
        self.adjV = adjV
        self.next_ = next_

class Edge:
    def __init__(self, v1=0, v2=0):
        self.V1 = v1
        self.V2 = v2

class GNode:

    def __init__(self, Nv=0):
        self.Nv = Nv
        self.Ne = 0
        self.G = [None]*Nv

    def insertEdge(self, e):
        node = AdjvNode(e.V2)
        node.next_ = self.G[e.V1]
        self.G[e.V1] = node

        node = AdjvNode(e.V1)
        node.next_ = self.G[e.V2]
        self.G[e.V2] = node

    # 如何解决层的问题 ？
    def BFS(self, v):
        visited = [False]*self.Nv
        queue = LQueue()
        count = 1
        visited[v] = True
        queue.push(v)
        level = 0
        last = v  # last 表示层中的最后一个结点
        tail = 0  # tail表示下层的尾（最后一个结点）

        while not queue.is_empty():
            pre = queue.deleteQ()
            # 遍历pre的邻接点入队，count++
            next_ = self.G[pre]
            while next_:
                if not visited[next_.adjV]:
                    # do
                    queue.push(next_.adjV)
                    count += 1
                    visited[next_.adjV] = True
                    tail = next_.adjV
                # 迭代
                next_ = next_.next_
            # 当把某层中的最后一个出队后，表明该层添加结束，需要更新last为下一层的tail
            if pre == last:
                level += 1  # level更新时，恰是这层都入队完成的时候
                last = tail
            if level == 6:  # 第6层入队完毕，计数完毕
                break
        return count

    def SDS(self):
        for i in range(self.Nv):
            count = self.BFS(i)
            print '%d: %.2f%%' % (i+1, count*100.0/self.Nv)

############## test #################
'''
10 9
1 2
2 3
3 4
4 5
5 6
6 7
7 8
8 9
9 10

1: 70.00%
2: 80.00%
3: 90.00%
4: 100.00%
5: 100.00%
6: 100.00%
7: 100.00%
8: 90.00%
9: 80.00%
10: 70.00%
'''

def readList():
    desc = raw_input()
    return map(int,  desc.strip().split())

def test():
    desc = readList()
    N = desc[0]
    M = desc[1]
    # build Graph
    g = GNode(N)
    for i in range(M):
        # 从1开始编号，因此0位置存的是编号1
        e_list = readList()
        e = Edge(e_list[0]-1, e_list[1]-1)
        g.insertEdge(e)
    g.SDS()


test()


