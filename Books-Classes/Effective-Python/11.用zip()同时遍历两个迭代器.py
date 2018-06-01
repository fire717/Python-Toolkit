#coding:utf-8


names = ['tom','jack','jy']
letters = [len(n) for n in names] #注意这里列表推导用法

#要获取最长的名字及其长度多少
longest_name = None
max_letter = 0

#常规做法 、看上去比较混乱 不易阅读
for i in range(len(names)):
    count = letters[i]
    if count > max_letter:
        longest_name = names[i]
        max_letter = count

#使用zip
for name,count in zip(names,letters):
    if count > max_letter:
        longest_name =name
        max_letter = count

'''
当遍历的两个迭代器长度不同时，会在最短的那里停止

python3中zip相当于生成器，会在遍历时逐次产生元组
而py2中则是直接把这些元组完全生成好一次性返回整个列表
故要在py2中遍历很大的迭代器，应用itertools内置模块中的izip()
同时其中的zip_longest函数可以平行遍历多个迭代器而不会在长度不同时提前终止
'''
