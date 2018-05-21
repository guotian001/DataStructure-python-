#encoding:utf-8
'''
实现一个函数：输入N,打印从1-N的正整数
'''

# 循环实现
def printN_1(N):
    for i in range(1, N+1):
        print i

# 递归实现
def printN_2(N):
    if N > 0:
        printN_2(N-1)
        print N


printN_1(10000)
print '================================='
printN_2(998)

sorted()
