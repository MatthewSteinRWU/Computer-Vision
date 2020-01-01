#!/usr/bin/env python


import cv2
import numpy as np

def gaussian_kernel(size, sigma=1):
    size = int(size) // 2
    x, y = np.mgrid[-size:size+1, -size:size+1]
    normal = 1 / (2.0 * np.pi * sigma**2)
    g =  np.exp(-((x**2 + y**2) / (2.0*sigma**2))) * normal
    return g


filename = 'selfie.jpg'
def main():
    image = cv2.imread(filename)
    rows=image.shape[0]
    cols=image.shape[1]
    orig=image.copy()
    cv2.namedWindow('Selfie Original', cv2.WINDOW_NORMAL)
    cv2.imshow('Selfie Original',orig)

    kernel = np.ones((5,5),np.float32)/25
    gk=gaussian_kernel(5,5)
    gk=gk/np.sum(gk)
    
    print 'Gaussian Kernel'
    print np.sum(gk)        
    dstl = cv2.filter2D(image,-1,kernel)
    dstg = cv2.filter2D(image,-1,gk)    
    #dstg = cv2.GaussianBlur(image,(5,5),0,0)
          
    cv2.namedWindow('Selfie Linear', cv2.WINDOW_NORMAL)
    cv2.imshow('Selfie Linear',dstl)
    cv2.namedWindow('Selfie Gauss', cv2.WINDOW_NORMAL)    
    cv2.imshow('Selfie Gauss',dstg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()



