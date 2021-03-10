void method(Mat &image) {

    int w = image.cols;
    int h = image.rows;
    for (int row = 0; row < h; row++) {
        uchar* uc_pixel = image.data + row*image.step;
        for (int col = 0; col < w; col++) {
            uc_pixel[0] = 255 - uc_pixel[0];
            uc_pixel[1] = 255 - uc_pixel[1];
            uc_pixel[2] = 255 - uc_pixel[2];
            uc_pixel += 3; //RGBA则+4
       
       }
    }

}
