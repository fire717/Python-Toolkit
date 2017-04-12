# -*- coding: utf-8 -*-

#协调世界时(coordinated universal time,UTC)是一种标准的实践表达方式，与时区无关
from datetime import datetime,timezone
'''
不要用time模块在不同时区间转换

若要在不同时区之间可靠的执行转换操作，应把内置的datetime模块与开发者社区提供的pytz模块搭配起来使用

开发者总是应该先把时间表示出UTC格式，然后对其执行各种转换操作，最后再转回本地时间
'''
