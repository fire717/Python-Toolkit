#include <opencv2/opencv.hpp>
#include <iostream>
#include <stdlib.h>
#include <math.h>

#include <time.h>


#define max(a,b) ((a) > (b) ? (a) : (b))
#define min(a,b) ((a) < (b) ? (a) : (b))


int getFeatures(const cv::Mat &img_gray, const cv::Rect &bbox, std::vector<cv::Point2f> &points);

int faceToPoints(const cv::Mat &img_gray, const std::vector<cv::Rect> &faces, std::vector<cv::Point2f> &total_points, std::vector<int> &points_count);

int estimatePointsDist(const cv::Mat &M,const std::vector<cv::Point2f> &points_part,const std::vector<cv::Point2f> &points_new_part,cv::Mat &src_mat,cv::Mat &dst_mat,std::vector<cv::Point2f> &src_inliers,std::vector<cv::Point2f> &dst_inliers);

int trackFaceByPoints(const cv::Size frame_gray_size, cv::Rect &face, std::vector<cv::Point2f> &points_part, std::vector<cv::Point2f> &points_new_part, int &point_count);

int faceTrack(const cv::Mat &frame_gray, const cv::Mat &frame_gray_old, std::vector<cv::Rect> &faces, std::vector<cv::Point2f> &total_points, std::vector<int> &points_count);

