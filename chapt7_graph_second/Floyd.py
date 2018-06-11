# encoding:utf-8
'''
多源最短路径
    稠密图，floyd (邻接矩阵存储)
    稀疏图，直接暴力解法，（其中使用堆）
'''
from chapt6_graph_first.MGraph import GNode
INFINITE = float('inf')
def Floyd(g, ):
    # 初始化：
    G = [[0]*g.Nv]*g.Nv
    path = [[-1]*g.Nv]*g.Nv
    for i in range(g.Nv):
        for j in range(g.Nv):
            G[i][j] = g.G[i][j]
            path[i][j] = i # 与下面的前驱结点保持一致

    for k in range(g.Nv):
        for i in range(g.Nv):
            for j in range(g.Nv):
                if G[i][k]+G[k][i]<G[i][j]: # 需要找个实例来看看，到底找个算法到底做了什么东西
                    G[i][j] = G[i][k]+G[k][i]
                    if i==j and G[i][j] < 0:# 如果==0呢，转再多圈也是0，所以一圈得到的就是最短路径，
                                            # 但是如果<0，转的圈数越多越小，但是该算法只会执行一圈，所以得到的就是错误的答案，算法失效

                        return False # 负值圈，不能解决
                    path[i][j]= k
    return True

def printPath(path,i, j):
    # 递归解决问题
    k = path[i][j]
    if k == i:
        print k
        return
    printPath[i][k]
    printPath[k][j]