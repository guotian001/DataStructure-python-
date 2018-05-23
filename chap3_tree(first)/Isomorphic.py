#encoding:utf-8


# https://pintia.cn/problem-sets/951072707007700992/problems/975887310869037056
###  存储结构，根据题意适合用静态链表 ，静态链表数组存储，left,right 存放的是数组下标


# 8
# A 1 2
# B 3 4
# C 5 -
# D - -
# E 6 -
# G 7 -
# F - -
# H - -

def readList():
    desc = raw_input()
    result = desc.strip().split()
    result[1] = toInt(result[1])
    result[2] = toInt(result[2])
    return result

def toInt(c):
    return NULL if c == '-' else int(c)

# left，right 指的是数组下标
class TNode:
    def __init__(self, elem, left, right):
        self.elem = elem
        self.left = left
        self.right = right

# NULL = '-' # 全局变量
# 下标应转为int，为保持一致，需要将'-' 用特殊的int代替，不妨设为-1
NULL = -1
def buildTree():
    N = input() # 结点数
    tree = [None]*N # 新建一个n的数组，python中仅做练习
    check = [0]*N # 每个结点的初始标记为0，当有结点指向他时，改为1，根节点没有别的结点指向，check为0
    for i in range(N):
        node_desc = readList()
        node = TNode(node_desc[0], node_desc[1],node_desc[2])
        tree[i] = node
        # 在输入遍历的时候就把check确定了
        if node_desc[1] != NULL:
            check[node_desc[1]] = 1
        if node_desc[2] != NULL:
            check[node_desc[2]] = 1
    root = -1
    for i in range(N):
        if check[i] == 0:
            root = i
            break
    return tree, root

# 递归判断，递归出口
def isomorphic(tree1,i1,tree2,i2):
    # 递归出口
        # 两树都空
        if i1 == NULL and i2 == NULL:
            return 1
        # 两树仅一空
        if (i1==NULL and i2!=NULL) or (i1!=NULL and i2==NULL):
            return 0
        # 两树都不空，根节点值不等
        # 代码走到这里说明两树都不空
        if tree1[i1].elem != tree2[i2].elem:
            return 0
        # 两树都不空，跟结点值相等，开始考虑子树，即开始递归问题
            ### 以一边为准即可
            # 1.左子树都不空且左子树结点值相等 （左、左）and（右、右）
        if tree1[i1].left!=NULL and tree2[i2].left!=NULL and tree1[tree1[i1].left].elem == tree2[tree2[i2].left].elem:
            return isomorphic(tree1, tree1[i1].left, tree2, tree2[i2].left) and isomorphic(tree1, tree1[i1].right, tree2, tree2[i2].right)
            # 2.else if 左左都空，比较右右
            # 1.2. 可以  合并  为 左左都空 or （左子树都不空且左子树结点值相等）， （左、左）and（右、右）
        elif tree1[i1].left==NULL and tree2[i2].left==NULL:
            return isomorphic(tree1, tree1[i1].right, tree2, tree2[i2].right)
            # else 其他情况都应该交换，左右 and 右左
        else:
            return isomorphic(tree1, tree1[i1].left, tree2, tree2[i2].right) and isomorphic(tree1, tree1[i1].right, tree2, tree2[i2].left)

def main():
    tree1, i1 = buildTree()
    tree2, i2 = buildTree()
    result = isomorphic(tree1, i1, tree2, i2)
    return 'Yes' if result == 1 else 'No'

########## test #####################
'''
8
A 1 2
B 3 4
C 5 -
D - -
E 6 -
G 7 -
F - -
H - -
8
G - 4
B 7 6
F - -
A 5 1
H - -
C 0 -
D - -
E 2 -

Yes

-------------


8
B 5 7
F - -
A 0 3
C 6 -
H - -
D - -
G 4 -
E 1 -
8
D 6 -
B 5 -
E - -
H - -
C 0 2
G - 3
F - -
A 1 4


No

'''
print main()