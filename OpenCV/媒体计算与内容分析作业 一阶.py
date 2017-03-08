#coding:utf-8

import cv2

def showImg(name):
    s=str(name)
    cv2.namedWindow(s)
    cv2.imshow(s,name)
    cv2.waitKey(0)
    cv2.destroyAllWindows()  

# read a picture
img = cv2.imread("dog.jpg")
showImg(img)


# switch to grey
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
showImg(imgGray)

cv2.imwrite("gray.jpg", imgGray)

# switch to binary
ret,imgBin = cv2.threshold(imgGray,127,255,cv2.THRESH_BINARY)  
showImg(imgBin)

cv2.imwrite("bin.jpg", imgBin)