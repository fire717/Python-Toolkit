

import cv2
import numpy as np

def rotate_bound(image, angle):
    # grab the dimensions of the image and then determine the
    # center
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)
 
    # grab the rotation matrix (applying the negative of the
    # angle to rotate clockwise), then grab the sine and cosine
    # (i.e., the rotation components of the matrix)
    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
 
    # compute the new bounding dimensions of the image
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))
 
    # adjust the rotation matrix to take into account translation
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY
 
    # perform the actual rotation and return the image
    return cv2.warpAffine(image, M, (nW, nH))

def rotate_bound_with_box(image,angle,box):
    #获取图像的尺寸
    #旋转中心
    (h,w) = image.shape[:2]
    (cx,cy) = (w/2,h/2)
    
    #设置旋转矩阵
    M = cv2.getRotationMatrix2D((cx,cy),-angle,1.0)
    cos = np.abs(M[0,0])
    sin = np.abs(M[0,1])
    
    # 计算图像旋转后的新边界
    nW = int((h*sin)+(w*cos))
    nH = int((h*cos)+(w*sin))
    
    # 调整旋转矩阵的移动距离（t_{x}, t_{y}）
    M[0,2] += (nW/2) - cx
    M[1,2] += (nH/2) - cy

    x1,y1,x4,y4 = box

    new_x1 = M[0][0] * x1 + M[0][1] * y1 + M[0][2] 
    new_y1 = M[1][0] * x1 + M[1][1] * y1 + M[1][2] 
    new_x2 = M[0][0] * x1 + M[0][1] * y4 + M[0][2] 
    new_y2 = M[1][0] * x1 + M[1][1] * y4 + M[1][2] 
    new_x3 = M[0][0] * x4 + M[0][1] * y1 + M[0][2] 
    new_y3 = M[1][0] * x4 + M[1][1] * y1 + M[1][2] 
    new_x4 = M[0][0] * x4 + M[0][1] * y4 + M[0][2] 
    new_y4 = M[1][0] * x4 + M[1][1] * y4 + M[1][2] 

    final_x1 = min(new_x1,new_x2,new_x3,new_x4)
    final_y1 = min(new_y1,new_y2,new_y3,new_y4)
    final_x2 = max(new_x1,new_x2,new_x3,new_x4)
    final_y2 = max(new_y1,new_y2,new_y3,new_y4)

    new_box = [final_x1,final_y1,final_x2,final_y2]
    new_box = [int(v) for v in new_box]
    
    return cv2.warpAffine(image,M,(nW,nH)), new_box


img = cv2.imread("res.jpg")
box = [100,200,50,100]
cv2.rectangle(img, (box[0],box[1]),(box[2],box[3]),(255,0,0),3)

img,box = rotate_bound_with_box(img,30,box)#cv2.flip(img, 1)
print(box)
cv2.rectangle(img, (box[0],box[1]),(box[2],box[3]),(0,255,0),1)



cv2.imwrite("res2.jpg", img)
