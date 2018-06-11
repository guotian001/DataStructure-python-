# encoding:utf-8
'''

拯救007
'''

import math
class Graph:
    def __init__(self, border=0, islandRadius=0,Ncrocodiles = 0,crocodiles=None):
        self.border=border
        self.islandRadius = islandRadius
        self.Ncrocodiles = Ncrocodiles
        self.crocodiles = crocodiles # 数组中存放数组坐标
from chap2_linearTable.LStack import LStack
def save007(G, length):
    visited = [False]*G.Ncrocodiles
    path = [-1]*G.Ncrocodiles
    answer = 0
    for i in range(G.Ncrocodiles):
        if not visited[i] and firstJump(G.islandRadius, G.crocodiles[i], length):
            visited[i] = True
            path[i] = -1 # 从岛上开始跳
            answer = DFS(i, visited, length, G, path)
            if answer:
                break
    # 打印
    if answer:
        printPath(path, answer, G.crocodiles)
    else:
        print 0

def printPath(path, v, crocodiles):
    stack = LStack()
    while True:
        stack.push(v)
        if path[v]==-1:
            break
        else:
            v = path[v]
    route = []
    while not stack.is_empty():
        route.append(stack.pop())
    print len(route)+1
    for i in route:
        print crocodiles[i]


# 判断是否可以从岛上跳过去
def firstJump(radius, crocodile, length):
    return math.sqrt(pow(crocodile[0], 2)+pow(crocodile[1], 2)) - radius <= length

# 修改过后的dfs
def DFS(v, visited, lenght, G, path):
    # 先检验是否能够从该鳄鱼跳到岸上
    if isSafe(G.crocodiles[v],G.border,  lenght):
        return v
    else:
        # 遍历跳跃
        for i in range(G.Ncrocodiles):
            if not visited[i] and jump(G.crocodiles[v], G.crocodiles[i], lenght):
                visited[i]=True
                path[i] = v
                answer = DFS(i, visited, lenght, G, path)
                if answer: # 如果可以出去就直接出去，否则，继续循环
                    return answer
        return 0 # 不能出去
def isSafe(crocodile, border, lenght):
    return border - abs(crocodile[0]) <= lenght or border - abs(crocodile[1]) <= lenght
def jump(crocodile1, crocodile2, length):
    return math.sqrt(pow(crocodile1[0]-crocodile2[0], 2)+pow(crocodile1[1]-crocodile2[1], 2))<= length


############# test ################
'''
17 15
10 -21
10 21
-40 10
30 -50
20 40
35 10
0 -10
-25 22
40 -40
-30 30
-10 22
0 11
25 21
25 10
10 10
10 35
-30 10

4
0 11
10 21
10 35

------------


4 13
-12 12
12 12
-12 -12
12 -12


0
'''
def readList():
    desc = raw_input()
    return map(int,  desc.strip().split())

if __name__ == '__main__':
    desc_list = readList()
    N = desc_list[0]
    D = desc_list[1]
    locations = []
    for i in range(N):
        locations.append(readList())
    g = Graph(50, 15 / 2.0, N, locations)
    save007(g, D)


