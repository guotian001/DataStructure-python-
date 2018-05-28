# encoding:utf-8
'''
判断给定的二叉搜索序列是否合理

思路：

    每遍历一次都缩小了下一个值可能出现的范围，即更新了范围的边界，因此，不如将这两个边界提出来做全局变量，
        每遍历一个，先考虑其是否满足边界条件， 再根据其与其前一个的关系更新范围边界

    设置两个哨兵min， max，给出一个区间
    每次向右，更新min；向左，更新max
    然后判定是否在当前区间内[min, max]，即是否合理

'''

def isSearchSequenece(list):
    min = float('-inf')
    max = float('inf')
    for i in range(1, len(list)):
        pre = list[i-1]
        curr = list[i]
        if curr > min and curr < max:
            # 满足条件， 更新边界
            if curr > pre:
                min = pre
            else:
                max = pre
        else:
            return False
    return True


## 或者利用，online方法，思路更加清晰：


def isSearchSequenece2(seq):

    min_ = float('-inf')
    max_ = float('inf')
    pre = seq[0]
    for i in range(1, len(seq)):
        if seq[i] > max_ or seq[i] < min_:
            return False
        else:
            # 更新边界
            if seq[i] > pre:
                min_ = pre
            else:
                max_ = pre
            # 更新pre
            pre = seq[i]
    return True


########### test  ##########

list1 = [30, 41, 33, 35, 34] # true
list2 = [30, 41, 50] # true
list3 = [30, 41, 33, 51] # false
list4 = [30, 41, 50, 33] # false

print isSearchSequenece2(list1)
print isSearchSequenece2(list2)
print isSearchSequenece2(list3)
print isSearchSequenece2(list4)