 # -*- coding:utf-8 -*-
import subprocess
#并发：交错执行程序
#并行：利用多核真正的并行
'''
用python编写并发程序很容易，也可以通过系统调用、子进程和C语言扩展等机制平行的处理一些事。
但要使并发式的python代码以真正平行的方式来运行相当困难。
所以我们要最为恰当的利用python提供的特性
'''
#现在的python最简单最好用的子进程管理模块——内置的subprocess
#用Popen构造器启动进程，然后用communicate方法读取子进程的输出信息并等待终止
proc = subprocess.Popen(['echo','hello from the child!'],stdout=subprocess.PIPE)
out,err = proc.communicate()
print out.decode('utf-8')
#运行报错...WindowsError: [Error 2] 查了下py2.4就有了呀...

procs=[]
#启动多个子进程：
for _ in range(10):
    proc = run_sleep(0.1)
    procs.append(proc)

'''
用subprocess模块运行子程序，还可以管理输入输出流

python解释器能平行地运行多条子进程，开发者可以充分利用cpu

可以给communicate传入timeout参数，以免子进程死锁或失去响应。
但只在py3.3以后才有timeout。
老版本需要内置的select模块来处理
'''
