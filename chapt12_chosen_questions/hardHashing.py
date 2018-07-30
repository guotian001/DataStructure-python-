#encoding:utf-8
'''
hash和拓扑排序的结合
'''

'''
根据顺序建立图，线性探测冲突比较多，稠密图，用矩阵表示比较合适

某点应该在的位置到他所在的位置上的点都是他的先驱结点，注意模（拐弯）

对该图进行拓扑排序
'''





# 获取度为0 的集合中的最小值， 用最小堆应该是比较合适的，对原来的进行一下改造即可， yeah


def myHash(key, N):
    return key%N

def buildGraph(L, N):
    # 邻接矩阵， 无权图
    G = [[0]*N for i in range(N)]

    # 添加边
    for i in range(N):
        if L[i]>=0:
            calPos = myHash(L[i], N)
            if calPos<i:
                for j in range(calPos, i):
                    G[j][i] = 1
            elif calPos>i:
                for j in range(calPos, i+N):
                    G[j%N][i] = 1
    return G

def initialIndegree(G, list, N):
    degrees = []
    idx = []
    for i in range(N):
        degree = 0
        if list[i]<0:
            degree = -1
        else:
            for j in range(N):
               if G[j][i]>0:
                   degree+=1

        degrees.append(degree)

        if degree==0:
            idx.append(i)

    return degrees, idx

from chapt5_tree_last.Heap import Heap
def topSort(G, list, N):
    degrees, idx = initialIndegree(G, list, N)
    list0 = [-list[i] for i in idx]
    result = []
    # 利用最小堆
    # 最小堆最大堆的转换，添加负号就好了
    heap = Heap(N)
    heap.buildHeap(list0)

    while not heap.isEmpty():
        data = heap.deleteMax()
        result.append(data)
        # 最好的方法是改进堆，传进去的是带下标的结点数据
        # 相邻结点入度-1
        pos = list.index(-data)
        for i in range(N):
            if G[pos][i]>0: # 邻接点
                degrees[i]-=1
                if degrees[i]==0:
                    heap.insert(-list[i])

    return result



'''
11
33 1 13 12 34 38 27 22 32 -1 21

------------
1 13 12 21 33 34 38 27 22 32

'''
def printList(list):
    for i in list:
        print -i,

from utils.readList import readList
if __name__ == '__main__':
    N = input()
    list = readList()
    G = buildGraph(list, N)
    listSorted = topSort(G, list, N)
    printList(listSorted)

