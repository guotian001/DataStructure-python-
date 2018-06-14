#encoding:utf-8
'''
how long does it take?
AOE问题中的工期是多少，显然用拓扑排序算法简单改进下就是可以的

'''
'''
9 12
0 1 6
0 2 4
0 3 5
1 4 1
2 4 1
3 5 2
5 4 0
4 6 9
4 7 7
5 7 4
6 8 2
7 8 4

18

------------------


4 5
0 1 1
0 2 2
2 1 3
1 3 4
3 2 5

Impossible  # 有回路，不可能完成，你等我，我等你。。。

'''

from chapt6_graph_first.LGraph import GNode
from utils.buildGraph import buildGraphFrom0
from chap2_linearTable.SQueue import SQueue

def getEnd(G):
    for i in range(G.Nv):
        # end没有后继结点
        if not G.G[i].firstEdge:
            return i
# 初始化入度
def initialInDegree(G):
    inDegree = [0]*G.Nv
    for i in range(G.Nv):
        next_ = G.G[i].firstEdge
        while next_:
            inDegree[next_.adjV]+=1
            next_ = next_.next_
    return inDegree

# 从拓扑排序改进可得
def getTime(G):
    inDegree = initialInDegree(G)
    queue = SQueue(G.Nv)
    earlistTime = [0]*G.Nv
    count = 0
    for i in inDegree:
        if i==0:
            queue.addQ(i)
    while not queue.is_empty():
        v = queue.deleteQ()
        count+=1
        # 处理v的邻接点
        next_ = G.G[v].firstEdge
        while next_:
            # 度减1
            inDegree[next_.adjV] -=1
            if inDegree[next_.adjV]==0:
                queue.addQ(next_.adjV)

            # time更新
            if earlistTime[v]+next_.weight>earlistTime[next_.adjV]:
                earlistTime[next_.adjV] = earlistTime[v]+next_.weight
            next_ = next_.next_
    if count<G.Nv:
        return None
    else:
        return earlistTime[getEnd(G)]


if __name__ == '__main__':
    G = buildGraphFrom0() # 有向图
    time = getTime(G)
    result = time if time else 'Impossible'
    print result
