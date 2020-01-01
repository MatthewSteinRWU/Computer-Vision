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

    e1 = cv2.getTickCount()
    print 'Starting tick count'
    print e1
    for x in range(1,rows-1):
        for y in range(1,cols-1):
            image[x,y]=np.average([orig[x-1,y-1],orig[x,y-1],orig[x+1,y-1],
                                   orig[x-1,y],  orig[x,y],  orig[x+1,y],
                                   orig[x-1,y+1],orig[x,y+1],orig[x+1,y+1]],axis=0)
    e2 = cv2.getTickCount()
    time = (e2 - e1)/ cv2.getTickFrequency()
    print 'Elapsend time: ',time
    
    cv2.namedWindow('Selfie Blurred', cv2.WINDOW_NORMAL)
    cv2.imshow('Selfie Blurred',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()




