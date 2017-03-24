 # -*- coding:utf-8 -*-



'''
如果想复用@property方法及其验证机制，那么可以自己定义描述符类

WeakKeyDictionary可以保证描述符类不会泄露内存

通过描述符协议来实现属性的获取和设置操作时，不要纠结于__getattribute__的方法具体运作细节
'''
