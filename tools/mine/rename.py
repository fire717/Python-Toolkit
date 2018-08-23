#coding:utf-8
#python rename.py "xx路径"  
import os
import sys

def getAllName(file_dir): 
    L=[] 
    for root, dirs, files in os.walk(file_dir):
        # root 所指的是当前正在遍历的这个文件夹的本身的地址
        # dirs 是一个 list ，内容是该文件夹中所有的目录的名字(不包括子目录)
        # files 同样是 list , 内容是该文件夹中所有的文件(不包括子目录)
        for file in files:
            if os.path.splitext(file)[1] == '.jpg' or os.path.splitext(file)[1] == '.png':
                L.append(os.path.join(root, file))
    return L


def main():
    name_list = getAllName("negative")
    pass

if __name__ == '__main__':
    # path = sys.argv[1] #"./55.jpg"
    # start = int(sys.argv[2])
    path = "cc"
    start = 0
    if path[-1]!='/':
        path+='/'
    print("读取图片路径...")
    name_list = getAllName(path)
    dir_path = os.path.dirname(path)
    print(dir_path)
    for i,n in enumerate(name_list):
        img_name = os.path.basename(n)
        #print(img_name)
        os.rename(dir_path+'/'+img_name, dir_path+'/'+dir_path.split('/')[-1]+'_'+str(start)+'.'+img_name.split('.')[-1])
        start+=1
    #print("图片数量： ", len(name_list))
    #makeLabel(name_list,dir_name='')
    print("Finish.")
