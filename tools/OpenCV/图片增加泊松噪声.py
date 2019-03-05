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



#############  v2
#v1在imshow的时候会有问题，原因在于声明新数组的时候，opencv需要dtype为np.uint8
#但是直接加，噪声又会变成黑色，因为默认dtype为float32，会有损失
#就需要假设一个np.clip(x,A,B) 会对x中的数字把小于A的变为A大于B的变为B
import cv2
import numpy as np
import random

def addPSNoise(img):
    #泊松噪声
    _mNoiseFactor = random.randint(50,100)
    MEAN_FACTOR = 2.0
    h, w = img.shape[:2]
    c = img.shape[-1]
    if c!=w and c!= 1:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 

    new_img = np.zeros((h,w,1),dtype=np.uint8)

    L = np.exp(-_mNoiseFactor * MEAN_FACTOR)
        
    th = random.choice([0, 0.5 ,1])
    for i in range(h):
        for j in range(w):
            k = 0
            p = 1

            while p>=L:
                k+=1
                p*=random.random()
            maxP = max(int(img[i][j] + (k - 1) / MEAN_FACTOR - _mNoiseFactor), 0)
            if maxP==img[i][j] and maxP!=0 and random.random()<th:
                maxP -= 10
            new_img[i][j] = np.clip(maxP, 0,255) 
    print(new_img[0][0])
    return new_img


img = cv2.imread("1.jpg")
img = addPSNoise(img)
print(img.shape, img[0][0])
cv2.imwrite("4.jpg",img)

cv2.namedWindow("Image")
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()  
