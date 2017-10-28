#coding:UTF-8
#数字图像处理课的作业，使用一些基本操作处理图片

import cv2
import cv2.cv as cv
import numpy as np
from numpy import random

def SaltAndPepper(src,percetage):
    NoiseImg=src
    NoiseNum=int(percetage*src.shape[0]*src.shape[1])
    for i in range(NoiseNum):
        randX=random.random_integers(0,src.shape[0]-1)
        randY=random.random_integers(0,src.shape[1]-1)
        if random.random_integers(0,1)==0:
            NoiseImg[randX,randY]=0
        else:
            NoiseImg[randX,randY]=255          
    return NoiseImg 

# read a picture
img = cv2.imread("test.jpg")
cv2.namedWindow("Image")
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()  

# switch to grey
emptyImage = np.zeros(img.shape, np.uint8)  
emptyImage2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 

cv2.namedWindow("Image")
cv2.imshow("Image",emptyImage2)
cv2.waitKey(0)
cv2.destroyAllWindows()  

cv2.imwrite("2.jpg", emptyImage2)

# add 10%Gausi-Noise
img1 = cv2.imread("test.jpg")
coutn = 100000
for k in xrange(0,coutn):
        #get the random point
    xi = int(np.random.uniform(0,img1.shape[1]))
    xj = int(np.random.uniform(0,img1.shape[0]))
        #add noise
    if k%10==0:
        if img1.ndim == 2:
            img1[xj,xi] = 255
        elif img1.ndim == 3:
            img1[xj,xi,0] = 25
            img1[xj,xi,1] = 20
            img1[xj,xi,2] = 20
        
cv2.namedWindow('img1')
cv2.imshow('img1',img1)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imwrite("3.jpg", img1)

# add 10% salt-noise
img2=cv2.imread('test.jpg')
NoiseImg=SaltAndPepper(img2,0.1)

cv2.imshow('img2',NoiseImg)
cv2.waitKey()
cv2.imwrite("4.jpg", NoiseImg)

# zhifangtu
image = cv2.imread("test.jpg")  
  
lut = np.zeros(256, dtype = image.dtype )#创建空的查找表  
  
hist,bins = np.histogram(image.flatten(),256,[0,256])   
cdf = hist.cumsum() #计算累积直方图  
cdf_m = np.ma.masked_equal(cdf,0) #除去直方图中的0值  
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())#等同于前面介绍的lut[i] = int(255.0 *p[i])公式  
cdf = np.ma.filled(cdf_m,0).astype('uint8') #将掩模处理掉的元素补为0  

result = cv2.LUT(image, cdf)  #计算  
  
cv2.imshow("OpenCVLUT", result)  
cv2.waitKey(0)  
cv2.destroyAllWindows()  
cv2.imwrite("5.jpg", result)
# clear noise
img = cv2.imread("test.jpg")  
median = cv2.medianBlur(img, 5)  
cv2.imshow("Median", median)  
cv2.waitKey(0)  
cv2.destroyAllWindows()  

cv2.imwrite("6.jpg", median)
# SBR ruihua
img = cv2.imread("test.jpg")  
  
x = cv2.Sobel(img,cv2.CV_16S,1,0)  
y = cv2.Sobel(img,cv2.CV_16S,0,1)  
  
absX = cv2.convertScaleAbs(x)   # 转回uint8  
absY = cv2.convertScaleAbs(y)  
  
dst = cv2.addWeighted(absX,0.5,absY,0.5,0)  
  
cv2.imshow("Result", dst)  
  
cv2.waitKey(0)  
cv2.destroyAllWindows()  
cv2.imwrite("7.jpg", dst)
# LPLS ruihua
img = cv2.imread("test.jpg")  
  
gray_lap = cv2.Laplacian(img,cv2.CV_16S,ksize = 3)  
dst2 = cv2.convertScaleAbs(gray_lap)  
  
cv2.imshow('laplacian',dst2)  
cv2.waitKey(0)  
cv2.destroyAllWindows()  
cv2.imwrite("8.jpg", dst2)

# add number

#cv.CV_WINDOW_AUTOSIZE这个参数设定显示窗口虽图片大小自动变化
cv.NamedWindow('You need to struggle', cv.CV_WINDOW_AUTOSIZE)
image=cv.LoadImage('test.jpg')
 
#创建一个矩形，来让我们在图片上写文字，参数依次定义了文字类型，高，宽，字体厚度等。。
font=cv.InitFont(cv.CV_FONT_HERSHEY_SCRIPT_SIMPLEX, 1, 1, 0, 3, 8)
 
#将文字框加入到图片中，(5,20)定义了文字框左顶点在窗口中的位置，最后参数定义文字颜色
cv.PutText(image, "3160602004", (30,30), font, (255,0,0))

cv.ShowImage('You need to struggle', image)
cv.WaitKey(0)
cv.SaveImage('9.jpg', image)
