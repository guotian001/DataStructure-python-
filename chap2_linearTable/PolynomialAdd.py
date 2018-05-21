#encoding:utf-8
class PolyNode:
    def __init__(self, coef=0, expon=0, next_=None):
        self._coef = coef
        self._expon = expon
        self._next = next_

class PolyNomial:
    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear



###########  工具类
def polyNomialAdd(P1, P2):
    # 先创建一个空头结点的链表存储结果，最后可以释放该结点
    front = PolyNode()
    result = PolyNomial(front, front) # 链表首尾都指向该空节点
    sum = 0
    p1F = P1.front
    p2F = P2.front
    while p1F and p2F:
        if p1F._expon > p2F._expon:
            attach(result, p1F._expon, p1F._coef)
            p1F = p1F._next
        elif p1F._expon < p2F._expon:
            attach(result, p2F._expon, p2F._coef)
            p2F = p2F._next
        else:
            sum = p1F._coef + p2F._coef
            if sum:
                attach(result, p1F._expon, sum)
            p1F = p1F._next
            p2F = p2F._next
    while p1F:
        attach(result, p1F._expon, p1F._coef)
        p1F = p1F._next
    while p2F:
        attach(result, p2F._expon, p2F._coef)
        p2F = p2F._next

    result.front = front._next # 去掉空头结点
    return result

def attach(result, expon, coef):
    if coef:
        temp = PolyNode(coef, expon)
        result.rear._next = temp
        result.rear = temp

def readPoly():
    P1_raw = raw_input()
    p1_list = map(int, P1_raw.strip().split())
    s = PolyNode()
    P = PolyNomial(s,s)
    for i in range(1, len(p1_list)-1, 2):
        attach(P, p1_list[i+1], p1_list[i])
    P.front = s._next
    return P
def mult(p1, p2):
    # 构造一个result表
    s = PolyNode()
    result = PolyNomial(s, s)
    if p1.front == None or p2.front == None:
        result.front = s._next
        return result
    p1F = p1.front
    while p1F:
        result.rear = result.front
        p2F = p2.front
        while p2F:
            c = p1F._coef * p2F._coef
            e = p1F._expon + p2F._expon
            if c:
                # insert
                # p1和p2最后一项的乘积一定是在结果的尾部，因此，可用rear来迭代，（省略更新rear的步骤）
                while result.rear._next and result.rear._next._expon > e:  # 找到待插入位置的前一结点, 如果result.rear.next为none，需要知道result.rear
                    result.rear = result.rear._next
                temp = PolyNode(c, e)
                # result.rear.next._expon = e
                positon = result.rear._next
                if positon and positon._expon == e:
                    sum = positon._coef + c
                    if sum:
                        positon._coef = sum
                    else:
                        result.rear._next = positon._next
                # result.rear._next为none
                elif not positon:
                    result.rear._next = temp
                # result.rear.next._expon < e
                elif positon._expon < e:
                    temp._next = positon
                    result.rear._next = temp
                if result.rear._next:# 当rear._next == none时，rear不后移更新，对86行代码而言，有可能将最后的结点删除
                    result.rear = result.rear._next # result.rear更新，因为p2是递减的，因此乘后应该是在该result.rear后面的，没有必要再从头进行遍历了 ！！！！！！！显然但是又容易忽略的。。。

                # 上述两段代码可以合并
                # else:
                #     result.rear._next = temp
                #     temp._next = positon
            p2F = p2F._next

        p1F = p1F._next
    result.front = s._next
    return result




def printPoly(p):
    if p.front == None:
        print '0 0',
    else:
        # flag = 0
        while p.front:
            # if not flag: # 第一个不输出空格,但是为了以后输出空格，需要在此处更改flag的值
            #     flag = 1
            # else:
            #     print ' ',
            print '%d %d'%(p.front._coef, p.front._expon),
            p.front = p.front._next


# 在指数递减的列表中插入一个结点，
# ！！！！！！！！！！！！！需要插入两个结点中间，因此需要找到待插入位置的前一结点，否则就丢掉了
# def insert(p, c, e):
#
#     while pre._next and pre._next._expon > e: # 找到待插入位置的前一结点, 如果pre.next为none，需要知道pre
#         pre = pre._next
#     temp = PolyNode(c,e)
#     # pre.next._expon = e
#     if positon and positon._expon == e:
#         sum = positon._coef + c
#         if sum:
#             pre._next = positon._next
#         else:
#             positon._coef = sum
#
#     # pre._next为none
#     positon = pre._next
#     if not positon:
#         pre._next = temp
#     # pre.next._expon < e
#     if positon._expon < e:
#         temp._next = positon
#         pre._next = temp
#     pre = pre._next
#
#     # 上述两段代码可以合并
#     # else:
#     #     pre._next = temp
#     #     temp._next = positon


def main():
    p1 = readPoly()
    p2 = readPoly()
    sum = polyNomialAdd(p1, p2)
    multi = mult(p1, p2)
    printPoly(multi)
    print
    printPoly(sum)

main()

# for i in range(3):
#     print 1,