def gray2rgb(imggray):
   # 原图 R G 通道不变，B 转换回彩图格式
   # 像素值为0-255
   imggray = np.reshape(imggray, (imggray.shape[:2]))
   R = imggray#/ 0.114
   G = imggray#/ 0.587
   B = imggray#/ 0.299
 
   grayRgb = np.zeros((imggray.shape[0],imggray.shape[1],3))
   grayRgb[:, :, 2] = B
   grayRgb[:, :, 0] = R
   grayRgb[:, :, 1] = G
 
   return grayRgb
