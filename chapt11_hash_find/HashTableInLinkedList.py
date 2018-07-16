#encoding:utf-8
'''
分离链接法
'''
class LNode:
    def __init__(self):
        self.data = None
        self.next_ = None

class HashTable:
    def __init__(self):
        self.tableSize = 0
        self.heads = None

from NextPrime import nextPrime
def createTable(tableSize):
    tableSize = nextPrime(tableSize)
    table = HashTable()
    table.tableSize = tableSize
    table.heads = [LNode() for i in range(tableSize)]
    return table


def find(key, table):
    pos = myHash(key, table.tableSize)
    p = table.heads[pos].next_ # 第一个结点
    while p and p.data!=key:
        p = p.next_
    return p # p可能是正确的，也可能是none

def insert(key, table):
    p = find(key, table)
    if not p:
        # 插入 到第一个位置
        pos = myHash(key, table.tableSize)
        node = LNode()
        node.data = key

        node.next_ = table.heads[pos].next_
        table.heads[pos].next_ = node
        return True
    else:
        print '键值已存在'
        return False


def myHash(key, size):
    return key%size

def delete(key, table):
    p = find(key, table)
    if p:

        pos = myHash(key, table.tableSize)
        pre = table.heads[pos]
        while pre.next_ and pre.next_.data!=key:
            pre = pre.next_

        # 找到了(pre.next_即为p)，删除
        pre.next_ = pre.next_.next_
        return True
    else:
        print '键值不存在'
        return False


##################
if __name__ == '__main__':
    # 47, 7, 29, 11, 16, 92, 22, 8, 3, 50, 37, 89, 94, 21
    table = createTable(11)
    insert(47, table)
    insert(7, table)
    insert(29, table)
    insert(11, table)
    insert(16, table)
    insert(92, table)
    insert(22, table)
    insert(8, table)
    insert(3, table)
    insert(50, table)
    insert(37, table)
    insert(89, table)
    insert(94, table)
    insert(21, table)
    print '-------------'
    print find(21, table)

    print delete(21, table)
    print '--------'