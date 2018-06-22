#encoding:utf-8
'''
PTA 排名
1.统计， 更新即可O(N)
2.排序，基数排序，次位优先

# 代码量还是挺足的。。。
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


'''
from utils.readList import readList
def sum_(list, K):
    # 若提交的都没通过编译/一个都没提交， 舍弃
    # 也就是说除了-1和-没有别的了
    # TODO 规则不清晰，待完善
    result = '-'
    for i in range(K):
        if list[i]!='-':
            if result=='-':
                result = list[i]
            else:
                result += list[i]
    return result

def count_(list, perfectScore, K):
    count__ = 0
    for i in range(K):
        if list[i] == perfectScore[i]:
            count__+=1
    return count__



# 头结点
class HeadNode:
    def __init__(self,head=None, tail=None):
        self.head = head
        self.tail = tail
# 元素结点
class Node:
    def __init__(self, score=None, count_=None, next_=None):
        self.score = score
        self.count_ = count_
        self.next_ = next_



if __name__ == '__main__':

    # 伪码，一个个实现下边的方法就好了。。。。改天再写了
    # read
    # static
    # bucket1
    # bucket2
    # print

    desc = readList()
    N = desc[0]
    K = desc[1]
    M = desc[2]
    # 初始化
    users = [['-','-','-','-'] for i in range(N)]

    perfectScore = readList()

    # 读入数据
    while M:
        submission = readList()
        if users[submission[0]][submission[1]]=='-' or users[submission[0]][submission[1]] < submission[2]:
            users[submission[0]][submission[1]] = submission[2]
    # 统计
    userStatic = [['-', 0] for i in range(N)]
    for i in range(N):
        userStatic[i][0] = sum_(users[i], K)
        userStatic[i][1] = count_(users[i])
        # 统计完成，次位优先开始排序
        # 未提交/未通过编译的不参与排序
        #1. 总分
        #2. 满分个数
        #3. id


    nodeList = None
    for i in range(N):
        node = Node(userStatic[0], userStatic[1])
        node.next_ = nodeList
        nodeList = node

    # 按满分个数建桶，分配

    B_ = []
    for i in range(K):
        B_.append(HeadNode())
    # 分配
    while nodeList:
        p = nodeList
        if B[p.count_].head:
            B[p.count_].tail.next_ = p
            B[p.count_].tail = p
        else:
            B[p.count_].head = B[p.count_].tail = p
        nodeList = nodeList.next_

    # 重新收集
    for i in range(K-1, -1, -1):
        if B[i].front:
            # 整桶收集
            B[i].tail.next_ = nodeList
            nodeList = B[i].front

    # 继续总分建桶
    top = getTop(perfectScore, K)
    B = []
    for i in range(top):
        B.append(HeadNode())

    # 分配
    while nodeList:
        p = nodeList
        if B[p.score].head:
            B[p.score].tail.next_=p
            B[p.score].tail=p
        else:
            B[p.score].head = B[p.score].tail = p
        nodeList = nodeList.next_

    # 输出
    printMy # 一个桶内的rank是一样的。。。