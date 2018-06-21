#encoding:utf-8
'''
insertionOrHeap

10
3 1 2 8 7 5 9 4 6 0
1 2 3 7 8 5 9 4 6 0

Insertion Sort
1 2 3 5 7 8 9 4 6 0

--------------

10
3 1 2 8 7 5 9 4 6 0
6 4 5 1 0 3 2 7 8 9

Heap Sort
5 4 3 1 0 2 6 7 8 9

'''
'''
插入排序特点：前面顺序，后面与原序列相同
'''
def InsertionOrHeap(list, temp, N):
    i = N-1
    while i:
        if temp[i]==list[i]:
            i-=1
        else:
            break
    # 如何判断是否是有序的？冒泡算法
    # 依次两两比较都是有序的
    for j in range(0, i):
        if temp[j]>temp[j+1]:
            return False # 归并
    return True # 插入


##############################
from utils.readList import readList

'''

3 1 2 8 7 5 9 4 6 0
6 4 5 1 0 3 2 7 8 9


5 4 3 1 0 2 6 7 8 9

'''
def swap(list, i, j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp

def percDown(list, i, N):
    parent = i
    temp = list[parent]
    while 2*parent+1<N:
        child = 2*parent+1
        if child<N-1 and list[child]<list[child+1]:
            child = child+1
        if temp<list[child]:
            list[parent] = list[child]
            parent = child
        else:
            break
    list[parent] = temp



def heapNext(list, N):
    # 找到位置
    # 找到前面的较大的数，交换
    for i in range(N-1, 0, -1):
        if list[i]<list[i-1]:
            break
    # i位置是错的
    # i位置前（含i）是个最大堆
    swap(list, 0, i)
    percDown(list, 0, i)

def insertionNext(list, N):
    # 找到合适的位置
    for i in range(N-1):
        if list[i]>list[i+1]:
            break
    # 进行一次插入
    if i < N-1: # 尚未排序完成
        temp = list[i+1]
        j = i+1
        # python中没有那种两个分号的while循环，用while来代替
        while j>=1 and temp<list[j-1]:
            list[j] = list[j - 1]
            j-=1 # 有交换时才进行移位
        list[j] = temp

if __name__ == '__main__':
    N = input()
    list_raw = readList()
    list = readList()
    if InsertionOrHeap(list_raw, list, N):
        print 'Insertion Sort'
        insertionNext(list, N)
    else:
        print 'Heap Sort'
        heapNext(list, N)

    print list