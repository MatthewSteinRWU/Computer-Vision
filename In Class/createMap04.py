#!/usr/bin/env python

import sys
sys.path.append("/opt/ros/kinetic/lib/python2.7/dist-packages")
import cv2
import numpy as np
import math
from drawMatches import drawMatches

# ---------- map parameters ----------- #

MAP_PIXEL_WIDTH = 1155  # in pixel

MAP_PIXEL_HEIGHT = 847

MAP_REAL_WIDTH = 1.1  # in meter

MAP_REAL_HEIGHT = .76

# ----- feature parameters DO NOT EDIT ----- #

MATCH_RATIO = 0.7
MIN_MATCH_COUNT = 10
MAP_FEATURES = 2000
# ---------- camera parameters ----------- #
CAMERA_WIDTH = 320
CAMERA_HEIGHT = 240

# assume a pixel in x and y has the same length
METER_TO_PIXEL = (float(MAP_PIXEL_WIDTH) / MAP_REAL_WIDTH + float(MAP_PIXEL_HEIGHT) / MAP_REAL_HEIGHT) / 2.
CAMERA_CENTER = np.float32([(CAMERA_WIDTH - 1) / 2., (CAMERA_HEIGHT - 1) / 2.]).reshape(-1, 1, 2)


filename1 = 'map.jpg'
filename2 = 'poster26.jpg'

def main():
    image1 = cv2.imread(filename1)
    if image1 is None:
      print 'Unable to open file ', filename1
      return
    image2 = cv2.imread(filename2)
    if image2 is None:
      print 'Unable to open file ', filename2
      return
    #create a single feature map presuming map is not too much bigger than viewport 

    # the edgeThreshold and patchSize can be tuned if the gap between cell is too large
    # MS Did just that, set edgeThreshold from 31 to 8 to get more features
    detector = cv2.ORB_create(nfeatures=MAP_FEATURES, scoreType=cv2.ORB_FAST_SCORE, edgeThreshold=8)

    kp1 = detector.detect(image1, None)
    
    kp1, des1 = detector.compute(image1, kp1)
          
    kp2 = detector.detect(image2, None)
    
    kp2, des2 = detector.compute(image2, kp2)                              

    gray1 = cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)
    
    index_params = dict(algorithm=6, table_number=6, key_size=12, multi_probe_level=1)
    search_params = dict(checks=50)
    matcher = cv2.FlannBasedMatcher(index_params, search_params)
                              
    matches = matcher.knnMatch(des1, des2, k=2)

    good=[]
    z=30  # Hard code z, distance from camera to floor
    for match in matches:
        if len(match) > 1 and match[0].distance < MATCH_RATIO * match[1].distance:
            good.append(match[0])

    print len(good)
    if len(good) > MIN_MATCH_COUNT:

        src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
        dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
        
        
        transform = cv2.estimateRigidTransform(dst_pts, src_pts, False)

        if transform is not None:
           
            pixel_center = cv2.transform(CAMERA_CENTER, transform)  # get global pixel
            transformed_center = cv2.transform(CAMERA_CENTER, transform)  # get global pixel
            transformed_center = [transformed_center[0][0][0] / METER_TO_PIXEL,  # map to global pose
                                  (MAP_PIXEL_HEIGHT - 1 - transformed_center[0][0][1]) / METER_TO_PIXEL]
            yaw = np.arctan2(transform[1, 0], transform[0, 0])  # get global heading

            # correct the pose if the drone is not level

            pose = [transformed_center[0], transformed_center[1] , z, yaw]
            print pose
            location = (int(pixel_center[0][0][0]),int(pixel_center[0][0][1]))

            cv2.circle(gray1,location,30,255,3)
        else:
            print 'Unable to compute transform from matches'

    out = drawMatches(gray1,kp1,gray2,kp2,good)
                              
    cv2.namedWindow('Map comparison', cv2.WINDOW_NORMAL)
    cv2.imshow('Map comparison',out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
