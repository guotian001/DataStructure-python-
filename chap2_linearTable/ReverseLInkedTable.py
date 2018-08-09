#encoding:utf-8
'''
    https://blog.csdn.net/songyunli1111/article/details/79416684
    思路很简单，关键是要理清
    old指向旧链的头，new指向新链的头
    ！！！！PS： 不要吝啬局部变量，真的不占空间，如果他们可以让问题更明确，更清晰的话
'''
class Node:
    def __init__(self, elem, next_ = None):
        self.elem = elem
        self._next = next_
'''
    可以直接用头结点来代表一条链表，如果不经常在头尾进行操作的话，
    这里使用头结点来代表一条链
    
    这样表示简洁清爽的多，不用像多项式加法中那样，全是点来点去，反而不够直观，不如直接就将头代表该链
'''
def reverse(head):
    if not head:
        return None
    new = None # 新链头
    old = head # 旧链头
    while old:
        temp = old._next # 存下旧链头的下个结点，避免丢失
        old._next = new # 旧链的头 更新到新链上
        new = old # 更新两个头
        old = temp
    return new
'''
    递归实现，将第一个结点后面的看成一个新的链，对其递归(先将这些rest排好)
    注意一点，反转后第一个结点的前驱就是原链中的second，也就是新链的头，也就是说剩下的结点组成的新链反转后的尾是second，就是原来的头
    递归：描述清楚，合理，解交给计算机
     ①先递归，再处理该（先把情形假设为已知）；②先处理该，再递归（正常思路）
'''
# ①
def reverseInRecursion(head):
    if head==None or head._next==None:
        return head # 只有一个结点的话直接return该结点
    second = head._next
    rest = reverseInRecursion(second) # 先将rest递归排列好
    second._next = head # second 就是反转好的rest的尾
    head._next = None
    return rest

######################################################################

'''
00100 6 3
00000 4 99999
00100 1 12309
68237 6 -1
33218 3 00000
99999 5 68237
12309 2 33218


00000 4 33218
33218 3 12309
12309 2 00100
00100 1 99999
99999 5 68237
68237 6 -1


'''

class AddressNode:
    def __init__(self, address, elem, next_ = None):
        self.address = address
        self.elem = elem
        self._next = next_


def readList():
    desc = raw_input()
    return map(int,  desc.strip().split())

# 返回一条链，头结点
def read():
    desc_list = readList()
    headAddress = desc_list[0]
    N = desc_list[1]
    K = desc_list[2]
    nodeDict = {}
    while N:
        nodeList = readList()
        nodeDict[nodeList[0]] = AddressNode(nodeList[0], nodeList[1], nodeList[2])
        N -= 1
    return dict2list(nodeDict, headAddress), K

def dict2list(dict, headAddress):
    head = dict[headAddress]
    p = head
    while p:
        p._next = dict.get(p._next) # 将next改为对象
        p = p._next
    return head

def printList(head):
    while head:
        next = head._next.address if head._next else -1
        if next == -1:
            print '%05d %d %d' %(head.address, head.elem, next)
        else:
            print '%05d %d %05d' %(head.address, head.elem, next)
        head = head._next


# 递归实现，不要太帅哦，算法中应该是经常使用的，毕竟描述是简单的，方程思想解放了很多应用题
# ②
def reverseWithK(head, K):
    # 递归
    # 找到k个，reverse
    # 对剩下的递归
    # head 接 rest的head
    if not head:
        return None # 递归出口1
    p = head
    i = 1
    while i < K and p:
        p = p._next
        i += 1
    if not p: # 小于k个，直接返回
        return head # 递归出口2
    else: # p指向第k个结点
        rest = p._next # 将剩下的链看做一个新的
        p._next = None # 将前k个作为一条单独的链反转
        new = reverse(head)
        new_rest = reverseWithK(rest, K) # 显然剩下的是个规模缩小了的同类问题，因此毫无疑问递归之
        head._next = new_rest # 将反转后的两条链连在一起，head为前k个链的反转后的尾
        return new




def main():
    head, k = read()
    new = reverseWithK(head,k)
    printList(new)

main()
