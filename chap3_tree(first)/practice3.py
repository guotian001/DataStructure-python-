# encoding:utf-8


class Stack:
    def __init__(self,maxSize = 20):
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

# 二叉树结点
class TNode:
    def __init__(self, data, left=None, right = None):
        self.data = data
        self.left = left
        self.right = right

'''
6
Push 1
Push 2
Push 3
Pop
Pop
Push 4
Pop
Pop
Push 5
Push 6
Pop
Pop

3 4 2 6 5 1


由堆栈操作可以得到一颗唯一的二叉树，输出这个树的后序遍历序列

'''

# 思路: push的时候看栈顶元素的left是否已经有值，pop的时候也看栈顶元素的left是否有值
def buildTree():

    N = input()
    count = 2*N-1
    s = Stack(N)
    root_data = int(raw_input()[-1])
    root = TNode(root_data)
    s.push(root)
    pre = None # pre记录pop之前的栈顶，
    while count:
        desc = raw_input()
        # if == push X:
        if 'Push' in desc:
            X = desc[-1]
            temp = TNode(X)
            if not s.is_empty() and s.get_top().left == None:
                s.get_top().left = temp
                s.push(temp)
            else: # 走到这一步说明一定pop过，即pre不为None
                pre.right = temp
                s.push(temp)
        else: # pop
            if s.get_top().left == None: # 尚未赋值
                s.get_top().left = None
                pre = s.pop() # 更新pre
            else:
                # 已经被赋值
                pre.right=None
                pre = s.pop() # 更新pre
        count-=1
    return root

def postOrderTraval(tree):
    if tree:
        postOrderTraval(tree.left)
        postOrderTraval(tree.right)
        print tree.data,

def main():
    tree = buildTree()
    postOrderTraval(tree)

main()