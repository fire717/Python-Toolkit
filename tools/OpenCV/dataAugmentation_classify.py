# -*- coding: utf-8 -*
# @fire 19.7.20
import numpy as np
import cv2

import random
import os
import cv2
import numpy as np
from math import *
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw


################# tool func


def r(val):
    # np.random.random()：Return random floats in the half-open interval [0.0, 1.0).
    #返回0-val的随机值
    return int(np.random.random() * val)

def randomChance(n):
    #n-(0,1)  n的概率为真
    #>n:true <n:false
    t = random.random()
    if t<n:
        return True
    else:
        return False

# test = [0.1,0.3,0.5,0.7,0.9]
# for t in test:
#     print(randomChance(t))

def getAllName(file_dir): 
    L=[] 
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.jpg':
                L.append(os.path.join(root, file))
    return L




############################################################   main func

def rot(img):
    """ 使图像轻微的畸变   倾斜
        img 输入图像
        factor 畸变的参数
        size 为图片的目标尺寸
    """
    angel = r(60) - 30
    max_angel = 30
    shape = img.shape
    size_o = [shape[1],shape[0]]
    size = (shape[1]+ int(shape[0]*cos((float(max_angel )/180) * 3.14)),shape[0])
    interval = abs( int( sin((float(angel) /180) * 3.14)* shape[0]));
    pts1 = np.float32([[0,0]         ,[0,size_o[1]],[size_o[0],0],[size_o[0],size_o[1]]])
    if(angel>0):
        pts2 = np.float32([[interval,0],[0,size[1]  ],[size[0],0  ],[size[0]-interval,size_o[1]]])
    else:
        pts2 = np.float32([[0,0],[interval,size[1]  ],[size[0]-interval,0  ],[size[0],size_o[1]]])
    M  = cv2.getPerspectiveTransform(pts1,pts2);
    dst = cv2.warpPerspective(img,M,size)
    return dst

def rotRandrom(img):
    #随机  透视变换
    #shape = size
    size = img.shape[1],img.shape[0]
    factor = random.randint(10,40)
    w = size[0]
    h = size[1]
    pts1 = np.float32([ [0, 0], 
                        [0, h], 
                        [w, 0], 
                        [w, h]])
    pts2 = np.float32([ [r(factor) ,     r(factor) ], 
                        [r(factor) ,     h - r(factor) ], 
                        [w - r(factor) , r(factor) ],
                        [w - r(factor) , h - r(factor) ]])
    M = cv2.getPerspectiveTransform(pts1, pts2)
    dst = cv2.warpPerspective(img, M, size)
    # 几何变换操作函数 第一个参数为原始图像 第二个参数为变换矩阵 第三个参数为输出图片的（宽，高）
    # 框坐标变换
    box = ((1,2),(3,4),(5,6),(7,8)) #左上 右上 左下 右下
    def _coords_affine(m,coords):
        affined_cords = []
        for cd in coords:
            n = np.array([[cd[0]],[cd[1]],[1]],dtype=np.float64)
            pro = np.dot(m,n)
            af_cd = (int(round(pro[0,0]/pro[2,0])),int(round(pro[1,0]/pro[2,0])))
            affined_cords.append(af_cd)
        return tuple(affined_cords)
    new_box = _coords_affine(M,box) #变换后的框坐标
    
    return dst

def rotate(image,  center=None, scale=1.0): #1
    angle = random.randint(1,355)
    (h, w) = image.shape[:2] #2
    if center is None: #3
        center = (w // 2, h // 2) #4
 
    M = cv2.getRotationMatrix2D(center, angle, scale) #5
 
    rotated = cv2.warpAffine(image, M, (w, h)) #6
    return rotated #7



def addPadding(img, h_ratio_max = 0.2, w_ratio_max = 0.2):

    h_ratio = random.random() * h_ratio_max
    w_ratio = random.random() * w_ratio_max

    h, w = img.shape[:2]
    h_pad = int(h*h_ratio)
    w_pad = int(w*w_ratio)
    h_new = h+h_pad*2
    w_new = w+w_pad*2
    image=np.array(Image.new("RGB", (w_new,h_new)))
    image[h_pad:h+h_pad,w_pad:w+w_pad,:] = img
    image = cv2.resize(image,(img.shape[1],img.shape[0]))
    return image

def changeColor(img):
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV);

    hsv[:,:,0] = hsv[:,:,0]*(0.6+ np.random.random()*0.6);
    hsv[:,:,1] = hsv[:,:,1]*(0.2+ np.random.random()*1.6);
    hsv[:,:,2] = hsv[:,:,2]*(0.5+ np.random.random()*0.6);

    img = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR);
    return img



def AddGauss(img, level=1):
    #高斯平滑
    return cv2.blur(img, (level * 2 + 1, level * 2 + 1))


def addNoise(img):

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

    if random.random()<0.5:
        img = _addGaussianNoise(img)
        
    else:
        img = _addPepperandSalt(img)
    return img  




def moveImg(img):
    def translate(image, x, y):
    # 定义平移矩阵
        M = np.float32([[1, 0, x], [0, 1, y]])
        shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
        return shifted
    h,w,_ = img.shape
    h_ratio_mid = 0.2
    h_move = int(h*(random.random()*0.4+0.05) - h*h_ratio_mid)
    img = translate(img, 0, h_move)

    w_ratio_mid = 0.16
    w_move = int(w*(random.random()*0.32+0.02) - w*w_ratio_mid)
    img = translate(img,  w_move,0)
    return img




def mirrorImg(img):
    rd = random.random()
    if rd<0.33:
        img = cv2.flip(img, 1)# 横向翻转图像
    elif rd<0.66:
        img = cv2.flip(img, 0)# 纵向翻转图像
    else:
        img = cv2.flip(img, -1)# 同时在横向和纵向翻转图像
    return img



def imgChange(img):
    #  moveImg  addPadding  rotate  rotRandrom  rot
    change1 = random.random()
    if change1< 0.2:
        img = moveImg(img)
    elif change1 < 0.4:
        img = addPadding(img)
    elif change1 < 0.6:
        img = rotate(img)
    elif change1 < 0.8:
        img = rotRandrom(img)
    else:
        img = rot(img)
    #  changeColor
    change2 = random.random()
    if change2 < 0.8:
        img = changeColor(img)

    #  mirrorImg
    change3 = random.random()
    if change3 < 0.9:
        img = mirrorImg(img)
    # addNoise  AddGauss
    change4 = random.random()
    if change4 < 0.5:
        img = addNoise(img)

    return img


def data_augment_single(img):
    if random.random()<0.8:
            h,w = img.shape[:2]
            img = imgChange(img)
            img = cv2.resize(img,(h, w))
    return img

def data_augment(data):
    data = data*255
    data = data.astype(np.uint8)
    aug_data = []
    for img in data:
        if random.random()<0.9:
            h,w = img.shape[:2]
            img = imgChange(img)
            img = cv2.resize(img,(h, w))
        aug_data.append(img)
    aug_data = np.array(aug_data)
    aug_data = aug_data.astype(np.float32)
    aug_data = np.multiply(aug_data, 1.0 / 255.0)
    return aug_data

if __name__ == '__main__':
    pass
    # img = cv2.imread("data/input/metal/metal22.jpg")
    # img = cv2.resize(img,(224, 224))
    # img = imgWhitening(img)
    # cv2.imshow('test', img)
    # cv2.waitKey(0)
    # cv2.destroyWindow('test')
