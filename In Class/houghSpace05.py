#!/usr/bin/env python
import sys
sys.path.append("/opt/ros/kinetic/lib/python2.7/dist-packages")

import cv2
import numpy as np
import random
	
def hough_line(img):
  # Rho and Theta ranges
  # Can change these values for finer or coarser bins
  thetas = np.deg2rad(np.arange(-90.0, 90.0,1))
  width, height = img.shape
  diag_len = int(np.ceil(np.sqrt(width * width + height * height)))   # max_dist
  rhos = np.linspace(-diag_len, diag_len, diag_len * 2.0)

  # Cache some resuable values
  cos_t = np.cos(thetas)
  sin_t = np.sin(thetas)
  num_thetas = len(thetas)

  # Hough accumulator array of theta vs rho
  accumulator = np.zeros((2 * diag_len, num_thetas), dtype=np.uint64)
  y_idxs, x_idxs = np.nonzero(img)  # (row, col) indexes to edges

  # Vote in the hough accumulator
  for i in range(len(x_idxs)):
    x = x_idxs[i]
    y = y_idxs[i]

    for t_idx in range(num_thetas):
      # Calculate rho. diag_len is added for a positive index
      rho = int(round(x * cos_t[t_idx] + y * sin_t[t_idx]) + diag_len)
      accumulator[rho, t_idx] += 1

  return accumulator, thetas, rhos


def main():
  rows=500
  cols=500
 
  black=np.zeros([rows,cols], dtype=np.uint8)
  cv2.namedWindow('Canvas', cv2.WINDOW_NORMAL)

  (x1,y1)=(random.randrange(rows),random.randrange(cols))
  (x2,y2)=(random.randrange(rows),random.randrange(cols))
  cv2.circle(black,(x1,y1),3,255,2)
  cv2.circle(black,(x2,y2),3,255,2)  
  accumulator, thetas, rhos = hough_line(black)

  idx = np.argmax(accumulator)
  rho = rhos[idx / accumulator.shape[1]]
  theta = thetas[idx % accumulator.shape[1]]
  print "rho={0:.2f}, theta={1:.0f}".format(rho, np.rad2deg(theta))
  a = np.cos(theta)
  b = np.sin(theta)
  x0 = a*rho
  y0 = b*rho
  seglength = 1000
  x1 = int(x0 + seglength*(-b))
  y1 = int(y0 + seglength*(a))
  x2 = int(x0 - seglength*(-b))
  y2 = int(y0 - seglength*(a))
  cv2.line(black,(x1,y1),(x2,y2),255,2)


  
  cv2.imshow('Canvas',black)


  cv2.waitKey(0)  
  cv2.destroyAllWindows() 

if __name__ == '__main__':
    main()
