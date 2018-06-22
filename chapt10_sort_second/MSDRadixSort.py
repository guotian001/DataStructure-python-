#encoding:utf-8
'''
主位优先的基数排序
一次之后，桶间有序，对桶内在进行排序，递归，出口，D=1时已经有序，从主到次的顺序，来到了1同一个桶内的各个位数都相等，故递归出口D=0

当然，如果桶内只有一个元素的话也不要再递归了。。。
'''
# 基数排序，主位优先 ，递归
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

def MSD(list, L, R, D):

    # 递归出口，所有位数都走完，或者桶内只有一个元素时
    if D==0 or R-L<1:
        return

    # 初始化桶
    B = []
    for i in range(Radix):
        B.append(HeadNode())
    # 初始化链表
    # LSD 初始化链表是为了避免不停的创建node结点，但是在下面缩写的算法中并不能避免不停的创建，每次创建都只使用了一次，
    # 不如用到的时候再创建
    # nodeList = None
    # for i in range(L, R+1):
    #     temp = Node(list[i])
    #     temp.next_ = nodeList
    #     nodeList = temp

    # 放进桶里
    for i in range(L, R+1):
        Di = getDigit(list[i], D)
        node = Node(list[i])

        node.next_ = B[Di].head
        B[Di].head = node
        # if 是空链表，tail还要更新
        if not B[Di].head:
            B[Di].tail = node

    # while nodeList:
    #     # 摘一个下来
    #     node = nodeList
    #     Di = getDigit(node.value, D)
    #
    #     # 放在头或尾都可以，这里放在头部，方便一点
    #     node.next_ = B[Di].head
    #     B[Di].head = node.next_
    #     # if 是空链表，tail还要更新
    #     if not B[Di].head:
    #         B[Di].tail = node
    #
    #     nodeList = nodeList.next_

    # 桶间有序
    # 按桶收集到list中，对桶内进行递归排序
    l = r = L # 初始化
    for b in range(Radix):
        node = B[b].head
        if node:
            while node:
                # 依次倒回list中
                list[r] = node.value
                r+=1
                node = node.next_
            # 递归
            MSD(list, l, r-1, D-1)
            l=r # 更新左端

def MSDRadixSort(list, N):
    MSD(list, 0, N-1, MaxDigit)


#############################################
if __name__ == '__main__':
    list = [64, 8, 216, 512, 27, 729, 0, 1, 343, 125]
    MSDRadixSort(list, len(list))
    print list
