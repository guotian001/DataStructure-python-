# encoding:utf-8
'''
    平衡二叉树，每个结点的平衡因子绝对值不超过1

    树高在插入的时候确定
'''

class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0 # 只有一个根节点的树高度为0  # 树高计算： max(Hl, Hr) + 1,从下往上计算，叶子结点的高度为0

def getHeight(node):
    return node.height if node else -1  # 叶节点高度为0，因此空节点应该为-1，这样只有左叶节点的树的高度才会等于 1 = 0 -（-1）
# LL旋转（左单旋）
def singleLeftRotation(A): # A为  被破坏结点/发现结点
    # LL 故A必有左子节点
    B = A.left
    A.left = B.right
    B.right = A
    # 更新结点的高度
    A.height = max(getHeight(A.left), getHeight(A.right)) + 1
    B.height = max(getHeight(B.left), getHeight(B.right)) + 1
    return B # B作为了根结点

# RR旋转（右单旋）
def singleRightRotation(A):
    B = A.right
    A.right = B.left
    B.left = A
    # 更新树高
    A.height = max(getHeight(A.left), getHeight(A.right)) + 1
    B.height = max(getHeight(B.left), getHeight(B.right)) + 1
    return B

# LR旋转(左右双旋)
def doubleLeftRightRotation(A):
    # A 必须有一个左子节点B，且B必须有一个右子节点C, 最后返回出去的是C
    # B = A.left
    # B = singleRightRotation(B)
    # B 与C右单旋， C被返回
    A.left = singleRightRotation(A.left)
    # A与C做左单旋， C被返回
    return singleLeftRotation(A)

# RL旋转（右左双旋）
def doubleRightLeftRotation(A):
    # A 肯定有右子节点B, B肯定有左子节点C
    # B 与 C 做左单旋，返回C
    A.right = singleLeftRotation(A.right)
    # A 与 C 做右单旋，返回C
    return singleRightRotation(A)



# 平衡二叉树的插入， 需要考虑到插入后的高度问题，找到对应的情景，进行相应的旋转
# 递归插入，跟二叉搜索树的不同之处： 加入平衡因子的计算检验，并考虑旋转问题
def insert(tree, X):
    if not tree: # 空树  空作为特殊情况
        return AVLNode(X) # 递归出口
    elif X > tree.data:
        # 可能会有旋转，因此需要重新赋值
        tree.right =  insert(tree.right, X) # 改变不了方法外的实参，但是可以改变变量指向的对象的属性值，编程中经常遇到，即height还是可以改变的
        # 校验平衡因子，是否需要旋转
        if getHeight(tree.left)-getHeight(tree.right) == -2:
            # 需要旋转,且tree在插入前一定有右子节点
            if X > tree.right.data:
                # RR旋转
                return singleRightRotation(tree)
            elif X < tree.right.data:  # 代码走到这里说明平衡因子被改变，即插入成功，即X 与树中的结点不等，因此，这个条件等价于else
            # else:
                return doubleRightLeftRotation(tree)
    elif X < tree.data:
        tree.left = insert(tree.left) # 递归，
        if getHeight(tree.left)-getHeight(tree.right) == 2:
            if X < tree.left.data:
                ## LL
                return singleLeftRotation(tree)
            else:
                return singleLeftRotation(tree)
    # else: 等于tree.data时 不做插入

    # 不要忘了更新树高，，，??? 真的需要更新树高么？  在旋转方法中已经更新过了哎

    # 如果有旋转的话当然就不要更新树高了，但是不要忘了，也可能插入之后不用旋转啊，这时就要更新树高了
    # PS： 代码走到这里说明tree没有旋转
    tree.height = max(getHeight(tree.left), getHeight(tree.right)) + 1
    return tree


########   test  #########  good

tree = None
tree = insert(tree,1)
tree = insert(tree,2)
tree = insert(tree,3)
tree = insert(tree,4)
tree = insert(tree,5)
tree = insert(tree,6)
print tree


############  TEST 指向对象的变量 和 通过变量更改对象的属性值的问题 #########
class Test:
    def __init__(self,height):
        self.height = height
def changeVar(test):
    print test # 值传递
    test = Test(10) # 这里改变，不能改变外面的变量的值，
    print test
    return test # 解决方法，返回出去，对外面的变量重新赋值  test = changeVar(test)

print '--------------------------------'

# test1 = Test(10)
# test2 = changeVar(test1)
# print test1
# print test2

test1 = Test(10)
print test1
test1 = changeVar(test1)
print test1
print '--------------------------------'

def changeAttr(test):
    test.height = 10000 # test 虽然是值传递。里面的test和外面的test是两个变量只不过值想等而已，

                        # 但是，这种对象情形下，里面的test和外面的test是指向同一个对象的两个变量，
                        # 对象只有一份，可以通过任何一个test变量来修改对象的属性值，
                        # 再根据另一个变量来访问对象的属性时，对象的属性值依然被改变

test2 = Test(10)
print test2.height
changeAttr(test2)
print test2.height


