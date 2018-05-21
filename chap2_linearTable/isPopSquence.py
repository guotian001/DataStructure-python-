# encoding:utf-8
# list实现一个栈
# list 作为栈
class Stack:
    def __init__(self,maxSize = 8):
        self.data = []
        self.maxSize = maxSize
    def is_full(self):
        return len(self.data) == self.maxSize
    def push(self, X):
        if self.is_full():
            return False
        else:
            self.data.append(X)
            return True
    def is_empty(self):
        return len(self.data) == 0
    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.data.pop()
    def get_top(self):
        if self.is_empty():
            return None
        else:
            return self.data[-1]

# 堆栈模拟，看是否能够得到出栈顺序，因为是模拟所以应该入栈再出栈
'''
遍历出栈序列，
    对于其中任一元素k，
        查看当前栈是否为空，
            若为空或栈顶元素不等于k，则根据入栈序列进行入栈，直至入栈序列中的元素k入栈。
            若直至入栈序列末尾仍无k，说明出栈序列错误。
            入栈完成后，将k出栈。
如上述操作，直至完成出栈序列遍历，说明出栈序列正确


因为栈顶元素一定先出，所以比较栈顶元素与当前元素，若不相等则只能往后找，即只能继续入栈直到等于当前元素
'''
'''
    怎么写出算法，在纸上将思路走一遍，最后能够分成几个步骤，清晰每个步骤的操作，这样之后那些边边角角的情况自然就好考虑些了，当然这些特殊边界的问题也要照顾到
    
'''
def isPopSquence(inSeq, outSeq, M):
    if not len(inSeq):
        return False
    j = 0 # 不是n平方的复杂度
    s = Stack(M)
    for i in range(len(outSeq)):
        curr = outSeq[i]
        while j < len(inSeq) and s.get_top() != curr:
            # 栈顶元素与curr不相等，因为是与栈顶元素的比较，所以需要入栈再出栈
            if s.push(inSeq[j]):
                j += 1
            else:
                return False
        if s.get_top() == curr: # 包含了j == len(inSeq)并且s.get_top() == curr的情形
                                # 搞不清楚的时候，找张纸，清晰的画出过程，比如引用变量啦，下标变量的迭代更替啦，
                                # 一定要把变量指到哪里了搞搞清楚，因为这涉及到边界的问题，
                                # 结合着个具体的小例子，就能轻易的将这些过程写出来，虽然如果不结合过程来看这些代码 仍然是不clear的
                                # 也就是说：不论写还是看算法的代码，都最好结合个具体的小例子（测试样例），尤其当你搞不太清楚的时候
                                # 由具体到一般
                                # 找张草稿纸先，
            s.pop()
        elif j == len(inSeq):
            return False
    return True



'''
    下标比较法
    思路： 对out 中的每个元素，其后比其小的元素都是降序排列的
    复杂度应该也是O(n)的，最坏情况所有元素遍历一遍
'''
def isPopSquence_compare(inSeq, outSeq):
    if not len(outSeq):
        return False
    # 识别出序列的下标
    index_list = get_index_list(inSeq, outSeq)
    while len(outSeq):
        a = temp = outSeq[0] # 头
        for j in range(i+1, len(outSeq)):
            if a > outSeq[j]: # 比较过一次的,如果没有false，应该移除掉，再下一个的后面肯定不会有问题
                if temp > outSeq[j]:
                    temp = outSeq[j]
                    outSeq.remove(temp)
                else:
                    return False
        outSeq.remove(a)
    return True


def get_index_list(inSeq, outSeq):
    result = []
    for i in range(len(outSeq)):
        result.append(inSeq.index(outSeq[i]))
    return result
'''
10 7 5 
1 2 3 4 5 6 7
3 2 1 7 5 6 4
7 6 5 4 3 2 1
5 6 4 3 7 2 1
1 7 6 5 4 3 2

YES
NO
YES
YES
YES
'''

def readList():
    desc = raw_input()
    return map(int,  desc.strip().split())

def main():
    firstList = readList()
    M = firstList[0]
    N = firstList[1]
    K = firstList[2]

    inSeq = [i for i in range(1, N+1)]
    result = []
    while K:
        outSeq = readList()
        result.append('YES' if isPopSquence(inSeq, outSeq, M) else 'NO')
        K -= 1
    for i in range(len(result)):
        print result[i]
main()