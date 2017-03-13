#coding:utf-8

#列表推导式
value = [len(x) for x in open('x.txt')]
print value
#生成器表达式
it = (len(x) for x in open('x.txt'))
#它会返回一个迭代器，而不会深入处理内容
#可通过next来输出下一个值
print next(it)

#同时返回的迭代器可以放到另一个生成器表达式的for中结合
roots = ((x,x**0.5) for x in it)
#其执行速度很快
#但返回的迭代器有状态，用过一轮后就不能再用了。

'''
当输入数据太大时，列表推导会因占用太多内存而出问题。
而由生成器表达式所返回的迭代器，可逐次产生输出值，避免内存占用太多。
'''
