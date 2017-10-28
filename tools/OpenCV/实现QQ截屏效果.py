#coding:utf-8

import cv2
import numpy as np
from PIL import ImageGrab

def catchScreen(posW,posN,posE,posS):
    '''
    input: position (int*4)
    output: None (save a picture)
    '''
    im = ImageGrab.grab((posW,posN,posE,posS)) 
    #a离左边距离px,离上面距离b,右边离屏幕左边距离c,下边离屏幕上边距离d
    im.save("part.png")
    #定义保存的路径和保存的图片格式
    
def draw_rect(event,x,y,flags,param):
    global x1,y1,x2,y2,drawing,img,imgSmall,finishDraw
    # 当按下左键是返回起始位置坐标
    if event==cv2.EVENT_LBUTTONDOWN:
        drawing=True
        x1,y1=x,y
    # 当鼠标左键按下并移动是绘制图形。 event 可以查看移动， flag 查看是否按下
    elif event==cv2.EVENT_MOUSEMOVE and flags==cv2.EVENT_FLAG_LBUTTON:
        if drawing==True:
            img[:,:]=newGray[:,:]
            img[y1:y,x1:x]=imgSmall[y1:y,x1:x]
            cv2.rectangle(img,(x1,y1),(x,y),(0,0,255),1)
    # 当鼠标松开停止绘画。
    elif event==cv2.EVENT_LBUTTONUP:
        drawing==False
        x2,y2=x,y
        finishDraw = True

def fullScreenCatch():
    global img,imgSmall,newGray,finishDraw

    base = ImageGrab.grab()
    base.save('fullScreen.png')

    img = cv2.imread("fullScreen.png")
    cv2.namedWindow("image", cv2.WND_PROP_FULLSCREEN)  
    cv2.moveWindow('image',0,0) #固定窗口出现位置        
    cv2.setWindowProperty("image", cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    cv2.setMouseCallback('image',draw_rect)

    imgSmall = img.copy() #鼠标移动过程中小窗口

    imgGray = img.copy() #灰色背景
    imgGray = cv2.cvtColor(imgGray,cv2.COLOR_BGR2GRAY) 
    cv2.imwrite("fullGray.png", imgGray) #save and reread,方式通道不一样不能数组赋值
    newGray = cv2.imread("fullGray.png")

    finishDraw = False
    while(1):
        cv2.imshow('image',img)
        k=cv2.waitKey(2)&0xFF

        if k & finishDraw: 
            catchScreen(x1,y1,x2,y2)
            #img2word(img)
            #chinese_word=eng2chinese(word)
            chinese_word='waiting...'

            #show word when stop draw
            font=cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img,chinese_word,(x1,y2+24), font, 0.8,(0,0,255),1)

            cv2.imshow('image',img)
            cv2.waitKey()
            break
    return 

if __name__ == '__main__':
    fullScreenCatch()
