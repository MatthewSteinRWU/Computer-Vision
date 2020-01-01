#!/usr/bin/env python
import sys
sys.path.append("/opt/ros/kinetic/lib/python2.7/dist-packages")

import cv2
import numpy as np


filename = 'Hall01.jpg'
def main():
    image = cv2.imread(filename)
    if image is None:
        print 'Unable to open file ', filename
        return
    
    orig = image.copy()
    rows=image.shape[0]
    cols=image.shape[1]
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,150,250,apertureSize = 3)
    #  Test the affect of different thresholds on lines returned
    lines = cv2.HoughLines(edges,1,np.pi/180,150)
    if lines is None:
        print 'No lines found'
        return
    
    print lines.shape
    # check shape of returned 
    for line in lines:
        for rho, theta in line:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000*(a))
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 - 1000*(a))
    
            cv2.line(image,(x1,y1),(x2,y2),(0,0,255),2)

    cv2.namedWindow('Hall Original', cv2.WINDOW_NORMAL)
    cv2.imshow('Hall Original',orig)
    cv2.namedWindow('Hall Edges', cv2.WINDOW_NORMAL)
    cv2.imshow('Hall Edges',edges)      
    cv2.namedWindow('Hall with Line', cv2.WINDOW_NORMAL)
    cv2.imshow('Hall with Line',image)    
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
