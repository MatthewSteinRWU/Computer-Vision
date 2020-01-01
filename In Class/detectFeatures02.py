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

    offset = 1
    k=.04
    thresh=2000000
    height = image.shape[0]
    width = image.shape[1]



    Kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], np.float32)
    Ky = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]], np.float32)
    
    Ix = cv2.filter2D(image, -1, Kx)
    Iy = cv2.filter2D(image,-1, Ky)

    Ixx=np.multiply(Ix,Ix)
    Iyy=np.multiply(Iy,Iy)
    Ixy=np.multiply(Ix,Iy)
    #Find determinant and trace, use to get corner response
    for y in range(offset, height-offset):
        for x in range(offset, width-offset):
            #Calculate sum of squares
            windowIxx = Ixx[y-offset:y+offset+1, x-offset:x+offset+1]
            windowIxy = Ixy[y-offset:y+offset+1, x-offset:x+offset+1]
            windowIyy = Iyy[y-offset:y+offset+1, x-offset:x+offset+1]
            Sxx = windowIxx.sum()
            Sxy = windowIxy.sum()
            Syy = windowIyy.sum()
            det = (Sxx * Syy) - (Sxy**2)
            trace = Sxx + Syy
            r = det - k*(trace**2)
            
                #If corner response is over threshold, color the point and add to corner list
            if r > thresh:
                image[y,x]=(0,0,255)


    cv2.namedWindow('Highlights', cv2.WINDOW_NORMAL)
    cv2.imshow('Highlights',image)

    cv2.waitKey(0)

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
