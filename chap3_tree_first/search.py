# encoding:utf-8
'''
顺序查找，table为数组，且其数据存储在1-len(table)中，即0元素为空
查找的时候可以将0元素设为待查找的元素，然后倒序遍历，失败返回0
'''
def sequentialSearch(table,X):
    table[0] = X
    for i in range(len(table)-1, -1, -1):
        if table[i] == X: # 最差会return0
            return i

def binarySearch(table, X):
    notFound = 0
    left  = 1
    right = len(table)-1
    while left <= right:
        mid = (left+right) / 2 # mid也要更新
        if table[mid] > X:
            right = mid -1
        elif table[mid] < X:
            left = mid + 1
        else:
            return mid
    return notFound


##################  test   ###################

table = [None, 1, 2, 3]
print sequentialSearch(table, 3)
print binarySearch(table, 3)