#module 'cv2.cv2' has no attribute 'xfeatures2d' 错误 https://zhuanlan.zhihu.com/p/150581915
import cv2


# def orb_detect(image_a, image_b):
#     # feature match
#     orb = cv2.ORB_create()
#     kp1, des1 = orb.detectAndCompute(image_a, None)
#     kp2, des2 = orb.detectAndCompute(image_b, None)
#     # create BFMatcher object
#     bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
#     # Match descriptors.
#     matches = bf.match(des1, des2)
#     # Sort them in the order of their distance.
#     matches = sorted(matches, key=lambda x: x.distance)
#     # Draw first 10 matches.
#     img3 = cv2.drawMatches(image_a, kp1, image_b, kp2,
#                            matches[:100], None, flags=2)
#     return bgr_rgb(img3)


def sift_detect(img1, img2, detector='sift'):
    if detector=='sift':
        print("Use sift detector.")
        sift = cv2.xfeatures2d.SIFT_create()
    else:
        print("Use surf detector.")
        sift = cv2.xfeatures2d.SURF_create()
        
    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)
    # BFMatcher with default params
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)
    # Apply ratio test
    good = [[m] for m, n in matches if m.distance < 0.5 * n.distance]
    # cv2.drawMatchesKnn expects list of lists as matches.
    img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags=2)
    return img3


if __name__ == "__main__":
    # load image
    image_a = cv2.imread('DJI_0966_4.jpg')
    image_b = cv2.imread('DJI_0966_88.jpg')

    img = sift_detect(image_a, image_b)
    cv2.imwrite("t.jpg", img)
