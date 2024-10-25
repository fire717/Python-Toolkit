#coding:utf-8

import cv2
import numpy as np
import os
import shutil
import random

def get_names(file_dir, tail_list = ['.jpg']): 
    L=[] 
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] in tail_list:
                L.append(os.path.join(root, file))
    return L

def copy_file(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(dstfile)    #分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #创建路径
        shutil.copyfile(srcfile,dstfile)      #复制文件

srcfiles="added/ourdata_true_clean_31W/"
dstfiles='ALL/'

name_list = get_names(srcfiles)
print(name_list[0])
#copy_file(srcfile,dstfile)

for i in range(len(name_list)):

    name_path = name_list[i]
    name = os.path.basename(name_path)

    rr = random.random()
    if rr<1:

        dstfile =  dstfiles+name
        copy_file(name_path,dstfile)
