
from imutils.video import VideoStream, FPS
import argparse
import imutils
import time
import cv2


video = "test_part.mp4"
tracker = "kcf"

(major, minor) = cv2.__version__.split(".")[:2]
print((major, minor))
if int(major)<3:
    tracker = cv2.Tracker_create(tracker.upper())

else:
    OPENCV_OBJECT_TRACKER = {
        "kcf": cv2.TrackerKCF_create
    }

    tracker = OPENCV_OBJECT_TRACKER[tracker]()

initBB = None

vs = cv2.VideoCapture(video)
fps = None

while True:
    ret, frame = vs.read()
    try:
        print(frame.shape)
    except:
        break
    frame = imutils.resize(frame, width=500)
    (H, W) = frame.shape[:2]

    if initBB is not None:
        (success, box) = tracker.update(frame)

        if success:
            (x, y, w, h) = [int(v) for v in box]
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
        fps.update()
        fps.stop()

        info = [
            ("Tracker", tracker),
            ("Success", "Yes" if success else "No"),
            ("FPS", "{:.2f}".format(fps.fps())),
        ]

        for (i, (k,v)) in enumerate(info):
            text = "{}: {}".format(k, v)
            cv2.putText(frame, text, (10, H-((i*20)+20)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255))

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(50) & 0xFF

    if key == ord("S"):
        initBB = cv2.selectROI("Frame", frame, fromCenter=False,
                showCrosshair=True)

        tracker.init(frame, initBB)
        fps = FPS().start()
    elif key==ord("Q"):
        break

vs.release()
cv2.destroyAllWindows()
