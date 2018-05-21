#encoding:utf-8
'''
给定一个整数序列，求该正整数序列的和最大子列,若其 <0, 则给出0

    最大子列，
    问题： 在于 子列首、尾两个变量在变化，
    办法： 先定住一个/或者先找一个锚点（发起点），单一变量法，复杂问题转换成基本问题，这样才有办法入手，有处下嘴

'''


'''
    智障解法
    1.找到所有的子序列，（两个for循环）
    2.从左至右依次计算子列和（智障的一步）
'''
# N 是数组的长度
def maxSubsquence1(A, N):
    maxSum = 0
    for i in range(N):
        for j in range(i, N):
            thisSum = 0 # thisSum是从 i到j 的子列和
            for k in range(i, j+1):
                thisSum = thisSum + A[k]
                if thisSum > maxSum:
                    maxSum = thisSum
    return maxSum

'''
    正常 遍历 思路
    找到所有的子序列，（两个for循环）,然后计算每个子序列的和就是了
'''
def maxSubsquence2(A, N):
    maxSum = 0
    for i in range(N):
        thisSum = 0
        for j in range(i, N):
            thisSum += A[j]
            if thisSum > maxSum:
                maxSum = thisSum
    return maxSum

'''
    分而治之法：
        从中点将序列分为左右两个，则最大序列在 1.左子序列最大值、2.右子序列最大值，3.跨越边界的最大值 间
        1和2可以递归求出
        3？ 从分界线（锚点）向左遍历找到max1,向右max2,则跨越边界的最大值是max1 + max2(注意小于0时要取0)，
        因为通过锚点将max1和max2连接起来的仍是原问题的子列，相当于通过分界线将两者粘起来了
'''
def maxSubsquence3(A, N):
    return divideAndConquer(A, 0, N-1) # 居然能忘了return。。。

def divideAndConquer(A, left, right): # 递归，显然这些边界应该用变量，因为他们是变化的啦
    # 递归结束条件
    if left == right:
        return A[left] if A[left] > 0 else 0 # [惊讶脸] python中的三目运算。。。
    mid = (left + right) /2
    maxLeft = divideAndConquer(A, left, mid) # 左边最大值
    maxRight = divideAndConquer(A, mid + 1, right) # 右边最大值
    # 跨边界最大值
    # 左
    maxLeftBorder = 0
    leftBorder = 0
    for i in range(mid, left-1, -1):  # 边界要写对哦
        leftBorder += A[i]
        if leftBorder > maxLeftBorder:
            maxLeftBorder = leftBorder
    # 右
    maxRightBorder = 0
    rightBorder = 0
    for i in range(mid+1, right+1):
        rightBorder += A[i]
        if rightBorder > maxRightBorder:
            maxRightBorder = rightBorder
    return max3(maxLeft, maxRight, maxLeftBorder + maxRightBorder)
def max3(A,B,C):
    maxInAB = A if A > B else B
    return maxInAB if maxInAB > C else C

'''
    在线（online）处理： 
        依次读入，当目前子列的和为负的时候，它对后进入的数字已经没有正的作用了，因此，应该抛弃（设为0），后面的相当于重新开始
        想法还是比较巧妙的
'''
def maxSubsquence4(A, N):
    maxSum = 0
    thisSum = 0
    for i in range(N):
        thisSum += A[i]
        if thisSum > maxSum: # 更新right
            maxSum = thisSum
        elif thisSum < 0: #  **********核心代码***********
            thisSum = 0 # 起不到正的作用，应该抛弃（设为0就相当于抛弃），从新的left开始 #更新left
    return maxSum

############################## test #########################

# A = [-1, -1,2,-2,8]
# print maxSubsquence1(A, len(A))
# print maxSubsquence2(A, len(A))
# print maxSubsquence3(A, len(A))
# print maxSubsquence4(A, len(A))

N = input('K:')
ARaw = input('list:')
print N
print ARaw

A = [1,2,3]
A.reverse()