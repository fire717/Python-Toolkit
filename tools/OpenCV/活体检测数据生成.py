

import numpy as np
import cv2
import random

FACE_CASCADE = cv2.CascadeClassifier(r'haarcascade_frontalface_alt.xml')


def detectFace(img):
    
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = FACE_CASCADE.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3,
                    minSize=(10, 10))
    return faces


def mergeHead(fore_img, bg_img):
    #合并纯人脸
    head_h = 75
    head_w = 75
    target_h = 224
    target_w = 224

    fore_img = cv2.resize(fore_img,(head_w,head_h))
    bg_h, bg_w = bg_img.shape[:2]

    if bg_h<target_h or bg_w<target_w:
        ratio = min(target_h,target_w)/min(bg_h, bg_w)
        bg_img = cv2.resize(fore_img,(int(bg_w*ratio), int(bg_h*ratio)))
        bg_h, bg_w = bg_img.shape[:2]

    roi_x = random.randint(head_w, bg_w-head_w)
    roi_y = random.randint(head_h, bg_h-head_h)

    roi = bg_img[roi_y:roi_y+head_h,roi_x:roi_x+head_w]

    img2gray = cv2.cvtColor(fore_img,cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 5, 255, 0)
    mask_inv = cv2.bitwise_not(mask)
    roi_part = cv2.bitwise_and(roi,roi,mask=mask_inv) 
    fore_part = cv2.bitwise_and(fore_img,fore_img,mask=mask) 
    dst = cv2.add(roi_part,fore_part)
     
    bg_img[roi_y:roi_y+head_h,roi_x:roi_x+head_w] = dst

    #crop
    crop_x1 = max(0, roi_x-head_w)
    crop_y1 = max(0, roi_y-head_h)
    crop_x2 = min(bg_w, roi_x+head_w*2)
    crop_y2 = min(bg_h, roi_y+head_h*2)
    crop_img = bg_img[crop_y1:crop_y2,crop_x1:crop_x2]

    crop_img = cv2.resize(crop_img,(target_w,target_h))
    return crop_img


def mergeFaceToFace(fore_img, bg_img):
    #模拟带面具  bg_img必须有人脸

    target_h = 224
    target_w = 224

    bg_h, bg_w = bg_img.shape[:2]
    if bg_h<target_h or bg_w<target_w:
        ratio = min(target_h,target_w)/min(bg_h, bg_w)
        bg_img = cv2.resize(fore_img,(int(bg_w*ratio), int(bg_h*ratio)))
        bg_h, bg_w = bg_img.shape[:2]

    faces = detectFace(bg_img)
    if len(faces)==0:
        print("No faces detected!")
        return None

    #找填充位置
    x,y,w,h = faces[0]

    random_x = max(0, x+random.randint(-6,2))
    random_y = max(0, y+random.randint(-6,2))
    random_w = min(bg_w, w+random.randint(-2,6))
    random_h = min(bg_h, h+random.randint(-2,6))
    fore_img = cv2.resize(fore_img,(random_w,random_h))

    roi = bg_img[random_y:random_y+random_h,random_x:random_x+random_w]
    cv2.imwrite("roi.jpg", roi)

    img2gray = cv2.cvtColor(fore_img,cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 5, 255, 0)
    mask_inv = cv2.bitwise_not(mask)
    cv2.imwrite("mask_inv.jpg", mask_inv)
    roi_part = cv2.bitwise_and(roi,roi,mask=mask_inv) 
    fore_part = cv2.bitwise_and(fore_img,fore_img,mask=mask) 
    dst = cv2.add(roi_part,fore_part)
     
    bg_img[random_y:random_y+random_h,random_x:random_x+random_w] = dst

    #crop
    crop_x1 = max(0, random_x-random_w)
    crop_y1 = max(0, random_y-random_h)
    crop_x2 = min(bg_w, random_x+random_w*2)
    crop_y2 = min(bg_h, random_y+random_h*2)
    crop_img = bg_img[crop_y1:crop_y2,crop_x1:crop_x2]

    crop_img = cv2.resize(crop_img,(target_w,target_h))
    return crop_img



