# encoding:utf-8
'''
统计工龄

桶排序
稍作修改，桶内存放的个数
'''
M = 51
def Count(list, N):
    B = [0]*M
    for i in range(N):
        B[list[i]]+=1
    # 输出
    for i in range(M):
        if B[i]:
            print '%d:%d'%(i, B[i])

'''
8
10 2 0 5 7 2 5 2

0:1
2:3
5:2
7:1
10:1
'''
############################
from utils.readList import readList
if __name__ == '__main__':
    N = input()
    list = readList()
    Count(list, N)
