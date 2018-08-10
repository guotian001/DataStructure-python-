#encoding:utf-8
'''
只能swap0操作，那么0就相当于表排序的物理操作时的空位一般
每次交换都是将0所在的位置的正确元素换过来


单元环：0次交换
含0多元环： n0-1次交换
不含0多元环： 1+ ((ni+1) - 1) 需要先把0换进去

思路： 分别找出这样的环

'''
# 是否还有环，有的话，给出一个环的头
def isStillLoop(table, N):
    for i in range(N):
        if table[i]!=i:
            return True, i
    return False, None


def doAndCount(table, list, i, N): # i==0时，含0，其他都不含0
    idx = i
    count = 1
    while table[table[idx]]!=table[idx]: # 要看当前指向的下一个指向是否是已经弄好的，是就是环结束了
        count+=1
        # idx指向下一个，并且把当前的T[]改成正确的
        temp = table[idx]
        table[idx]=idx
        idx = temp

    table[idx]=idx # 下标还是要改的
    return count-1 if i==0 else count+1


def getCount(list, N):
    # 建立下标
    table = [0]*N
    for i in range(N):
        table[list[i]] = i
    count = 0
    isLoop, idx = isStillLoop(table, N)
    while isLoop:
        count += doAndCount(table, list, idx, N)
        isLoop, idx = isStillLoop(table, N)
    return count



'''
10
3 5 7 2 6 4 9 0 8 1

-----------------
9
'''
from utils.readList import readList
if __name__ == '__main__':
    N = input()
    list = readList()
    print getCount(list, N)