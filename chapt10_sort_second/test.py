# encoding:utf-8
'''

插入排序
'''

def insertionSort(list, N):
    for i in range(1,N):
        # 将一个元素插入到前面的有序序列中去
        temp = list[i]
        # 找到位置
        j = i
        while list[j-1]>temp and j>0:
            list[j] = list[j-1]
            j-=1
        list[j] = temp

if __name__ == '__main__':
    list = [1,2,4,3,2,111,4,58,5,3]
    insertionSort(list, len(list))
    print list