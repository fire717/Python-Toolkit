# -*- coding:utf-8 -*-


#初始化父类的传统方式，是在子类里用子类实例直接调用父类的__init__方法。

class MyBaseClass(object):
    def __init__(self,value):
        self.value = value


class MyChildClass(MyBaseClass):
    def __init__(self):
        def __init__(self):
            MyBaseClass.__init__(self,5)

#这种办法对于简单的继承体系可行，但在许多情况下会出问题。

#使用内置的super函数
'''
Python2有两个问题：
1.super语句很麻烦。必须指定当前所在的类和self对象，且指定相关的方法名称（通常是__init__）以及那个方法的参数。
2.调用super时，必须写出当前类的名称。由于我们以后很可能会修改类体系，所以类的名称也可能变化，那时，必须修改每一条super调用语句才行。

Python3则没有这些问题
（py3可以通过__class__变量准确引用当前类，但py2没有定义__class__ / py2是用特殊的方式实现super的）
'''

'''
python采用标准的方法解析顺序来解决超类初始化次序及钻石继承问题

总是应该使用内置的super函数来初始化父类
'''
