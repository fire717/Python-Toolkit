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


def mycopyfile(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(dstfile)    #分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #创建路径
        shutil.copyfile(srcfile,dstfile)      #复制文件

srcfiles="added/ourdata_true_clean_31W/"
dstfiles='ALL/'

name_list = getAllName(srcfiles)
print(name_list[0])
#mycopyfile(srcfile,dstfile)

for i in range(len(name_list)):

    name_path = name_list[i]
    name = os.path.basename(name_path)

    rr = random.random()
    if rr<1:

        dstfile =  dstfiles+name
        mycopyfile(name_path,dstfile)
