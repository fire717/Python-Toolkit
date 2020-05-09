import cv2
import numpy as np
import random




def isGray(img):
    #判断一个三通道的图像是否为灰度图
    ratio = 0.5
    #为了提高检测速度，设置随机判断截取的比例

    h,w = img.shape[:2]
    h_list = random.sample(range(h), int(h*ratio))
    w_list = random.sample(range(w), int(w*ratio))

    count = 0
    for i in h_list:
        for j in w_list:
            color_std = np.std(img[i][j])
            if color_std!=0:
                count+=1
    if count == 0:
        return True
    else:
        return False



image = cv2.imread("1.jpg")
print(isGray(image))
