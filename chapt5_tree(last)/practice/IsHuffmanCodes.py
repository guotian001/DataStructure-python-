#encoding:utf-8
'''

    检验是否是哈夫曼编码，
        1.检验cost是否正确
            自己构建一颗树，得出，然后求出二者比较
        2.检验是否含有前缀码
            自己在论坛中回答的思路：根据编码构建结点（初始结点设为0，表示非编码结点），如果是编码结点则，将其频率放进去，结点结构中加上是否是待编码结点的flag
'''

'''
7
A 1 B 1 C 1 D 3 E 3 F 6 G 6
4
A 00000
B 00001
C 0001
D 001
E 01
F 10
G 11
A 01010
B 01011
C 0100
D 011
E 10
F 11
G 00
A 000
B 001
C 010
D 011
E 100
F 101
G 110
A 00000
B 00001
C 0001
D 001
E 00
F 10
G 11

Yes
Yes
No
No


'''

# 自顶向下的书写方法，先类似伪码，需要的方法，可以先定义出来，然后实现之，实现的过程中再对方法的参数进行详细完备的定义。。。

def main():
    N = input()
    dict = readWeight()
    list = dict.values()
    from HuffmanTree import huffmanWithList, wpl
    h = huffmanWithList(list)
    cost = wpl(h)
    M = input()
    result = []
    while M:
        result.append('Yes' if check(dict, cost, N) else 'No')
        M-=1
    for i in range(len(result)):
        print result[i]

def build(code, tree):
    curr = tree
    for i in range(len(code)):
        if curr.flag:
            return False
        if code[i] == '0':
            if not curr.left:
                curr.left = Node()
            curr = curr.left
        else:
            if not curr.right:
                curr.right = Node()
            curr = curr.right
    curr.flag = 1  # curr指向字符结点
    return True


# 根据编码构建一个特殊的树
class Node:
    def __init__(self, flag=0, left=None, right=None):
        self.flag = flag
        self.left = left
        self.right = right
def isPre(codeDict):
    tree = Node()
    for k in codeDict:
        if not build(codeDict[k], tree):
            return True
    return False

def check(dict, cost, N):
    codeDict = readCodes(N)
    cost_curr = getCost(dict, codeDict)
    if cost_curr > cost:
        return False
    # 构建树
    return False if isPre(codeDict) else True

def getCost(dict, codeDict):
    cost = 0
    for k in dict:
        cost+=dict[k]*len(codeDict[k])
    return cost


def readCodes(N):
    codeDict = {}
    while N:
        code = raw_input().strip().split()
        codeDict[code[0]] = code[1]
        N-=1
    return codeDict

def readWeight():
    raw = raw_input().strip().split()
    dict = {}
    for i in range(0,len(raw)-1, 2):
        dict[raw[i]] = int(raw[i+1])
    return dict


main()
