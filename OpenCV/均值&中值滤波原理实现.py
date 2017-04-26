# -*- coding: utf-8 -*-
import cv2
import numpy as np
img=cv2.imread('a.jpg',0)

coutn = 500
for k in xrange(0,coutn):
        #get the random point
   xi = int(np.random.uniform(0,img.shape[1]))
   xj = int(np.random.uniform(0,img.shape[0]))
   if k%2==0:   
       img[xj,xi] = 25
   elif k%2!=0:
       img[xj,xi]=0

cv2.imshow('img',img)
cv2.waitKey(0)

result = cv2.medianBlur(img,5) 

img1 = img
x=img.shape[0]
y=img.shape[1]
'''
#JUNZHI
for i in xrange(1,x-1):
    for j in xrange(1,y-1):
        img[i,j]=(int(img1[i-1,j-1])+int(img1[i-1,j])+int(img1[i-1,j+1])+int(img1[i,j-1])+int(img1[i,j])+\
            int(img1[i,j+1])+int(img1[i+1,j-1])+int(img1[i+1,j])+int(img1[i+1,j+1]))/9
'''  
#ZHONGZHI 
for i in xrange(1,x-1):
    for j in xrange(1,y-1):
        med=list((int(img1[i-1,j-1]),int(img1[i-1,j]),int(img1[i-1,j+1]),int(img1[i,j-1]),int(img1[i,j]),\
            int(img1[i,j+1]),int(img1[i+1,j-1]),int(img1[i+1,j]),int(img1[i+1,j+1])))
        med.sort()
        img[i,j] = med[4]

cv2.imshow('img1',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
