#include <opencv2/opencv.hpp>
#include <iostream>
#include <stdlib.h>

#include <time.h>
#include <windows.h> 

#include "LKtrack.h"



int main()
{	

	cv::VideoCapture capture;
	cv::Mat frame, frame_gray, frame_gray_old;
	frame = capture.open("C:/Users/Fire/Desktop/face_track/test4.mp4");
	if (!capture.isOpened())
	{
		printf("can not open ...\n");
		return -1;
	}
	cv::namedWindow("output", cv::WINDOW_AUTOSIZE);

	cv::CascadeClassifier detector;
	detector.load("haarcascade_frontalface_default.xml");


	std::vector<cv::Point2f> total_points,  points_good, points_good_new;
	std::vector<int> points_count;
	std::vector<cv::Rect> faces;
	int frame_id = 0;

	while (frame_id<1000)
	{
		auto read_ret = capture.read(frame);
		if (!read_ret) {
			break;
		}
		double start = GetTickCount();
		cv::resize(frame, frame, cv::Size(frame.cols / 2, frame.rows / 2), 0, 0, cv::INTER_LINEAR);
		cvtColor(frame, frame_gray, cv::COLOR_BGR2GRAY);

		if (frame_id%5==0) {
			// detect face
			detector.detectMultiScale(frame_gray, faces, 1.3, 5);
			

			int ret = faceToPoints(frame_gray, faces, total_points, points_count);
		}
		else {
			// track
			faceTrack(frame_gray, frame_gray_old, faces, total_points, points_count);
			
		}
		



		//time
		double  end = GetTickCount();
		printf("time: %.4f\n", (end - start) / 1000.0);


		// draw box
		if(faces.size() > 0){
			for (int i = 0; i < faces.size();i++) {
				cv::rectangle(frame, faces[i], cv::Scalar(255, 0, 0), 2);
			}	
		}
		if (total_points.size() > 0) {
			for (int i = 0; i < total_points.size(); i++)
			{
				cv::circle(frame, total_points[i], 1, cv::Scalar(0, 0, 255), 2, 8, 0);
			}
		}

		imshow("output", frame);
		if ((char)cv::waitKey(10)  == 27) {
			break;
		}
		frame_id += 1;

		frame_gray_old = frame_gray.clone();
			
	}
	capture.release();
	return 0;
}
