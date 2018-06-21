#encoding:utf-8
'''
表排序，如果元素本身移动起来比较困难的话，通过定义一组指针指向这些元素，然后通过移动这些指针来达到间接对元素进行排序

就好比用小纸条来代替小张、小明。。。通过移动这些小纸条来对他们进行排序


物理排序： 利用环：如何判断环的结束？在放在正确的位置后，间table更新，当找到的是table[i]=i时，说明，环即将结束，将temp拿过来环即结束


'''
class elem:
    def __init__(self, key=None, size=0):
        self.key = key # 用来排序
        self.size = size


def replaceA(A, index, next):
    A[index] = A[next]

# 物理排序，利用环
def physicSort(A, table, N):
    for i in range(N):
        if table[i]!=i:
            # 环
            # 先用最基础的方法将过程反应出来，不要害怕定义太多的指针变量，因为后面有需要的话，可以在此基础上进行删减修改来提高效率，
            # 由易到难，先给出个基础版的/朴实版的
            # 像作文一样，后面有需要的话可以进行修缮
            # 先给出基础版本，有需要的话再给出美化版本
            index = i
            next = table[index] # next也可以写在下面的代码中
            temp = A[index]
            while table[next]!=next:
                # 处理操作
                replaceA(A, index, next)
                table[index] = index
                # 更新
                index = next
                next = table[index]
            A[index] = temp
            table[index] = index


def insertionSort(A, table, N):
    for i in range(1, N):
        temp = A[table[i]].key
        j = i
        while j>0 and A[table[j-1]].key>temp:
            table[j] = table[j-1]
            j-=1
        table[j] = i

def TableSort(A, N):
    # A的移动非常耗费时间，故用数组指针替代
    table = [i for i in range(N)]
    # 数组指针的交换很简单，则对其可以调用前面学过的排序算法
    # eg: 插入算法
    insertionSort(A, table, N)
    # 输出A的顺序
    for i in range(N):
        print A[table[i]].key
    print '------------------------'
    # 物理排序
    physicSort(A, table, N)
    for i in range(N):
        print A[i].key

#############
if __name__ == '__main__':
    A = []
    A.append(elem('f'))
    A.append(elem('d'))
    A.append(elem('c'))
    A.append(elem('a'))
    A.append(elem('g'))
    A.append(elem('b'))
    A.append(elem('h'))
    A.append(elem('e'))

    TableSort(A, len(A))