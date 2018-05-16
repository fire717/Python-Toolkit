#coding:utf-8
#!/usr/bin/python
import itchat,time
import random
import threading
from itchat.content import *
#import sys
#reload(sys)
#sys.setdefaultencoding('utf8') #Python的str默认是ascii编码，和unicode编码冲突



@itchat.msg_register(FRIENDS)
def add_friend(msg, status=3):
    itchat.add_friend(**msg['Text']) # 该操作会自动将新好友的消息录入，不需要重载通讯录
    time.sleep(5)
    itchat.send_msg(u'在吗，有人吗！？', msg['RecommendInfo']['UserName'])

def wait_active(seconds,msg): 
    global user_step
    time.sleep(seconds)
    user_step[msg['FromUserName']] /= 1000  #解锁以继续流程

    back_re=random.randint(1,3)   #设置唤醒的主动回复
    if back_re == 1:
        backword=u'还在吗'
    if back_re == 2:
        backword=u'我回来了'
    if back_re == 3:
        backword=u'嘿'
    itchat.send(backword, toUserName=msg['FromUserName'])
    return

def wait_time(seconds,msg):
    t=threading.Thread(target=wait_active,args=(seconds,msg,))
    t.setDaemon(True)
    t.start()
    return

def delay_reply(delay_time,words,msg):
    time.sleep(delay_time)
    itchat.send(words, toUserName=msg['FromUserName'])
    return 
 
