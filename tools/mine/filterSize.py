#coding:utf-8
 
import os
import sys

def getAllName(file_dir): 
    L=[] 
    for root, dirs, files in os.walk(file_dir):
        # root 所指的是当前正在遍历的这个文件夹的本身的地址
        # dirs 是一个 list ，内容是该文件夹中所有的目录的名字(不包括子目录)
        # files 同样是 list , 内容是该文件夹中所有的文件(不包括子目录)
        for file in files:
            if os.path.splitext(file)[1] in ['.mp4',]:
                L.append(os.path.join(root, file))
    return L

def getFileSize(filePath):
    #filePath = unicode(filePath,'utf8')
    fsize = os.path.getsize(filePath)
    fsize = fsize/float(1024)  #kb
    return round(fsize,2)



if __name__ == '__main__':

    path = "fight/"
    print("读取路径...")
    name_list = getAllName(path)
    #dir_path = os.path.dirname(path)
    #print(dir_path)

    for i,n in enumerate(name_list):
        if getFileSize(n) < 1:
            print(n)
    print("Finish.")
