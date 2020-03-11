import numpy as np
import cv2
import time

from math import isnan

from skimage import transform as tf


#多目标

c = 0

def applyGeometricTransformation(p_count,startXs, startYs, newXs, newYs, bbox):
    #print("----------0000  ",startXs,p_count,bbox)
    n_object = len(p_count)#bbox.shape[0]
    newbbox = np.zeros((n_object,bbox.shape[1],bbox.shape[2]),dtype=np.int32)#np.zeros_like(bbox)
    Xs = []
    Ys = []
    new_p_count = []

    for obj_idx in range(n_object):
        if p_count[obj_idx]==0:
            continue
        startXs_obj = startXs[:p_count[obj_idx]]
        startYs_obj = startYs[:p_count[obj_idx]]
        newXs_obj = newXs[:p_count[obj_idx]]
        newYs_obj = newYs[:p_count[obj_idx]]

        Xs_tmp = newXs[:p_count[obj_idx]].copy()
        Ys_tmp = newYs[:p_count[obj_idx]].copy()


        startXs = startXs[p_count[obj_idx]:]
        startYs = startYs[p_count[obj_idx]:]
        newXs = newXs[p_count[obj_idx]:]
        newYs = newYs[p_count[obj_idx]:]


        desired_points = np.hstack((startXs_obj,startYs_obj))
        actual_points = np.hstack((newXs_obj,newYs_obj))
        global frame_id
        retval, inliers = cv2.estimateAffinePartial2D(desired_points, actual_points)
        
        
        #print("1Mpart " ,retval)
        if retval is not None:
            print("333: ",retval,inliers)
            mat = np.vstack((retval,np.array([0,0,1])))
            # coords = np.vstack((bbox[obj_idx,:,:].T,np.array([1,1,1,1])))
            # new_coords = mat.dot(coords)
            # newbbox[obj_idx,:,:] = new_coords[0:2,:].T


            # estimate the new bounding box with only the inliners (Added by Yongyi Wang)
            THRES = 1

            projected = mat.dot(np.vstack((desired_points.T.astype(float),np.ones([1,np.shape(desired_points)[0]]))))
            distance = np.square(projected[0:2,:].T - actual_points).sum(axis = 1)
            
            print(projected[0:2,:].T)
            print(actual_points)
            print(projected[0:2,:].T - actual_points)
            print(np.square(projected[0:2,:].T - actual_points))
            print(np.square(projected[0:2,:].T - actual_points).sum(axis = 1))
            b
            # print(desired_points.shape) # 20,2
            # print(desired_points.T.shape) #2,20
            # print(np.ones([1,np.shape(desired_points)[0]]).shape)  #1,20
            # print(projected) #3,20
            # print(projected[0:2,:].T)  #20,2
            # print(projected[0:2,:].T - actual_points)  # (20,)
            # print(np.square(projected[0:2,:].T - actual_points))
            #b

            print("1111 ",len(actual_points))
            actual_inliers = actual_points[distance < THRES]
            desired_inliers = desired_points[distance < THRES]
            print("2222 ",len(actual_inliers))
            if np.shape(desired_inliers)[0]<4:
                print('too few points')
                actual_inliers = actual_points
                desired_inliers = desired_points

            retval, inliers = cv2.estimateAffinePartial2D(desired_inliers, actual_inliers)
            mat = np.vstack((retval,np.array([0,0,1])))
            coords = np.vstack((bbox[obj_idx,:,:].T,np.array([1,1,1,1])))
            new_coords = mat.dot(coords)
            newbbox[obj_idx,:,:] = new_coords[0:2,:].T
            print("distance:", distance)
            Xs_tmp[distance >= THRES, 0] = -1
            Ys_tmp[distance >= THRES, 0] = -1

            #print("------------------------")

        Xs.append(Xs_tmp)
        Ys.append(Ys_tmp)
        new_p_count.append(len(Xs_tmp))

    Xs = np.concatenate(Xs,axis = 0)
    Ys = np.concatenate(Ys,axis = 0)

    
    #print(Xs)
    #print("===1===")
    return Xs, Ys, newbbox, new_p_count








cap = cv2.VideoCapture("t1.mp4")#cv2.VideoCapture(0)
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


# ShiTomasi 角点检测参数
feature_params = dict( maxCorners = 80,
                       qualityLevel = 0.1, #0.01
                       minDistance = 7,  #10
                       blockSize = 7,
                       )  #3

