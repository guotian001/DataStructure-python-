#encoding:utf-8
'''
开放定址法
平方探测
'''
MAX_TABLE_SIZE = 100000 # 允许开辟的最大散列表长度
Legitimate = 1
Empty = 2
Deleted = 3


class Cell:
    def __init__(self):
        self.data = None
        self.info = Empty # 状态标识


# 散列表结点的定义
# 实际上是一个结点对象
class HashTable:
    def __init__(self):
        self.tableSize = None
        self.cells = None

#  返回大于等于N且不超过MAXTABLESIZE的最小素数 */
from math import sqrt
def nextPrime(N):
    # 素数一定是奇数，故只考虑奇数
    p = N if N%2 else N+1
    while p<MAX_TABLE_SIZE:
        for i in range(int(sqrt(p)), 1, -1):
            if not p%i: # 不是素数
                break
        # for正常结束的话，说明是素数
        if i==2: # 从平方根直到2
            break
        else:
            p+=2
    return p

def createTable(tableSize):
    table = HashTable()
    tableSize = nextPrime(tableSize)
    table.tableSize = tableSize
    table.cells = [Cell() for i in range(tableSize)]
    return table

# 求余法
def myHash(key, size):
    return key%size

# 在表中查找
# 找到的结果还需自己判断
def find(hashTable, key):
    pos =CalPos =  myHash(key, hashTable.tableSize) # di是在计算出的位置上进行增减操作的
    Cnum = 0 # 冲突次数
    while hashTable.cells[pos].info!=Empty and hashTable.cells[pos].data!=key:
        # 开始探测
        Cnum+=1
        if Cnum%2: # 奇数
            pos = CalPos + (Cnum+1)/2*(Cnum+1)/2
        else:
            pos = CalPos - Cnum/2*Cnum/2

        pos %= hashTable.tableSize
    return pos

def insert(H, key):
    pos = find(H, key)
    if H.cells[pos].info!=Legitimate: # 并未存在
        H.cells[pos].data = key
        H.cells[pos].info = Legitimate
        return True
    else:
        print '键值已存在'
        return False

def delete(H, key):
    pos = find(H, key)
    if H.cells[pos].info!=Legitimate:  # 并未存在
        print '键值不存在'
        return False
    else:
        H.cells[pos].info = Deleted
        return True
def myFind(h, key):
    pos = find(h, key)
    if h.cells[pos].info == Legitimate:
        print '元素 %d 查找成功, index: %d' % (key, pos)
    else:
        print '元素 %d 不存在' % key

if __name__ == '__main__':
    # 47， 7， 29， 11， 9， 84， 54， 20， 30
    h = createTable(11)
    insert(h, 47)
    insert(h, 7)
    insert(h, 29)
    insert(h, 11)
    insert(h, 9)
    insert(h, 84)
    insert(h, 54)
    insert(h, 20)
    insert(h, 30)

    print '----------'


    myFind(h,29)
    delete(h, 29)
    myFind(h,29)