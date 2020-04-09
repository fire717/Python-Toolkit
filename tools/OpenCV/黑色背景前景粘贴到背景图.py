
import numpy as np
import cv2





bg_img = cv2.imread("img_11.jpg")
fore_img = cv2.imread("000000-color.jpg")


fore_img = cv2.resize(fore_img,(100,100))
roi = bg_img[300:400,200:300]


img2gray = cv2.cvtColor(fore_img,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, 0)
mask_inv = cv2.bitwise_not(mask)


roi_part = cv2.bitwise_and(roi,roi,mask=mask_inv) 

fore_part = cv2.bitwise_and(fore_img,fore_img,mask=mask) 
 
dst = cv2.add(roi_part,fore_part)
 
bg_img[300:400,200:300] = dst
cv2.imwrite("res.jpg", bg_img)
