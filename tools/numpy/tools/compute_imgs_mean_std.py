#coding:utf-8
# Fire
# 利用公式 只用遍历一次

import cv2
import os
import numpy as np
from PIL import Image



def getAllName(file_dir, tail_list = ['.jpg']): 
    L=[] 
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] in tail_list:
                L.append(os.path.join(root, file))
    return L


imgs = getAllName("origin/dataset_en")
img_num = len(imgs)
print(img_num)
pix_num = img_num*224*224

R_mean = 0
G_mean = 0
B_mean = 0
R_std = 0
G_std = 0
B_std = 0
for idx in range(img_num):
    filename = imgs[idx]
    print(filename)
    img = cv2.imread(filename) 
    img = cv2.resize(img, (224,224))

    img = np.array(img)
    img = img.astype(np.float32)
    #img = np.multiply(img, 1.0 / 255) 

    R_mean += np.sum(img[:, :, 2])
    G_mean += np.sum(img[:, :, 1])
    B_mean += np.sum(img[:, :, 0])

    R_std += np.sum(np.power(img[:, :, 2],2.0))
    G_std += np.sum(np.power(img[:, :, 1],2.0))
    B_std += np.sum(np.power(img[:, :, 0],2.0))

R_mean = R_mean*1.0/pix_num
G_mean = G_mean*1.0/pix_num
B_mean = B_mean*1.0/pix_num

R_std = np.sqrt(R_std/pix_num - R_mean*R_mean)
G_std = np.sqrt(G_std/pix_num - G_mean*G_mean)
B_std = np.sqrt(B_std/pix_num - B_mean*B_mean)

res_mean = [R_mean, G_mean, B_mean]
res_std = [R_std, G_std, B_std]

print(img_num)
print("res R G B mean:", res_mean)
print("res R G B std:", res_std)
