# coding:utf-8
# 看的麻省理工公开课讲求平方根的算法，顺手写了一个，还需要改进的是当不存在平方数时会报错

import random

def squareR(x,number):
    if x*x == number:
        print x
    else:
        y=(number/x+x)/2
        squareR(y,number)

number = input("Please input ur number:") 
x = random.randint(1,number)

squareR(x,number)

input()
