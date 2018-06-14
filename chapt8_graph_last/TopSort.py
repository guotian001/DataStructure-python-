# encoding:utf-8
'''
拓扑排序
    ： 暴力遍历入度为0的结点，O(V^2)， 适合稠密图
    利用容器(比如队列) , O(V+E), 适合稀疏图
'''
from chap2_linearTable.SQueue import SQueue

def initialInDegree(G):
    inDegree = [0]*G.Nv
    for i in range(G.Nv):
        next_ = G.G[i].firstEdge
        while next_:
            inDegree[next_.adjV]+=1
            next_ = next_.next_
    return inDegree

def TopSort(G):
    # 初始化
    inDegree = initialInDegree(G)
    queue = SQueue(G.Nv)
    # 算法开始
    topSort = []
    count = 0
    for i in inDegree:
        if i == 0:
            queue.addQ(i)
    while not queue.is_empty():
        v = queue.deleteQ()
        topSort.append(v)
        count+=1
        # 对v的邻接点进行减度
        next_ = G.G[v].firstEdge
        while next_:
            inDegree[next_.adjV] -= 1
            if inDegree[next_.adjV] == 0:
                queue.addQ(next_.adjV)
            next_ = next_.next_
    # if count<G.Nv:
    #     return False # 存在回路
    # else:
    #     return topSort
    return None if count<G.Nv else topSort