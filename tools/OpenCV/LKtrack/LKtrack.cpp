#include "LKtrack.h"


int getFeatures(const cv::Mat &img_gray, const cv::Rect &bbox, std::vector<cv::Point2f> &points) {
    //get face feature points
    int ret = 0;
    points.clear();

    cv::Mat bbox_mask = cv::Mat::zeros(img_gray.rows, img_gray.cols, CV_8UC1);
    bbox_mask(cv::Range(bbox.tl().y, bbox.tl().y + bbox.height), cv::Range(bbox.tl().x + (int)(bbox.width*0.1), bbox.tl().x + (int)(bbox.width*0.8))) = 255;

    static int max_corners = 40;
    static double quality_level = 0.15;
    static double min_distance = 3.0;
    static int block_size = 3;
    cv::goodFeaturesToTrack(img_gray,
                            points,
                            max_corners,
                            quality_level,
                            min_distance,
                            bbox_mask,
                            block_size);

    //std::cout << "points " << points.size() << std::endl;
    if (points.size() == 0) {
        ret = 1;
    }

    return ret;
}

int faceToPoints(const cv::Mat &img_gray,
                 const std::vector<cv::Rect> &faces,
                 std::vector<cv::Point2f> &total_points,
                 std::vector<int> &points_count) {
    //face box list to feature points
    int ret = 0;
    total_points.clear();
    points_count.clear();

    if (faces.size() > 0) {
        for (int i = 0; i < faces.size(); i++) {

            std::vector<cv::Point2f> points_tmp;
            cv::Rect bbox((int)faces[i].x, (int)faces[i].y, faces[i].width, faces[i].height);
            int ret = getFeatures(img_gray, bbox, points_tmp);

            if (ret == 0) {
                total_points.insert(total_points.end(), points_tmp.begin(), points_tmp.end());
                points_count.push_back(points_tmp.size());
            }
        }
    }
    return ret;
}


int estimatePointsDist(const cv::Mat &M,
                       const std::vector<cv::Point2f> &points_part,
                       const std::vector<cv::Point2f> &points_new_part,
                       cv::Mat &src_mat,
                       cv::Mat &dst_mat,
                       std::vector<cv::Point2f> &src_inliers,
                       std::vector<cv::Point2f> &dst_inliers) {
    // estimate the new bounding box with only the inliners
    //output: src_inliers, dst_inliers

    float dist_threshold = 0.9;

    cv::Mat src_mat_T;
    cv::transpose(src_mat, src_mat_T);
    cv::Mat src_points_pad = cv::Mat::ones(3, points_part.size(), CV_32F);
    src_mat_T.copyTo(src_points_pad(cv::Rect(0, 0, points_part.size(), 2)));
    cv::Mat projected = M * src_points_pad;
    cv::Mat projected_part_T;
    cv::transpose(projected(cv::Rect(0, 0, points_part.size(), 2)), projected_part_T);

    std::vector<float> points_dist;
    float* src_ptr = projected_part_T.ptr<float>(0);
    float* dst_ptr = dst_mat.ptr<float>(0);
    for (int i = 0; i < points_part.size(); i++) {
        float dist_tmp = pow(src_ptr[2 * i] - dst_ptr[2 * i], 2) + pow(src_ptr[2 * i + 1] - dst_ptr[2 * i + 1], 2);
        points_dist.push_back(dist_tmp);
    }

    for (int i = 0; i < points_dist.size(); i++) {
        if (points_dist[i] < dist_threshold) {
            src_inliers.push_back(points_part[i]);
            dst_inliers.push_back(points_new_part[i]);
        }
    }

    return 0;
}


