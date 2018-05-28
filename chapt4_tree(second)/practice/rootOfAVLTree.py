#encoding:utf-8
'''
给定一个插入序列，求对应的AVL树的树根
'''
class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0

def getHeight(tree):
    return tree.height if tree else -1

# RR旋转
def singleRightRotation(A):
    B = A.right
    A.right = B.left
    B.left = A
    A.height = max(getHeight(A.left), getHeight(A.right)) + 1
    B.height = max(getHeight(B.left), getHeight(B.right)) + 1
    return B

# LL旋转
def singleLeftRotation(A):
    B = A.left
    A.left = B.right
    B.right = A
    A.height = max(getHeight(A.left), getHeight(A.right)) + 1
    B.height = max(getHeight(B.left), getHeight(B.right)) + 1
    return B

# LR旋转
def doubleLeftRightRotation(A):
    A.left = singleRightRotation(A.left)
    return singleLeftRotation(A)

# RL旋转
def doubleRightLeftRotation(A):
    A.right = singleLeftRotation(A.right)
    return singleRightRotation(A)

# 一颗AVL树的插入
def insert(tree, X):
    if not tree:
        tree = AVLNode(X)
    else:
        if X > tree.data:
            tree.right = insert(tree.right, X)
            if getHeight(tree.left)-getHeight(tree.right) == -2:
                if X > tree.right.data:
                    return singleRightRotation(tree)
                else: # 代码到这里说明insert成功，故不存在想等的情况
                    return doubleRightLeftRotation(tree)
        elif X < tree.data:
            tree.left = insert(tree.left, X)
            if getHeight(tree.left)-getHeight(tree.right) == 2:
                if X < tree.left.data:
                    return singleLeftRotation(tree)
                else:
                    return doubleLeftRightRotation(tree)
        # else: 相等时不做处理
    # 更新heigh
    tree.height = max(getHeight(tree.left), getHeight(tree.right)) + 1
    return tree

###############   test
'''
5
88 70 61 96 120

70


7
88 70 61 96 120 90 65
88
'''

def readList():
    desc = raw_input()
    return map(int,  desc.strip().split())

def test():
    N = input()
    list = readList()
    tree = None
    for i in range(len(list)):
        tree = insert(tree, list[i])
    print tree.data

test()
