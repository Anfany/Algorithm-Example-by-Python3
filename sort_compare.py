#  # -*- coding：utf-8 -*-
# &Author  AnFany



# 本文提供8种排序算法
import numpy as np
from prettytable import PrettyTable # 用表格输出时间对比
import time


paidict = {'Bubble': ['冒泡'], 'Insert': ['直接插入'],'Shell': ['希尔'],
           'Select': ['直接选择'],'Quick': ['快速'], 'Heap': ['堆'],
           'Merge': ['归并'], 'sorted': ['Python自带'], 'Radix': ['基数']}

# 直接插入排序
def Insert(listdata):
    for i in range(1, len(listdata)):
        # 设置当前值前一个元素的标识
        j = i - 1
        # 如果当前值小于前一个元素,则将当前值作为一个临时变量存储,将前一个元素后移一位
        if listdata[i] < listdata[j]:
            temp, listdata[i] = listdata[i], listdata[j]
            # 继续往前寻找,如果有比临时变量大的数字,则后移一位,直到找到比临时变量小的元素或者达到列表第一个元素
            j = j - 1
            while j >= 0 and listdata[j] > temp:
                listdata[j + 1] = listdata[j]
                j = j - 1
            # 将临时变量赋值给合适位置
            listdata[j + 1] = temp
    return listdata

# 希尔排序
def Shell(listdata):
    n = len(listdata)
    # 希尔增量
    gap = int(n / 2)
    while gap > 0:
        # 按增量进行直接插入排序
        for i in range(gap, n):
            j = i
            # 直接插入排序
            while j >= gap and listdata[j - gap] > listdata[j]:
                listdata[j - gap], listdata[j] = listdata[j], listdata[j - gap]
                j -= gap
        # 得到新的增量
        gap = int(gap / 2)
    return listdata

# 直接选择排序
def Select(listdata):
    for i in range(len(listdata) - 1):
        minnum = i
        for j in range(i + 1, len(listdata)):
            if listdata[j] < listdata[minnum]:
                minnum = j
        listdata[i], listdata[minnum] = listdata[minnum], listdata[i]
    return listdata

# 堆排序
def adjust_heap(lists, i, size):
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    max = i
    if i < size / 2:
        if lchild < size and lists[lchild] > lists[max]:
            max = lchild
        if rchild < size and lists[rchild] > lists[max]:
            max = rchild
        if max != i:
            lists[max], lists[i] = lists[i], lists[max]
            adjust_heap(lists, max, size)

# 创建堆
def build_heap(lists, size):
    for i in range(0, (int(size/2)))[::-1]:
        adjust_heap(lists, i, size)

# 堆排序
def Heap(lists):
    size = len(lists)
    build_heap(lists, size)
    for i in range(0, size)[::-1]:
        lists[0], lists[i] = lists[i], lists[0]
        adjust_heap(lists, 0, i)
    return lists

# 基数排序
def Radix(listdata):
    k = len(str(max(listdata)))  # k获取最大位数
    for k in range(k):  # 遍历位数，从低到高
        s = [[] for i in range(10)]  # 生成存放数的十个桶
        for i in listdata:  # 遍历元素
            s[i // (10 ** k) % 10].append(i)  # 分桶
        listdata = [a for b in s for a in b]  # 合并桶
    return listdata

# 归并排序
def Merge(listdata):
    n = len(listdata)

    if n == 1:
        return listdata
    mid = n // 2

    # 对分割的左半部分进行归并排序
    leftdata = Merge(listdata[:mid])
    # 对分割的右半部分进行归并排序
    rightdata = Merge(listdata[mid:])

    # 对排序之后的两部分进行合并
    # 定义两个游标
    left, right = 0, 0

    merge_result_li = []
    left_n = len(leftdata)
    right_n = len(rightdata)

    while left < left_n and right < right_n:
        if leftdata[left] <= rightdata[right]:
            merge_result_li.append(leftdata[left])
            left += 1
        else:
            merge_result_li.append(rightdata[right])
            right += 1

    merge_result_li += leftdata[left:]
    merge_result_li += rightdata[right:]

    # 将合并后的结果返回
    return merge_result_li

# 冒泡排序
def Bubble(listdata):
    for i in range(len(listdata) - 1):  # 这个循环负责设置冒泡排序进行的次数
        for j in range(len(listdata) - i - 1):  # ｊ为列表下标
            if listdata[j] > listdata[j + 1]:
                listdata[j], listdata[j + 1] = listdata[j + 1], listdata[j]
    return listdata

# 快速排序
def Quick(listdata):
    if len(listdata) == 0:
        return []
    pivots = [x for x in listdata if x == listdata[0]]
    lesser = Quick([x for x in listdata if x < listdata[0]])
    greater = Quick([x for x in listdata if x > listdata[0]])
    return lesser + pivots + greater

# 最终的主程序
if __name__ == "__main__":
    numpdata = np.arange(1, 100000)
    count = [5, 50, 500, 5000, 50000]
    # 不同数组长度，每种排序算法运行50次的平均值得对比
    colu = ['排序'] + ['%s条' % f for f in count]
    x = PrettyTable(colu)
    x.title = '不同算法用时(毫秒)对比，随机取数区间[1, 100000]'
    for pa in paidict:
        print(pa)
        timep = []
        for ci in count:
            np.random.shuffle(numpdata)
            ldata = list(np.random.choice(numpdata, ci))
            start = time.clock()
            result = eval(pa)(ldata)
            end = time.clock()
            if result == sorted(ldata):
                timep.append('%.5f' % ((end - start) * 1000))
            else:
                print('排序算法：%s错误' % pa)
        x.add_row([paidict[pa][0]] + timep)
    print(x)






