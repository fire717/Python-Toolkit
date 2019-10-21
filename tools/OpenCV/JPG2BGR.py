import cv2

imgpath = "t2.jpg"
saveimg = r"manyfaces_320240.bgr"

img = cv2.imread(imgpath)
save_img_size_w = 320  #要转换后的图片的尺寸
save_img_size_h = 240
if img is None:
    print("img is none")
else:
    img = cv2.resize(img,(save_img_size_w,save_img_size_h))
    #cv2.imwrite('1.jpg',img)
    (B, G, R) = cv2.split(img)
    with open(saveimg,'wb')as fp:
        for i in range(save_img_size_h):
            for j in range(save_img_size_w):
                fp.write(B[i, j])
        for i in range(save_img_size_h):
            for j in range(save_img_size_w):
                fp.write(G[i, j])
        for i in range(save_img_size_h):
            for j in range(save_img_size_w):
                fp.write(R[i, j])

    print("save success")
