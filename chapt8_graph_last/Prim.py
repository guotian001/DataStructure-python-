#encoding:utf-8
'''
prim算法，当图较稠密时，该算法合算，

当图稀疏的时候有时间复杂度更小的kruskal算法

'''
# 伪码描述
def Prim():
    while True:
        v = findMinDist()
        if not v:
            break
        # 将v收进来
        dist[v] = 0
        for i in AdjV(v):
            if dist[i]!=0 and weight(v, i)<dist[i]:
                dist[i] = weight(v, i)
                parent[i] = v
    if Ncount < Nv:
        Error('生成树不存在')
        Error('图不连通')

#####################################################################################
# 稠密图有优势，故原图用邻接矩阵表示；最小生成树，可以只存parent，这样其实已经可 以确定一了, #
#  也可以专门用个邻接表来存储最小生成树                                                 #
#####################################################################################

from chapt6_graph_first.MGraph import GNode
from chapt6_graph_first.LGraph import GNode as LNode, Edge
INFINITE = float('inf')

# 未被收录的dist的最小点
def findMinDist(dist, Nv):
    min_ = INFINITE
    index = -1
    for i in range(Nv):
        if dist[i]!=0 and dist[i]<min_:
            min_ = dist[i]
            index = i
    # 走到这里可能是因为所有的dist都为0了，也可能是图不连通，dist中存的只是0和INFINITE
    return i if min_<INFINITE else False

def prim(G):
    # 初始化
    Nv = G.Nv
    dist = [INFINITE]*Nv # 存储的是结点到生成树的最小距离
    parent = [-1]*Nv # 认为所有点都是独立的结点（根节点）（父节点尚不确定）
    Tcount = 0
    totalWeight=0
    # 将结点0作为根节点
    for i in range(Nv):
        if G.G[0][i]<INFINITE:
            dist[i] = G.G[0][i]
            parent[i] = 0
    dist[0] = 0
    Tcount+=1
    
    # 新建最小生成树
    tree = LNode(Nv)

    # 正式开始prim
    while True:
        v = findMinDist()
        if not v: #可能是因为所有的dist都为0了，也可能是图不连通，dist中存的只是0和INFINITE
            break
        # 将v收进来
        Tcount+=1
        totalWeight+=dist[v]
        e = Edge(parent[v], v, dist[v])
        tree.insertEdge(e)
        dist[v] = 0
        # 遍历V的邻接点
        for i in range(Nv):
            if dist[i]!=0 and G.G[v][i]<dist[i]:
                dist[i] = G.G[v][i]
                parent[i] = v
    # 判断到底是否正常结束
    if Tcount<Nv:
        return None, None
    else:
        return tree, totalWeight

