#encoding:utf-8
'''
PTA 排名
1.统计， 更新即可O(N)
2.排序，基数排序，次位优先

# 代码量还是挺足的。。。

# 提纲掣领，要有个提纲。。。
'''


'''
7 4 20
20 25 25 30
00002 2 12
00007 4 17
00005 1 19
00007 2 25
00005 1 20
00002 2 2
00005 1 15
00001 1 18
00004 3 25
00002 2 25
00005 3 22
00006 4 -1
00001 2 18
00002 1 20
00004 1 15
00002 4 18
00001 3 4
00001 4 2
00005 2 -1
00004 2 0


1 00002 63 20 25 - 18
2 00005 42 20 0 22 -
2 00007 42 - 25 - 17
2 00001 42 18 18 4 2
5 00004 40 15 0 25 -


'''
from utils.readList import readList
def sumAndCount(list, K, perfectScore):
    # 若提交的都没通过编译/一个都没提交， 统计时舍弃
    # -1 编译不通过 - 未提交，计分的时候-1按0分算
    result = 0
    WrongCount = 0
    perfectCount = 0
    for i in range(K):
        if list[i]==-1: # -1仅仅是个标识，具体统计的时候并不扣分，按0分算
            WrongCount+=1
            list[i]=0
        elif list[i]=='-':
            WrongCount+=1
        else:
            result+=list[i]
            if list[i]==perfectScore[i]:
                perfectCount+=1

    result =  result if WrongCount!=4 else -2 # -2:不展示标识
    return result, perfectCount




# 头结点
class HeadNode:
    def __init__(self,head=None, tail=None):
        self.head = head
        self.tail = tail
# 元素结点
class Node:
    def __init__(self, index=None, score=None, count_=None, next_=None):
        self.index = index
        self.score = score
        self.count_ = count_
        self.next_ = next_



def readData():
    desc = readList()
    N = desc[0]
    K = desc[1]
    M = desc[2]

    # 初始化
    users = [['-', '-', '-', '-'] for i in range(N)]

    perfectScore = readList()

    # 读入数据
    while M:
        submission = readList()
        submission[0]-=1
        submission[1]-=1
        if users[submission[0]][submission[1]] == '-' or users[submission[0]][submission[1]] < submission[2]:
            users[submission[0]][submission[1]] = submission[2]
        M-=1

    return users, N, K, perfectScore

def doStatic(users, N, K):
    # 统计
    # 总分满分个数
    userStatic = [[0, 0] for i in range(N)]

    for i in range(N):
        userStatic[i][0], userStatic[i][1]= sumAndCount(users[i], K, perfectScore)
    return userStatic

'''

1 00002 63 20 25 - 18
'''
def doPrint(B, top, users, K):
    rank = 0
    for i in range(top-1, -1, -1):
        if B[i].head:
            rank+=1
            node = B[i].head
            while node:
                print '%d %05d %d' % (rank, node.index+1, node.score),
                for i in range(K):
                    print users[node.index][i],
                print
                node = node.next_

def getTop(perfectScore, K):
    result = 0
    for i in range(K):
        result+=perfectScore[i]
    return result

def BucketSortAndPrint(users, N, K, perfectScore, userStatic):
    # 统计完成，次位优先开始排序
    # 未提交/未通过编译的不参与排序
    # 1. 总分
    # 2. 满分个数
    # 3. id
    # bucket1
    # 需要一个id正序的list，表示按id排序
    nodeList = pre = Node(0, userStatic[0][0], userStatic[0][1])

    for i in range(1, N):
        node = Node(i, userStatic[i][0], userStatic[i][1])
        pre.next_ = node
        pre = node

    # 按满分个数建桶，分配
    B = []
    for i in range(K):
        B.append(HeadNode())
    # 分配
    while nodeList:
        p = nodeList
        nodeList = nodeList.next_
        p.next_=None
        if B[p.count_].head:
            B[p.count_].tail.next_ = p
            B[p.count_].tail = p
        else:
            B[p.count_].head = B[p.count_].tail = p

    # 重新收集，应该满分个数降序排列，即大的在前
    for i in range(K):
        if B[i].head:
            # 整桶收集
            B[i].tail.next_ = nodeList
            nodeList = B[i].head

    # bucket2
    # 继续总分建桶
    top = getTop(perfectScore, K)
    B = []
    for i in range(top):
        B.append(HeadNode())

    # 分配
    while nodeList:
        p = nodeList
        nodeList = nodeList.next_
        p.next_ = None
        if p.score >= 0:  # 不展示的直接abandon
            if B[p.score].head:
                B[p.score].tail.next_ = p
                B[p.score].tail = p
            else:
                B[p.score].head = B[p.score].tail = p

    # 输出
    doPrint(B, top, users, K)  # 一个桶内的rank是一样的。。。


if __name__ == '__main__':

    # 伪码，一个个实现下边的方法就好了。。。。改天再写了
    # read
    users, N, K, perfectScore = readData()
    # static
    userStatic = doStatic(users, N, K)

    BucketSortAndPrint(users, N, K, perfectScore, userStatic)