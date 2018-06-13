#encoding:utf-8
'''
堆：
    ① 优先队列的一种有效表示（数据结构），
    ② 两个特性：
        1. 结构性：完全二叉树（数组表示，方便）（完全二叉树为了保证树的平衡，提高效率）
        2. 有序性：任意结点的关键值是其子树所有结点的最大值，即任意结点的关键值都比其左右子结点的关键值大（递归定义）（最大堆）
                  从 根结点 到 任意结点 所经路径 上的结点序列的有序性（最大堆递减，最小堆递增）

主要操作：插入和删除
'''
maxData = float('inf')
class Heap:
    # 堆的创建操作
    def __init__(self, maxSize):
        self.elements = [None]*(maxSize+1) # 堆的存储从下标1开始
        self.size=0
        self.capacity=maxSize
        '''
            maxData 最大的元素，所以插入的元素总是比它小，也就是说插入的元素不会到下标0位置，即不会破坏存储结构（从0开始存储）
    
            优点： 只有当插入的元素是堆中最大的元素的时候，才会有与maxData的比较
            而如果使用下标判断的话（&&i>1），每插入一个元素都需要进行下标的比较
        '''
        self.elements[0]=maxData # 定义一个哨兵，插入操作时有用

    def isFull(self):
        return self.size == self.capacity
    # 插入
    '''
        插入一个元素时，增加一个新的结点保持结构性，
        *** 保证有序性，从结点出发，找到其所在的位置，肯定位于结点到根节点的路径上，***
        *** 向上比较，移动，每比较一次就移动一次（刚好能腾出来一个坑放置元素）     ***
            
            从该结点位置出发，比较其父节点与item的大小，
            如果小于item，则，父节点下移，移动到父节点位置，循环
            否则，将item放在该位置即可
    '''
    def insert(self,item):
        if self.isFull():
            print '最大堆已满'
            return False
        ### 向下过滤 ###

        # item应该位于从i到根节点的路径上，采用比较一个，移动一个的操作（刚好有坑，新建出来的）
        # 其实上述算法是从交换改进得到的，交换：将item放在i位置，然后依次向上比较，如果item>父节点 ,则进行交换，
        # 从交换改进成移动（最后腾出来一个坑，填进去就好了，这样item就不用动来动去，一步到位），提升了一点效率

        i = self.size+1 # 添加一个新的结点, 从这个结点开始
        # 找到待插入元素的位置，并将相关元素下沉
        while item > self.elements[i/2]: # 与i的父节点比较关键值
            self.elements[i] = self.elements[i/2] #父节点下移到相应子节点
            i/=2
        # 父节点不小于item，将item放在对应的子节点上
        self.elements[i] = item # i>=1 ，因为self.elements[0]=maxData，所以设置这个哨兵，保证结构不被破坏，
                                # 并且只在item比堆中的元素都大时才需要进行比较
        return True


    def insert(self,item):
        if self.isFull():
            print '最大堆已满'
            return False
        self.size+=1
        i = self.size
        # item应该位于从i到根节点的路径上，采用比较一个，移动一个的操作（刚好有坑，新建出来的）
        # 其实上述算法是从交换改进得到的，交换：将item放在i位置，然后依次向上比较，如果item> ,则进行交换，
        # 从交换改进成移动（最后腾出来一个坑，填进去就好了，这样item就不用动来动去，一步到位），提升了一点效率
        while item > self.elements[i/2]:
            self.elements[i]=self.elements[i/2]
            i/=2
        self.elements[i]=item
        return True


    def isEmpty(self):
        return self.size==0

    # 删除操作
    '''
        删除的是最大元素（根节点）
        保证结构性，将数组最后一个元素（item）放到根节点上，然后调整其到正确的位置即可（保证结构性）
            1. 根节点上的元素应该大于左右子节点，如果小于，则应调整，将左右子节点中的较大者交换到根节点位置
            2. item到较大子节点上，并且现在其位于子树的根节点上，因此循环进行上述交换过程
        与插入情况类似，用移动替代交换操作（少一次赋值），因此，需要记录待插入位置，并更新之然后循环直到边界
    '''
    def deleteMax(self):
        if self.isEmpty():
            print '最大堆一空'
            return None
        temp = self.elements[self.size]
        self.size-=1
        maxItem = self.elements[1]
        # 从1开始
        parent=1
        while parent*2 <= self.size: # 循环直到没有子节点
            # 找到最大的child
            child = parent*2
            if child!=self.size and self.elements[child] < self.elements[child+1]:
                child = child+1
            # child 现在是最大子节点
            if temp < self.elements[child]:
                self.elements[parent] = self.elements[child] # 上浮
                parent = child
            else:
                break
        self.elements[parent] = temp
        return maxItem

    # i 的左右子树都是堆，对结点i进行调整
    def percDown(self, i):
        temp = self.elements[i]
        parent = i
        while 2*parent <= self.size:
            child = 2*parent
            if child != self.size and self.elements[child] < self.elements[child+1]:
                child+=1
            if temp < self.elements[child]:
                self.elements[parent] = self.elements[child]
                parent = child
            else:
                break
        self.elements[parent] = temp

    # 线性时间复杂度构建堆
    # 时间复杂度证明？
    def buildHeap(self, list):
        self.__init__(2*len(list))
        self.elements[1:] = list
        self.size = len(list)
        # 调整方法：如果结点的左右子树都是堆，那么调整结点使该树成为堆即可，叶子结点可以看做堆
        # 从最后一个有子结点的结点开始调整，叶子结点看做堆
        for i in range(self.size/2,0,-1):
            self.percDown(i)



##########################   test ###########
h = Heap(20)
list = [79,66,43,83,30,87,38,55,91,72,49,9]
h.buildHeap(list)
print h.elements[1:]

h2 = Heap(10)
h2.insert(18)
h2.insert(10)
h2.insert(25)
h2.insert(31)
h2.insert(44)
print h2.elements[1:h2.size+1]
h2.deleteMax()
print h2.elements[1:h2.size+1]














