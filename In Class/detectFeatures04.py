#!/usr/bin/env python

import sys
sys.path.append("/opt/ros/kinetic/lib/python2.7/dist-packages")
import cv2
import numpy as np


filename = 'Building02.jpg'
def main():
    image = cv2.imread(filename)
    if image is None:
      print 'Unable to open file ', filename
      return
    #print image.shape
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    gray = np.float32(gray)
    for i in range(3,23,2):
        for j in range(3,9,2):
            cpy=image.copy()
            dst = cv2.cornerHarris(gray,i,j,0.08)
            cpy[dst>0.01*dst.max()]=[0,0,255]
            cv2.namedWindow('Harris', cv2.WINDOW_NORMAL)
            cv2.imshow('Harris',cpy)
            cv2.waitKey(500)
            print i, j

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
