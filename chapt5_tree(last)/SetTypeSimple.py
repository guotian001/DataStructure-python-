# encoding:utf-8
'''
集合的简化表示，集合中的元素都可以用连续的非负整数来表示，所以只需要一个整形的数组，下标数组的下标i就代表着集合的第i个元素，数组中存的值是这第i个
元素的父节点的下标，也就是说data与i相等了。。。
'''


def find(s, x):
    # 默认集合元素全部初始化为-1
    while s[x] >= 0:
        x = s[x]
    return x


def union(s, root1, root2):
    # 这里默认Root1和Root2是不同集合的根结点
    s[root2] = root1
