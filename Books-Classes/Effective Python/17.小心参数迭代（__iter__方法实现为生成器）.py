# -*- coding:utf-8 -*-


#迭代器智能产生一轮结果。在抛出过StopIteration异常的迭代器或生成器上继续迭代第二轮是不会有结果的
#在已用完的迭代器上继续迭代不会报错...因为区分不了StopIteration异常是因为迭代器本来就没有输出值还是本来有但是用完了
#解决方法：新编一种实现迭代器协议的容器类
'''
pyhton在for循环及相关表达式中遍历某种容器的内容时，就要依靠这个迭代器协议。
在执行类似for x in foo这样的语句时，python实际上会调用iter(foo)。内置的iter函数又会调用foo.__iter__这个特殊方法。
该方法必须返回迭代器对象，而那个迭代器本身则实现了名为__next__的特殊方法。
此后，for循环会在迭代器对象上反复调用内置的next函数，直至耗尽并产生StopIteration异常。
'''
class ReadVisits(object):
    """docstring for ReadVisits"""
    def __init__(self, data_path):
        self.data_path = data_path
    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)

'''
Python的迭代器协议，描述了容器和迭代器应该如何与iter与next内置函数、for循环及相关表达式相互配合。

把__iter__方法实现为生成器，即可定义自己的容器类型

想判断某个值是迭代器还是容器，可以拿该值为参数，两次调用iter函数，若结果相同，则是迭代器，调用内置的next函数，即可令该迭代器前进一步
'''
