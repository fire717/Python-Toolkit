#coding:utf-8

#当需要循环的是数值时可以使用range()
for x in range(10):
    pass
#或者获取列表元素时可直接迭代
food = ['apple','egg','rice']
for x in food:
    pass

#而当需要元素所在索引时，一般我们用
for x in range(len(food)):
    pass

#这样很生硬

'''
Python内置函数enumerate()可把各种迭代器(包括各种序列及各种支持迭代的对象)包装为生成器
每次产生一对输出值，前者表示循环下标，后者表示从迭代器中获取到的下一个序列元素
同时可以有第二个参数，指明开始计数的索引值，默认为0
'''

for i,food in enumerate(food):
    print i,food
#输出
#0 apple
#1 egg
#2 rice

for i,food in enumerate(food,2):
    print i,food
#输出
#2 apple
#3 egg
#4 rice
