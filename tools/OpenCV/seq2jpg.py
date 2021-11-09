# -*- coding:utf-8 -*-
import os.path
import fnmatch
import shutil


def open_save(file, savepath):
    # 读入一个seq文件，然后拆分成image存入savepath当中
    f = open(file, 'rb')
    # 将seq文件的内容转化成str类型
    string = f.read().decode('latin-1')

    # splitstring是图片的前缀，可以理解成seq是以splitstring为分隔的多个jpg合成的文件
    splitstring = "\xFF\xD8\xFF\xE0\x00\x10\x4A\x46\x49\x46"
    # split函数做一个测试,因此返回结果的第一个是在seq文件中是空，因此后面省略掉第一个
    """
    >>> a = ".12121.3223.4343"
    >>> a.split('.')
    ['', '12121', '3223', '4343']
    """
    strlist = string.split(splitstring)
    # print(strlist)
    # print('######################################')
    f.close()
    count = 0
    # delete the image folder path if it exists
    if os.path.exists(savepath):
        shutil.rmtree(savepath)
        # create the image folder path
    if not os.path.exists(savepath):
        os.makedirs(savepath)
    # 遍历每一个jpg文件内容，然后加上前缀合成图片
    for img in strlist:
        filename = str(count) + '.jpg'
        filenamewithpath = os.path.join(savepath, filename)
        if count > 0:
            i = open(filenamewithpath, 'wb+')
            i.write(splitstring.encode('latin-1'))
            i.write(img.encode('latin-1'))
            i.close()
        count = count + 1


if __name__ == "__main__":
    rootdir = "F:/data/image"
    saveroot = "F:/data/jpg"

    for parent, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
            if fnmatch.fnmatch(filename, '*.seq'):
                thefilename = os.path.join(parent, filename)
                thesavepath = saveroot + '/' + parent.split('/')[-1] + '/' + filename.split('.')[0] + '/'
                print("Filename=" + thefilename)
                print("Savepath=" + thesavepath)
                open_save(thefilename, thesavepath)
