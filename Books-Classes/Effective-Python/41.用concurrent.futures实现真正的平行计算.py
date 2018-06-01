# -*- coding: utf-8 -*-

'''
把引发CPU性能瓶颈的那部分代码，用C语言扩展模块来改写，即可在尽量发挥python特性的前提下，有效提升程序的执行速度。
但是这样做的工作量比较大，而且可能会引入bug。

multiprocessing模块提供了一些强大的工具。对于某些类型的任务来说，开发者只需要编写少量代码，即可实现平行计算。
*该做法会以子进程的形式，平行的运行多个解释器，从而令python程序能够利用多核心CPU。

若想利用强大的multiprocessing模块，最恰当的做法，就是通过内置的concurrent.futures模块以及其ProcessPoolExecutor类来使用它。

multiprocessing模块所提供的那些高级功能，都特别复杂，所以开发者尽量不要直接使用它们。
'''
