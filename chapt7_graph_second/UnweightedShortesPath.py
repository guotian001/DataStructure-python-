#encoding:utf-8
'''
无权图的单源最短路径
'''
from chapt6_graph_first.LGraph import LGraph
from chapt6_graph_first.SQueue import SQueue

# dist， path 是初始化为-1的数组
def unweighted(G, v, dist, path):
    queue = SQueue(G.Nv)
    queue.addQ(v)
    dist[v] = 0
    while not queue.is_empty():
       node = queue.deleteQ()
       # 遍历node的邻接点
       curr = G.G[node].firstEdge
       while curr:
           if dist[curr.adjV] == -1:
               dist[curr.adjV] = dist[node]+1
               queue.addQ(dist[curr.adjV])
               path[curr.adjV] = node
           curr = curr.next_

from chap2_linearTable import LStack
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


