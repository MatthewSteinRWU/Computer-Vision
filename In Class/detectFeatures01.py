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
    print image.shape

    cents = [(904,69),
             (1019,96),
            (726,332)]
    windowSize=7



    Kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], np.float32)
    Ky = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]], np.float32)
    
    Ix = cv2.filter2D(image, -1, Kx)
    for i in range(0,3):
        cv2.rectangle(Ix,(cents[i][0]+windowSize,cents[i][1]+windowSize),
                  (cents[i][0]-windowSize,cents[i][1]-windowSize),(0,0,255),1)

    Iy = cv2.filter2D(image,-1, Ky)
    for i in range(0,3):
        cv2.rectangle(Iy,(cents[i][0]+windowSize,cents[i][1]+windowSize),
                  (cents[i][0]-windowSize,cents[i][1]-windowSize),(0,0,255),1)
    for i in range(0,3):
        cv2.rectangle(image,(cents[i][0]+windowSize,cents[i][1]+windowSize),
                  (cents[i][0]-windowSize,cents[i][1]-windowSize),(0,0,255),1)
    cv2.namedWindow('Ix', cv2.WINDOW_NORMAL)
    #cv2.imshow('Ix',Ix[50:150,950:1050])
    cv2.imshow('Ix',Ix)
    cv2.namedWindow('Iy', cv2.WINDOW_NORMAL)
    #cv2.imshow('Iy',Iy[50:150,950:1050])
    cv2.imshow('Iy',Iy)
    cv2.namedWindow('Highlights', cv2.WINDOW_NORMAL)
    cv2.imshow('Highlights',image)   
    cv2.waitKey(0)

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
