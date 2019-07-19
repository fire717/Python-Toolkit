# -*- coding: utf-8 -*-
import cv2
import numpy as np
import os



def findBox(img):
    h, w, c = img.shape
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #cv2.imwrite('gray.jpg', gray)

    blurred = cv2.GaussianBlur(gray, (9, 9),0) 

    gradX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0)
    gradY = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1)

    gradient = cv2.subtract(gradX, gradY)
    gradient = cv2.convertScaleAbs(gradient)  #求梯度
    cv2.imwrite('1gradient.jpg', gradient)

    blurred = cv2.GaussianBlur(gradient, (9, 9),0)
    (_, thresh) = cv2.threshold(blurred, 20, 255, cv2.THRESH_BINARY)
    cv2.imwrite('2thresh.jpg', thresh)


    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7)) 
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    cv2.imwrite('3opening.jpg', opening)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (20, 20)) 
    closed = cv2.dilate(opening, kernel, iterations=2)
    cv2.imwrite('3closed.jpg', closed)

    (_, cnts, _) = cv2.findContours(closed,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


    c = sorted(cnts, key=cv2.contourArea, reverse=True)[0]

    rect = cv2.minAreaRect(c)
    box = np.int0(cv2.boxPoints(rect))

    draw_img = cv2.drawContours(img.copy(), [box], -1, (0, 0, 255), 3)
    cv2.imwrite('4draw_img.jpg', draw_img)

    Xs = [i[0] for i in box]
    Ys = [i[1] for i in box]
    x1 = max(0, min(Xs))
    x2 = min(w, max(Xs))
    y1 = max(0, min(Ys))
    y2 = min(h, max(Ys))
    crop_img= img[y1:y2, x1:x2]

    return crop_img


img_path = r'glass/'
for name in os.listdir(img_path):

    img = cv2.imread(os.path.join(img_path, name))
    crop_img = findBox(img)
    cv2.imwrite('%s.jpg' % name, crop_img)
