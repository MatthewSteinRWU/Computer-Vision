import numpy as np
import random
import cv2

def drawMatches(img1, kp1, img2, kp2, matches):
    """
    Based on an answer from stackoverflow, https://stackoverflow.com/a/20260048

    My own implementation of cv2.drawMatches as OpenCV 2.4.9
    does not have this function available but it's supported in
    OpenCV 3.0.0

    This function takes in two images with their associated 
    keypoints, as well as a list of DMatch data structure (matches) 
    that contains which keypoints matched in which images.

    An image will be produced where a montage is shown with
    the first image followed by the second image beside it.

    Keypoints are delineated with circles, while lines are connected
    between matching keypoints.

    img1,img2 - Grayscale images
    kp1,kp2 - Detected list of keypoints through any of the OpenCV keypoint 
              detection algorithms
    matches - A list of matches of corresponding keypoints through any
              OpenCV keypoint matching algorithm
    """

    # Create a new output image that concatenates the two images together
    # (a.k.a) a montage
    rows1 = img1.shape[0]
    cols1 = img1.shape[1]
    rows2 = img2.shape[0]
    cols2 = img2.shape[1]

    # Create the output image
    # The rows of the output are the greater between the two images
    # and the columns are simply the sum of the two together
    # The intent is to make this a color image, so make this 3 channels
    out = np.zeros((max([rows1,rows2]),cols1+cols2,3), dtype='uint8')

    # Place the first image to the left, each BGR is the gray value
    out[:rows1,:cols1] = np.dstack([img1, img1, img1])

    # Place the next image to the right of it
    out[:rows2,cols1:] = np.dstack([img2, img2, img2])

    # For each pair of points we have between both images
    # draw circles, then connect a line between them
 
    for mat in matches:
        # MS Create a random color
        red=random.randint(0,255)
        grn=random.randint(0,255)
        blu=random.randint(0,255)
        # Get the matching keypoints for each of the images
        img1_idx = mat.queryIdx
        img2_idx = mat.trainIdx

        # x - columns
        # y - rows
        (x1,y1) = kp1[img1_idx].pt
        (x2,y2) = kp2[img2_idx].pt

        # Draw a small circle at both co-ordinates
        # radius 4
        # colour random
        # thickness = 1
        cv2.circle(out, (int(x1),int(y1)), 4, (red,grn,blu), 1)   
        cv2.circle(out, (int(x2)+cols1,int(y2)), 4, (red,grn,blu), 1)

        # Draw a line in between the two points
        # thickness = 1
        # colour random
        cv2.line(out, (int(x1),int(y1)), (int(x2)+cols1,int(y2)), (red,grn,blu), 1)

    # Return the image 
    return out