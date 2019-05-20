#手写体变形
#参考文献：Best Practices for Convolutional Neural Networks Applied to Visual Document Analysis
#参考博客：https://blog.csdn.net/maliang_1993/article/details/82020596
import numpy as np
import pandas as pd
import cv2
from scipy.ndimage.interpolation import map_coordinates
from scipy.ndimage.filters import gaussian_filter
import matplotlib.pyplot as plt
import random

def Elastic_transform(image):
    alpha = random.randint(80,100)
    sigma = random.choice([8,9,10])
    shape = image.shape
    #print(*shape)
    shape_size = shape[:2]
    dx = gaussian_filter((np.random.random(shape) * 2 - 1), sigma) * alpha
    dy = gaussian_filter((np.random.random(shape) * 2 - 1), sigma) * alpha
    dz = np.zeros_like(dx)
    x, y, z = np.meshgrid(np.arange(shape[1]), np.arange(shape[0]), np.arange(shape[2]))
    indices = np.reshape(y+dy, (-1, 1)), np.reshape(x+dx, (-1, 1)), np.reshape(z, (-1, 1))
    return map_coordinates(image, indices, order=1, mode='reflect').reshape(shape)


img = cv2.imread("write.jpg")
img = Elastic_transform(img)
cv2.imwrite("2.jpg", img)
