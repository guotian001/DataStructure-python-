#encoding:utf-8
'''
快速排序
'''
def insertionSort(list, left, right):
    for i in range(left+1,right+1):
        temp = list[i]
        j = i
        while j>left and list[j-1]>temp:
            list[j] = list[j-1]
            j-=1
        list[j] = temp

def swap(list, i, j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp

def median3(list, left, right):
    center = (left+right)/2
    if list[left]>list[center]:
        swap(list, left, center)
    if list[center]>list[right]:
        swap(list, center, right)
    # 上面两步可以确定一个： 上面两步确定right最大
    if list[left]>list[center]:
        swap(list, left, center)

    # 将pivot放在right-1的位置
    swap(list, center, right-1)
    return list[right-1]



def quickSort(list, left, right):
    if right-left>=cutoff:

        pivot = median3(list, left, right)
        i = left+1
        j = right-2
        while True:
            while list[i]<pivot: # 程序是有执行顺序的，先走i再走j
                i+=1
            while list[j]>pivot:
                j-=1
            if i<j:
                swap(list, i, j)
            else:
                break
        swap(list, i, right-1)
        # 递归
        quickSort(list, left, i-1)
        quickSort(list, i+1, right)
    else: # 递归出口，median3的需要保证序列中至少3个元素，因此，cutoff>=3
        insertionSort(list, left, right)

def qSort(list, N):
    quickSort(list, 0, N-1)

if __name__ == '__main__':
    cutoff = 3
    list = [5,4,6,3,8,9,11,0]
    qSort(list, len(list))
    print list