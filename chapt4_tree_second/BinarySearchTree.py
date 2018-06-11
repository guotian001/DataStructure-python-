# encoding:utf-8
'''
二叉搜索树，BST
左子树都小于结点的值，右子树都大于结点的值

'''

class BinTreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# 递归查找
def find_recursion(tree, X):
    if tree==None:
        return None
    if X > tree.data:
        return find_recursion(tree.right, X) # 尾递归
    elif X < tree.data:
        return find_recursion(tree.left, X) # 尾递归
    else:
        return tree

# 迭代查找
def find_iteration(tree, X):
    while tree:
        if X > tree.data:
            tree = tree.right
        elif X < tree.data:
            tree = tree.left
        else:
            return tree
    return None # 查找失败

# 查找最大最小元素
'''
    最大元素一定在最右分支的端结点上（最右叶结点）
    最小元素一定在最左分支的端结点上（最左叶节点）
'''
def findMin(tree):
    if not tree:
        return None
    # 如果存在左结点，则递归到左分支上
    elif tree.left:
        return findMin(tree.left)
    # 否则就返回
    else:
        return tree

def findMax(tree):
    while tree:
        if tree.right:
            tree = tree.right
        else:
            return tree
    return None

    # 精简后的代码
    # if tree:
    #     while tree.right:
    #         tree = tree.right
    # return tree

# 递归插入
def insert(tree, X):
    # 递归出口
    if not tree:
        tree = BinTreeNode(X)  # tree改变不能改变函数体外的值，因此需要返回出去，重新赋值一次
    else:
        if X > tree.data:
            tree.right = insert(tree.right, X)
        elif X < tree.data:
            tree.left = insert(tree.left, X)
        # 相等则不用插入
    return tree  # 最后将tree返回, 也不为过


# 删除元素，递归
# 先找到待删除节点 三种情况
    # 1. 无子节点，直接删除，即node= None即可
    # 2. 有一个结点
        # 有左： 把左结点替上，node = node.left
        # 有右： 把右结点替上 node = node.right
    # 3. 有左右结点
        # 选一个结点替代该结点，左子树的最大结点或者右子树的最小结点（为了替代后仍是二叉搜索树），然后再子树中再删除该结点（递归）
def delete(tree, X):
    # 递归出口
    if not tree:
        print '待删除结点未找到'
    else:
        if X > tree.data:
            tree.right = delete(tree.right, X)
        elif X < tree.data:
            tree.left = delete(tree.left, X)
        else: # 找到
            if not tree.left: # 存在右结点或者不存在子节点
                tree = tree.right
            elif not tree.right:
                tree = tree.left
            else: # 左右结点都存在
                # 从右子树找
                temp = findMin(tree.right)
                tree.data = temp.data
                tree.right = delete(tree.right, temp.data)
    return tree # 重新赋值一次是最保险的，不用担心值传递引起的问题。反正重新赋值一次是肯定能可以的



def init():
    tree = None
    tree = insert(tree, 'Jan')
    tree = insert(tree, 'Feb')
    tree = insert(tree, 'Mar')
    return tree

tree = init()
print tree
