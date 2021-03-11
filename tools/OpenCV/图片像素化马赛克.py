#coding: utf-8
#from imutils.video import VideoStream, FPS
import argparse
#import imutils
import time
import cv2
import numpy as np


def imgColor(img):
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    hsv[:,:,0] = hsv[:,:,0]*1.0
    hsv[:,:,1] = hsv[:,:,1]*1.1
    hsv[:,:,2] = hsv[:,:,2]*1.2
    img = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
    return img



def imgChange(img):
    w = 480
    h = 640
    img = cv2.resize(img, (h//2, w//2))

    # img = imgColor(img)
    img = cv2.convertScaleAbs(img,alpha=1.3,beta=0)

    block_len = 20

    for i in range(w//block_len):
        for j in range(h//block_len):
            #colors = np.reshape(img[block_len*i:block_len*(i+1),block_len*j:block_len*(j+1)],(-1,3))
            #colors = img[block_len*i:block_len*(i+1),block_len*j:block_len*(j+1)].reshape((-1,3))
            #mean_color = np.mean(colors, axis=0)
            #sumImg = opencv.cv.cvGetSubRect(img, opencv.cv.cvRect(x,y,w,h) )
            mean_color = cv2.mean(img[block_len*i:block_len*(i+1),block_len*j:block_len*(j+1)])[:3]
            #print(mean_color)
            img[block_len*i:block_len*(i+1), block_len*j:block_len*(j+1)] = mean_color

    img = cv2.resize(img, (h, w), interpolation=cv2.INTER_AREA)
    return img




"""




"""
def main():
    capture = cv2.VideoCapture(0)#"test_part.mp4"
    # FRAME_WIDTH = 640
    # FRAME_HEIGHT = 480

    # capture.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
    # capture.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

    initBox = None
    #fps = None

    track_times = []

    while True:
        t = time.time()
        ret, frame = capture.read()
        if not ret:
            break


        new_frame = imgChange(frame)

        cv2.imshow("Frame", new_frame)
        key = cv2.waitKey(1) & 0xFF


        if key==ord("Q"):
            break
        print("time: ", time.time() - t)


    capture.release()
    cv2.destroyAllWindows()

"""


"""


if __name__ == "__main__":
    main()

