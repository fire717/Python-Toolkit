# -*- coding: utf-8 -*-

def palindrome(i):
    """return true if the given i is a palindrome"""
    return i == i[::-1]

print(repr(palindrome.__doc__))
#通过__doc__属性返回文档

#每个模块、类、函数都应有顶级的docstring
#放在最前面，第一行一般描述功能，且用双引号

'''
通过docstring编写文档，修改代码时也要更新文档

文档应介绍本模块的内容，且列出重要函数

为类编写文档时应在class语句下的docstring介绍本类的行为、属性，及子类该实现的方法

为函数的docstring应介绍每个参数，函数的返回值，函数在执行中可能抛出的异常等。
'''
