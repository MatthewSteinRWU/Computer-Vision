#!/usr/bin/env python

import sys
sys.path.append("/opt/ros/kinetic/lib/python2.7/dist-packages")
import cv2
import numpy as np


filename = 'Building01.jpg'
def main():
    image = cv2.imread(filename)
    if image is None:
      print 'Unable to open file ', filename
      return
    #print image.shape

    detector = cv2.ORB_create(nfeatures=1000, scoreType=cv2.ORB_FAST_SCORE, edgeThreshold=8)

    kp = detector.detect(image, None)
    
    kp, des = detector.compute(image, kp)
          
    # kp is a list of keypoints, des are the associated descriptors for each
    img_keypoints = np.empty((image.shape[0], image.shape[1], 3), dtype=np.uint8)
    # print len(kp)
    cv2.drawKeypoints(image, kp, img_keypoints, color=(255,0,255))
 
    cv2.namedWindow('Building', cv2.WINDOW_NORMAL)
    cv2.imshow('Building',img_keypoints)
    cv2.waitKey(0)    
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
