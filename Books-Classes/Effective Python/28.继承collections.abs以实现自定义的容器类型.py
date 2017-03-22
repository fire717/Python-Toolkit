 # -*- coding:utf-8 -*-
#大部分python编程工作都是在定义类
#python中每一个类，某种程度上来说都是容器，都封装了属性与功能
#比如设计简单的序列，可以继承内置的list

#自定义列表统计各元素出现频率的方法
class FrequencyList(list):
    """docstring for FrequencyList"""
    def __init__(self, members):
        super(FrequencyList,self).__init__(members)
         
    def frequency(self):
        counts={}
        for item in self:
            counts.setdefault(item,0)
            counts[item] += 1
        return counts
                 
foo = FrequencyList(['a','b','a','c','b','a','d'])
print 'Length is', len(foo)
foo.pop()
print 'After pop:',repr(foo)
#repr()将任意值转为字符串 / 函数得到的字符串通常可以用来重新获得该对象，repr（）的输入对python比较友好。
#函数str() 用于将值转化为适于人阅读的形式，而repr() 转化为供解释器读取的形式。
#试了下，直接输出foo也是可以的
print 'Frequency:',foo.frequency()
'''
输出：
Length is 7
After pop: ['a', 'b', 'a', 'c', 'b', 'a']
Frequency: {'a': 3, 'c': 1, 'b': 2}
'''
 
 
'''
如果要定制的子类很简单，就可以直接从python的容器类型（如list或dict）中继承。

想正确实现自定义的容器类型，可能需要编写大量的特殊方法。

编写自制的容器类型时，可以从collections.abc模块的抽象基类中继承，那些基类能够确保我们的子类具备适当的接口及行为。
'''
