#!/usr/bin/env python
#  Selfie  linear filter
import sys
sys.path.append("/opt/ros/kinetic/lib/python2.7/dist-packages")
import cv2
import numpy as np
filename = 'selfie.jpg'
def main():
        image = cv2.imread(filename)
        rows=image.shape[0]
        cols=image.shape[1]
        #  Apply a linear averaging filter, average the 17 neighbors to get the new pixel value
        orig=image.copy()
        cv2.namedWindow('Selfie Original', cv2.WINDOW_NORMAL)
        cv2.imshow('Selfie Original', orig)
        # Measure how long processing takes
        e1=cv2.getTickCount()
        print e1
        for x in range(200,500):  # Ignore outer column
                for y in range(200,500):
                        image[x,y]=(3.0*orig[x-1,y-1]/17+orig[x,y-1]/17+3.0*orig[x+1,y-1]/17+
                                                      orig[x-1,y]/17+            orig[x,y]/17+   orig[x+1,y]/17+
                                                      3.0*orig[x-1,y+1]/17+orig[x,y+1]/17+3.0*orig[x+1,y+1]/17)
                
        e2=cv2.getTickCount()
        time=(e2-e1)/cv2.getTickFrequency()
        print 'Elasped Time: ', time
        cv2.namedWindow('Selfie Modified', cv2.WINDOW_NORMAL)
        cv2.imshow('Selfie Modified', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == '__main__':
        main()

