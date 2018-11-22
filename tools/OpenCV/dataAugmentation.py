#coding:utf-8
import random
import os
import cv2
import numpy as np
from math import *
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

def rot(img,angel,shape,max_angel):
    """ 使图像轻微的畸变
        img 输入图像
        factor 畸变的参数
        size 为图片的目标尺寸
    """
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

def addPadding(img, h_ratio_max = 0.12, w_ratio_max = 0.2):

    h_ratio = random.random() * h_ratio_max
    w_ratio = random.random() * w_ratio_max

    h, w = img.shape[:2]
    h_pad = int(h*h_ratio)
    w_pad = int(w*w_ratio)
    h_new = h+h_pad*2
    w_new = w+w_pad*2
    image=np.array(Image.new("RGB", (w_new,h_new)))
    image[h_pad:h+h_pad,w_pad:w+w_pad,:] = img
    return image



def rotRandrom(img, factor, size):
    #随机 几何变换（移动、旋转） 透视变换
    #shape = size
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

def tfactor(img):
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV);

    hsv[:,:,0] = hsv[:,:,0]*(0.9+ np.random.random()*0.2);
    hsv[:,:,1] = hsv[:,:,1]*(0.25+ np.random.random()*0.7);
    hsv[:,:,2] = hsv[:,:,2]*(0.15+ np.random.random()*0.8);

    img = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR);
    return img

def AddGauss(img, level):
    #高斯平滑
    return cv2.blur(img, (level * 2 + 1, level * 2 + 1));

def AddNoiseSingleChannel(single):
    diff = 255-single.max();
    noise = np.random.normal(0,1+r(1),single.shape);
    noise = (noise - noise.min())/(noise.max()-noise.min())
    noise= diff*noise;
    noise= noise.astype(np.uint8)
    dst = single + noise
    return dst

def addNoise(img,sdev = 0.5,avg=10):
    img[:,:,0] =  AddNoiseSingleChannel(img[:,:,0]);
    img[:,:,1] =  AddNoiseSingleChannel(img[:,:,1]);
    img[:,:,2] =  AddNoiseSingleChannel(img[:,:,2]);
    return img

def random_envirment(img,data_set):
    index=r(len(data_set))
    env = cv2.imread(data_set[index])

    env = cv2.resize(env,(img.shape[1],img.shape[0]))

    bak = (img==0);
    bak = bak.astype(np.uint8)*255;
    inv = cv2.bitwise_and(bak,env)
    img = cv2.bitwise_or(inv,img)
    return img

NoPlates = "G:/fire/car/end-to-end-for-chinese-plate-recognition-master/NoPlates"
noplates_path = [];
for parent,parent_folder,filenames in os.walk(NoPlates):
    for filename in filenames:
        path = parent+"/"+filename;
        noplates_path.append(path)

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
    if randomChance(0.2):
        img = rot(img,r(20)-10,img.shape,10); #倾斜
    if randomChance(0.3): 
        img = addPadding(img) #填充周围 增大图片 相当于缩小车牌
        img = random_envirment(img,noplates_path) #随机背景
    if randomChance(0.3):
        img = rotRandrom(img,2,(img.shape[1],img.shape[0])); #透视变换 旋转平移
    if randomChance(0.1):
        img = tfactor(img) #变色
    if randomChance(0.1):
        img = AddGauss(img, 0+r(2)); #高斯平滑模糊
        #上下翻转 、 镜像 、 平移 
    if randomChance(0.1):
        img = addNoise(img) #添加噪声
    if randomChance(0.1):
        img = moveImg(img) #平移
    if randomChance(0.1):
        img = mirrorImg(img) #翻转

    return img

def dataAug(origin_path,gene_path,city,counts):
    #input: a dir of imgs,target generate path, city, times:增加数据倍数
    #output: augdata
    #ratio = 3000.0/counts
    img_names = getAllName(origin_path)
    # print(len(img_names))
    #cc = 0
    for n in img_names:
        #if city in n:
        if 1:
            #print(n)
            #cc+=1
            image = cv2.imdecode(np.fromfile(n,dtype = np.uint8),-1)
            bsname = os.path.basename(n)  

            if counts<10:
                times = ceil(10/counts)
                for t in range(times):
                    image2 = imgChange(image)
                    cv2.imencode('.jpg', image2)[1].tofile(gene_path+bsname.split('.')[-2]+'_'+str(t)+'.jpg')
            else:
                tmp = random.random()
                if tmp<10/counts: 
                    image3 = imgChange(image)
                    cv2.imencode('.jpg', image3)[1].tofile(gene_path+bsname.split('.')[-2]+'_0'+'.jpg')


if __name__ == '__main__':
    dataAug('t/','tt/','c',1)
