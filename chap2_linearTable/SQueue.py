#encoding:utf-8
'''
    队列，顺序存储
    1. front指向队列中第一个元素   前面   的位置，rear指向队列中最后一个元素的位置
        eg：
        非循环，
                创建队列时， front = rear = -1
                出队front + 1， 入队rear+1

                队列空：front = rear
                队列满： rear = n-1

        循环：
            因为是循环着来的，初始的时候可以设为任意下标，即可以从环上的任意位置开始，只要顺着一个方向，入队rear+1， 出队front+1即可，
            超过利用求余法

            队列空 ： front = rear
            队列满： front = rear。。。why， 循环队列时利用front和rear的差来表示队列中的元素的情况， n个空间的数组的可以有n种差值的情形，
                                            但是元素有0 - n共n+1种，so。。。
                解决方法：
                    留出一个，即当队列中剩一个空位的时候即认为队列满：即（rear+1）% maxSize == front，（front指的是第一个元素前面的位置），环的方向：
                        0，1,2,3,4,0,1,2

'''
class SQueue:
    def __init__(self, maxSize = 8):
        self._rear = 0
        self._front = 0
        self._maxSize = maxSize
        self._data = [None] * maxSize

    def is_full(self):
        return (self._rear+1)%self._maxSize == self._front
    def is_empty(self):
        return self._rear == self._front
    def addQ(self, X):
        if self.is_full():
            print '队列满'
            return False
        else:
            self._rear = (self._rear + 1) % self._maxSize
            self._data[self._rear] = X
            return True

    def deleteQ(self):
        if self.is_empty():
            print '队列空'
            return None
        else:
            self._front = (self._front+1)%self._maxSize
            return self._data[self._front] # front指向第一个元素前面的元素


if __name__ == '__main__':
    queue = SQueue()
    queue.addQ(1)
    queue.addQ(2)
    queue.addQ(3)
    queue.addQ(4)
    print queue.deleteQ()
    print queue.deleteQ()
    print queue.deleteQ()
    print queue.deleteQ()