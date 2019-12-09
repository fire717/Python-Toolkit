#coding:utf-8
from PIL import Image
import cv2
import numpy as np

def gray_jpg_resize(read_path, save_path, resize_w, resize_h):
    img = cv2.imread(read_path, 0)
    print(img.shape)
    img = cv2.resize(img,(resize_w,resize_h))
    cv2.imwrite(save_path, img)


def f8UC1_to_JPG(read_path, save_path, w, h):

    with open(read_path, "rb") as f:
        raw_data = f.read()
    print(len(raw_data))
    print(raw_data[:10])
    print(w*h)

    total_p = w*h
    rgb_bytes = bytearray(w*h)


    for i in range(total_p):
        rgb_bytes[i] = raw_data[i]

    img = Image.frombytes(data=bytes(rgb_bytes), decoder_name="raw", mode='L', size=(w,h))
    print("Image object created. Starting to save")
    img.save(save_path, "JPEG")


def f8UC3_package_to_JPG(read_path, save_path, w, h):

    with open(read_path, "rb") as f:
        raw_data = f.read()
    print(len(raw_data))
    print(raw_data[:10])
    print(w*h)

    total_p = w*h*3
    rgb_bytes = bytearray(w*h*3)


    for i in range(total_p):
        rgb_bytes[i] = raw_data[i]

    img = Image.frombytes(data=bytes(rgb_bytes), decoder_name="raw", mode='RGB', size=(w,h))

    #img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
    print("Image object created. Starting to save")
    #img.save(save_path, "JPEG")
    cv2.imwrite(save_path, np.array(img))


def f8UC3_planar_to_JPG(read_path, save_path, w, h):

    with open(read_path, "rb") as f:
        raw_data = f.read()
    print(len(raw_data))
    print(raw_data[:10])
    print(w*h)

    total_p = w*h*3
    rgb_bytes = bytearray(w*h*3)


    for i in range(total_p):
        rgb_bytes[i] = raw_data[i]

    b = Image.frombytes(data=bytes(rgb_bytes[:w*h]), decoder_name="raw", mode='L', size=(w,h))
    g = Image.frombytes(data=bytes(rgb_bytes[w*h:w*h*2]), decoder_name="raw", mode='L', size=(w,h))
    r = Image.frombytes(data=bytes(rgb_bytes[w*h*2:]), decoder_name="raw", mode='L', size=(w,h))

    img = cv2.merge([np.array(b),np.array(g),np.array(r)])
    print("Image object created. Starting to save")
    #img.save(save_path, "JPEG")
    cv2.imwrite(save_path, np.array(img))


def JPG_to_8UC1(read_path, save_path):

    img = Image.open(read_path)
    print(img.size)
    w, h = img.size
    img = np.array(img, dtype=np.uint8)
    # print(len(img[0]),img[0][0],hex(img[0][0]))


    with open(save_path, "wb") as f:
        f.write(img)


def f8UC1_3_to_JPG(read_path_B, read_path_G, read_path_R, save_path):
    b = cv2.imread(read_path_B, 0)
    g = cv2.imread(read_path_G, 0)
    r = cv2.imread(read_path_R, 0)

    img = cv2.merge([np.array(b),np.array(g),np.array(r)])
    print("Image object created. Starting to save")
    #img.save(save_path, "JPEG")
    cv2.imwrite(save_path, np.array(img))



