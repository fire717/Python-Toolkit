# coding:utf-8
# https://www.chilkatsoft.com/refdoc/pythonCkMailManRef.html   chilkat模块文档
# http://justcoding.iteye.com/blog/918934    例子
# 下一步工作 读取完邮件后删除 已完成
# 优化代码，打包EXE，增加指令功能
# 用的好好的，突然报错了，应该是拉的太频繁被网易服务器限制了。。。T.T这条路也只能走到这了

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
username = 'xxx@126.com'
password = 'xxxxx'

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

        if email.ck_from().decode('gbk') == u'firetest <firetest@126.com>':
            #print email.subject() + "\n"
            #######################指令区####################
            if email.subject() == '1':
                os.system('tgp_daemon.exe')
                #为了防止弹出权限提示不直接打开，需要以管理员身份运行此程序
            if email.subject() == '2':
                f = open('f.txt','w')
            if email.subject() == '3':
                pass
            if email.subject() == '4':
                pass
            if email.subject() == '5':
                pass
            if email.subject() == '6':
                pass
            if email.subject() == '7':
                pass
            if email.subject() == '8':
                os.system('notepad')
            if email.subject() == '9':
                os.system('Shutdown.exe -s -t 60')
            #########################指令区完########################

            mailman.DeleteEmail(email)
