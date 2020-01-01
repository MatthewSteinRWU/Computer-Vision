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
    
    cents = [(904,69),
             (1019,96),
            (726,332)]
    windowSize=7

    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    gray = np.float32(gray)

    cpy=image.copy()
    dst = cv2.cornerHarris(gray,2,3,0.04)
    for i in range(0,3):
        cv2.rectangle(dst,(cents[i][0]+windowSize,cents[i][1]+windowSize),
                  (cents[i][0]-windowSize,cents[i][1]-windowSize),255,1)

        cv2.rectangle(cpy,(cents[i][0]+windowSize,cents[i][1]+windowSize),
                  (cents[i][0]-windowSize,cents[i][1]-windowSize),(0,255,255),1)

    print dst.max()
    window1=dst[cents[1][1]-windowSize:cents[1][1]+windowSize,
    cents[1][0]-windowSize:cents[1][0]+windowSize]
    print window1.size
  
    cpy[dst>0.01*dst.max()]=[0,0,255]
    window1=cpy[cents[1][1]-windowSize:cents[1][1]+windowSize+1,
    cents[1][0]-windowSize:cents[1][0]+windowSize+1]    
    cv2.namedWindow('Harris', cv2.WINDOW_NORMAL)
    cv2.imshow('Harris',dst)
    cv2.namedWindow('Building', cv2.WINDOW_NORMAL)
    cv2.imshow('Building',cpy)
    cv2.namedWindow('Window', cv2.WINDOW_NORMAL)
    cv2.imshow('Window',window1)
    cv2.waitKey(0)
 

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
