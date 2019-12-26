# -*- coding: utf-8 -*
# @fire 19.7.20
# update 19.12.15    @ change to class

import numpy as np
import cv2

import random
import os
import cv2
import numpy as np
from math import *
#import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw


################# tool func
def randomVal(val):
    # np.random.random()：Return random floats in the half-open interval [0.0, 1.0).
    #返回0-val的随机值
    return int(np.random.random() * val)

def randomSmallerChance(n):
    #n-(0,1)  n的概率为真
    #>n:true <n:false
    t = random.random()
    if t<n:
        return True
    else:
        return False
##################################


class DataAugment(object):
    """docstring for ClassName"""
    def __init__(self, img):
        # img is opencv type
        self.img = img
        self.img_h = img.shape[0]
        self.img_w = img.shape[1]
        self.img_channel = img.shape[2]

    def imgDistortion(self):
        # 畸变 倾斜
        #### param zore ###
        angel = randomVal(80) - 40
        max_angel = 40
        ###################
        
        size_o = [self.img.shape[1],self.img.shape[0]]
        size = (self.img.shape[1]+ int(self.img.shape[0]*cos((float(max_angel )/180) * 3.14)),self.img.shape[0])
        interval = abs( int( sin((float(angel) /180) * 3.14)* self.img.shape[0]));
        pts1 = np.float32([[0,0]         ,[0,size_o[1]],[size_o[0],0],[size_o[0],size_o[1]]])
        if(angel>0):
            pts2 = np.float32([[interval,0],[0,size[1]  ],[size[0],0  ],[size[0]-interval,size_o[1]]])
        else:
            pts2 = np.float32([[0,0],[interval,size[1]  ],[size[0]-interval,0  ],[size[0],size_o[1]]])
        M  = cv2.getPerspectiveTransform(pts1,pts2);
        self.img = cv2.warpPerspective(self.img,M,size)
        self.img = cv2.resize(self.img, (self.img_w, self.img_h))


    def imgPerspective(self):
        # 透视变换
        #### param zore ###
        factor = random.randint(20,60)
        ###################

        pts1 = np.float32([ [0, 0], 
                            [0, self.img_h], 
                            [self.img_w, 0], 
                            [self.img_w, self.img_h]])
        pts2 = np.float32([ [randomVal(factor) ,     randomVal(factor) ], 
                            [randomVal(factor) ,     self.img_h - randomVal(factor) ], 
                            [self.img_w - randomVal(factor) , randomVal(factor) ],
                            [self.img_w - randomVal(factor) , self.img_h - randomVal(factor) ]])
        M = cv2.getPerspectiveTransform(pts1, pts2)
        self.img = cv2.warpPerspective(self.img, M, (self.img_w, self.img_h))


    def imgRotate(self): #1
        # 旋转
        #### param zore ###
        rotate_angle = random.randint(10,340)
        rotate_center = None
        rotate_scale = random.random()*0.4 + 0.8
        ###################
        
        if rotate_center is None: #3
            mid_w_move = random.randint(0,40) - 20
            mid_h_move = random.randint(0,40) - 20
            rotate_center = (self.img_w // 2 + mid_w_move, self.img_h // 2 + mid_h_move) #4
     
        M = cv2.getRotationMatrix2D(rotate_center, rotate_angle, rotate_scale) #5
     
        self.img = cv2.warpAffine(self.img, M, (self.img_w, self.img_h)) #6


    def imgMove(self):
        # 平移
        #### param zore ###
        h_ratio_mid = 0.2
        w_ratio_mid = 0.16
        ###################

        def _translate(image, x, y):
        # 定义平移矩阵
            M = np.float32([[1, 0, x], [0, 1, y]])
            shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
            return shifted
        
        h_move = int(self.img_h*(random.random()*0.4+0.05) - self.img_h*h_ratio_mid)
        self.img = _translate(self.img, 0, h_move)
        
        w_move = int(self.img_w*(random.random()*0.32+0.02) - self.img_w*w_ratio_mid)
        self.img = _translate(self.img,  w_move,0)


    def imgMirror(self):
        # 镜像图片(翻转)

        if randomSmallerChance(0.3):
            self.img = cv2.flip(self.img, 1)# 横向翻转图像
        elif randomSmallerChance(0.6):
            self.img = cv2.flip(self.img, 0)# 纵向翻转图像
        else:
            self.img = cv2.flip(self.img, -1)# 同时在横向和纵向翻转图像


    def imgChannel(self):
        # 通道变换(交换、复制)

        b, g, r = self.img[:,:,:1], self.img[:,:,1:2], self.img[:,:,2:3]

        if randomSmallerChance(0.06):
            b = b*random.random()
            b = b.astype('uint8')
        elif randomSmallerChance(0.12):
            g = g*random.random()
            g = g.astype('uint8')
        elif randomSmallerChance(0.18):
            r = r*random.random()
            r = r.astype('uint8')
        elif randomSmallerChance(0.28):
            b,g = r,r
        elif randomSmallerChance(0.38):
            b,r = g,g
        elif randomSmallerChance(0.48):
            g,r = b,b
        elif randomSmallerChance(0.58):
            b,g = g,b
        elif randomSmallerChance(0.68):
            r,g = g,r
        elif randomSmallerChance(0.78):
            b,r = r,b
        else:
            b = (b+g+r)/3
            b = b.astype('uint8')
            g,r = b,b

        self.img = np.concatenate([b, g, r], axis=-1)


    def imgColor(self):
        # 色彩变换
        #### param zore ###

        ###################

        hsv = cv2.cvtColor(self.img,cv2.COLOR_BGR2HSV);
        hsv[:,:,0] = hsv[:,:,0]*(0.6+ np.random.random()*0.6);
        hsv[:,:,1] = hsv[:,:,1]*(0.2+ np.random.random()*1.6);
        hsv[:,:,2] = hsv[:,:,2]*(0.5+ np.random.random()*0.6);

        self.img = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR);


    def imgPadding(self):
        # 边缘填充
        #### param zore ###
        h_ratio_max = 0.2
        w_ratio_max = 0.2
        ###################

        h_ratio = random.random() * h_ratio_max
        w_ratio = random.random() * w_ratio_max

        h_pad = int(self.img_h*h_ratio)
        w_pad = int(self.img_w*w_ratio)
        h_new = self.img_h+h_pad*2
        w_new = self.img_w+w_pad*2
        new_img = np.array(Image.new("RGB", (w_new,h_new)))
        new_img[h_pad:self.img_h+h_pad, w_pad:self.img_w+w_pad,:] = self.img
        self.img = cv2.resize(new_img,(self.img_w, self.img_h))


    def imgGauss(self):
        # 高斯平滑
        #### param zore ###
        blur_level = random.randint(1,3)
        ###################

        self.img = cv2.blur(self.img, (blur_level * 2 + 1, blur_level * 2 + 1))


    def imgNoise(self):
        # 随机噪声
        #### param zore ###
        type_ratio = 0.5
        ###################

        def _addGaussianNoise(img,sdev = 0.5):
            def _AddGaussianNoiseSingleChannel(src,means,sigma):
                NoiseImg=src
                rows=NoiseImg.shape[0]
                cols=NoiseImg.shape[1]
                for i in range(rows):
                    for j in range(cols):
                        NoiseImg[i,j]=NoiseImg[i,j]+random.gauss(means,sigma)
                        if  NoiseImg[i,j]< 0:
                             NoiseImg[i,j]=0
                        elif  NoiseImg[i,j]>255:
                             NoiseImg[i,j]=255
                return NoiseImg
            avg = random.randint(3,10)
            img[:,:,0] =  _AddGaussianNoiseSingleChannel(img[:,:,0], sdev, avg)
            avg = random.randint(3,10)
            img[:,:,1] =  _AddGaussianNoiseSingleChannel(img[:,:,1], sdev, avg)
            avg = random.randint(3,10)
            img[:,:,2] =  _AddGaussianNoiseSingleChannel(img[:,:,2], sdev, avg)
            return img

        def _addPepperandSalt(src):
            percetage=0.001+random.random()*0.099
            NoiseImg=src
            NoiseNum=int(percetage*src.shape[0]*src.shape[1])
            for i in range(NoiseNum):
                randX=random.randint(0,src.shape[0]-1)
                randY=random.randint(0,src.shape[1]-1)
                if random.randint(0,1)<=0.5:
                    NoiseImg[randX,randY]=0
                else:
                    NoiseImg[randX,randY]=255          
            return NoiseImg

        if random.random()<type_ratio:
            self.img = _addGaussianNoise(self.img)
            
        else:
            self.img = _addPepperandSalt(self.img)


    def imgShelter(self):
        # 随机遮挡区域
        #### param zore ###
        shelter_size = random.randint(70,100)
        shelter_num = int((110 - shelter_size)*0.1)
        color_random = False
        ###################

        if color_random:
            d = np.random.randint(0, 255, (shelter_size,shelter_size,self.img_channel))
        else:
            d = np.random.randint(0,255)*np.ones((shelter_size,shelter_size,self.img_channel))
        for i in range(shelter_num):
            x = random.randint(0, self.img_w - shelter_size - 1)
            y = random.randint(0, self.img_h - shelter_size - 1)
            self.img[y:y+shelter_size, x:x+shelter_size] = d

    def imgPadToSquare(self):
        # 图片填充为正方形
        
        max_value = max(self.img_h, self.img_w)
        pad_value = max_value - min(self.img_h, self.img_w)
        left_top = int(pad_value*random.random())
        right_bottom = pad_value - left_top
        
        new_img = np.zeros((max_value, max_value, self.img_channel), dtype=np.uint8)
        if(max_value==self.img_w):
            new_img[left_top:max_value-right_bottom,:] = self.img
        else:
            new_img[:,left_top:max_value-right_bottom] = self.img

        self.img = new_img
        self.img_h = new_img.shape[0]
        self.img_w = new_img.shape[1]



    def imgPart(self):
        # 图片取部分再resize放大到原尺寸
        #### param zore ###
        part_ratio_max = 0.4
        part_ratio_min = 0.2
        ###################

        part_ratio = 1 - (random.random()*(part_ratio_max - part_ratio_min) + part_ratio_min)

        new_h = int(part_ratio*self.img_h)
        new_w = int(part_ratio*self.img_w)

        left = int((self.img_w - new_w)*random.random())
        top = int((self.img_h - new_h)*random.random())

        new_img = self.img[top:top+new_h,left:left+new_w]
        new_img = cv2.resize(new_img,(self.img_w, self.img_h))
        self.img = new_img


    def imgFixedPart(self):
        # 图片取固定部分（左上右上左下右下中间）再resize放大到原尺寸
        #### param zore ###
        part_ratio = 0.6
        ####################

        new_h = int(part_ratio*self.img_h)
        new_w = int(part_ratio*self.img_w)

        if randomSmallerChance(0.2):
            left = 0
            top = 0
        elif randomSmallerChance(0.4):
            left = self.img_w - new_w
            top = 0
        elif randomSmallerChance(0.6):
            left = 0
            top = self.img_h - new_h
        elif randomSmallerChance(0.8):
            left = self.img_w - new_w
            top = self.img_h - new_h
        else:
            left = (self.img_w - new_w)//2
            top = (self.img_h - new_h)//2

        new_img = self.img[top:top+new_h,left:left+new_w]
        new_img = cv2.resize(new_img,(self.img_w, self.img_h))
        self.img = new_img


    ####### merge all ########
    def imgOutput(self):
        if randomSmallerChance(0.8):
            self.imgFixedPart()

        self.imgPadToSquare() 

        if randomSmallerChance(0.4):
            if randomSmallerChance(0.8):
                self.imgChannel()
            else:
                self.imgColor()

        if randomSmallerChance(0.8):
            if randomSmallerChance(0.2):
                self.imgDistortion()
            elif randomSmallerChance(0.5):
                self.imgPerspective()
            elif randomSmallerChance(0.8):
                self.imgRotate()
            else:
                self.imgMove()

        if randomSmallerChance(0.2):
            if randomSmallerChance(0.6):
                self.imgGauss()
            else:
                self.imgNoise()

        if randomSmallerChance(0.8):
            self.imgMirror()

        if randomSmallerChance(0.4):
            self.imgPadding()

        if randomSmallerChance(0.4):
            self.imgShelter()

        return self.img






if __name__ == '__main__':

    img = cv2.imread("1.jpg")
    print(img.shape)
    imgAug = DataAugment(img)
    img = imgAug.imgOutput()

    cv2.imwrite("2.jpg", img)
