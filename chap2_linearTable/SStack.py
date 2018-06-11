#encoding:utf-8
'''
python 中没有找到数组类型，权用list替代，以供练习(虽然很扯)
'''
class Stack:
    def __init__(self,maxSize = 20):
        self.data = []
        self.maxSize = maxSize
    def is_full(self):
        return len(self.data) == self.maxSize
    def push(self, X):
        if self.is_full():
            return False
        else:
            self.data.append(X)
            return True
    def is_empty(self):
        return len(self.data) == 0
    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.data.pop()
    def get_top(self):
        if self.is_empty():
            return None
        else:
            return self.data[-1]