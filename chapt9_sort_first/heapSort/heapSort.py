# encoding:utf-8
'''
堆排序，选择排序中的改进：获取最小元用堆来实现

'''

# 向下过滤 ; percolate 过滤
def percDown(list, i, N):
    temp = list[i]
    parent = i
    while 2*parent+1<N:
        child = 2*parent+1 # 左孩子结点
        if child<N-1 and list[child]<list[child+1]:
            child = child+1 # 较大子节点
        if temp<list[child]:
            list[parent] = list[child]
            parent = child
        else:
            break
    list[parent] = temp

def swap(list, i, j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp

def HeapSort(list, N): # N是元素的个数
    # buildHeap
    for i in range(N/2-1, -1, -1):
        percDown(list, i, N)# 向下过滤
    # 交换（改进的deleteMax）
    for i in range(N-1, 0, -1):
        swap(list, 0, i)# 改进之处，将delete掉的元素依次放在数组的尾部即可
        percDown(list, 0, i)

#################

if __name__ == '__main__':
    list = [1,10000,4,666,5,4,3,8,8,999,7]
    HeapSort(list, len(list))
    print list
