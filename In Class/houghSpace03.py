#!/usr/bin/env python

import sys
sys.path.append("/opt/ros/kinetic/lib/python2.7/dist-packages")
import cv2
import numpy as np
import random
	


def main():
  rows=500
  cols=500
  diag_len = int(np.ceil(np.sqrt(cols**2 + rows**2)))

  black=np.zeros([rows,cols], dtype=np.uint8)
  hs=np.zeros([2*diag_len, 5*190], dtype=np.uint8)

  (x,y)=(random.randrange(rows),random.randrange(cols))
  thetas = np.deg2rad(np.arange(-90.0, 90.0,1)) 
  for theta in thetas:   
    rho = int(round(x * np.cos(theta) + y * np.sin(theta)) + diag_len)
    
    cv2.line(black, (x,y),(int(rho*np.sin(theta)),int(rho*np.cos(theta))),255,3)
   
    cv2.circle(hs,(5*int(np.rad2deg(theta)+90),int(rho)),2,255,2)
    print (int(np.rad2deg(theta)+90),int(rho))
    cv2.namedWindow('Canvas', cv2.WINDOW_NORMAL)
    cv2.imshow('Canvas',black)
    cv2.namedWindow('Hough Space', cv2.WINDOW_NORMAL)
    cv2.imshow('Hough Space',hs)
    cv2.waitKey(100)

  cv2.waitKey(0)   
  cv2.destroyAllWindows() 

if __name__ == '__main__':
    main()
