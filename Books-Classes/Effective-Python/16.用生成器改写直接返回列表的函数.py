# -*- coding:utf-8 -*-


#eg.查出字符串中每个词的首字母在整个字符串里的位置
def index_words(text):
    result = []
    if text:
        result.append(0)
    for index,letter in enumerate(text):
        if letter == ' ':
            result.append(index+1)
    return result

address = 'Four score and seven years ago...'
result = index_words(address)
print result


#使用生成器改写
'''
生成器（generator）是用yield表达式的函数。
调用生成器时，它不会真的运行，只是返回迭代器。每次在该迭代器上调用内置的next时，迭代器会把生成器推进到下一个yield表达式那里。
生成器传给yield的每一个值，都会由迭代器返回给调用者
'''
def index_words_iter(text):
    if text:
        yield 0
    for index,letter in enumerate(text):
        if letter == ' ':
            yield index+1
#调用该生成器后所返回的迭代器，可以传给内置的list函数，将其转换为列表（参考第9条）
result = list(index_words_iter(address))
print result

#同时index_words在返回前会把所有结果放在列表里，当输入量很大时就可能耗尽内存崩溃。
#生成器改写后的版本可以应对任意长度的输入数据

#eg.2.从文件里读入各行，逐个处理每行单词
def index_file(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in  line:
            offset+=1
            if letter == ' ':
                yield offset

with open('xx,txt','r') as f:
    it = index_file(f)
    results = islice(it,0,3)
    print list(results)

###定义生成器函数时唯一需要注意的就是：函数返回的迭代器是有状态的，不能反复调用。
