#encoding:utf-8
'''
判断是归并排序还是插入排序？
思路，从后面往前遍历直至不一致，再遍历前一个元素是否是正确的位置，是 插入排序，否归并排序
'''
def InsertionOrMerge(list, temp, N):
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
'''
10
3 1 2 8 7 5 9 4 6 0
1 2 3 7 8 5 9 4 6 0

Insertion Sort
1 2 3 5 7 8 9 4 6 0
-----------------

10
3 1 2 8 7 5 9 4 0 6
1 3 2 8 5 7 4 9 0 6

Merge Sort
1 2 3 8 4 5 7 9 0 6


'''
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
            j-=1
        list[j] = temp
'''

10
3 1 2 8 7 5 9 4 0 6
1 3 2 8 5 7 4 9 0 6
'''
from chapt9_sort_first.MergeSort.Merge import merge1
from chapt9_sort_first.MergeSort.MSort_nonRecur import merge_pass

def getLengthFirst(list, N):
    lenght = 1
    while lenght<N and list[lenght]>list[lenght-1]:
        lenght+=1
    return lenght

def getLength(list, start, end):
    l = 1
    while start+l<=end and  list[start+l]>list[start+l-1]:
        l+=1
    return l

def findlength(list, N):
    length = getLengthFirst(list, N)
    start = 0 + length
    while start < N:
        end = start + length - 1
        l = getLength(list, start, end)
        start = start + l # 一个一个序列的走
        if l < length:
            length = l
    return length

def mergeNext(list, N):

    # 找出length
    length = findlength(list, N)

    # 在进行一次归并
    temp = [0]*N
    merge_pass(list, temp, N, length)
    return temp


# 插入排序，找到位置，再进行一次
# 归并排序，关键是找出length：从左到右进行遍历，先找出一个数字，然后进行检验修正，这样可以保证O(N)找到
from utils.readList import readList
if __name__ == '__main__':
    N = input()
    list_raw = readList()
    list = readList()
    if InsertionOrMerge(list_raw, list, N):
        print 'Insertion Sort'
        insertionNext(list, N)
    else:
        print 'Merge Sort'
        list = mergeNext(list, N)
    print list


