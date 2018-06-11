#encoding:utf-8
'''
分别用DFS,BFS列出如的连通集
'''
class SQueue:
    def __init__(self, maxSize = 8):
        self._rear = 0
        self._front = 0
        self._maxSize = maxSize
        self._data = [None] * maxSize

    def is_full(self):
        return (self._rear+1)%self._maxSize == self._front
    def is_empty(self):
        return self._rear == self._front
    def addQ(self, X):
        if self.is_full():
            print '队列满'
            return False
        else:
            self._rear = (self._rear + 1) % self._maxSize
            self._data[self._rear] = X
            return True

    def deleteQ(self):
        if self.is_empty():
            print '队列空'
            return None
        else:
            self._front = (self._front+1)%self._maxSize
            return self._data[self._front] # front指向第一个元素前面的元素

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
        list = []
        for i in range(Nv):
            list.append(AdjvNode(-1))
        self.G = list

    def insertEdge(self, e):
        # 小的插到前面方便遍历
        # pre = None
        # next_ = self.G[e.V1]
        # while next_ and e.V2 > next_.adjV:
        #     pre = next_
        #     next_ = next_.next_
        # node = AdjvNode(e.V2)
        # node.next_ = next_
        # if pre:
        #     pre.next_=node
        # else:
        #     self.G[e.V1] = node

        # 如果在设计数据机构的时候加个空头结点会方便很多
        curr = self.G[e.V1]
        while curr.next_ and e.V2>curr.next_.adjV:
            curr = curr.next_
        node = AdjvNode(e.V2)
        node.next_ = curr.next_
        curr.next_ = node

        curr = self.G[e.V2]
        while curr.next_ and e.V1>curr.next_.adjV:
            curr = curr.next_
        node = AdjvNode(e.V1)
        node.next_ = curr.next_
        curr.next_ = node

    # visited已经初始化
    def DFS(self, v, visited):
        print v,
        visited[v] = True
        # 遍历其邻接点
        next_ = self.G[v].next_
        while next_:
            if not visited[next_.adjV]:
                self.DFS(next_.adjV, visited)
            next_ = next_.next_

    def BFS(self, v, visited):
        print v,
        visited[v] = True
        queue = SQueue(20)
        queue.addQ(v)
        while not queue.is_empty():
            pre = queue.deleteQ()
            # 遍历pre的邻接点，访问并入队
            next_ = self.G[pre].next_
            while next_:
                if not visited[next_.adjV]:
                    print next_.adjV,
                    visited[next_.adjV] = True
                    queue.addQ(next_.adjV)
                next_=next_.next_

    def listComponentsWithDFS(self):
        visited = [False]*self.Nv
        for i in range(self.Nv):
            if not visited[i]:
                print '{',
                self.DFS(i,visited)
                print '}'

    def listComponentsWithBFS(self):
        visited = [False] * self.Nv
        for i in range(self.Nv):
            if not visited[i]:
                print '{',
                self.BFS(i, visited)
                print '}'




################ test #########################
'''
8 6
0 7
0 1
2 0
4 1
2 4
3 5

{ 0 1 4 2 7 }
{ 3 5 }
{ 6 }
{ 0 1 2 7 4 }
{ 3 5 }
{ 6 }

'''
def test():
    descList = raw_input().strip().split()
    Nv = int(descList[0])
    Ne = int(descList[1])

    # buildGraph
    g = GNode(Nv)
    while Ne:
        edge_list = raw_input().strip().split()
        e = Edge(int(edge_list[0]), int(edge_list[1]))
        g.insertEdge(e)
        Ne-=1

    g.listComponentsWithDFS()
    g.listComponentsWithBFS()

test()