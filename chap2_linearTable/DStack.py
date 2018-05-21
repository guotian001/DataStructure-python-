#encoding:utf-8
'''
请用一个数组实现两个堆栈，要求最大地利用数组空间，使
数组只要有空间入栈操作就可以成功。
'''

class DStack:
    maxSize = 20
    def __init__(self):
        self.data = [None]*maxSize
        self.top1 = -1 # 栈1从数组的头开始
        self.top2 = maxSize # 栈2从数组的尾开始   数组下标为（0， maxSize-1）

    # tag 栈的标记：1代表栈1,2代表栈2
    def push(self, tag, X):
        if self.top2 - self.top1 == 1:
            print '栈满'
            return False
        else:
            if tag == 1:
                self.top1 += 1
                self.data[self.top1] = X
            else:
                self.top2 -= 1
                self.data[self.top2] = X
            return True
    def pop(self, tag):
        if tag == 1:
            if self.top1 == -1:
                print '栈1空'
                return None
            else:
                s = self.data[self.top1]
                self.top1 -=1
                return s
        else:
            if self.top2 == maxSize:
                print '栈2空'
                return None
            else:
                s = self.data[self.top2]
                self.top2 += 1
                return s


