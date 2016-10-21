# -*- coding: utf-8 -*-
# https://www.chilkatsoft.com/refdoc/pythonCkMailManRef.html   chilkat模块文档
# http://justcoding.iteye.com/blog/918934    例子
# 下一步工作 读取完邮件后删除

import time
import sys
import chilkat
import os

#主函数设置时间间隔
def sleeptime(hour,min,sec):
    return hour*3600 + min*60 + sec
second = sleeptime(0,0,3)

#设置邮件接收
host = 'pop.126.com'
username = 'firetest@126.com'
password = 'fire15yww8t4u'

while 1==1:
    time.sleep(second)
    
    #循环执行
    mailman = chilkat.CkMailMan()

    success = mailman.UnlockComponent("30-day trial")
    if (success != True):
        print "Component unlock failed"
        sys.exit()

    mailman.put_MailHost(host)
    mailman.put_PopUsername(username)
    mailman.put_PopPassword(password)
    mailman.put_PopSsl(True)
    mailman.put_MailPort(995)

    bundle = mailman.GetAllHeaders(1)

    if (bundle == None ):
        print mailman.lastErrorText()
        sys.exit()

    for i in range(0,bundle.get_MessageCount()):
        email = bundle.GetEmail(i)

    # Display the From email address and the subject.
        print email.ck_from()
        print email.subject() + "\n"
    #根据主题数字执行不同指令

        if email.subject() == '4':
            f = open('f.txt','w')
        if email.subject() == '5':
            os.system('notepad')
input()
