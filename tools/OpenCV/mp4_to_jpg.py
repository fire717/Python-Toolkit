import cv2
import os

from ssim import *


#获得视频的格式
read_path = 'D14-领导从车闸出去录像/D14_20210901160459.mp4'
save_dir = "true_img"
save_name = "cardoor1"


videoCapture = cv2.VideoCapture(read_path)
  
#获得码率及尺寸
fps = videoCapture.get(cv2.CAP_PROP_FPS)
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)), 
        int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
fNUMS = videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)
print(fps, size, fNUMS)
 
#读帧
success, frame = videoCapture.read()

idx = 0
# interval = 6
resize_size = (320,180)
last_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
last_frame = cv2.resize(last_frame, resize_size)
th = 0.9


while success :
    if(idx%2000==0):
        print(idx)

    success, frame = videoCapture.read() #获取下一帧

    # if idx % interval==0:
    frame_this = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame_this = cv2.resize(frame_this, resize_size)
    ssim = compute_ssim(last_frame,frame_this)
    
    if ssim<th:
        print(ssim)
        save_path = os.path.join(save_dir,save_name, save_name+"_"+str(idx)+'.jpg')
        cv2.imwrite(save_path, frame)
        last_frame = frame_this

    idx+=1
 
videoCapture.release()
