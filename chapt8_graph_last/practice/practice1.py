# encoding:utf-8
'''
公路村村通问题，
    其实就是最小生成树的问题
    M（≤3N），稀疏图，显然用kruskal合适点
'''

'''
6 15
1 2 5
1 3 3
1 4 7
1 5 4
1 6 2
2 3 4
2 4 6
2 5 2
2 6 6
3 4 6
3 5 1
3 6 1
4 5 10
4 6 8
5 6 3

12
'''
from utils.buildGraph import buildGraphFrom1
from chapt6_graph_first.LGraph import GNode, Edge

# def Kruskal(G):
#     heap = buildHeap()
#     tree = GNode(G.Nv)
#     Ne = G.Ne
#     eCount = 0
#     # 循环，直到没有边或者达到形成树为止
#     while eCount<Ne
from chapt8_graph_last.Kruskal import Krustkal
if __name__ == '__main__':
    G = buildGraphFrom1()

    tree,cost = Krustkal(G)
    print cost
