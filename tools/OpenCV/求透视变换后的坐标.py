import cv2
import numpy as np
import matplotlib.pylab as plt
 
a=cv2.imread('DJI_0966_4.jpg')
# a = cv2.resize(a, (640,360))




# pts = np.float32([ [349,196],[357,181],[361,204],[361,178] ])
 
# pts1 = np.float32([[349,186],[357,172],[361,195],[361,167]])
pts = np.float32([ [100,100],[100,980],[1820,980],[1820,100]])
 
pts1 = np.float32([[200,0],[0,880],[1720,1080],[1920,200]])
 
M = cv2.getPerspectiveTransform(pts,pts1)
 
dst = cv2.warpPerspective(a,M,(1920,1080))

# p = cv2.perspectiveTransform(np.array([[1920,1080]]),M)
# print(p)

pts = np.float32(np.array([[1820,980]])).reshape([-1, 2])  # 要映射的点
pts = np.hstack([pts, np.ones([len(pts), 1])]).T
target_point = np.dot(M, pts)
target_point = [[target_point[0][x],target_point[1][x]] for x in range(len(target_point[0]))]
print(target_point)

cv2.imwrite("tt.jpg",dst)
