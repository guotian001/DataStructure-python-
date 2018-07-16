#encoding:utf-8
'''
开放定址法：平方探测法
'''
MAX_TABLE_SIZE = 100000 # 允许开辟的最大散列表长度
Legitimate = 1
Empty = 2
Deleted = 3

class Cell:
    def __init__(self):
        self.data = None
        self.info = Empty

class HashTable:
    def __init__(self):
        self.tableSize=0
        self.cells = None
from NextPrime import nextPrime
def createTable(tableSize):
    tableSize = nextPrime(tableSize)
    table = HashTable()
    table.tableSize = tableSize
    table.cells = [Cell() for i in range(tableSize)]
    return table
def myHash(key, size):
    return key%size

def find(key, table):
    pos = calPos = myHash(key, table.tableSize)
    CNum = 0
    # 平方探测法
    while table.cells[pos].info!=Empty and table.cells[pos].data!=key: # 冲突
        CNum+=1
        if CNum%2:
            pos = calPos + (CNum+1)/2*(CNum+1)/2
        else:
            pos = calPos - CNum/2*CNum/2

        pos%=table.tableSize
    return pos

def myFind(key, table):
    pos = find(key, table)
    if table.cells[pos].info==Legitimate:
        print '元素 %d 查找成功, index: %d' % (key, pos)
    else:
        print '元素 %d 不存在' % key

''' 不能物理删除，需要占位 '''
def delete(key, table):
    pos = find(key, table)
    if table.cells[pos].info==Legitimate:
        table.cells[pos].info = Deleted
        return True
    else:
        print '元素 %d 不存在' % key
        return False

def insert(key, table):
    pos = find(key, table)
    if table.cells[pos].info==Legitimate:
        print '元素 %d 已存在' % key
        return False
    else:
        table.cells[pos].data = key
        table.cells[pos].info = Legitimate
        return True


