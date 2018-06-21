#encoding:utf-8
'''
冒泡排序：
    依次比较相邻的两个元素，如果不满足条件则交换，这样一趟下来可以排序好一个
    优点：同时适用于链表和数组，稳定排序
    缺点：最坏情况下，时间复杂度是O(N^2)
'''

def swap(list, i, j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp

# 从小到大排序
def BubbleSort(list, N):
    for j in range(N-1, -1, -1): # 一趟排序好一个
        flag = 0
        for i in range(j):
            if list[i]>list[i+1]: #依次比较相邻元素
                swap(list,i,i+1)
                flag = 1
        if flag == 0: #没有发生交换，说明已经有序
            break


if __name__ == '__main__':
    list = [1,5,3,6,90,11,11]
    BubbleSort(list, len(list))
    print list