######################故事流程区########################
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    global user_step
    user_step[msg['FromUserName']]=user_step.get(msg['FromUserName'],0) #dict.get(key, default=None) 返回给定键的值。如果键不可用，则返回默认值None。
    if user_step[msg['FromUserName']]==0:
        user_step[msg['FromUserName']]=1
        delay_reply(2,'救救我，我被关起来了',msg)
        return 
    if user_step[msg['FromUserName']]==1:
        user_step[msg['FromUserName']]=20000
        delay_reply(2,'我也不知道怎么回事',msg)
        delay_reply(2,'一觉醒来就在这里了',msg)
        delay_reply(2,'我在手里摸到一个手机',msg)
        delay_reply(3,'当然不是我的，我还是中学生没有手机',msg)
        delay_reply(5,'没办法打电话，不过连了网，上面只装了这个微信，我也不记得谁的微信号，只能搜附近的人，然后就加了你了',msg)
        user_step[msg['FromUserName']]=2
        return 
    if user_step[msg['FromUserName']]==2:
        user_step[msg['FromUserName']]=333333
        delay_reply(2,'一个暗暗的小房子',msg)
        delay_reply(2,'有窗，但是被木条封起来了，基本没有光线',msg)
        delay_reply(2,'这里好黑，我好害怕',msg)
        delay_reply(2,'我现在该怎么办呢？',msg)
        user_step[msg['FromUserName']]=3
        return 
    if u'蜡烛'in msg['Text'] and user_step[msg['FromUserName']]==3:
        delay_reply(2,'我找不到蜡烛啊...',msg)
        return
    if u'窗'in msg['Text'] and user_step[msg['FromUserName']]==3:
        delay_reply(3,'窗户被木条封起来了呀，钉死了，什么都看不到，也拉不开',msg)
        return
    if u'闪光'in msg['Text'] and user_step[msg['FromUserName']]==3:
        delay_reply(2,'这是很老的手机，都没有闪光灯',msg)
        return
    if u'灯'in msg['Text'] and user_step[msg['FromUserName']]==3:
        user_step[msg['FromUserName']]=44444444
        delay_reply(2,'好吧，我先去找找灯',msg)
        delay_reply(10,'找到灯了！',msg)
        delay_reply(2,'黄色的灯泡，不是特别亮',msg)
        delay_reply(3,'不过比刚才黑黑的好多了，谢谢你',msg)
        user_step[msg['FromUserName']]=4
        return 
    if user_step[msg['FromUserName']]==4:
        user_step[msg['FromUserName']]=55555555
        delay_reply(2,'恩，我看看房间都有些什么',msg)
        delay_reply(5,'有床、桌子...算了我先去都检查一下吧，一会再找你',msg)
        wait_time(800,msg)
        user_step[msg['FromUserName']]=5*1000
        return 
    if user_step[msg['FromUserName']]==5:
        user_step[msg['FromUserName']]=6666666
        delay_reply(2,'我都检查过了，给你描述一下吧',msg)
        delay_reply(5,'一张普通的折叠床，白色的床单、被子、枕头，然后没了',msg)
        delay_reply(6,'然后是一把很普通的木椅子，我甚至倒过来看了，除了左边扶手有点晃动，应该是螺丝松了',msg)
        delay_reply(7,'椅子旁边是个很旧的木桌，有三个抽屉，左边抽屉是空的，中间抽屉锁住了，右边抽屉里有本书',msg)
        delay_reply(4,'对了，还有个保险箱，上面是圆形的密码锁，一共三位',msg)
        delay_reply(5,'还有那扇门，就是一个圆形的把手，有锁孔，打不开应该就是锁住了',msg)
        delay_reply(2,'下一步该怎么办？',msg)
        user_step[msg['FromUserName']]=6
        return 
    if u'椅'in msg['Text'] and len(msg['Text'])<20 and user_step[msg['FromUserName']]==6:
        delay_reply(2,'我看了椅子，没什么特别的',msg)
        return
    if u'桌'in msg['Text'] and len(msg['Text'])<20 and user_step[msg['FromUserName']]==6:
        delay_reply(2,'桌子都检查完了',msg)
        return
    if u'书'in msg['Text'] and len(msg['Text'])<20 and user_step[msg['FromUserName']]==6:
        delay_reply(3,'很普通的一本英文书，我也不认识',msg)
        return
    if u'保险箱'in msg['Text'] and len(msg['Text'])<20 and user_step[msg['FromUserName']]==6:
        delay_reply(2,'锁住了，我随便试了几个密码，打不开',msg)
        return
    if u'床'in msg['Text'] and len(msg['Text'])<20 and user_step[msg['FromUserName']]==6:
        delay_reply(2,'恩我走到床边了，然后呢',msg)
        return
    if u'枕头'in msg['Text'] and len(msg['Text'])<20 and u'白色' not in msg['Text'] and user_step[msg['FromUserName']]==6:
        user_step[msg['FromUserName']]=7777777
        delay_reply(3,'好吧，我再去检查下枕头好了',msg)
        wait_time(600,msg)
        user_step[msg['FromUserName']]=7*1000
        return
    if user_step[msg['FromUserName']]==7:
        user_step[msg['FromUserName']]=88888
        delay_reply(4,'你还别说，真的发现一把钥匙！你怎么知道的？',msg)
        user_step[msg['FromUserName']]=8
        return 
    if user_step[msg['FromUserName']]==8:
        user_step[msg['FromUserName']]=8999999
        delay_reply(2,'算了，我先去试试吧',msg)
        delay_reply(7,'门打不开，钥匙都插不进去，不过那个锁着的抽屉打开了。',msg)
        delay_reply(2,'你猜猜里面有什么',msg)
        user_step[msg['FromUserName']]=9
        return 
    if user_step[msg['FromUserName']]==9:
        user_step[msg['FromUserName']]=999999
        delay_reply(2,'我就知道你猜不到',msg)
        delay_reply(3,'里面有一张纸片，写着什么 PAGE117 ',msg)
        delay_reply(2,'什么鬼意思？',msg)
        user_step[msg['FromUserName']]=10
        return 
    if u'书' in msg['Text'] and len(msg['Text'])<16 and user_step[msg['FromUserName']]==10:
        user_step[msg['FromUserName']]=1111111
        delay_reply(2,'书吗？你怎么什么都知道',msg)
        delay_reply(2,'右边抽屉是有本书，我看看',msg)
        delay_reply(10,'太棒了！在117页上面有一句话。圆周率小数点后第10/11/12位',msg)
        delay_reply(6,'圆周率我知道，但是记不住啊，你能帮我查查吗？我觉得应该是那个保险箱的密码！',msg)
        user_step[msg['FromUserName']]=11
        return
    if u'589' in msg['Text'] and len(msg['Text'])<6 and user_step[msg['FromUserName']]==11:
        user_step[msg['FromUserName']]=122222
        delay_reply(2,'是吗？那我试试',msg)
        delay_reply(10,'真的打开了！',msg)
        delay_reply(2,'不过我又想让你猜猜里面是什么了..',msg)
        user_step[msg['FromUserName']]=12
        return

    if u'589' not in msg['Text'] and user_step[msg['FromUserName']]==11: 
        delay_reply(2,'真的吗？那我试试',msg)
        delay_reply(5,'骗子，不对啊',msg)
        return 

    if user_step[msg['FromUserName']]==12:
        user_step[msg['FromUserName']]=1333311
        delay_reply(2,'我就知道你猜不到，是一个螺丝刀！',msg)
        delay_reply(2,'恩，你想让我去试试椅子上那个松动的把手吧，我也想到了，我先去试试。',msg)
        wait_time(300,msg)
        user_step[msg['FromUserName']]=13*1000
        return
    if user_step[msg['FromUserName']]==13:
        user_step[msg['FromUserName']]=1344441
        delay_reply(3,'嗯，真的打开了，里面居然是空心的，还有个东西',msg)
        delay_reply(3,'你猜猜...算了直接告诉你吧！是一把钥匙！',msg)
        delay_reply(2,'我觉得就是门的钥匙了..我去试试',msg)
        delay_reply(2,'门打开了！',msg)
        delay_reply(2,'外面是条黑黑的走廊',msg)
        delay_reply(5,'我先出去了，如果能出去，等我到家了再联系你！',msg)
        user_step[msg['FromUserName']]=14
        return
    if user_step[msg['FromUserName']]==14:
        return '恭喜通关！游戏结束！'

#########################设置多种随机回复#######################
    out_re=random.randint(1,5)
    time.sleep(2)
    if user_step[msg['FromUserName']] < 1000:    #防止进入线程阻塞时还能回复
        if out_re==1:   
            if user_step[msg['FromUserName']]==3:
                return "我怕黑呀" 
            return '[流泪]救救我'
        if out_re==2:
            if user_step[msg['FromUserName']]==3:
                return "好黑，什么都看不见"    
            return '我好想回家...'
        if out_re==3:    
            return '我现在到底该怎么办..'
        if out_re==4:    
            return '请你一定要救救我啊'
        if out_re==5:    
            return '[流泪][流泪][流泪]'
#################################################################
#    
user_step={} #通过字典保存每个用户名字及对应的游戏进程

#保存备份
'''
while int(time.strftime('%S',time.localtime(time.time()))) % 2 == 0:
    jsObj = json.dumps(user_step) 
    fileObject = open('data.json', 'w') 
    fileObject.write(time.strftime('%Y-%m-%d',time.localtime(time.time()))) 
    fileObject.write('\n') 
    fileObject.write(jsObj)
    fileObject.write('\n')   
    fileObject.close()  
'''
itchat.auto_login(hotReload=True,enableCmdQR=2)
itchat.run()
