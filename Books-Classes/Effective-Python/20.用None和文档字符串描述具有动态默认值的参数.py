# -*- coding:utf-8 -*-
import time
#使用动态参数作为默认值
#一般写法：
def log(message,when=time.asctime( time.localtime(time.time()) )): #最简单的获取可读的时间模式的函数是asctime()
    print('%s: %s' % (when,message))

log('hi there!')
time.sleep(1)
log('hi again')
#会发现两个消息时间一样
#【因为】time.asctime只在函数定义的时候执行了一次
#参数的默认值，只会在程序加载模块并读到本函数的定义时评估一次。

#正确写法
def log2(message,when=None):
    when = time.asctime( time.localtime(time.time()) ) if when is None else when
    print('%s: %s' % (when,message))
log2('hi there!')
time.sleep(1)
log2('hi again')

'''
>>输出：
Fri Mar 17 15:18:38 2017: hi there!
Fri Mar 17 15:18:38 2017: hi again
Fri Mar 17 15:18:39 2017: hi there!
Fri Mar 17 15:18:40 2017: hi again
'''

#对于以动态值作为实际默认值的关键字参数来说，应该把形式上的默认值写为None，并在函数的文档字符串里描述该默认值对应的实际行为
