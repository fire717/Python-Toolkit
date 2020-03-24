import os
import numpy as np
import os,shutil
import random
import cv2
import time
import math



def RGB2HSV(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    m = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        if g >= b:
            h = ((g-b)/m)*60
        else:
            h = ((g-b)/m)*60 + 360
    elif mx == g:
        h = ((b-r)/m)*60 + 120
    elif mx == b:
        h = ((r-g)/m)*60 + 240
    if mx == 0:
        s = 0
    else:
        s = m/mx
    v = mx
    return h, s, v

def HSV2RGB(h,s,v):
    assert 0<=h<360
    assert 0<=s<=1
    assert 0<=v<=1
    c = v*s
    x = c*(1-abs((h/60)%2-1))
    m = v-c
    if h<60:
        r,g,b = c,x,0
    elif h<120:
        r,g,b = x,c,0
    elif h<180:
        r,g,b = 0,c,x
    elif h<240:
        r,g,b = 0,x,c
    elif h<300:
        r,g,b = x,0,c
    elif h<360:
        r,g,b = c,0,x

    r,g,b = (r+m)*255, (g+m)*255, (b+m)*255
    return r, g, b


def computeLABColorDistance(rgb1, rgb2):
    R_1,G_1,B_1 = rgb1
    R_2,G_2,B_2 = rgb2
    rmean = (R_1 +R_2 ) / 2
    R = R_1 - R_2
    G = G_1 -G_2
    B = B_1 - B_2
    dist =  np.sqrt((2+rmean/256)*(R**2)+4*(G**2)+(2+(255-rmean)/256)*(B**2))
    return dist

class ColorSimilarity(object):
    def __init__(self, palette_img_path):
        #http://sergeykarayev.com/rayleigh/doc/images/palette_14_3.png
        self.palette_img = cv2.imread(palette_img_path)
        self.palette_color = []

        self.initPalette()

    def initPalette(self):
        palette_img_RGB = cv2.cvtColor(self.palette_img, cv2.COLOR_BGR2RGB)
        for i in range(15):
            for j in range(9):
                color_bgr = self.palette_img[25+50*j][25+50*i]
                #print(i*6+j,color_bgr)
                self.palette_color.append(color_bgr)

    def computeLABColorDistance(self, rgb1, rgb2):
        R_1,G_1,B_1 = rgb1
        R_2,G_2,B_2 = rgb2
        rmean = (R_1 +R_2 ) / 2
        R = R_1 - R_2
        G = G_1 -G_2
        B = B_1 - B_2
        dist =  np.sqrt((2+rmean/256)*(R**2)+4*(G**2)+(2+(255-rmean)/256)*(B**2))
        return dist


    def nearestColor(self, color_rgb):
        #color_rgb = [r,g,b]
        H_1,S_1,V_1 = RGB2HSV(*color_rgb)
        print("hsv: ",H_1,S_1,V_1)
        if V_1<0.15:
            min_dist = 1.0
            min_dist_cate = 134

        else:
            dist_list = []

            for j,rgb2 in enumerate(self.palette_color):
                dist = self.computeLABColorDistance(rgb1, rgb2)
                dist_list.append([dist, j])

            dist_list = sorted(dist_list, key=lambda x:x[0])

        #print(min_dist, min_dist_cate)

        mid_dist = dist_list[0][0]
        min_cate = dist_list[0][1]

        if min_cate in range(127,134) and dist_list[1][1] not in range(127,134):
            mid_dist = dist_list[1][0]
            min_cate = dist_list[1][1]
        print(min_cate)
        return mid_dist, self.palette_color[min_cate]


    def sortedNearestColor(self, color_rgb):
        #color_rgb = [r,g,b]
        H_1,S_1,V_1 = RGB2HSV(*color_rgb)
        print("hsv: ",H_1,S_1,V_1)
        if V_1<0.15:
            min_dist = 1.0
            min_dist_cate = 134

        else:
            dist_list = []

            for j,rgb2 in enumerate(self.palette_color):
                dist = self.computeLABColorDistance(rgb1, rgb2)
                dist_list.append([dist, self.palette_color[j]])

            dist_list = sorted(dist_list, key=lambda x:x[0])


        return dist_list


"""
需求颜色(RGB)：
0白色： 255,255,255
1黑色： 0,0,0
2红色： 255,0,0
3绿色： 0,255,0
4蓝色： 0,0,255
5灰色： 125,125,125
6粉色： 255,192,203 
7紫色： 128,0,128
8黄色： 255,255,0
9棕色： 165,42,42
10咖色： 96,57,18
11驼色： 180,133,83
-1:其他
"""
label_color_ = [[[255,255,255],"白色"], 
                    [[0,0,0],"黑色"], 
                    [[255,0,0],"红色"], 
                    [[0,255,0],"绿色"], 
                    [[0,0,255],"蓝色"], 
                    [[125,125,125],"灰色"], 
                    [[255,192,203],"粉色"], 
                    [[128,0,128],"紫色"], 
                    [[255,255,0],"黄色"], 
                    [[165,42,42],"棕色"], 
                    [[96,57,18],"咖色"], 
                    [[180,133,83],"驼色"]]




if '__main__' == __name__:

    
    # random test
    rgb1 = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
    #rgb1 = [213,162,163]
    print("Color: ",rgb1)

    color_img = np.ones((100,200,3))*[rgb1[2],rgb1[1],rgb1[0]]
    cv2.imwrite("color_img.jpg",color_img)


    color_similarity = ColorSimilarity("palette_14_3.png")
    min_dist, min_cate = color_similarity.nearestColor(rgb1)

    print(min_dist,min_cate)
    color_img = np.ones((100,200,3))*[min_cate[2],min_cate[1],min_cate[0]]
    cv2.imwrite("color_img_label1.jpg",color_img)

    # color_img = np.ones((100,200,3))*[dist_list[1][1][2],dist_list[1][1][1],dist_list[1][1][0]]
    # cv2.imwrite("color_img_label2.jpg",color_img)

    # color_img = np.ones((100,200,3))*[dist_list[2][1][2],dist_list[2][1][1],dist_list[2][1][0]]
    # cv2.imwrite("color_img_label3.jpg",color_img)

    
    # avg_color = np.mean([dist_list[0][1],dist_list[1][1],dist_list[2][1]],axis=0)
    # print(avg_color)
    # color_img = np.ones((100,200,3))*[avg_color[2],avg_color[1],avg_color[0]]
    # cv2.imwrite("color_img_label_mean.jpg",color_img)

    # print(computeLABColorDistance(dist_list[0][1], avg_color))
    # print(computeLABColorDistance(dist_list[1][1], avg_color))
    # print(computeLABColorDistance(dist_list[2][1], avg_color))
    """
    wrong:
    162, 139, 174 done
    38, 63, 49  done
    67, 15, 66  done
    52, 104, 100    cate=17 不算在标签颜色

    """


    # with open("color_map.txt","w") as f:
    #     for i in range(135):
    #         f.write(str(i)+","+"-1\n")






    
