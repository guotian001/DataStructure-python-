/***
    python 不晓得数组怎么用，故顺序表用java实现
****/
public class sequenceList {
    int last;
    int MAXSIZE;
    int ERROR = -1;
    Object[] data = new Object[MAXSIZE];


    // 创建空表
    sequenceList makeEmpty() {
        sequenceList list = new sequenceList();
        list.last = -1;
        return list;
    }

    // 查找元素的下标，不存在
    int find(Object x, sequenceList list) {
        int i = 0;
        while (i <= list.last && !x.equals(list.data[i])) {
            i++;
        }
        if (i > list.last) {
            return ERROR;
        } else {
            return i;
        }
    }
    // 插入
    // postion 存储下标，从0开始
    Boolean insert(sequenceList list, Object X, int position) {
        if (list.last == MAXSIZE-1) { // maxsize 为数组长度，下标从0开始
            System.out.println("表满");
            return false;
        }
        if (position < 0 || position > list.last+1){ // 保持顺序，不能最大为插入末尾（last+1）
            System.out.println("插入位置不合法");
            return false;
        }
        // 依次将position及其后的元素后移，并将X放在position上
        for (int i = list.last;i >= position; i--){
            list.data[i+1] = list.data[i];
        }
        list.data[position] = X;
        list.last++; // 不要忘记更新last
        return true;
    }

    // 注意:在删除位置参数P上与课程视频有所不同，课程视频中i是序列位序（从1开始），这里P是存储下标位置（从0开始），两者差1
    Boolean delete(int position, sequenceList list) {
        if (position < 0 || position > list.last) { // <= last，互斥条件是>last
            System.out.println("不存在第"+position+"个元素");
            return false;
        }
        // 删除，将position后面的元素依次前移
        for (int j = position+1;j <= list.last; j++) {
            list.data[j-1] = list.data[j];
        }
        // 更新last
        list.last--;
        return true;
    }
}
