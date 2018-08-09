#encoding:utf-8
'''
基数排序：基数指的是进制，适合N<<M时，根据进制建桶
次位优先/主位优先

大多数情况下，次位优先要比主位优先快，但是，特殊情形：次位基本相同，只有主位才体现出不同来，显然主位优先快（实际上每种方法都有自己擅长的情境，只不过有些情境的出场率较高罢了）
'''
# 基数排序，次位优先
# /* 假设元素最多有MaxDigit个关键字，基数全是同样的Radix */
Radix = 10
MaxDigit = 4

# 头结点
class HeadNode:
    def __init__(self,head=None, tail=None):
        self.head = head
        self.tail = tail
# 元素结点
class Node:
    def __init__(self, value=None, next_=None):
        self.value = value
        self.next_ = next_


def getDigit(value, Di):
    # 降位，求余
    temp = 1
    for i in range(1, Di):
        temp*=Radix
    value/=temp
    return value%Radix



def LSDRadixSort(list, N):
    # 初始化桶
    B = []
    for i in range(Radix):
        B.append(HeadNode())

    # list存起来，避免不停的创建结点
    nodeList = None
    for i in list:
        node = Node(i)
        node.next_ = nodeList
        nodeList = node

    for Di in range(1, MaxDigit+1): # 位数
        # 分配

        while nodeList:
            # 从链表中摘一个
            node = nodeList
            nodeList = node.next_
            node.next_ = None

            d = getDigit(node.value, Di)
            # 无空头结点
            if B[d].head:
                B[d].tail.next_ = node
                B[d].tail = node
            else: # 为空
                B[d].head = B[d].tail = node


        # 收集
        for i in range(Radix-1, -1, -1):
            if B[i].head:
                # 整桶插入
                B[i].tail.next_ = nodeList
                nodeList = B[i].head
                # 清空桶
                B[i].head = B[i].tail = None
    # 倒回
    while nodeList:
        list[i] = nodeList.value
        i+=1
        nodeList = nodeList.next_

if __name__ == '__main__':
    list = [64, 8, 216, 512, 27, 729, 0, 1, 343, 125]
    LSDRadixSort(list, len(list))
    print list
