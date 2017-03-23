 # -*- coding:utf-8 -*-


#使用python强大的特性时，遵循最小惊讶原则(rule of le)
#即 这些机制只适合用来实现那些广为人知的python编程范式

#实时计算当前所剩配额
@property
def quato(self):
    return self.max_quota - self.quota_consumed

'''
python内置的@property修饰器，使开发者可以把类设计的很灵巧，令调用者能轻松访问该类的实例属性。
@property还有一种高级用法，可以把简单的数值属性迁移为实时计算(on-the-fly calculation，按需计算、动态计算)
我们只需要给本类添加新的功能即可，不需要修改原有代码。
在持续完善接口的过程中，也是一种重要的缓冲手段
'''

'''
@property可以为现有的实例属性添加新的功能

可以用@property来逐步完善数据模型

如果@property用的太频繁，那就应该考虑彻底重构该类并修改相关的调用代码
'''
 
