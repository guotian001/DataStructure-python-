#encoding:utf-8
'''
递归实现 归并排序

'''
def Merge_Sort(list, N):
    tempList = [0]*N
    MSort(list, 0, N-1, tempList)

from Merge import merge
def MSort(list, L, rightEnd, tempList):
    if L<rightEnd:
        center = (L+rightEnd)/2
        MSort(list, L, center, tempList)
        MSort(list, center+1, rightEnd, tempList)
        merge(list, L, center+1, rightEnd, tempList)


if __name__ == '__main__':
    list = [1,2,4,66,49,10,3333,5,4,3,6,3]
    Merge_Sort(list,len(list))
    print list