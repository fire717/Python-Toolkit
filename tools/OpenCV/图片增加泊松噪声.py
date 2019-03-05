import cv2
import numpy as np
import random

def addPSNoise(img):
    #泊松噪声
    _mNoiseFactor = 50#random.randint(20,50)#25  [1，50]
    MEAN_FACTOR = 2.0
    h, w = img.shape[:2]
    c = img.shape[-1]
    if c!=w and c!= 1:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
        
    new_img = np.zeros((h,w,1))

    L = np.exp(-_mNoiseFactor * MEAN_FACTOR)
        
    th = random.choice([0, 0.5 ,1])
    for i in range(h):
        for j in range(w):
            k = 0
            p = 1

            while p>=L:
                k+=1
                p*=random.random()
            maxP = max((img[i][j] + (k - 1) / MEAN_FACTOR - _mNoiseFactor), 0)
            if maxP!=img[i][j] and maxP!=0 and random.random()<th:
                maxP -= 10
            new_img[i][j] = max(maxP, 0)
    return new_img


img = cv2.imread("1.jpg")
img = addPSNoise(img)
cv2.imwrite("4.jpg",img)
