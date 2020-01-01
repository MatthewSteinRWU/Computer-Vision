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

    fast = cv2.FastFeatureDetector_create()
    cpy=image.copy()
    # find and draw the keypoints
    kp = fast.detect(image,None)


    # Print all default params
    print("Threshold: ", fast.getThreshold());
    print("nonmaxSuppression: ", fast.getNonmaxSuppression());
    print("neighborhood: ", fast.getType());
    print("Total Keypoints with nonmaxSuppression: ", len(kp));

    
    cv2.drawKeypoints(image, kp, cpy, color=(255,0,255))

 
    cv2.namedWindow('Building', cv2.WINDOW_NORMAL)
    cv2.imshow('Building',cpy)
    cv2.waitKey(0)    
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
