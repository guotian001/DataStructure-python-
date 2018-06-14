# encoding:utf-8
'''
    图的邻接表表示
'''

MaxVertexNum = 10 # 最多顶点数
INFINITY = float('inf')
from SQueue import SQueue
class Edge:
    def __init__(self, v1=0, v2=0, weight=0):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight

# 邻接点
class AdjVNode:
    def __init__(self, adjV=0, weight=0, next_=None):
        self.adjV = adjV # 邻接点下标
        self.weight = weight
        self.next_ = next_
# 顶点表头结点的定义
class Vnode:
    def __init__(self, firstEdge=None, data=None):
        self.firstEdge = firstEdge # 边表头结点
        self.data = data # 顶点的数据 # 多数情况下顶点是不存数据的

class GNode:
    # 初始化一个由VertexNum 个顶点但是没有边的图
    def __init__(self, Nv=0, Ne=0):
        self.Nv = Nv # 顶点数
        self.Ne = Ne # 边数
        self.G = [Vnode() for i in range(Nv)] # 邻接表

    def insertEdgeDirect(self, e):
        newNode = AdjVNode()
        newNode.adjV = e.v2
        newNode.weight = e.weight
        # 将新建的邻接点插入邻接点表的头部
        newNode.next_ = self.G[e.v1].firstEdge
        self.G[e.v1].firstEdge = newNode

    def insertEdge(self, e):
        newNode = AdjVNode()
        newNode.adjV = e.v2
        newNode.weight = e.weight
        # 将新建的邻接点插入邻接点表的头部
        newNode.next_ = self.G[e.v1].firstEdge
        self.G[e.v1].firstEdge = newNode

        # 若为无向图，还需对称的再插入一条边
        newNode2 = AdjVNode()
        newNode2.adjV = e.v1
        newNode2.weight = e.weight
        newNode2.next_ = self.G[e.v2].firstEdge
        self.G[e.v2].firstEdge = newNode2

    def buildGraph(self):
        Nv = input()
        self.__init__(Nv)
        Ne = input()
        self.Ne = Ne
        while Ne:
            e = Edge()
            e_list = raw_input().strip().split()
            e.v1 = e_list[0]
            e.v2 = e_list[1]
            e.weight = e_list[2]
            self.insertEdge(e)
            Ne-=1

        for i in range(Nv):
            self.G[i].data = raw_input()

    def DFS(self, v):
        visited = [False]*self.Nv
        self.DFS(v, visited)
    def DFS(self, v, visited):
        self.visit(v)
        visited[v]=True
        # 遍历邻接点，递归DFS
        next = self.G[v].firstEdge
        while next:
            if not visited[next.adjV]:
                self.DFS(next.adjV)
            next = next.next_

    def visit(self, v):
        print '正在访问顶点%d' % v

    def BFS(self, v):
        visited = [False]*self.Nv
        self.BFS(v, visited)

    def BFS(self, v, visited):
        queue = SQueue(self.Nv)
        self.visit(v)
        visited[v] = True
        queue.addQ(v)
        while not queue.is_empty():
            pre = queue.deleteQ()
            # 遍历pre的邻接点
            next_ = self.G[pre].firstEdge
            while next_:
                if not visited[next_.adjV]:
                    self.visit(next_.adjV)
                    visited[next_.adjV] = True
                    queue.addQ(next_.adjV)
                next_ = next_.next_

    def listComponents(self):
        visited = [False]*self.Nv
        for i in range(self.Nv):
            if not visited[i]:
                # self.BFS(i, visited)
                self.DFS(i, visited)





