# -*- coding:utf-8 -*-



###令函数接受可选的位置参数（*args）
#普通写法
def log(message,values):
    if not values:
        print message
    else:
        values_str = ', '.join(str(x) for x in values)
        print('%s : %s' %(message,values_str))

log('my number are',[1,2])
log('hi there',[])

#升级
def log(message,*values): #唯一的不同
    if not values:
        print message
    else:
        values_str = ', '.join(str(x) for x in values)
        print('%s : %s' %(message,values_str))

log('my number are',[1,2])
log('hi there') #这里就不需要传入空的[]了

'''
*args令函数接受数量可变的位置参数

调用函数时可采用*操作符，把序列中的元素当成位置参数，传给该函数

对生成器使用*操作符，可能导致程序耗尽内存崩溃（故只有当我们确定输入的参数个数较少时才能用*）

在已接受*args参数的函数上继续添加位置参数，可能会产生难以排查的bug（故应使用只能以【关键字形式指定】（参见21条）的参数来扩展）
'''
