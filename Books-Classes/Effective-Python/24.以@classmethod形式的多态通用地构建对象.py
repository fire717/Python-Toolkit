 # -*- coding:utf-8 -*-


#python中对象支持多态，类也支持多态



#从上条开始的内容就不怎么熟悉了，所以先简单摘录吧..

class GenericInputData(object):
    def read(self):
        raise NotImplementedError

    @classmethod  #这种形式的多态针对整个类
    def generate_inputs(cls,config):
        raise NotImplementedError


'''
Python程序中，每个类只能有一个构造器，即__init__方法。

通过@classmethod机制，可以用一种与构造器相仿的方式来构造类的对象。

通过类方法多态机制，我们能够以更加通用的方式来构建并拼接具体的子类。
'''
