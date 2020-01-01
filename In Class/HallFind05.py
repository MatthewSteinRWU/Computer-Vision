#!/usr/bin/env python


import cv2
import numpy as np
import sys
from itertools import combinations

def intersection(rho1, theta1, rho2, theta2):
    """Finds the intersection of two lines given in Hesse normal form.

    Returns closest integer pixel locations.
    See https://stackoverflow.com/a/383527/5087436
    """
    if theta1 != theta2:
      A = np.array([
          [np.cos(theta1), np.sin(theta1)],
          [np.cos(theta2), np.sin(theta2)]
      ])
      b = np.array([[rho1], [rho2]])
      x0, y0 = np.linalg.solve(A, b)
      x0, y0 = int(np.round(x0)), int(np.round(y0))
      return x0, y0
    else:
      return 0,0


#filename = 'Hall01.jpg'
def main():

    #for eachArg in sys.argv:
    #    print eachArg
    filename = sys.argv[1]

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
    lines = cv2.HoughLines(edges,2,2*np.pi/180,100)
    if lines is None:
        print 'No lines found'
        return
      
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
            cv2.line(image,(x1,y1),(x2,y2),(0,0,255),2)
    xtotal=0
    xcount=0
    ytotal=0
    ycount=0
    for line1,line2 in combinations(lines,2):
      rho1=line1[0][0]
      theta1=line1[0][1]
      rho2=line2[0][0]
      theta2=line2[0][1]
      #print rho1, theta1, rho2, theta2
      if theta1 != 0 and theta2 != 0: # ignore verticals    

        x0, y0 = intersection(rho1,theta1,rho2,theta2)
        xtotal+=x0
        xcount+=1
        ytotal+=y0
        ycount+=1
        cv2.circle(image, (x0,y0),3,(255,0,0),-1)

    
    cv2.circle(image, (xtotal/xcount,ytotal/ycount),50,(0,255,255),3)  
    cv2.namedWindow('Hall with Line', cv2.WINDOW_NORMAL)
    cv2.imshow('Hall with Line',image)    
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
