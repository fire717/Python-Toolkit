# -*- coding: utf-8 -*-

#1.双向队列
#FIFO 时间O(1)
from collections import deque
fifo = deque()
fifo.append(1) 
x = fifo.popleft()

#2.有序字典
#标准字典无序因为实现方式是快速哈希表
from collections import OrderedDict
a = OrderedDict()
a['foo'] = 1
a['bar'] = 2
b = OrderedDict()
b['foo'] = 'red'
b['bar'] = 'blue'

for value1,value2 in zip(a.values(),b.values()):
    print(value1,value2)
#>>(1, 'red')
#  (2, 'blue')

#3.带有默认值的字典
from collections import defaultdict
stats = defaultdict(int)
stats['my_counter'] += 1

#4.堆队列（优先级队列）
#堆heap是一种数据结构
#heapq模块提供了heappush、heappop、nsmallest等函数,复杂度与列表长度对数成正比

#5.二分查找
#bisect模块中的bisect_left等函数，提供了高效的二分折半搜索算法
#其返回的索引代表待搜寻的值在序列中的插入点
from bisect import *
#i = bisect_left(x,991234)
#复杂度为对数级别

#6.与迭代器有关的工具
#内置的itertools模块中包含大量函数，可以组合并操控迭代器
import itertools
help(itertools)

'''
我们应该用python内置的模块来描述各种算法和数据结构

开发者不应该自己去重新实现那些功能，因为我们很难把它写好
'''