def addSelfHeadToHead(img):
    #模拟带面具  

    target_h = 224
    target_w = 224

    bg_h, bg_w = img.shape[:2]
    if bg_h<target_h or bg_w<target_w:
        ratio = min(target_h,target_w)/min(bg_h, bg_w)
        bg_img = cv2.resize(fore_img,(int(bg_w*ratio), int(bg_h*ratio)))
        bg_h, bg_w = bg_img.shape[:2]

    faces = detectFace(img)
    if len(faces)==0:
        print("No faces detected!")
        return None

    #找填充位置
    x,y,w,h = faces[0]
    roi = img[y:y+h,x:x+w].copy()

    random_x = max(0, x+random.choice([-10,-8,-6]))
    random_y = max(0, y+random.choice([-10,-8,-6]))
    random_w = min(bg_w, w+random.choice([-5,5,7,9,11,13]))
    random_h = min(bg_h, h+random.choice([-5,5,7,9,11,13]))

    roi = cv2.resize(roi,(random_w,random_h))
    img[random_y:random_y+random_h,random_x:random_x+random_w] = roi

    #crop
    crop_x1 = max(0, random_x-random_w)
    crop_y1 = max(0, random_y-random_h)
    crop_x2 = min(bg_w, random_x+random_w*2)
    crop_y2 = min(bg_h, random_y+random_h*2)
    crop_img = img[crop_y1:crop_y2,crop_x1:crop_x2]

    crop_img = cv2.resize(crop_img,(target_w,target_h))
    return crop_img


def addSelfHead(img):
    #复制本图的人脸
    head_h = 75
    head_w = 75
    target_h = 224
    target_w = 224
    img_h, img_w = img.shape[:2]

    if bg_h<target_h or bg_w<target_w:
        ratio = min(target_h,target_w)/min(bg_h, bg_w)
        bg_img = cv2.resize(fore_img,(int(bg_w*ratio), int(bg_h*ratio)))
        bg_h, bg_w = bg_img.shape[:2]

    
    faces = detectFace(img)
    if len(faces)==0:
        print("No faces detected!")
        return None

    x,y,w,h = faces[0]
    roi = img[y:y+h,x:x+w].copy()
    roi = cv2.resize(roi,(head_w,head_h))

    #找填充位置
    range_max = 20

    draw_x1 = random.randint(head_w, img_w-head_w)
    draw_y1 = random.randint(head_h, img_h-head_h)
    img[draw_y1:draw_y1+head_h,draw_x1:draw_x1+head_w] = roi

    #crop
    crop_x1 = max(0, draw_x1-head_w)
    crop_y1 = max(0, draw_y1-head_h)
    crop_x2 = min(img_w, draw_x1+head_w*2)
    crop_y2 = min(img_h, draw_y1+head_h*2)
    crop_img = img[crop_y1:crop_y2,crop_x1:crop_x2]

    crop_img = cv2.resize(crop_img,(target_w,target_h))
    return crop_img


def addBoard(img):
    target_h = 224
    target_w = 224

    img_h, img_w = img.shape[:2]
    faces = detectFace(img)
    if len(faces)==0:
        print("No faces detected!")
        return None

    x,y,w,h = faces[0]

    #draw box
    
    draw_x1 = max(0,random.randint(x-range_max, x))
    draw_y1 = max(0,random.randint(y-range_max, y))
    draw_x2 = min(img_w,random.randint(x+w, x+w+range_max))
    draw_y2 = min(img_h,random.randint(y+h, y+h+range_max))

    color = random.randint(0,255)
    colors = (color, color, color)
    line_w = random.randint(1,5)
    img = cv2.rectangle(img, (draw_x1,draw_y1), (draw_x2,draw_y2), colors, line_w)

    #crop
    range_max = 20
    crop_x1 = max(0, x-w+random.randint(range_max))
    crop_y1 = max(0, y-h+random.randint(range_max))
    crop_x2 = min(img_w, x+w*2-random.randint(range_max))
    crop_y2 = min(img_h, y+h*2-random.randint(range_max))
    crop_img = img[crop_y1:crop_y2,crop_x1:crop_x2]

    crop_img = cv2.resize(crop_img,(target_w,target_h))
    return crop_img





if __name__ == "__main__":

    bg_img = cv2.imread("00a4bd7c8c92aa38.jpg")
    fore_img = cv2.imread("000000-color.jpg")

    # res_img = mergeHead(fore_img, bg_img)
    # cv2.imwrite("res.jpg", res_img)

    #res_img = addSelfHead(bg_img)
    res_img = addSelfHeadToHead(bg_img)
    cv2.imwrite("res.jpg", res_img)

    # res_img = addBoard(bg_img)
    # cv2.imwrite("res.jpg", res_img)

    # res_img = mergeFaceToFace(fore_img, bg_img)
    # cv2.imwrite("res.jpg", res_img)
