# encoding:utf-8
'''
旅游规划
'''
INFINITE = float('inf')

class Edge:
    def __init__(self, v1, v2, weight=1, cost=0):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight
        self.cost = cost

class GNode:
    def __init__(self, Nv = 0):
        self.Nv = Nv
        self.Ne = 0
        self.G = [[INFINITE]*Nv for i in range(Nv)]
        self.cost = [[INFINITE]*Nv for i in range(Nv)]

    def insertEdge(self, e):
        self.G[e.v1][e.v2] = e.weight
        self.cost[e.v1][e.v2] = e.cost

        self.G[e.v2][e.v1] = e.weight
        self.cost[e.v2][e.v1] = e.cost



def readList():
    desc = raw_input()
    return map(int,  desc.strip().split())


def findMinDistNotCollected(dist, N, collected):
    min_ = INFINITE
    index = -1
    for i in range(N):
        if not collected[i] and dist[i]<min_:
            min_ = dist[i]
            index = i
    if index==-1:
        return None
    else:
        return index

def dijkstra(s,N, G):
    collected = [False]*N
    path = [-1]*N
    dist = [INFINITE]*N
    cost = [INFINITE]*N
    # 初始化
    collected[s] = True
    for i in range(N):
        if g.G[s][i]<INFINITE: # 邻接点
            dist[i] = g.G[s][i]
            cost[i] = g.cost[s][i]
            path[i] = s

    # 算法开始
    while True:
        v = findMinDistNotCollected(dist, N, collected)
        if not v:
            break
        collected[v] = True
        # 对v的邻接点更新dist
        for i in range(N):
            if not collected[i] and g.G[v][i]<INFINITE:
                if g.G[v][i]<0:
                    return False
                if dist[v]+g.G[v][i]<dist[i]:
                    dist[i] = dist[v]+g.G[v][i]
                    cost[i] = cost[v]+g.cost[v][i]
                    path[i] = v
                elif dist[v]+g.G[v][i]==dist[i] and cost[v]+g.cost[v][i]<cost[i]: # 等于也可能更新
                   # 如果可以减少过路费的话
                    cost[i] = cost[v] + g.cost[v][i]
                    path[i] = v
    return dist, cost


'''
4 5 0 3
0 1 1 20
1 3 2 30
0 3 4 10
0 2 2 20
2 3 1 20

3 40
'''


if __name__ == '__main__':
    desc = readList()

    N = desc[0]
    M = desc[1]
    S = desc[2]
    D = desc[3]


    # buildGraph
    g = GNode(N)
    g.Ne = M
    while M:
        e_list = readList()
        g.insertEdge(Edge(e_list[0], e_list[1], e_list[2], e_list[3]))
        M-=1

    dist, cost = dijkstra(S, N, g)
    print dist[D],
    print cost[D]

