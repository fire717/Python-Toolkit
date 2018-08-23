#coding:utf-8

import cv2
import numpy as np
import os,shutil
import random

def getAllName(file_dir): 
    L=[] 
    for root, dirs, files in os.walk(file_dir):
        # root 所指的是当前正在遍历的这个文件夹的本身的地址
        # dirs 是一个 list ，内容是该文件夹中所有的目录的名字(不包括子目录)
        # files 同样是 list , 内容是该文件夹中所有的文件(不包括子目录)
        for file in files:
            if os.path.splitext(file)[1] == '.jpg':
                L.append(os.path.join(root, file))
    return L


def moveImg(origin_data_dir, target_dir ):
    name_list = getAllName(origin_data_dir)
    for d in name_list:
        if random.random()<2:
            file = os.path.basename(d)  
            # print(os.path.basename(d))
            # print(d, target_dir+'/'+file)
            try:
                os.rename(d, target_dir+'/'+file)
            except:
                continue

moveImg('gen_all','ALL')
