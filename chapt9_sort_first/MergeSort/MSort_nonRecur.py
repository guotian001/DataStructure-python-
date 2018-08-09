# encoding:utf-8
'''
非递归实现 归并排序，
归并排序非常适合于外部排序
'''

from Merge import merge1

# 核心代码，找个具体的例子走一遍
def merge_pass(list, temp, N, length):  # length指的是已经有序的序列的长度
    # for循环，准确地用while循环改写
    i=0
    while i < N-2*length: # 这里等于或者小于都是可以的，不过按老师所说的思路，应该小于，否则如果刚好剩下的是2*length个，下面的merger会在这里做掉，不过不影响结果
        merge1(list, i, i+length, i+2*length-1, temp)
        i+=2*length # merge的是两个序列，所以乘以2

    if i+length<N: # 说明剩余的多于一个有序的序列，需要归并
        merge1(list, i, i+length, N-1, temp)
    else: # 剩余的最多是一个序列的长度
        for j in range(i, N):
            temp[j] = list[j]



def merge_sort(list, N):
    temp = [0]*N
    length = 1
    while length<N: # 当length>=N时就没有合并的必要了,这个序列中就是有序的了
        merge_pass(list, temp, N, length)
        length*=2
        merge_pass(temp, list, N, length) # 这一步可能是多余的，但是能够保证循环跳出时，结果是存在list中的，即可能多一步导到list中的操作
        length*=2

if __name__ == '__main__':

    list = [1,3,24,53,6,7,53,3,37,9,6]
    merge_sort(list, len(list))
    print list

