import matplotlib.pyplot as plt
import numpy as np
import cv2

def get_contour(img_gray):
    """获取连通域

    :param img: 输入图片
    :return: 最大连通域
    """
    # 灰度化, 二值化, 连通域分析


    ret, img_bin = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

    
    contours, hierarchy = cv2.findContours(img_bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    return hierarchy, contours[0]


def cropHead(img, hair_mask, landmarks):
    

    hierarchy, contours = get_contour(hair_mask)
    #print(contours.shape)#(239, 1, 2)

    contours = np.concatenate((landmarks,contours), axis=0)


    # cv2.drawContours(img, contours,-1,(0,0,255),3) 

    hull = cv2.convexHull(contours)
    #print(hull)

    # length = len(hull)
    # for i in range(len(hull)):
    #     cv2.line(img, tuple(hull[i][0]), tuple(hull[(i+1)%length][0]), (0,255,0), 2)


    res = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)

    pattern = np.zeros_like(res)
    pattern = cv2.fillPoly(pattern, [hull.astype(np.int)], (1., 1., 1., 1.))

    cv2.imwrite("masked.png", res*pattern)


    # cv2.imwrite('224_landmark.jpg', img)



if __name__ == '__main__':

    img = img = cv2.imread('224.jpg')
    h,w = img.shape[:2]
    print(img.shape)
    
    hair_mask = cv2.imread('224_mask.jpg',0)
    print(hair_mask.shape)


    landmarks = []
    with open("landmark.txt", "r") as f:
        landmark_lines = f.readlines()
    for i,line in enumerate(landmark_lines):
        if i%2==1:
            continue
        line = line.strip().split(' ')[-2:]
        p = [float(x) for x in line]
        p = [int(p[0]*w), int(p[1]*h)]
        landmarks.append(p)
        #cv2.circle(img, (p[0],p[1]),2, (255,0,0), 2)
    #print(np.array(landmarks).shape)
    landmarks = np.array(landmarks)
    landmarks = landmarks[:,np.newaxis,:]
    print(landmarks.shape)


    cropHead(img, hair_mask, landmarks)

