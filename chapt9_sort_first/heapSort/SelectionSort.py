#encoding:utf-8
'''
选择排序，每次挑出最小的元素，放在已排序好的序列的末端
'''
INFINITE = float('inf')
def scan4Min(list, i, k):
    min_ = INFINITE
    minPosition = i-1
    for i in range(i, k+1):
        if list[i]<min_:
            min_ = list[i]
            minPosition = i
    return minPosition

def swap(list, i, minPostion):
    temp = list[i]
    list[i] = list[minPostion]
    list[minPostion] = temp

def selectionSort(list, N):
    for i in range(N):
        minPostion = scan4Min(list, i, N-1)  # 显然scan算法有改进的空间
        swap(list, i, minPostion)

#################

if __name__ == '__main__':
    list = [1,2,4,5,7,22,33,555,4]
    selectionSort(list, len(list))
    print list