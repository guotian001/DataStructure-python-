#encoding:utf-8
class Node:
    def __init__(self, elem, next_=None):
        self._elem = elem
        self._next = next_

class LQueue:
    def __init__(self, maxSize = 8):
        self._front = None
        self._rear = None
        self._maxSize = maxSize
    def is_empty(self):
        return self._front == None
    def deleteQ(self):
        if self.is_empty():
            print '队列为空'
            return None
        else:
            # 不带空头结点
            if self._front == self._rear:
                self._front = self._rear = None
            else:
                temp = self._front
                self._front._next  = temp._next
            return temp._elem
    def len(self):
        i = 0
        while self._front:
            self._front = self._front._next
            i+=1
        return i
    def is_full(self):
        return len(self) == self._maxSize
    def push(self,X):
        if self.is_full():
            print '队列达到最大值'
            return False
        else:
            temp = Node(X, self._front)
            self._front = temp
            return True