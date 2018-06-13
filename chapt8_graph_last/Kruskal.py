#encoding:utf-8
'''
kruskal:
    适用稀疏图 O（ElogE）

    森林合并成树，利用最小堆从边集中挑选最小边
    并查集知识判断是否有回路，如加入形成回路，则原来的结点一定是同一个集合

'''

# 伪码描述
def Kruskal():
    while Ecount<Nv-1 and not edgeHeap.isEmpty:
        e = deleteMinEdge()
        if not isLoop(tree, e):
            tree.insertEdge(e)

    if Ecount<Nv-1:
        Error('生成树不存在')
        Error('图不连通')

##########################
## 图稀疏时有优势，故原图用邻接表表示
from chapt6_graph_first.LGraph import GNode, Edge

def initialVSet(Nv):
    return [-1]*Nv
INFINITE = float('-inf')
def initialESet(G, Nv):
    # 用数组将边存起来，然后再进行调整
    # eSet[0]存放的是无穷小
    eSet = [INFINITE]
    eCount = 0
    for i in range(Nv):
        v = G.G[i].firstEdge
        while not v:
            # 避免重复收录无向图的边, 只收录v1<v2的边
            if i < v.adjV:
                e = Edge(i, v.adjV, v.weight)
                eSet.append(e)
                eCount+=1
            v = v.next_
    return eSet, eCount

def percDown(eSet, i, N):
    tempE = eSet[i]
    temp = tempE.weight
    parent = i
    while 2*parent<=N: # 还有子节点
        child = 2*parent
        if child<N and eSet[child+1].weight<eSet[child].weight:
            child = child+1
        # child是小子节点
        if temp<eSet[child].weight:
            # 结点上浮
            eSet[parent] = eSet[child]
            # 开始递归
            parent = child
        else:
            # 找到正确的位置parent
            break
    eSet[parent] = tempE

def buildMinHeap(G, Nv):
    eSet, eCount = initialESet(G, Nv)
    # 调整算法，如果结点的左右子树都是堆，那么只要调整该结点就可以使该树成为堆，从最后一个有子节点的开始
    for i in range(eCount/2, 0, -1):
        percDown(eSet, i, eCount)
    return eSet
# 删除根节点
def deleteMin(eSet):
    N = len(eSet)
    if N<=1:
        return None
    minE = eSet[1]
    eSet[1] = eSet[N]
    eSet.pop(N)
    percDown(eSet, 1, N-1)
    return minE

def find(S, v):
    if S[v]<0:
        return v
    else:
        S[v] = find(S, S[v])
        return S[v]

def isLoop(vSet, e):
    #检测e的两个端点是否是同一个集合
    root1 = find(vSet, e.V1)
    root2 = find(vSet, e.V2)
    return True if root1==root2 else False

def union(S, v1, v2):
    # 小集合并入大集合
    if S[root1]<S[root2]:
        S[root2] = root1
        S[root1]+=S[root2]
    else:
        S[root1] = root2
        S[root2]+=S[root1]
    return True



def Krustkal(G):
    # 初始化
    Ecount = 0
    totalWeight = 0
    Nv = G.Nv
    tree = GNode(Nv)
    vSet = initialVSet(Nv)
    eSet = buildMinHeap(G, Nv)
    while Ecount<Nv-1:
        e = deleteMin(eSet) # 还有一种方法，依次将最值从数组右端开始存储，不过需要从0开始存储
        if not e:
            break
        if not isLoop(vSet, e):
            # 合并
            union(vSet, e.V1, e.V2)
            tree.insertEdge(e)
            totalWeight+=e.weight
            Ecount+=1
    if Ecount<Nv-1:
        return False
    else:
        return tree




