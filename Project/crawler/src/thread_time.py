

import urllib.request
import requests
import os
import threading
import time


def downloadImg(img_url,save_path):
    global finish
    res=requests.get(img_url)
    with open(save_path ,'wb') as f:
        f.write(res.content)
    finish = 1



with open("photos.txt","r") as f:
    lines = f.readlines()
    print(len(lines),lines[0])
    

finish = 0

# img_url = "http://media1.modcloth.com/community_outfit_image/000/000/185/212/img_full_3668308b292c.jpg"
# save_path = "1.jpg"
# print(finish)
# t = threading.Thread(target=downloadImg,args =(img_url,save_path))
# t.start()
# t.join(0.5)
# print(finish)
# b




base_path = "./imgs/"
for i,line in enumerate(lines):

    if(i<25000):
        continue

    if(i%5000==0):

        print(i)

    save_dir_id = i//10000


    idx,img_url = line.strip().split(",")
    # print(idx)
    # print(img_url)

    img_name = img_url.split("/")[-1].split("?")[0]
    # print(img_name)


    save_dir = os.path.join(base_path,str(save_dir_id))
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    save_path = os.path.join(save_dir,img_name)
    # print(save_path)

    finish = 0
    t = threading.Thread(target=downloadImg,args =(img_url,save_path))
    t.start()
    t.join(10)

    if finish==0:
        #print("Fail: idx ",idx)
        with open("fail.txt","a") as f:
            f.write(line)
    else:
        pass

    
