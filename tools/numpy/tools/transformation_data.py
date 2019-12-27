#coding:utf-8
#python rename.py "xx路径"  
import cv2

import numpy as np
from PIL import Image

import random

def transformation_data(x_train, y_train, x_test, y_test):
    data_list = []
    for i in range(len(x_train)):
        pair = [x_train[i], y_train[i]]
        data_list.append(pair)
    for i in range(len(x_test)):
        pair = [x_test[i], y_test[i]]
        data_list.append(pair)

    split_ratio = 0.9
    train_num = int(len(data_list)*split_ratio)
    random.shuffle(data_list)
    # train_list = data_list[:train_num]
    # test_list = data_list[train_num:]
    print(data_list[0][1].shape)
    #b

    x_train = []
    y_train = []
    x_test = []
    y_test = []
    for i in range(len(data_list)):
        if i <train_num:
            x_train.append(data_list[i][0])
            y_train.append(data_list[i][1])
        else:
            x_test.append(data_list[i][0])
            y_test.append(data_list[i][1])

    x_train = np.array(x_train)
    y_train = np.array(y_train)
    x_test = np.array(x_test)
    y_test = np.array(y_test)

    return x_train, y_train, x_test, y_test
#(3384, 224, 224, 3) (3384, 47) (1128, 224, 224, 3) (1128, 47)
#shape222:  (3384, 224, 224, 3) (3384, 47) (1128, 224, 224, 3) (1128, 47)

x1 = np.ones((3384, 224, 224, 3))*1
y1 = np.ones((3384, 47))*2
x2 = np.ones((1128, 224, 224, 3))*3
y2 = np.ones((1128, 47))*4


print(x1.shape,y1.shape,x2.shape,y2.shape)
#print(x1[0],y1[0],x2[0],y2[0])

x1,y1,x2,y2 = transformation_data(x1,y1,x2,y2)
print(x1.shape,y1.shape,x2.shape,y2.shape)
