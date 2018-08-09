#encoding:utf-8
'''
判断插入还是归并排序，并再多进行一次
'''

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


14
4 2 1 3 13 14 12 11 8 9 7 6 10 5
1 2 3 4 11 12 13 14 6 7 8 9 5 10

'''

'''
思路:
    1. 插入排序好判断：从前到后找有序序列，然后判断后面的序列是否与元序列一致，顺便返回不有序的位置以便进行下一步的插入操作
    2. 找到归并排序的长度，从2开始逐步判断，判断时只需判断相邻片段的尾首即可
    
'''

def IsInsertion(list, temp, N):
    for i in range(N):
        if temp[i] > temp[i+1]:
            break
    for j in range(i+1, N):
        if list[j]!=temp[j]:
            return False, None
    return True, i+1

def insertionNext(list, i, N): # i 是待插入元素的位置
    temp = list[i]
    j = i-1
    while list[j]>temp and j>-1:
        list[j+1] = list[j]
        j-=1
    # j=-1才会跳出循环
    list[j+1]=temp



# 这个还是比较有思想的
def getLength(list, N):
    l = 2
    flag = True
    while l<=N:
        # 判断
        end = 0+l-1
        while end<N-1:
            if list[end]<=list[end+1]:
                end+=l*2 # 判断下个长度的序列内部是否有序
            else:
                flag = False
                break

        if flag:
            l*=2
        else:
            return l




from chapt9_sort_first.MergeSort.MSort_nonRecur import merge_pass
def mergeNext(list, N):
    l = getLength(list, N)

    # 在进行一次归并
    temp = [0] * N
    merge_pass(list, temp, N, l)
    return temp


def printList(list):
    for i in list:
        print i,


from utils.readList import readList
if __name__ == '__main__':
    N = input()
    list_raw = readList()
    list = readList()
    isInsertion, index = IsInsertion(list_raw, list, N)

    if isInsertion:
        print 'Insertion Sort'
        insertionNext(list, index, N)
    else:
        print 'Merge Sort'
        list = mergeNext(list, N)
    printList(list)
