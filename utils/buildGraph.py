#encoding:utf-8
from utils.readList import readList
from chapt6_graph_first.LGraph import GNode, Edge
def buildGraphFrom1():
    desc = readList()
    N = desc[0]
    M = desc[1]
    # 新建图
    G = GNode(N)
    G.Ne = M
    while M:
        eList = readList()
        G.insertEdge(Edge(eList[0] - 1, eList[1] - 1, eList[2]))
        M -= 1
    return G

def buildGraphFrom0():
    desc = readList()
    N = desc[0]
    M = desc[1]
    # 新建图
    G = GNode(N)
    G.Ne = M
    while M:
        eList = readList()
        # 有向图
        G.insertEdgeDirect(Edge(eList[0], eList[1], eList[2]))
        M -= 1
    return G