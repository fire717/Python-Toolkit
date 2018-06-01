#coding:utf-8

list[start:end:stride]  
#第三个参数代表步数，即间隔

xlist=[::-1] #可以反转以字节形式存储的字符串
#但对ASCII字符有用，对已经编码成utf-8字节串的unicode没用

'''
同时，指定了stride时代码可读性变差，同时使start、end索引的含义变得模糊
【所以】，我们不应该把stride与start和end写在一起。
如果非要用stride，就尽量采用正值，同时省略start和end索引。

一定要用时，可以先使用stride，赋给变量，再对其二次切割。
但会多产生一份原数据的浅拷贝，所以第一次切割时应该尽可能缩减切割后的列表尺寸。

python内置的itertools模块有个islide方法，不允许为start、end、stride指定负值。
'''
