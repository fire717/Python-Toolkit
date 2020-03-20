#图片颜色聚类，200*200的输入，sklearn400ms左右，opencv50ms左右

import os

import numpy as np
import os,shutil
import random

import cv2
from sklearn.cluster import KMeans
from sklearn.externals import joblib

import time


random.seed = 0


def getKmeansColor(img, n_cluster):

    h,w,c = img.shape
    img = img[int(h*0.2):int(h*0.8), int(w*0.2):int(w*0.8)]
    h,w,c = img.shape

    img = cv2.resize(img,(200,200))

    cv2.imwrite("data.jpg",img)

    data = np.reshape(img, (-1,3))

    #调用kmeans类
    clf = KMeans(n_clusters=n_cluster)
    s = clf.fit(data)

    #中心
    print(clf.cluster_centers_)

    #每个样本所属的簇
    #print(clf.labels_)
    from collections import Counter
    color_count_dict = Counter(clf.labels_)
    color_count_ratio = []
    for i in range(n_cluster):
        color_count_ratio.append(color_count_dict[i]*1.0/len(data))
    print(color_count_ratio)


    #用来评估簇的个数是否合适，距离越小说明簇分的越好，选取临界点的簇个数
    #print(clf.inertia_)

    #进行预测
    #print(clf.predict(feature))



    #保存模型
    #joblib.dump(clf , 'km.pkl')

    #载入保存的模型
    #clf = joblib.load('c:/km.pkl')

    '''
    #用来评估簇的个数是否合适，距离越小说明簇分的越好，选取临界点的簇个数
    for i in range(5,30,1):
        clf = KMeans(n_clusters=i)
        s = clf.fit(feature)
        print i , clf.inertia_
    '''

    return clf.cluster_centers_, color_count_ratio



def kmeansColorOpenCV(img, n_cluster):

    # save pre work
    h,w,c = img.shape
    img = img[int(h*0.2):int(h*0.8), int(w*0.2):int(w*0.8)]
    h,w,c = img.shape
    img = cv2.resize(img,(200,200))
    cv2.imwrite("data.jpg",img)
    data = img.reshape((-1,3))

    # convert to np.float32
    data = np.float32(data)

    # define criteria, number of clusters(K) and apply kmeans()
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    ret,labels,centers=cv2.kmeans(data,n_cluster,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
    # ret
    # labels：标志数组。
    # centers：有聚类中心组成的数组。
    print(ret)

    # print(label)
    # print(label.shape)
    # print(centers)
    # print(centers.shape)


    #每个样本所属的簇
    #print(clf.labels_)
    from collections import Counter
    labels = list(np.reshape(labels,(1,-1))[0])

    color_count_dict = Counter(labels)
    color_count_ratio = []
    for i in range(n_cluster):
        color_count_ratio.append(color_count_dict[i]*1.0/len(data))
    print(color_count_ratio)


    return centers, color_count_ratio



if '__main__' == __name__:
    n_cluster = 5
    img = cv2.imread("1.jpg")

    t = time.time()
    cluster_centers, color_count_ratio = kmeansColorOpenCV(img, n_cluster)
    print("time: ", time.time() - t)

    # 可视化结果
    res_img_h = n_cluster*2*10*2
    res_img_w = 100
    res = np.ones((res_img_h,res_img_w,3))*255
    y_start = 0
    for i in range(n_cluster):
        color_h = int(res_img_h*color_count_ratio[i])
        cv2.rectangle(res, (0, y_start), (100, y_start+color_h), [int(x) for x in cluster_centers[i]], -1) 
        y_start += color_h

    cv2.rectangle(res, (0, 0), (res_img_w-1, res_img_h-1), (0,0,0),2) 

    cv2.imwrite("res.jpg", res)


    #cate = classify(cluster_centers, color_count_ratio)
    #print("cate: ",cate)
