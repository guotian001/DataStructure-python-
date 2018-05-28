# encoding:utf-8
'''
    判断给定的插入序列是否是同一颗二叉搜索树

    思路：
        转化为树的查找问题
        1. 利用初始序列构建一颗二叉搜索树，
        2. 判断给定序列是否与新建的树一致
            判定方法： 将树中的每个结点初始化一个0 flag，对序列中的每个数字，依次去树中查找，如果查找所经过的数据应为已访问过的（flag=1），
            否则即是两棵树不一致
            why： 待判定序列是一个插入序列，每一个元素，都是待插入的结点，如果在给定树中查找给定的结点，发现前面的结点的flag为0，
            即这个坑还没有被占，那么应该用该元素填进去，所以两棵树就不一致了
'''

class TNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.flag = 0 # 这个坑是否已经占过了（根据插入序列）， 如果占过，自然要放在之后，否则，没被占过，，data又不一致，故树就不一致了那就应该占了
                      # data与位置一致，树才一致

def insert(tree, X):
    if not tree:
        tree = TNode(X)
    else:
        if X > tree.data:
            tree.right = insert(tree.right, X) # 肯能原来是none，现在不是了，因此需要重新赋值
        elif X < tree.data:
            tree.left = insert(tree.left, X)
        # else: 等于的时候不做处理
    return tree

# 根据序列新建一颗树
def buildTree(seq):
    # 不停的插入即可了吧
    tree = None
    for i in range(len(seq)):
        tree = insert(tree, seq[i])
    return tree

# 核心代码
# X 肯定能在树中找到,
# 递归实现
def check(tree, X):
    if not tree:
        return False
    if tree.flag == 0:
        if tree.data == X:
            tree.flag = 1
            return True
        else:
            return False
    else:
        if X < tree.data:
                return check(tree.left, X)
        elif X > tree.data:
                return check(tree.right, X)
        else:# 等于
            return False

# 判断插入序列生成的树 是否与给定的tree一致
def judge(tree, seq):
    for i in range(len(seq)):
        if not check(tree, seq[i]):
            return False
    return True



#############  test
'''
4 2
3 1 4 2
3 4 1 2
3 2 4 1
2 1
2 1
1 2
0
-----------------
Yes
No
No
'''

#怎么把数据读进去。。

def readList():
    desc = raw_input()
    return map(int,  desc.strip().split())

def main():
    result = []
    desc = readList()
    N = desc[0]
    while N: # N = 0 输入结束
        count = desc[1]
        tree = buildTree(readList())
        while count:
            result.append(judge(tree, readList()))
            count-=1
        desc = readList()
        N = desc[0]
    # 输出结果
    for i in range(len(result)):
        print 'Yes' if result[i] else 'No'


main()

def testInputPrint():
    N = 3
    while N:
        x = input()
        print x
        x-=1
