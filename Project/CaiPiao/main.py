#coding:utf-8

import random

def create_today():
    red_length=0
    today_temp = []

    while red_length<=5:
        temp_red=random.randint(1,33)
        if temp_red not in today_temp:
            today_temp.append(temp_red)
            red_length+=1

    today_temp.sort()
    temp_blue = random.randint(1,16)

    today_temp.append(temp_blue)
    return today_temp

def examine_history(today_temp):
    history = []
    for line in open("history.txt"):
        history.append(list(map(int,line.split(','))))
        #line.split(',')把字符串转为list，此时每个元素还是str，然后map每一个执行int，再list即可

    if today_temp not in history:
        return False
    else:return True


number = create_today()

while examine_history(number):
    number = create_today()

print number

input()
