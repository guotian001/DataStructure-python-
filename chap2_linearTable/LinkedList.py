#encoding:utf-8
# 链接表，核心 是结点
class LNode:
    def __init__(self,elem,next_=None):
        self.elem = elem
        self.next_ = next_
ERROR = None

class LList:
    def __init__(self):
        self._head = None
    def is_empty(self):
        return self._head is None

    def length(self):
        i = 0
        head = self._head
        while head:
            head = head.next_
            i += 1
        return i
    def find(self, X):
        p = self._head
        while p and p.elem != X:
            p = p.next_
        return p
    # K代表位置，从0开始
    # K 可能会是非法值， 比如 -1，。。。。
    def findKth(self, K):
        p = self._head
        i = 0
        while p and i < K:
            p = p.next_
            i += 1
        if i == K:
            return p
        else:
            return None
    # 带头结点的插入: 插入到position位置，即插入到position-1后；带头结点的链表不用更新头结点
    # 注意: 在插入位置参数P上与课程视频有所不同，课程视频中i是序列位序（从1开始），这里P是链表结点指针，在P之前插入新结点
    def insert(self, X, position):
        # 头结点链表中，如果存在于，则一定有前置结点，最次是头结点
        pre = self._head
        while pre and pre.next_ != position:
            pre = pre.next_
        if not pre: # pre为none
            print '插入位置参数错误'
            return False
        else:
            temp = LNode()
            temp.elem = X
            temp.next_ = position
            pre.next_ = temp
            return True
    # i 为位置
    def insert_(self, i, X):
        temp = LNode()
        temp.elem = X
        if i == 1:
            temp.next_ = self._head
            self._head = temp
            return True
        p = findKth(self, i-1)
        if not p:
            print '参数%d错误' %(i)
            return False
        else:
            temp.next_ = p.next_
            p.next_ = temp
            return True



    # / *带头结点的删除 * /
    # / *注意:在删除位置参数P上与课程视频有所不同，课程视频中i是序列位序（从1开始），这里P是拟删除结点指针 * /
    def delete(self, postion):
        # 找到position的前置结点
        pre = self._head
        while pre and pre.next_ != postion:
            pre = pre.next_
        if not postion:
            print '删除位置参数错误'
            return False
        else:
            pre.next_ = postion.next_
            return True

    def delete_(self, i):
        s = self._head
        if i == 1:
            # 第一个结点可能为空
            if not self._head:
                return True
            else:
                self._head = s.next_
                return True
        else:
            p = findKth(self, i-1)
            if not p:
                print '第%d个结点不存在' % (i-1)
                return False
            else:
                if not p.next_:
                    print '第%d个结点不存在' % (i)
                    return False
                else:
                    temp = p.next_
                    p.next_ = temp.next_
                    return True
