#!/usr/bin/env python

import cv2
import numpy as np


filename = 'selfie.jpg'
def main():
    image = cv2.imread(filename)
    rows=image.shape[0]
    cols=image.shape[1]

    
    #array=image.copy()
    for x in range(200,300):
        for y in range(cols):
              image[x,y]=np.clip(image[x,y]+[-20,-20,20], 0, 255)
    for x in range(301,400):
        for y in range(cols):
              image[x,y]=np.clip(image[x,y]+[20,20,20], 0, 255)
    for x in range(401,500):
        for y in range(cols):
              image[x,y]=np.clip(image[x,y]+[20,-20,-20], 0, 255)
             
    cv2.namedWindow('Selfie Mod', cv2.WINDOW_NORMAL)
    cv2.imshow('Selfie Mod',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
