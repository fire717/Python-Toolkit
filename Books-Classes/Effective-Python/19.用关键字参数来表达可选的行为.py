# -*- coding:utf-8 -*-


#python函数可按位置传递参数
def remainder(number,divisor):
    return number % divisor

assert remainder(20,7)==6

#而所有位置参数都可以按关键字传递，且顺序不限，只要把位置参数全部指定即可
#等效调用方法：
remainder(20,7)
remainder(20,divisor=7)
remainder(number=20,divisor=7)
remainder(divisor=7,number=20)
###但【位置参数】【必须】出现在【关键字参数】【之前】###
#每个参数只能指定一次

'''
灵活使用关键字参数的好处：
1.提高可读性
2.提供默认值
3.提供一种扩充函数的有效方式

那么给函数添加新的行为时，可用带默认值的关键字参数，以便与原有的函数调用代码兼容

可选的关键字参数总是应该以关键字形式来指定，而不是位置参数的形式。
'''
