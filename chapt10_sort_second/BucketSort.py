#encoding:utf-8
'''
桶排序，待排数N >> key值范围M， 可以对key值建立M个桶。
比如 将N=40000个学生的成绩（0-100）进行排序，可对成绩进行建桶(101)

'''

class Node:
    def __init__(self, key = None, next_ = None):
        self.key = Key
        self.next_ = next_

def bucketSort(list, N, M):
    # 初始化桶
    buckets = [None]*M
    for i in range(N):
        node = Node(list[i])
        node.next_ = buckets[list[i]]
        buckets[list[i]] = node

    # 输出
    for i in range(M):
        if buckets[i]:
            next = buckets[i]
            while next:
                print next.key
                next = next.next_


if __name__ == '__main__':
    list = range(10)
    print list