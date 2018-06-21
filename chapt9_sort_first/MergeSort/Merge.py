#encoding:utf-8
'''
将两个有序序列归并成一个序列
'''
def merge(list, L, R, rightEnd, tempList):
    LStart = L
    merge1(list, L, R, rightEnd, tempList)
    # 倒回
    for i in range(LStart, rightEnd+1):
        list[i] = tempList[i]

def merge1(list, L, R, rightEnd, tempList):
    leftEnd = R-1 # 假设两个序列紧挨着
    T = L
    while L<=leftEnd and R<=rightEnd:
        if list[L]<=list[R]:
            tempList[T] = list[L]
            L+=1
        else:
            tempList[T] = list[R]
            R+=1
        T+=1
    while L<=leftEnd:
        tempList[T] = list[L]
        L+=1
        T+=1
    while R<=rightEnd:
        tempList[T] = list[R]
        R+=1
        T+=1


if __name__ == '__main__':
    list = [1,3,7,2,4]
    tempList = [0]*len(list)
    merge1(list,0,3,4,tempList)
    print list
    print tempList
