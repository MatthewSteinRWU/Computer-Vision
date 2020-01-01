#!/usr/bin/env python

import sys
sys.path.append("/opt/ros/kinetic/lib/python2.7/dist-packages")
import cv2
import numpy as np

# ---------- map parameters ----------- #
MAP_PIXEL_WIDTH = 1155  # in pixel
MAP_PIXEL_HEIGHT = 847
MAP_REAL_WIDTH = 1.1  # in meter
MAP_REAL_HEIGHT = .76

# ----- feature parameters DO NOT EDIT ----- #
MATCH_RATIO = 0.7
MAP_FEATURES = 6000

filename = 'map.jpg'
def main():
    image = cv2.imread(filename)
    if image is None:
      print 'Unable to open file ', filename
      return

    """
    create a single feature map presuming map is not much bigger than viewport 
    :param file_name: the image of map
    """
    # the edgeThreshold and patchSize can be tuned if the gap between cell is too large
    # MS Did just that, set edgeThreshold from 31 to 8 to get more features
    detector = cv2.ORB_create(nfeatures=MAP_FEATURES, scoreType=cv2.ORB_FAST_SCORE, edgeThreshold=8)

    kp = detector.detect(image, None)
    
    kp, des = detector.compute(image, kp)
          
    # kp is a list of keypoints, des are the associated descriptors for each
    img_keypoints = np.empty((image.shape[0], image.shape[1], 3), dtype=np.uint8)
    # print len(kp)
    cv2.drawKeypoints(image, kp, img_keypoints, color=(0,255,255))
    cv2.namedWindow('Static map', cv2.WINDOW_NORMAL)
    cv2.imshow('Static map',img_keypoints)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
