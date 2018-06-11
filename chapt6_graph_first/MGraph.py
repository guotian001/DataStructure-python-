# encoding:utf-8
'''
图的邻接矩阵表示
'''
MaxVertexNum = 10 # 最多顶点数
INFINITY = float('inf')
from SQueue import SQueue

class Edge:
    def __init__(self, v1=0, v2=0, weight=0):
        self.v1 = v1
        self.v2 = v2
        # 有向边<v1, v2>
        # 无向边可以用两个有向边表示，无向边是双向边
        self.weight = weight

# 图结点
class GNode:
    # 初始化一个有VertexNum个顶点但没有边的图
    def __init__(self, VertexNum):
       self.Nv = VertexNum
       self.Ne = 0
       self.G = [[INFINITY]*MaxVertexNum]*MaxVertexNum # 邻接矩阵， 有权重的情况下，初始化为无限大
                                                        # 不存在自回路，所以对角元存储的应该是无穷大
       self.Data = [None]*MaxVertexNum # 存储顶点的数据，很多情况下顶点是没有数据的，因此不用此属性
    def insertEdge(self, e):
        self.G[e.v1][e.v2] = e.weight
        # 无向图， 还要对称插入一下
        self.G[e.v2][e.v1] = e.weight
    # 建立表
    def buildGraph(self):
        Nv = input() # 读入顶点个数
        self.__init__(Nv)
        Ne = input() # 读入边数
        self.Ne = Ne
        e = Edge()
        while Ne:
            # 输入边，格式“起点 终点 权重”
            e_list = raw_input().strip().split()
            e.v1 = e_list[0]
            e.v2 = e_list[1]
            e.weight = e_list[2]
            self.insertEdge(e)
            Ne-=1
        # 如果顶点有数据的话，读入数据
        for i in raw_input(Nv):
            # 依次读入结点数据
            self.Data[i] = raw_input()


    def visit(self, v):
        print '正在访问顶点%d' % v

    def DFS(self, v):
        visited = [False]*self.Nv
        self.DFS(v, visited)
    def DFS(self, v, visited):
        self.visit(v)
        visited[v] = True
        # 遍历v的邻接点
        for i in range(self.Nv):
            if self.isEdge(v, i) and not visited[i]:
                self.DFS(i)
# /* 此函数根据图的不同类型要做不同的实现，关键取决于对不存在的边的表示方法。*/
# /* 例如对有权图, 如果不存在的边被初始化为INFINITY, 则函数实现如下:         */
    def isEdge(self, v, w):
        return True if self.G[v][w]<INFINITY else False

    # 访问完后将其入队；从队列中pop，访问其邻接点，并邻接点入队
    def BFS(self, v):
        visited = [False]*self.Nv
        self.BFS(v,visited)
    def BFS(self, v, visited):
        queue = SQueue(self.Nv)
        self.visit(v)
        visited[v] = True
        queue.addQ(v)
        while not queue.is_empty():
            pre = queue.deleteQ()
            # 找到其邻接点，并入队
            for i in range(self.Nv):
                if self.isEdge(pre,i) and not visited[i]:
                    self.visit(i)
                    visited[i] = True
                    queue.addQ(i)

    def listComponents(self):
        visited = [False]*self.Nv
        for i in range(self.Nv):
            if not visited[i]:
                # self.DFS(i, visited)
                self.BFS(v, visited)





