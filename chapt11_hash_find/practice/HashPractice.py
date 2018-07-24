#encoding:utf-8
'''
简化版的开放定址法，二次探测

只能增加的平方探测

'''
from math import sqrt
def nextPrime(M):
    M = M if M%2 else M+1
    while True:
        for i in range(int(sqrt(M)), 1, -1):
            if not M%i: # 不是素数
                break
        if i==2:
            break
        else:
            M+=2
    return M

class HashTable:
    def __init__(self):
        self.size = 0
        self.list = None
def createTable(M):
    size = nextPrime(M)
    table = HashTable()
    table.size = size
    table.list = [None]*size
    return table

def myHash(data, size):
    return data%size

def insert(data, table):
    CCnt = 0
    pos = calPos = myHash(data, table.size)

    while table.list[pos]!=None:
        CCnt+=1
        pos = calPos+CCnt*CCnt
        if pos>table.size-1:
            return '-'

    table.list[pos] = data
    return pos

def printList(L):
    for i in L:
        print i,

'''
4 4
10 6 4 15


0 1 4 -
'''
from utils.readList import readList
if __name__ == '__main__':

    desc = readList()
    M = desc[0]
    N = desc[1]
    datas = readList()
    poss = []

    # 创建hash表
    table = createTable(M)
    # 插入数据
    for i in range(N):
        pos = insert(datas[i], table)
        poss.append(pos)
    # 输出位置信息
    printList(poss)
