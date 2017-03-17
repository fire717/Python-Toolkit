# -*- coding:utf-8 -*-


#【py3】中.可以定义一种只能以关键字形式指定的参数
def xx(x1,x2,*,x3=1,x4=2):
    # *代表位置参数就此终结，之后的参数都只能以关键字形式指定
    pass
#这样就不能用位置参数的形式来指定关键字参数了

xx(1,2,3,4)#报错
xx(1,2,x3=3,x4=4)#OK

#【py2】没有这种语法
#可在参数列表中使用**操作符，且令函数在遇到无效的调用时抛出TypeError异常，也可实现与py3相同的功能。
#**操作符与*类似，区别在于，它不是用来接收数量可变的位置参数，而是用来接收任意数量的关键字参数（即便没有定义在函数中）
def print_args(*args,**kwargs):
    print 'positional:',args
    print 'keywords:',kwargs

print_args(1,2,foo='bar',stuff='meep')

'''
先令该函数接受**kwargs参数，然后用pop方法把期望的关键字参数从kwargs字典取走，
若字典的键里没有那个关键字，则pop方法的第二个参数就会成为默认值
最后，为了防止无效调用，我们需要确认kwargs字典里已经没有关键字参数了
'''
def safe_division_d(number,divisor,**kwargs):
    ignore_overflow = kwargs.pop('ignore_overflow',False)
    ignore_zero_div = kwargs.pop('ignore_zero_div',False)
    if kwargs:
        raise TypeError('Unexpected **kwards:%r' % kwargs)

safe_division_d(1,10)
safe_division_d(1,0,ignore_zero_div=True)
safe_division_d(1,10**500,ignore_overflow=True)

#此时不能以位置参数的形式来指定关键字参数的值
safe_division_d(1,0,False,True) #会报错

#也不能传入不符合预期的关键字参数
safe_division_d(1,0, unexpected=True) #报错

'''
关键字参数能够使函数调用的意图更加明确

对于各参数之间容易混淆的函数，可以声明只能以关键字形式指定的参数，确保调用者必须通过关键字来指定他们。
对于接受多个Boolean标志的函数，更应该这么做
'''