int trackFaceByPoints(const cv::Size frame_gray_size,cv::Rect &face, std::vector<cv::Point2f> &points_part, std::vector<cv::Point2f> &points_new_part, int &point_count) {
    //feature points to face box
    int ret = 0;

    cv::Mat src_mat = cv::Mat(points_part.size(), 2, CV_32F, points_part.data());
    cv::Mat dst_mat = cv::Mat(points_new_part.size(), 2, CV_32F, points_new_part.data());

    cv::Mat Mpart = cv::estimateAffinePartial2D(src_mat, dst_mat);
    if (Mpart.cols == 3) {
        float M_mat[1][3] = { {0,0,1} };
        cv::Mat add_line(1, 3, CV_32FC1, M_mat);
        cv::Mat M = cv::Mat::zeros(3, 3, CV_32F);
        Mpart.copyTo(M(cv::Rect(0, 0, 3, 2)));
        add_line.copyTo(M(cv::Rect(0, 2, 3, 1)));


        std::vector<cv::Point2f> src_inliers, dst_inliers;
        ret = estimatePointsDist(M, points_part, points_new_part, src_mat, dst_mat, src_inliers, dst_inliers);

        if (src_inliers.size() > 3 && src_inliers.size() < points_part.size()) {
            //compute new M
            src_mat = cv::Mat(src_inliers.size(), 2, CV_32F, src_inliers.data());
            dst_mat = cv::Mat(dst_inliers.size(), 2, CV_32F, dst_inliers.data());
            Mpart = cv::estimateAffinePartial2D(src_mat, dst_mat);
            if (Mpart.cols == 3) {
                M = cv::Mat::zeros(3, 3, CV_32F);
                Mpart.copyTo(M(cv::Rect(0, 0, 3, 2)));
                add_line.copyTo(M(cv::Rect(0, 2, 3, 1)));
                //std::cout << "compute new M----------- " << std::endl;
            }
        }

        // compute new face box
        float face_mat[4][2] = { {(float)face.tl().x, (float)face.tl().y},
                                 {(float)face.br().x, (float)face.tl().y},
                                 {(float)face.tl().x, (float)face.br().y},
                                 {(float)face.br().x, (float)face.br().y} };

        cv::Mat face_src(4, 2, CV_32FC1, face_mat);
        cv::Mat face_res;

        cv::Mat face_src_T;
        cv::transpose(face_src, face_src_T);

        cv::Mat face_src_T_add = cv::Mat::ones(3, 4, CV_32F);

        face_src_T.copyTo(face_src_T_add(cv::Rect(0, 0, 4, 2)));

        cv::Mat mutl_res = M * face_src_T_add;
        cv::Mat mutl_res_part = mutl_res(cv::Rect(0, 0, 4, 2));

        cv::transpose(mutl_res_part, face_res);

        auto* data = face_res.ptr<float>(0);

        cv::Rect new_face((int)max(min(data[0], data[4]),0),
                          (int)max(min(data[1], data[3]),0),
                          (int)min(max(data[2], data[6]) - min(data[0], data[4]),frame_gray_size.width),
                          (int)min(max(data[5], data[7]) - min(data[1], data[3]),frame_gray_size.height));

        auto box_change_ratio = (float)(new_face.width*new_face.height)/(float)(face.width*face.height);
        if(box_change_ratio>1.5 || box_change_ratio<0.5){
            //box �仯̫��
            ret = 2;
        }

        face = new_face;
        point_count = point_count;
    }
    else {
        ret = 1;
    }

    return ret;
}



int faceTrack(const cv::Mat &frame_gray,
              const cv::Mat &frame_gray_old,
              std::vector<cv::Rect> &faces,
              std::vector<cv::Point2f> &total_points,
              std::vector<int> &points_count) {


    std::vector<cv::Rect> faces_new;
    std::vector<cv::Point2f> total_points_new;
    std::vector<int> points_count_new;


    if (total_points.size() > 0 && faces.size() > 0) {
        static std::vector<uchar> status;
        static std::vector<float> err;
        static cv::Size winSize(21, 21);
        static cv::TermCriteria termcrit(cv::TermCriteria::MAX_ITER | cv::TermCriteria::EPS, 30, 0.01);
        cv::calcOpticalFlowPyrLK(frame_gray_old, frame_gray,
                                 total_points, total_points_new, status, err,
                                 winSize,
                                 2,
                                 termcrit,
                                 0, 1e-4);


        int points_count_start = 0;
        for (int i = 0; i < points_count.size(); i++) {

            std::vector<cv::Point2f> points_part, points_new_part;
            int points_count_tmp = 0;
            //std::vector<cv::Point2f> good_points, good_points_new;

            //points_part.assign(total_points.begin() + points_count_start, total_points.begin() + points_count_start + points_count[i]);
            //points_new_part.assign(total_points_new.begin() + points_count_start, total_points_new.begin() + points_count_start + points_count[i]);


            //std::cout << "status " << status.size() << " " << (int)status[0] << std::endl;
            for (int j = 0; j < points_count[i]; j++) {
                if ((int)status[points_count_start + j] == 1) {
                    points_part.push_back(total_points[points_count_start + j]);
                    points_new_part.push_back(total_points_new[points_count_start + j]);
                    points_count_tmp += 1;
                }
            }

            if (points_count_tmp == 0) {
                continue;
            }

            points_count_start += points_count[i];

            cv::Rect face_new = faces[i];
            int point_count_new = points_count_tmp;

            int ret = trackFaceByPoints(frame_gray.size(), face_new, points_part, points_new_part, point_count_new);

            if (ret == 0) {
                faces_new.push_back(face_new);
                points_count_new.push_back(point_count_new);
            }

        }

    }


    faces.clear();
    total_points.clear();
    points_count.clear();

    if (faces_new.size() > 0) {
        faces.assign(faces_new.begin(), faces_new.end());
        total_points.assign(total_points_new.begin(), total_points_new.end());
        points_count.assign(points_count_new.begin(), points_count_new.end());
    }


    return 0;
}
