#!/usr/bin/env python

import cv2
import numpy as np


filename = 'selfie.jpg'
def main():
    image = cv2.imread(filename)
    rows=image.shape[0]
    cols=image.shape[1]

    #array=image.copy()
    for y in range(cols):
        for x in range(int(200+200*np.sin(y/200.0)),int(300+200*np.sin(y/200.0))):
            image[x,y]=np.clip(image[x,y]+[-20,-20,20], 0, 255)
        for x in range(int(300+200*np.sin(y/200.0)),int(400+200*np.sin(y/200.0))):
            image[x,y]=np.clip(image[x,y]+[30,30,30], 0, 255)
        for x in range(int(400+200*np.sin(y/200.0)),int(500+200*np.sin(y/200.0))):
            image[x,y]=np.clip(image[x,y]+[20,-20,-20], 0, 255)             
    cv2.namedWindow('Selfie Mod', cv2.WINDOW_NORMAL)
    cv2.imshow('Selfie Mod',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('patrioticselfie.jpg',image)

if __name__ == '__main__':
    main()
