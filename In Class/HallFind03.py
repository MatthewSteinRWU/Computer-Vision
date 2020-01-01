#!/usr/bin/env python


import cv2
import numpy as np

def intersection(rho1, theta1, rho2, theta2):
    """Finds the intersection of two lines given in Hesse normal form.

    Returns closest integer pixel locations.
    See https://stackoverflow.com/a/383527/5087436
    """
    A = np.array([
        [np.cos(theta1), np.sin(theta1)],
        [np.cos(theta2), np.sin(theta2)]
    ])
    b = np.array([[rho1], [rho2]])
    x0, y0 = np.linalg.solve(A, b)
    x0, y0 = int(np.round(x0)), int(np.round(y0))
    return x0, y0

filename = 'Hall01.jpg'
def main():
    image = cv2.imread(filename)
    if image is None:
        print 'Unable to open file ', filename
        return
    
    rows=image.shape[0]
    cols=image.shape[1]
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,150,250,apertureSize = 3)
    # Arguments are distance resolution, angle resolution, threshold
    # Large distance resolution yields larger bins so more lines meeting
    # threshold.  Larger angular resolution yeilds fewer lines with similar
    # lines counting as the same line
    lines = cv2.HoughLines(edges,2,3*np.pi/180,120)
    if lines is None:
        print 'No lines found'
        return
      
    theta1=0
    rho1=0
    for line in lines:
        for rho, theta in line:
          if theta != 0: # ignore verticals
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            seglength = 1000
            x1 = int(x0 + seglength*(-b))
            y1 = int(y0 + seglength*(a))
            x2 = int(x0 - seglength*(-b))
            y2 = int(y0 - seglength*(a))
            if theta != theta1:
              cv2.line(image,(x1,y1),(x2,y2),(0,0,255),2)
              x0, y0 = intersection(rho1,theta1,rho,theta)
              cv2.circle(image, (x0,y0),3,(255,0,0),-1)
              theta1=theta
              rho1=rho

    
    cv2.namedWindow('Hall with Line', cv2.WINDOW_NORMAL)
    cv2.imshow('Hall with Line',image)    
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
