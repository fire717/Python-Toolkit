# -*- coding: utf-8 -*-

#如果python程序要同时执行许多事务，那么开发者经常需要协调这些事务。
#而在各种协调方式中，较为高效的一种，则是采用函数管线（pipeline） / 类似流水线

#涉及阻塞式I/O操作或子进程的工作任务，尤其适合用此办法处理。

#内置的queue模块 
#好像只有python3有
from queue import Queue
queue = Queue() 

def consumer():
    print('Consumer waiting')
    queue.get()
    print('Consumer done')

thread = Thread(target=consumer)
thread.start()

print('producer putting')
queue.put(objecy())
thread.join()
print("producer done")

'''
管线是一种优秀的任务处理方式，它可以把处理流程划分为若干阶段，并使用多条python线程来同时执行这些任务

构建并发式的管线时，要注意许多问题，其中包括：如何防止某个阶段陷入持续等待的状态之中、如何停止工作线程、如何防止内存膨胀等

Queue类提供的机制，可以彻底的解决上述问题，它具备阻塞式的队列操作、能够指定缓冲区尺寸，还支持join方法，可构建健壮的管线
'''
