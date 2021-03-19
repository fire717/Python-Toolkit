//https://www.jianshu.com/p/fc2f247fc2c4
//这两种差不多，最快，且method5不需要连续存储



void method5(cv::Mat img){
    int height = img.rows;
    int width = img.cols;
    for(int row=0; row < height; row++){
        const uchar *ptr = img.ptr(row);
        for(int col=0; col < width; col++){
            int a = ptr[0];
            int b = ptr[1];
            int c = ptr[2];
            ptr += 3; 
        }
    }
}

void method6(cv::Mat img){
    int height = img.rows;
    int width = img.cols;
    const uchar *uc_pixel = img.data;
    for(int row=0; row < height; row++){
        uc_pixel = img.data + row*img.step;
        for(int col=0; col < width; col++){
            int a = uc_pixel[0];
            int b = uc_pixel[1];
            int c = uc_pixel[2];
            uc_pixel += 3;
        }
    }
}
