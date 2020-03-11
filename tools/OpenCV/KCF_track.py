#coding: utf-8
#from imutils.video import VideoStream, FPS
import argparse
#import imutils
import time
import cv2


tracker = cv2.TrackerKCF_create()
#需要安装contrib    pip install opencv-contrib-python

capture = cv2.VideoCapture("test_part.mp4")
initBox = None
#fps = None

track_times = []

while True:
    ret, frame = capture.read()
    if not ret:
        break

    #frame = imutils.resize(frame, width=500)
    #(H, W) = frame.shape[:2]

    if initBox is not None:

        t = time.time()
        (success, box) = tracker.update(frame)
        track_times.append(time.time()-t)

        if success:
            (x, y, w, h) = [int(v) for v in box]
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
        #fps.update()
        #fps.stop()

        # info = [
        #     ("Tracker", tracker),
        #     ("Success", "Yes" if success else "No"),
        #     #("FPS", "{:.2f}".format(fps.fps())),
        # ]

        # for (i, (k,v)) in enumerate(info):
        #     text = "{}: {}".format(k, v)
        #     cv2.putText(frame, text, (10, H-((i*20)+20)),
        #         cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255))


    cv2.imshow("Frame", frame)
    key = cv2.waitKey(10) & 0xFF

    if key == ord("S"):
        initBox = cv2.selectROI("Frame", frame, fromCenter=False,
                showCrosshair=True)
        print("initBox: ",initBox) #(368, 40, 132, 199) x, y, w, h
        tracker.init(frame, initBox)
        #fps = FPS().start()
    if key==ord("Q"):
        break

capture.release()
cv2.destroyAllWindows()


import numpy as np
print(len(track_times), np.max(track_times), np.min(track_times), np.mean(track_times))
#73 0.026923418045043945 0.009968280792236328 0.01155070082782066

