#coding:utf-8
#transfer jpeg、png、JPG、PNG to jpg
import os
import cv2
import glob



img_dir = "yoga_img"


files = glob.glob(os.path.join(img_dir,"*"))
print(len(files))


for filename in files:
    basename = os.path.basename(filename)

    if filename.endswith("jpg"):
        continue
    elif filename.endswith("jpeg"):
        os.rename(filename, filename.replace(".jpeg",".jpg"))
    elif filename.endswith("png"):
        img = cv2.imread(filename)
        cv2.imwrite(filename.replace(".png",".jpg"),img)
        os.remove(filename)

    elif filename.endswith("JPG"):
        os.rename(filename, filename.replace(".JPG",".jpg"))
    elif filename.endswith("PNG"):
        img = cv2.imread(filename)
        cv2.imwrite(filename.replace(".PNG",".jpg"),img)
        os.remove(filename)
    else:
        print("Unknown filename: " + filename)



print("Finish.")
