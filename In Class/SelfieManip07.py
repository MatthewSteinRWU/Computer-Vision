#!/usr/bin/env python

import cv2
import numpy as np


filename = 'selfie.jpg'
def main():
    image = cv2.imread(filename)
    rows=image.shape[0]
    cols=image.shape[1]
    orig=image.copy()
    cv2.namedWindow('Selfie Original', cv2.WINDOW_NORMAL)
    cv2.imshow('Selfie Original',orig)


  
    lpn = laplacian = cv2.Laplacian(image,cv2.CV_64F)
    edges = cv2.Canny(image,100,200)
    cv2.namedWindow('Selfie Laplacian', cv2.WINDOW_NORMAL)
    cv2.imshow('Selfie Laplacian',lpn)
    cv2.namedWindow('Selfie Canny', cv2.WINDOW_NORMAL)
    cv2.imshow('Selfie Canny',edges)    
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
