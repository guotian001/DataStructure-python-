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

def save007(G, length):
    visited = [False]*G.Ncrocodiles
    answer = False
    for i in range(G.Ncrocodiles):
        if not visited[i] and firstJump(G.islandRadius, G.crocodiles[i], length):
            answer = DFS(i, visited, length, G)
            if answer:
                break
    print 'Yes' if answer else 'No'

# 判断是否可以从岛上跳过去
def firstJump(radius, crocodile, length):
    return math.sqrt(pow(crocodile[0], 2)+pow(crocodile[1], 2)) - radius <= length

# 修改过后的dfs
def DFS(v, visited, lenght, G):
    # 先检验是否能够从该鳄鱼跳到岸上
    if isSafe(G.crocodiles[v],G.border,  lenght):
        return True
    else:
        # 遍历跳跃
        for i in range(G.Ncrocodiles):
            if not visited[i] and jump(G.crocodiles[v], G.crocodiles[i], lenght):
                visited[i]=True
                answer = DFS(i, visited, lenght, G)
                if answer:
                    return answer
def isSafe(crocodile, border, lenght):
    return border - abs(crocodile[0]) <= lenght or border - abs(crocodile[1]) <= lenght
def jump(crocodile1, crocodile2, length):
    return math.sqrt(pow(crocodile1[0]-crocodile2[0], 2)+pow(crocodile1[1]-crocodile2[1], 2))<= length


############# test ################
'''
14 20
25 -15
-25 28
8 49
29 15
-35 -2
5 28
27 -29
-8 -28
-20 -35
-25 -20
-13 29
-30 15
-35 40
12 12

Yes


4 13
-12 12
12 12
-12 -12
12 -12

No
'''
def readList():
    desc = raw_input()
    return map(int,  desc.strip().split())

def test():
    desc_list = readList()
    N = desc_list[0]
    D = desc_list[1]
    locations = []
    for i in range(N):
        locations.append(readList())
    g = Graph(50, 15/2.0, N, locations)
    save007(g,D)

test()

