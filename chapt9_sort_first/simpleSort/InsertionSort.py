# encoding:utf-8
'''
类似扑克牌的插入操作，
依次将元素插入到已经有序的序列中，怎么插入？
从后往前比较，找到位置，然后插入，后面的元素都需要挪动
其实，跟前面的树里面的是一样的，在依次比较交换的基础上改进而来，依次比较，移动而非交换，找到合适的位置后，再填进去
'''
def insertionSort(list, N):
    for j in range(1, N): # 第0个看做已经有序
        temp = list[j]

        # j = i - 1
        # while j >= 0 and list[j] > temp:
        #     list[j + 1] = list[j]
        #     j -= 1
        # list[j + 1] = temp

        i = j
        while i>=1 and temp<list[i-1]:
            list[i] = list[i-1]
            i-=1
        list[i] = temp


if __name__ == '__main__':
    list = [8,11,9]
    insertionSort(list, len(list))
    print list
