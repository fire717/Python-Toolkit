 # -*- coding:utf-8 -*-


#通用代码的动态行为，可以通过__getattr__特殊方法来做
#若某个类定义了__getattr__,同时系统在该类对象的实例字典中又找不到待查的属性，那么系统就会调用这个方法
class LazyDB(object):
    """docstring for LazyDB"""
    def __init__(self):
        self.exists = 5
        
    def __getattr__(self,name):
        value = 'Value for %s' % name
        setsttr(self,name,value)
        return value
#适合实现无结构数据（无模式数据）的按需访问


#__getattribute__，程序每次访问对象时都会调用这个，即使属性字典已有该属性
#这样就可以在程序每次访问属性时检查全局事物状态


#赋值后以惰性的方式退回数据库，可用__setattr__
#它也可以拦截对属性的赋值操作。只要对实例的属性赋值，无论是直接赋值，还是通过内置的setattr函数赋值，都会触发__setattr__方法

'''
通过__getattr__和__setattr__，我们可以用惰性的方式加载保存对象的属性

要理解__getattr__和__getattribute__的区别：前者只会在带访问的属性缺失时触发，而后者则会在每次访问属性时触发

若要在__getattribute__和__setattr__方法中访问实例属性，那么应该直接通过super()（也就是object类的同名方法）来做，以避免无限递归
'''

 
