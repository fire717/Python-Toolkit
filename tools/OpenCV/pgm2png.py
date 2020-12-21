from PIL import Image
import os
import cv2
import numpy as np

def getFileNames(file_dir, tail_list=['.png','.jpg','.JPG','.PNG']): 
    L=[] 
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] in tail_list:
                L.append(os.path.join(root, file))
    return L


read_dir = 'faces'

img_names = getFileNames(read_dir,['.pgm'])
print(len(img_names))

for img_name in img_names:
    if img_name[-3:] == 'pgm':
        img = Image.open(img_name)
        img = np.array(img)
        save_name = img_name[:-3]+'png'
        cv2.imwrite(save_name, img)
