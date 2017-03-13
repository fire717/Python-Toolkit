#coding:utf-8

#列表推导式
a=[1,2,3,4]
aquares = [x**2 for x in a]
even_aquares = [x**2 for x in a if x%2==0]

#内置的map()
squares = map(lambda x:x**2,a)
alt = map(lambda x:x**2, filter(lambda x: x%2==0, a)) #注意列表a在filter括号中
assert even_squares == list(alt)

'''
除非调用只有一个参数的函数，列表推导式比map要清晰
同时在后面添加条件也能实现filter()的过滤效果
 
字典和集合也有和列表类似的推导机制
'''
