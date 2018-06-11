# encoding:utf-8
'''
哈利波特的考试
'''
'''
6 11
3 4 70
1 2 1
5 4 50
2 6 50
5 6 60
1 3 70
4 6 60
3 6 80
5 1 100
2 4 60
5 2 80

4 70
'''
INFINITE = float('inf')

def readList():
    desc = raw_input()
    return map(int,  desc.strip().split())

class Edge:
    def __init__(self, V1, V2, weight = 1):
        self.V1 = V1
        self.V2 = V2
        self.weight = weight
class GNode:
    def __init__(self, Nv):
        self.Nv = Nv
        self.Ne = 0
        self.G =  [[INFINITE]*Nv for i in range(Nv)] # 注意python中二维数组的定义

    def insertEdge(self, e):
        self.G[e.V1][e.V2] = e.weight
        # 无向图， 还要对称插入一下
        self.G[e.V2][e.V1] = e.weight


def floyd(G, N):
    D = G.G
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if D[i][k] + D[k][j] < D[i][j]:
                    D[i][j] = D[i][k] + D[k][j]
                    if i == j and D[i][j] < 0:
                        return None # 存在负值圈，算法失效
    return D

def findMaxInline(D, i, N):
    max_ = -1
    index = -1
    for j in range(N):
        if i!=j and D[i][j] > max_: # 除了对角元
            max_ = D[i][j]
            index = j
    return max_, index

def findMinInMax(D, N):
    min_ = float('inf')
    index = -1
    for i in range(N):
        temp, j = findMaxInline(D, i, N)
        # 一张连通的图，应该所有的点都是通的
        if temp == INFINITE:# 不连通
            print 0
            return
        if temp < min_:
            min_ = temp
            index = i

    return min_, index


if __name__ == '__main__':
    # buildGraph
    desc = readList()
    N = desc[0]
    E = desc[1]
    G = GNode(N)
    G.Ne = E
    while E:
        edgeList = readList()
        e = Edge(edgeList[0]-1, edgeList[1]-1, edgeList[2])
        G.insertEdge(e)
        E-=1

    # Floyd
    D = floyd(G, N)
    # 找到每行中的最大值的最小值
    min_, index = findMinInMax(D, N)
    print index+1,
    print min_