def YUV420SP_to_JPG(read_path, save_path, width, height):

    def _readYuvFile(filename,width,height):
        fp=open(filename,'rb')
        uv_width=width//2
        uv_height=height//2

        Y=np.zeros((height,width),np.uint16,'C')
        U=np.zeros((uv_height,uv_width),np.uint16,'C')
        V=np.zeros((uv_height,uv_width),np.uint16,'C')

        for m in range(height):
            for n in range(width):
                Y[m,n]=ord(fp.read(1))
        for m in range(uv_height):
            for n in range(uv_width):
                V[m,n]=ord(fp.read(1))
                U[m,n]=ord(fp.read(1))

        fp.close()
        return (Y,U,V)

    def _yuv2rgb(Y,U,V,width,height):
        U=np.repeat(U,2,0)
        U=np.repeat(U,2,1)
        V=np.repeat(V,2,0)
        V=np.repeat(V,2,1)
        rf=np.zeros((height,width),float,'C')
        gf=np.zeros((height,width),float,'C')
        bf=np.zeros((height,width),float,'C')

        rf=Y+1.14*(V-128.0)
        gf=Y-0.395*(U-128.0)-0.581*(V-128.0)
        bf=Y+2.032*(U-128.0)

        # rf = Y + 1.402 * (V - 128)                 # r
        # gf = Y - 0.34413 * (U - 128) - 0.71414 * (V-128)  # g
        # bf = Y + 1.772 * (U-128) + 0                          # b


        for m in range(height):
            for n in range(width):
                if(rf[m,n]>255):
                    rf[m,n]=255
                if(gf[m,n]>255):
                    gf[m,n]=255
                if(bf[m,n]>255):
                    bf[m,n]=255
                if(rf[m,n]<0):
                    rf[m,n]=0
                if(gf[m,n]<0):
                    gf[m,n]=0
                if(bf[m,n]<0):
                    bf[m,n]=0

        r=rf.astype(np.uint8)
        g=gf.astype(np.uint8)
        b=bf.astype(np.uint8)
        return (r,g,b)

    data=_readYuvFile(read_path,width,height)
    Y=data[0]

    RGB=_yuv2rgb(data[0],data[1],data[2],width,height)
    im_r=Image.fromstring('L',(width,height),RGB[0].tostring())
    im_g=Image.fromstring('L',(width,height),RGB[1].tostring())
    im_b=Image.fromstring('L',(width,height),RGB[2].tostring())
    im_rgb=Image.merge('RGB',(im_r,im_g,im_b))
    im_rgb.save(save_path)



if __name__=="__main__":

    yuv_data_path = "save_gmm_yuv420sp_test333.yuv"
    save_path = "save_gmm_yuv420sp_test333.jpg"
    YUV420SP_to_JPG(yuv_data_path, save_path, 1920//1, 1080//1)

    # yuv_data_path = "save_gmm_yuv420sp_test444.yuv"
    # save_path = "resize_test444.jpg"
    # U8C3_planar_to_JPG(yuv_data_path, save_path, 720//1, 576//1)

    # yuv_data_path = "save_gmm_yuv420sp_test666.yuv"
    # save_path = "resize_test666.jpg"
    # U8C1_to_JPG(yuv_data_path, save_path, 720//1, 576//1)

    # read_path = "1080.jpg"
    # save_path = "1080.yuv"
    # JPG_to_U8C1(read_path, save_path)

    # yuv_data_path = "save_gmm_yuv420sp_test333.yuv"
    # save_path = "save_gmm_yuv420sp_test333.jpg"

    # f8UC1_to_JPG(yuv_data_path, save_path, 720//1, 576//1)


    # yuv_data_path = "save_gmm_yuv420sp_test444.yuv"
    # save_path = "save_gmm_yuv420sp_test444.jpg"
    # f8UC3_package_to_JPG(yuv_data_path, save_path, 1920//1, 1080//1);

    yuv_data_path = "save_gmm_yuv420sp_test444.yuv"
    save_path = "save_gmm_yuv420sp_test444.jpg"
    f8UC3_planar_to_JPG(yuv_data_path, save_path, 416//1, 416//1);


    # yuv_data_path = "save_gmm_yuv420sp_test444.yuv"
    # save_path = "resize_test444.jpg"
    # f8UC1_to_JPG(yuv_data_path, save_path, 416//1, 416//1)
    # yuv_data_path = "save_gmm_yuv420sp_test555.yuv"
    # save_path = "resize_test555.jpg"
    # f8UC1_to_JPG(yuv_data_path, save_path, 416//1, 416//1)
    # yuv_data_path = "save_gmm_yuv420sp_test666.yuv"
    # save_path = "resize_test666.jpg"
    # f8UC1_to_JPG(yuv_data_path, save_path, 416//1, 416//1)
    # jpg_path_b = "resize_test444.jpg"
    # jpg_path_g = "resize_test555.jpg"
    # jpg_path_r = "resize_test666.jpg"
    # save_path = "resize_test111.jpg"
    # f8UC1_3_to_JPG(jpg_path_b, jpg_path_g, jpg_path_r, save_path)
