#!/usr/bin/env python

import sys
sys.path.append("/opt/ros/kinetic/lib/python2.7/dist-packages")
import cv2
import numpy as np
import random
	


def main():
  rows=500
  cols=500
  for j in range(10):
    black=np.zeros([rows,cols], dtype=np.uint8)
    
    point1=(random.randrange(rows),random.randrange(cols))
    for slope in range(-10,10):

      b=slope*point1[1]
      point2=(0,b)

      cv2.line(black, point1,point2,255,3)

    cv2.namedWindow('Canvas', cv2.WINDOW_NORMAL)
    cv2.imshow('Canvas',black)
    cv2.waitKey(1000)
cv2.destroyAllWindows() 

if __name__ == '__main__':
    main()
