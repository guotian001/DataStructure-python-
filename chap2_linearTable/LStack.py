#encoding:utf-8
class SNode:
    def __init__(self, elem, next_ = None):
        self.elem = elem
        self.next_ = next_

# 带空头结点的链栈，即栈顶结点是该空头结点的下一个结点
class LStack:
    def __init__(self):
        self.S = SNode()
    def is_empty(self):
        return self.S.next_ == None
    def push(self, X):
        temp = SNode(self,X,self.S.next_)
        self.S.next_ = temp

    def pop(self):
        if is_empty(self):
            print '栈空'
            return None
        else:
            top = self.S.next_
            self.S.next_ = top.next_
            return top.elem
