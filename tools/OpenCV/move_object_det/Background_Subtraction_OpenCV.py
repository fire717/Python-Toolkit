import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()

c=1
path = 'VID/'
while(1):
    ret, frame = cap.read()

    t = time.time()
    fgmask = fgbg.apply(frame)
    print(time.time() - t)

    timeF = 2  # 视频帧计数间隔频率
    if (c % timeF == 0) : # 每隔timeF帧进行存储操作
        cv2.imwrite(path + str(c) + '_1.jpg', frame)
        cv2.imwrite(path + str(c) + '.jpg', fgmask)  # 存储为图像   不能带中文
    c+=1

    cv2.imshow('frame',fgmask)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

