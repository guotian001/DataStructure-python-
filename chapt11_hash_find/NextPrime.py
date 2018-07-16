#encoding:utf-8

MAX_TABLE_SIZE = 100000 # 允许开辟的最大散列表长度
from math import sqrt
def nextPrime(n):
    n = n if n%2 else n+1
    while n<MAX_TABLE_SIZE:
        for i in range(int(sqrt(n)), 1, -1):
            if not n%i: # 可以整除
                break
        if i==2: # for循环正常结束
            break
        else:
            n+=2
    return n

##########
if __name__ == '__main__':
    print nextPrime(11)