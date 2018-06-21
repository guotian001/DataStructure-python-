#encoding:utf-8
'''
希尔排序
    在插入排序的基础上改进得到
'''

def Shellsort(list, N):
    # 原始希尔序列, 还有别的增量序列
    D = N/2
    while D>0:
        # 插入排序
        for i in range(D, N):
            temp = list[i]
            j = i
            # 一次摸牌
            while j>=D and temp<list[j-D]:# 前面已经有序，一旦找到就可以停止
                list[j] = list[j-D]
                j-=D
            list[j] = temp

        D/=2 # 进入下一个间隔
    return list


def Shellsort_Sedgewick(list, N):
    # Sedgewick序列
    # / *这里只列出一小部分增量 * /
    Sedgewick = [929, 505, 209, 109, 41, 19, 5, 1, 0]
    k = 0
    while Sedgewick[k]>=N:# 初始的增量Sedgewick[Si]不能超过待排序列长度
        k+=1

    D = Sedgewick[k]
    while D>0:
        # 插入排序
        for i in range(D, N):
            temp = list[i]
            j = i
            # 一次摸牌
            while j>=D and temp<list[j-D]:# 前面已经有序，一旦找到就可以停止
                list[j] = list[j-D]
                j-=D
            list[j] = temp

        # 进入下一个间隔
        k+=1
        D = Sedgewick[k]


if __name__ == '__main__':
    list = [4,1,22,5100,4,88,5,444]
    Shellsort_Sedgewick(list, len(list))
    print list

