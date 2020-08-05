import os
import sys

import numpy as np
import cv2

import time
import random
import multiprocessing

def getAllName(file_dir, tail_list = ['.jpg','.png','.jpeg']): 
    L=[] 
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] in tail_list:
                L.append(os.path.join(root, file))
    return L





img_names = getAllName("head_voc/JPEGImages")


def processImg(img_name):
    img = cv2.imread(img_name)
    # do xxxx


t = time.time()

pool = multiprocessing.Pool(processes = 8)
pool_outputs = pool.map(processImg, img_names[37000:])
pool.close()
pool.join()

print("time: ", time.time()-t)
