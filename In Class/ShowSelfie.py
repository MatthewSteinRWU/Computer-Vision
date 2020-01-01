#!/usr/bin/env python

import sys
import io
import cv2

filename = 'selfie.jpg'
def main():
    print 'Displaying ', filename
    image = cv2.imread(filename)
    cv2.namedWindow('Selfie', cv2.WINDOW_NORMAL)
    cv2.imshow('Selfie',image)
    cv2.waitKey(10000)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
