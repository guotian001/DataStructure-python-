#encoding:utf-8
'''
集合的简化表示，集合中的元素都可以用连续的非负整数来表示，所以只需要一个整形的数组，下标数组的下标i就代表着集合的第i个元素，数组中存的值是这第i个
元素的父节点的下标，也就是说data与i相等了。。。
'''

def find(s, x):
    while s[x]>=0: # 本质上就是根据数组中存放的元素来进行判断的，本身就不是根据下标来判断的
        x=s[x]
    return x

def union(s, root1, root2):
    s[root2]=root1

# 按树的高度进行归并， 数组存放的是  -树高
def union1(s, root1, root2):
    if s[root1] < s[root2]: #1高
        s[root2] = root1
    else:
        if s[root1] == s[root2]:
            root2+=1 # 只有两个等高的树进行归并的时候，树高才更新，并且只+1
        s[root1]=root2

# 按集合的规模（元素个数）进行归并， 数组存放的是  -元素个数
def union2(s, root1, root2):
    if s[root1] < s[root2]:
        s[root1] += s[root2]
        s[root2]=root1
    else:
        s[root2] += s[root1]
        s[root1]=root2

'''
算法书写，自顶向下，先搭框架，把函数定义出来，然后一步步实现函数即可，类似于先写目录，提纲挈领
'''
########
'''
5
C 3 2
I 3 2
C 1 5
I 4 5
I 2 4
C 3 5
S

no
no
yes
There are 2 components.

'''

def main():
    N = input()
    S = buildSet(N)

    # do while  有时候写起来还是比较简洁的

    while True:
        index = read()
        if index[0] == 'C':
            check_connection(S, index[1], index[2])
        elif index[0] == 'I':
            input_connection(S, index[1], index[2])
        elif index[0] == 'S':
            check_networks(S)
        if index[0]=='S':
            break

def read():
    index = raw_input().strip().split()
    return [index[0]] + map(int, index[1:])
    # if len(index) > 1:
    #     return [index[0]] + map(int, index[1:])
    # else:
    #     return index
def buildSet(n):
    # 初始时都是独立的集合，单元素集合
    return [-1]*n

def check_connection(S, u, v):
    root1 = find(S, u-1)
    root2 = find(S, v-1)
    if root1 == root2:
        print 'yes'
    else:
        print 'no'

def input_connection(S, u, v):
    root1 = find(S, u-1)
    root2 = find(S, v-1)
    if root1!=root2:
        union(S, root1, root2)

def check_networks(S):
    count= 0
    for i in S:
        if i == -1:
            count+=1
    if count==1:
        print 'The network is connected.'
    else:
        print 'There are %d components.' % count


main()