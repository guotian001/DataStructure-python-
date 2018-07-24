#encoding:utf-8
'''
电话狂人：

hash思想：
    1.创建hash表
    2.读入数据
    3.扫描输出

分离链接法

'''
class LNode:
    def __init__(self):
        self.data = None
        self.count = 0
        self.next_ = None

class HashTable:
    def __init__(self):
        self.tableSize = 0
        self.heads = None

from chapt11_hash_find.NextPrime import nextPrime
def createTable(tableSize):
    tableSize = nextPrime(tableSize)
    table = HashTable()
    table.tableSize = tableSize
    table.heads = [LNode() for i in range(tableSize)]
    return table

# 获取电话号码的后5位并转为数字
def getLast5(key):
    return int(key[-5:])

def find(key, table):
    pos = myHash(getLast5(key), table.tableSize)
    p = table.heads[pos].next_ # 第一个结点
    while p and p.data!=key:
        p = p.next_
    return p # p可能是正确的，也可能是none

def insert(key, table):
    p = find(key, table)
    if not p:
        # 插入 到第一个位置
        pos = myHash(getLast5(key), table.tableSize)
        node = LNode()
        node.data = key
        node.count = 1

        node.next_ = table.heads[pos].next_
        table.heads[pos].next_ = node
        return True
    else:
        p.count += 1
        return False


def myHash(key, size):
    return key%size


# 找到次数最多的最小号码
# 穷历
def scanAndOutput(table):
    minPhone = None
    maxCnt = PNum = 0
    # PNum = 1  这种写法是错误的，因为后面的maxCnt不是最终的cnt
    p = None
    for i in range(table.tableSize):
        p = table.heads[i].next_
        while p:
            if p.count > maxCnt:
                maxCnt = p.count
                minPhone = p.data
                # 每更新一次maxCnt，PNum也需要重置(新的maxCnt)
                PNum = 1

            elif p.count == maxCnt:
                PNum += 1
                if p.data < minPhone:
                    minPhone = p.data
            p = p.next_

    # 输出
    if PNum == 1:
        print minPhone, maxCnt
    else:
        print minPhone, maxCnt, PNum



'''
4
13005711862 13588625832
13505711862 13088625832
13588625832 18087925832
15005713862 13588625832

13588625832 3
'''
if __name__ == '__main__':

    N = input()
    table = createTable(2*N)

    for i in range(N):
        pair = raw_input().strip().split()
        insert(pair[0], table)
        insert(pair[1], table)

    scanAndOutput(table)
