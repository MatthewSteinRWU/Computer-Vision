#!/usr/bin/env python

import cv2
import numpy as np


filename = 'selfie.jpg'
def main():
    image = cv2.imread(filename)
    rows=image.shape[0]
    cols=image.shape[1]

    b = image[:,:,0]
    g = image[:,:,1]
    r = image[:,:,2]
    black=np.zeros([rows,cols], dtype=np.uint8)
    white=np.full([rows,cols], 255, dtype=np.uint8) 
    array = np.zeros((2*rows,3*cols,3), dtype='uint8')
    array[:rows,:cols]=np.dstack([b,black,black])
    array[:rows,cols:2*cols]=np.dstack([black,g,black])
    array[:rows,2*cols:3*cols]=np.dstack([black,black,r])
    array[rows:2*rows,:cols]=np.dstack([b,white,white])
    array[rows:2*rows,cols:2*cols]=np.dstack([white,g,white])
    array[rows:2*rows,2*cols:3*cols]=np.dstack([white,white,r])    
    
             
    cv2.namedWindow('Selfie bgr', cv2.WINDOW_NORMAL)
    cv2.imshow('Selfie bgr',array)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
