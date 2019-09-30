#coding:utf-8
from __future__ import print_function
import numpy as np
import cv2
from cv2 import dnn
import sys
 
# import tensorflow as tf
# from tensorflow.python.framework import graph_util
import os

print(cv2.__version__)

blob = dnn.blobFromImage(cv2.imread("3.jpg"), 1, (48, 48), (104, 117, 123))
print("Input:", blob.shape, blob.dtype)


net = dnn.readNetFromCaffe('deploy.prototxt', 'snapshot_iter_100000.caffemodel')
net.setInput(blob)
prob = net.forward()
print("Output:", prob.shape, prob)


