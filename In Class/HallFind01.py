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

    lines = cv2.HoughLines(edges,1,np.pi/180,100)
    if lines is None:
        print 'No lines found'
        return
    
    print lines.shape
    for line in lines:
        for rho, theta in line:
           print "rho={0:.2f}, theta={1:.0f}".format(rho, np.rad2deg(theta))

    cv2.namedWindow('Hall Original', cv2.WINDOW_NORMAL)
    cv2.imshow('Hall Original',orig)
    cv2.namedWindow('Hall Edges', cv2.WINDOW_NORMAL)
    cv2.imshow('Hall Edges',edges)      
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
