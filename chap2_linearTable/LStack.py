#encoding:utf-8
class SNode:
    def __init__(self, elem=None, next_ = None):
        self.elem = elem
        self.next_ = next_

# 带空头结点的链栈，即栈顶结点是该空头结点的下一个结点
class LStack:
    def __init__(self):
        self.S = SNode()
    def is_empty(self):
        return self.S.next_ == None
    def push(self, X):
        temp = SNode(X,self.S.next_)
        self.S.next_ = temp

    def pop(self):
        if self.is_empty():
            print '栈空'
            return None
        else:
            top = self.S.next_
            self.S.next_ = top.next_
            return top.elem

if __name__ == '__main__':
    stack = LStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print stack.pop()
    print stack.pop()
    print stack.pop()
    print stack.pop()
    print stack.pop()