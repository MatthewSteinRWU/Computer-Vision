#!/usr/bin/env python

import cv2

filename = 'selfie.jpg'
def main():

    image = cv2.imread(filename)
    print 'image is ',image.shape[0],' rows and ',image.shape[1],  'columns', 'and depth ', image.shape[2]

if __name__ == '__main__':
    main()
