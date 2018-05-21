#encoding:utf-8
'''
计算多项式在给定点的值
f(x) = a0 + a1* x + a2* x**2 + ...
'''
import math
import time

# 循环实现
# n是x的次方上限
def f(n, a, x):
    sum = 0
    for i in range(n+1): # python中的遍历，自由
        # sum += a[i] * math.pow(x, i)  # 每次遍历都需要计算一次幂
        sum += a[i] * myPow(x, i)  # 每次遍历都需要计算一次幂
    return sum

def myPow(x, i):
    result = 1
    for t in range(i):
        result = result*x
    return result



'''
其实可以把上次计算的结果存起来，下次再乘一下，这样就不用每次都计算一次幂了，缓存中间结果，提高计算性能

f(x) = a0 + x*(a1+x*(a2+x*a3)) ; n = 3
'''
def f_2(n, a, x):
    p = a[n]
    for i in range(n, 0, -1): # 逆序遍历    # 变量含义要明确，边界扣扣清楚，错误一般在边界，可以写出来看看
        p = a[i-1] + x*p  # 迭代过来
    return p


# a = [0,1,2,3,4,5,6,7,8,9], 测试两个函数需要的时间


l = range(10)
MAX_SIZE = 1000
a = time.time()
for i in range(MAX_SIZE):
    f(9, l, 1.1)
b = time.time()
print 'f\'s time is ',b-a
c = time.time()
for i in range(MAX_SIZE):
    f_2(9, l, 1.1)
d = time.time()
print 'f_2\'s time is ', d-c

print f(len(l)-1, l, 1.1)
print f_2(len(l)-1, l, 1.1)

## practice
a = [1.0/i for i in range(1, 101)]
a.insert(0, 1)

MAX_SIZE = 1000
start1 = time.time()
n = len(a) - 1
for i in range(MAX_SIZE):
    f(n, a, 1.1)
end1 = time.time()
print 'f\'s time is ',end1-start1
start2 = time.time()
for i in range(MAX_SIZE):
    f_2(n, a, 1.1)
end2 = time.time()
print 'f_2\'s time is ', (end2-start2)