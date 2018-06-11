#encoding:utf-8
'''
单源有权最短路径
'''
# collected[] path[] dist[]都初始化好
# 伪码/接口，不同的结构不同的方法，不同的实现
def dijkstra(collected, path, dist):
    # 循环执行直到所有点都被collected
    while True:
        v = getMinDistNotCollected() # 遍历/最小堆
        if not v:
            break
        collected[v] = True
        # 遍历更新v的邻接点
        for w in getAdjV(v):
            if not collected[w] and dist[v]+getWeight(v, w)<dist[w]:
                # 更新
                dist[w] = dist[v]+getWeight(v, w)
                path[w] = v


# 邻接矩阵存储图

INFINITE = float('inf')
from chapt6_graph_first.MGraph import GNode

def getMinDistNotCollected(collected, dist, n):
    # 遍历扫描
    minDist = INFINITE
    minV = -1
    for i in range(n):
        if not collected[i] and dist[i]<minDist:
            minDist = dist[i]
            minV = i
    if minV>-1:
        return minV
    else:
        return  None

def dijkstra(g, dist, path, s):
    # 初始化
    collected = [False]*g.Nv
    path = [-1]*g.Nv
    dist = [INFINITE]*g.Nv

    collected[s] = True
    for i in range(g.Nv):
        if g.G[s][i]<INFINITE:
            dist[i] = g.G[s][i]
            path[i] = s

    # 开始dijkstra算法
    while True:
        v = getMinDistNotCollected()
        if not v:
            break
        collected[v] = True
        # 找到v的邻接点
        for i in range(g.Nv):
            if not collected[i] and g.G[v][i]<INFINITE:
                if g.G[v][i] < 0:
                    return False
                if dist[v] + g.G[v][i] < dist[i]:
                    dist[i] = dist[v]+g.G[v][i]
                    path[i] = v

    return True

from chap2_linearTable.LStack import LStack
def printPath(path, v):
    # 堆栈操作
    stack = LStack()
    # 起点为-1
    while True:
        stack.push(v)
        if path[v] == -1:
            break
        v = path[v]

    # 开始输出
    while not stack.is_empty():
        print stack.pop(),