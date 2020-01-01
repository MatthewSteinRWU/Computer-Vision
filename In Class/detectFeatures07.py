#!/usr/bin/env python

import sys
sys.path.append("/opt/ros/kinetic/lib/python2.7/dist-packages")
import cv2
import numpy as np
from drawMatches import drawMatches


filename1 = 'Building01.jpg'

filename2 = 'Building02.jpg'
MATCH_RATIO = 0.7

def main():
    image1 = cv2.imread(filename1)
    if image1 is None:
      print 'Unable to open file ', filename1
      return
    image2 = cv2.imread(filename2)
    if image2 is None:
      print 'Unable to open file ', filename2
      return

    detector = cv2.ORB_create(nfeatures=5000, scoreType=cv2.ORB_FAST_SCORE, edgeThreshold=4)

    kp1 = detector.detect(image1, None)
    
    kp1, des1 = detector.compute(image1, kp1)
          
    kp2 = detector.detect(image2, None)
    
    kp2, des2 = detector.compute(image2, kp2)
          
    index_params = dict(algorithm=6, table_number=6, key_size=12, multi_probe_level=1)
    search_params = dict(checks=50)
    matcher = cv2.FlannBasedMatcher(index_params, search_params)
                          
    matches = matcher.knnMatch(des1, des2, k=2)
    print len(matches)
    good = []
    for match in matches:
        if len(match) > 1 and match[0].distance < MATCH_RATIO * match[1].distance:
            good.append(match[0])

    # Need to draw only good matches, so create a mask
    # print 'compute_location'
    gray1 = cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)
    #out = drawMatches(gray1,kp1,gray2,kp2,(match[0] for match in matches))
    out = drawMatches(gray1,kp1,gray2,kp2,good) 

 
    cv2.namedWindow('Matches', cv2.WINDOW_NORMAL)
    cv2.imshow('Matches',out)
    cv2.waitKey(0)    
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
