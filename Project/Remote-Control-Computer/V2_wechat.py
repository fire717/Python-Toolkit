#coding=utf-8

import itchat, time
import os
from itchat.content import *
# 通过该命令安装该API： pip install NetEaseMusicApi
from NetEaseMusicApi import interact_select_song
import sys
reload(sys)
sys.setdefaultencoding('utf8') #Python的str默认是ascii编码，和unicode编码冲突

with open('stop.mp3', 'w') as f: pass
def close_music():
    os.startfile('stop.mp3')

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
#######################指令区####################
    if msg['FromUserName'] != msg['ToUserName']: return 
    if msg['Text'] == u'打开CMD':   #测试未通过
        os.system('cmd')
        return 'OK!'
    if msg['Text'] == u'打开记事本':
        os.system('notepad')
        return 'OK!'
    if msg['Text'] == u'自动关机':
        os.system('Shutdown.exe -s -t 60')
        return 'OK!'
    if msg['Text'] == u'打开TGP':
        os.system(u'tgp_daemon.exe')
        return 'OK!'
        #为了防止弹出权限提示不直接打开，需要以管理员身份运行此程序
    if msg['Text'] == u'打开网易云':
        os.system(u'cloudmusic.exe')
        return 'OK!'
    if u'播放' in msg['Text']:
        interact_select_song(msg['Text'].replace(u'播放',''))
        return 'OK!'
    if msg['Text'] == u'关闭播放':
        close_music()
        return 'OK!'
#########################指令区完########################
    return 'error'
    
itchat.auto_login(hotReload=True)
itchat.run()
