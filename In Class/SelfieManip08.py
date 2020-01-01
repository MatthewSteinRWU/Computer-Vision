
#!/usr/bin/env python

import cv2
import numpy as np
from non_max_suppression import non_max_suppression

def gaussian_kernel(size, sigma=1):
    size = int(size) // 2
    x, y = np.mgrid[-size:size+1, -size:size+1]
    normal = 1 / (2.0 * np.pi * sigma**2)
    g =  np.exp(-((x**2 + y**2) / (2.0*sigma**2))) * normal
    return g


def sobel_filters(img):
    Kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], np.float32)
    Ky = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]], np.float32)
    
    Ix = cv2.filter2D(img, -1, Kx)

    Iy = cv2.filter2D(img,-1, Ky)

     
    G = np.hypot(Ix, Iy)
    G = G / G.max() * 255

    theta = np.arctan2(Iy, Ix)
    
    return (G, theta)


filename = 'selfie.jpg'
def main():
    image = cv2.imread(filename)
    rows=image.shape[0]
    cols=image.shape[1]
    cv2.namedWindow('Selfie Original', cv2.WINDOW_NORMAL)
    cv2.imshow('Selfie Original',image)

    gk=gaussian_kernel(9,2)

    blur = cv2.filter2D(image,-1,gk)
          
    cv2.namedWindow('Selfie Blurred', cv2.WINDOW_NORMAL)
    cv2.imshow('Selfie Blurred',blur)

    gray=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    
    sobel, theta = sobel_filters(gray)
    cv2.namedWindow('Selfie Sobel', cv2.WINDOW_NORMAL)
    cv2.imshow('Selfie Sobel',sobel.astype(np.int8))

 
    nonmax =  non_max_suppression(sobel, theta)   
    cv2.namedWindow('Selfie Nonmax', cv2.WINDOW_NORMAL)
    cv2.imshow('Selfie Nonmax',nonmax.astype(np.int8))

    edges=  cv2.Canny(image,100,200)
    cv2.namedWindow('Selfie Canny', cv2.WINDOW_NORMAL)
    cv2.imshow('Selfie Canny',edges)    
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()



