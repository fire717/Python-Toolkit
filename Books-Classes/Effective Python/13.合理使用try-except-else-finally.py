'''
如果既要异常向上传播，又要在异常发生时执行清理工作，可使用try/finally结构

try/except/else结构可以清晰描述哪些异常由自己的代码处理，哪些传播到上一级

无论try块是否异常，都可用try/finally复合语句的finall块执行清理工作

else块可缩减try中代码量，并把没有异常时要执行的语句与try/except隔离开

顺利运行try后，若想使某些操作能在finally块的清理代码之前执行，则可将这些操作写到else块中
'''
