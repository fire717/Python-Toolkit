import numpy as np
import cv2
import time



from skimage import transform as tf

def applyGeometricTransformation(startXs, startYs, newXs, newYs, bbox):
    n_object = bbox.shape[0]
    newbbox = np.zeros_like(bbox)
    Xs = newXs.copy()
    Ys = newYs.copy()
    for obj_idx in range(n_object):
        startXs_obj = startXs[:,[obj_idx]]
        startYs_obj = startYs[:,[obj_idx]]
        newXs_obj = newXs[:,[obj_idx]]
        newYs_obj = newYs[:,[obj_idx]]
        desired_points = np.hstack((startXs_obj,startYs_obj))
        actual_points = np.hstack((newXs_obj,newYs_obj))
        t = tf.SimilarityTransform()
        t.estimate(dst=actual_points, src=desired_points)
        mat = t.params

        # estimate the new bounding box with all the feature points
        # coords = np.vstack((bbox[obj_idx,:,:].T,np.array([1,1,1,1])))
        # new_coords = mat.dot(coords)
        # newbbox[obj_idx,:,:] = new_coords[0:2,:].T

        # estimate the new bounding box with only the inliners (Added by Yongyi Wang)
        THRES = 1
        projected = mat.dot(np.vstack((desired_points.T.astype(float),np.ones([1,np.shape(desired_points)[0]]))))
        distance = np.square(projected[0:2,:].T - actual_points).sum(axis = 1)
        actual_inliers = actual_points[distance < THRES]
        desired_inliers = desired_points[distance < THRES]
        if np.shape(desired_inliers)[0]<4:
            print('too few points')
            actual_inliers = actual_points
            desired_inliers = desired_points
        t.estimate(dst=actual_inliers, src=desired_inliers)
        mat = t.params
        coords = np.vstack((bbox[obj_idx,:,:].T,np.array([1,1,1,1])))
        new_coords = mat.dot(coords)
        newbbox[obj_idx,:,:] = new_coords[0:2,:].T
        Xs[distance >= THRES, obj_idx] = -1
        Ys[distance >= THRES, obj_idx] = -1

    return Xs, Ys, newbbox

def trackPointToBox(p0):
    xmin = min(p0[:,:,0])
    xmax = max(p0[:,:,0])
    ymin = min(p0[:,:,1])
    ymax = max(p0[:,:,1])

    faces = [[xmin, ymin, xmax-xmin, ymax-ymin]]
    return faces








cap = cv2.VideoCapture("face_track/test.mp4")#cv2.VideoCapture(0)
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

isDetect = 0

# ShiTomasi 角点检测参数
feature_params = dict( maxCorners = 100,
                       qualityLevel = 0.3, #0.01
                       minDistance = 7,  #10
                       blockSize = 7 )  #3

# lucas kanade光流法参数
lk_params = dict( winSize  = (15,15),
                  maxLevel = 2,
                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# 创建随机颜色
color = np.random.randint(0,255,(100,3))

# 获取第一帧，找到角点
ret, old_frame = cap.read()
#找到原始灰度图
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)

#获取图像中的角点，返回到p0中
p0 = cv2.goodFeaturesToTrack(old_gray, mask = None, **feature_params)
#print(p0,type(p0),type(p0[0][0][0]))
#p0=0

# 创建一个蒙版用来画轨迹
mask = np.zeros_like(old_frame)

use_detect = True

faces = []
ii = 0
while(ii<400):
    t1 = time.time()

    ii+=1

    ret,frame = cap.read()
    if frame is None:
        break
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)




    if ii%5==0:#use_detect:
    #face
    #t = time.time()
        faces = detector.detectMultiScale(frame_gray, 1.3, 5)
        print(faces)#[[615 109 115 115]]
        #print("time1: ", time.time()- t)


        if len(faces)>0:

            for (x, y, w, h) in faces:

                face_mask = np.zeros(shape = frame.shape[:2], dtype=np.uint8)
                face_mask[y:y+h,x:x+w] = 255
                p0 = cv2.goodFeaturesToTrack(old_gray, mask = face_mask, **feature_params)




            

        img = frame

        use_detect = False

    else:
        # track
        # 计算光流
        #t = time.time()
        p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
        #print("time2: ", time.time()- t)
        # 选取好的跟踪点
        #print(p0.shape)#(17, 1, 2)
        #print(p0[:,:,0].shape)
        #print(st)

        good_new = p1[st==1]
        good_old = p0[st==1]

        # 画出轨迹
        for i,(new,old) in enumerate(zip(good_new,good_old)):
            a,b = new.ravel()
            c,d = old.ravel()
            #mask = cv2.line(mask, (a,b),(c,d), color[i].tolist(), 2)
            #frame = cv2.circle(frame,(a,b),5,color[i].tolist(),-1)
        img = cv2.add(frame,mask)


        
        new_faces = []
        #faces = trackPointToBox(p0)
        for (x, y, w, h) in faces:
            bbox1 = np.array([[[x,y],[x+w,y],[x,y+h],[x+w,y+h]]], dtype=np.float32) 
            startXs = p0[:,:,0]
            startYs = p0[:,:,1]
            newXs = p1[:,:,0]
            newYs = p1[:,:,1]
            Xs, Ys ,bbox2 = applyGeometricTransformation(startXs, startYs, newXs, newYs, bbox1)
            #print(Xs.shape)
            print(bbox2)
            #print(bbox2[0][0][0],bbox2[0][2][0])

            xmin = min(bbox2[0][0][0],bbox2[0][2][0])
            xmax = max(bbox2[0][1][0],bbox2[0][3][0])
            ymin = min(bbox2[0][0][1],bbox2[0][2][1])
            ymax = max(bbox2[0][1][1],bbox2[0][3][1])
            #print(xmin,ymin,xmax,ymax)
            new_faces = np.array([[xmin,ymin,xmax-xmin,ymax-ymin]],dtype = np.int32)
            print(new_faces)

        faces = new_faces

        # 更新上一帧的图像和追踪点
        old_gray = frame_gray.copy()
        p0 = good_new.reshape(-1,1,2)
        use_detect = True
        #print("time2: ", time.time()- t)


    # 画人脸框
    if len(faces)>0:
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('frame',img)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

    print("time total frame: ", time.time()- t1)

    

cv2.destroyAllWindows()
cap.release()