# lucas kanade光流法参数
lk_params = dict( winSize  = (12,12),
                  maxLevel = 2,
                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))




faces = []
frame_id = 0
p0 = []

while(frame_id<5000):
    t1 = time.time()


    ret,frame = cap.read()

    if frame is None:
        break

    size = (int(480), int(270))  
    frame = cv2.resize(frame,size, interpolation=cv2.INTER_AREA)
    #print(frame.shape)  #"test.mp4" (720, 1280, 3)
    #b
    if frame is None:
        break
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    
    if frame_id%5==0:
        #t = time.time()
        faces = detector.detectMultiScale(frame_gray, 1.3, 5)
        #print(faces)#[[615 109 115 115]]
        #print("time1: ", time.time()- t)

        if len(faces)>0:
            p_count = []
            p0 = []
            for (x, y, w, h) in faces:

                face_mask = np.zeros(shape = frame.shape[:2], dtype=np.uint8)
                face_mask[y:y+h,x+int(w*0.18):x+int(w*0.64)] = 255
                #获取图像中的角点，返回到p0中
                p0_tmp = cv2.goodFeaturesToTrack(frame_gray, mask = face_mask, **feature_params)
                #print("p0_tmp:    ",p0_tmp)
                if p0_tmp is not None:
                    p0.append(p0_tmp)
                    p_count.append(len(p0_tmp))
                else:
                    p_count.append(0)
            #print(p0)
            if len(p0)>0:
                p0 = np.concatenate(p0,axis=0)
                #p0 = np.array(p0)
            #print("p0.shape ",p0.shape)
            #print("-----------------")
            #b
    else:
        if len(p0)>0 and len(faces)>0:
            # track
            # 计算光流
            #t = time.time()
            p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
            #status ：输出状态向量（无符号字符）;如果找到相应特征的流，则向量的每个元素设置为1，否则设置为0。
            #print("st: ", st)
            # 选取好的跟踪点
            good_new = p1[st==1]
            good_old = p0[st==1]

            good_new = np.reshape(good_new, (-1,1,2))
            good_old = np.reshape(good_old, (-1,1,2))

            #faces = trackPointToBox(p0)
            total_bbox =[]
            for (x, y, w, h) in faces:
                bbox1 = np.array([[x,y],[x+w,y],[x,y+h],[x+w,y+h]], dtype=np.float32) 
                total_bbox.append(bbox1)
            total_bbox = np.array(total_bbox)

            print("p0 ",p0.shape,good_old.shape)
            startXs = good_old[:,:,0]
            startYs = good_old[:,:,1]
            newXs = good_new[:,:,0]
            newYs = good_new[:,:,1]

            Xs, Ys ,bbox2, p_count = applyGeometricTransformation(p_count,startXs, startYs, newXs, newYs, total_bbox)


            new_faces = []


            for box_id in range(len(bbox2)):
                xmin = min(bbox2[box_id][0][0],bbox2[box_id][2][0])
                xmax = max(bbox2[box_id][1][0],bbox2[box_id][3][0])
                ymin = min(bbox2[box_id][0][1],bbox2[box_id][2][1])
                ymax = max(bbox2[box_id][1][1],bbox2[box_id][3][1])

                if not isnan(xmin):
                #print(xmin,ymin,xmax,ymax)
                #new_faces = np.array([[xmin,ymin,xmax-xmin,ymax-ymin]],dtype = np.int32)
                    new_faces.append([xmin,ymin,xmax-xmin,ymax-ymin])
                #print(new_faces)

                # 更新上一帧的图像和追踪点 

            faces =  np.array(new_faces)
            p0 = good_new.reshape(-1,1,2)




    ####### 画人脸框
   # print(faces)
    if len(faces)>0:
        for (x, y, w, h) in faces:
            #print(x, y, w, h)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    if len(p0)>0:
        drawX = p0[:,:,0]
        drawY = p0[:,:,1]
        for draw_p_i in range(len(drawX)):
            cv2.circle(frame, (drawX[draw_p_i], drawY[draw_p_i]), 1, (255, 0, 0), 2)

    cv2.imshow('frame',frame)

    if cv2.waitKey(10) & 0xFF == 27:#ord('q'):
        break

    frame_id+=1
    old_gray = frame_gray.copy()

    print("time total frame: ", time.time()- t1)

    

cv2.destroyAllWindows()
cap.release()
