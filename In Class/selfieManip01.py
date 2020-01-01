#!/usr/bin/env python

import cv2

filename = 'selfie.jpg'
def main():

	image = cv2.imread(filename)
	array=image.copy()
	rows=image.shape[0]
	cols=image.shape[1]
	for x in range(200,400):
		for y in range(cols):
			array[x,y]=[255,0,0]
	cv2.imwrite('Self01.jpg',array)

if __name__ == '__main__':
    main()

