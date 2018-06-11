#encoding:utf-8
'''
    完全二叉搜索树
    即，用完全二叉树来表示二叉搜索树
    给定输入序列，输出完全二叉搜索树的层序遍历
'''
# 数组存储
# 递归解决
'''
10
1 2 3 4 5 6 7 8 9 0

6 3 8 1 5 7 9 0 2 4
'''
import math
def CBST():
    N = input()
    rawList = raw_input().strip().split()
    list = [int(i) for i in rawList]
    # 排序
    list.sort()
    tree = [None]*N
    solve(0, N-1, 0, list, tree)
    for i in tree:
        print i,


# 递归解决
def solve(L, R, root, list, tree):
    # 递归出口
    n = R-L+1
    if n==0:
        return
    # n=1时，下面这一套规则仍然成立
    # 找到左子树的节点数
    length = getLeftLength(L, R)
    tree[root] = list[L+length]
    # 开始递归解决问题
    Lroot = 2*root+1
    Rroot = Lroot+1
    # 左
    solve(L, L+length-1, Lroot, list, tree)
    # 右
    solve(L+length+1, R, Rroot, list, tree)

def getLeftLength(L, R):
    N = R - L + 1
    H = int(math.log(N, 2)) # 搞清楚H到底表示的是啥
    X = N+1-math.pow(2, H)
    X = X if X<=math.pow(2, H-1) else math.pow(2, H-1)
    return int(math.pow(2, H-1)-1+X)


CBST()

