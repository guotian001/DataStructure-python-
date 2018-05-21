#encoding:utf-8
'''
python 中没有找到数组类型，权用list替代，以供练习(虽然很扯)
'''
class SStack:
    ERROR = 'ERROR'
    def __init__(self):
        self._top = None
        self.MaxSize = None
        self.data = None
    def createStack(self, maxSize):
        self._top = -1
        self.MaxSize = maxSize
        self.data = [None]*maxSize
    def isFull(self):
        return self._top  == self.MaxSize-1
    def push(self, X):
        if isFull(self):
            print '栈满'
            return False
        else:
            self._top += 1
            self.data[self._top] = X
    def isEmpty(self):
        return self._top == -1
    def pop(self):
        if isEmpty(self):
            print '栈空'
            return ERROR
        else:
            s = self.data[self._top]
            self._top -= 1
            return s
