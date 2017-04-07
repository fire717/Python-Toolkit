# -*- coding: utf-8 -*-

'''
线程的三个缺点：
1.为了确保数据安全，必须用特殊的工具协调线程
2.线程需要占用大量内存
3.线程启动时开销比较大
'''

#而协程(coroutine)可以避免上述问题
#原理其实是对生成器的扩展
'''
每当生成器函数执行到yield表达式时，消耗生成器的那段代码，就通过send方法给生成器回传一个值。
生成器收到后会将其视为yield的执行结果。
'''
def my_coroutine():
    while True:
        received = yield
        print('Received:',received)

it = my_coroutine()
next(it)
it.send('1')
it.send('2')
#>>('Received:', '1')
# ('Received:', '2')

'''
协程令程序看上去好像能够同时运行大量函数

对于生成器内的yield表达式，外部代码通过send方法传给生成器的那个值，就是该表达式所要具备的值

协程可以把程序的核心逻辑与程序同外部环境交互时所用的代码分离

py2不支持yield from表达式，也不支持从生成器内通过return语句向外界返回某个值
'''
