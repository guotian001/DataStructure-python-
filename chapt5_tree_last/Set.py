#encoding:utf-8
'''
集合

双亲表示法，结点指向父结点；树根表示树
数组实现，每个数组两个域，data、parent（指向父节点的下标）

'''
class Node:
    def __init__(self, data=None, parent=-1): # 为了union操作中把小树挂在大树下，避免树越来越深，影响find操作效率，
                                                # 根节点parent可以设置为（-集合节点数）
        self.data = data
        self.parent = parent

def find(S, x): # 这是优化后的代码。。。
    # 找到
    # x_index = -1
    # for i in range(len(S)): # 循环下标而已，需要考虑待循环的下标，有时不如while来的简洁。。，f
    #     if S[i].data == x:
    #         x_index = i
    #         break
    #
    #
    # # 找到其根节点
    # if x_index!=-1:
    #     # 迭代算法中，在纸上理清迭代过程（当前所处的位置，以及迭代循环的条件是什么），然后代码实现之
    #     while S[x_index].parent>=0: # 循环的条件经常出问题，可以先写循环体，最后再补上循环的条件
    #         x_index = S[x_index].parent
    # return x_index # if x_index = -1 ，直接走到这里return了出去

    i = 0
    # python中没有for循环，对for循环最自然的改写就是while循环了
    while i < len(S) and S[i].data != x:  # while 是迭代的本质
        i+=1
    if i >= len(S):
        return -1

    while S[x_index].parent >= 0:  # 循环的条件经常出问题，可以先写循环体，最后再补上循环的条件
        x_index = S[x_index].parent
    return x_index


def union(s, x1, x2):
    root1 = find(s, x1)
    root2 = find(s, x2)
    # if root1!=root2:
    #     s[root2].parent = root1

    if root1!=root2:
        # 小集合并入大集合，根据集合的元素个数尔雅
        if s[root1].parent < s[root2].parent: # root1含的元素个数多
            s[root1].parent += s[root2].parent
            s[root2].patent=root1
        else:
            s[root2].parent+=s[root1].parent
            s[root1].parent=root2



