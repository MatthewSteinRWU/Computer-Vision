#!/usr/bin/env python
"""
single_map_localization.py

Localization presuming the camera can always see a majority of the map
Suitable for RWU flight playpen where drone hovers above a 40"x32" map
If sufficient number of matches are found, transform returned as average

"""

import os
import io
import cv2
import numpy as np
import camera_info_manager
import picamera
import picamera.array
import rospy
import argparse
from cv_bridge import CvBridge, CvBridgeError
from single_map_helper_monitor import Single_Map_Localization, create_map
# ---------- map parameters ----------- #

MAP_PIXEL_WIDTH = 1155  # in pixel
MAP_PIXEL_HEIGHT = 847
MAP_REAL_WIDTH = 1.1  # in meter
MAP_REAL_HEIGHT = .76
# -------------------------- #



# ---------- camera parameters ----------- #
CAMERA_WIDTH = 320
CAMERA_HEIGHT = 240

# assume a pixel in x and y has the same length
METER_TO_PIXEL = (float(MAP_PIXEL_WIDTH) / MAP_REAL_WIDTH + float(MAP_PIXEL_HEIGHT) / MAP_REAL_HEIGHT) / 2.
CAMERA_CENTER = np.float32([(CAMERA_WIDTH - 1) / 2., (CAMERA_HEIGHT - 1) / 2.]).reshape(-1, 1, 2)

# ---------- localization parameters ----------- #
MAX_BAD_COUNT = -10
NUM_FEATURES = 400

def main():
    parser = argparse.ArgumentParser(description='Display Image Matching Regions')

    args = parser.parse_args()
    # [x, y, z, yaw]
    pos = [0, 0, 0, 0]

    angle_x = 0.0
    angle_y = 0.0
    # localization does not estimate z
    z = 0.33

    first_locate = True
    #MS Local test, set to locate position immediately without waiting for web interface
    # locate_position = False
    locate_position = True

    map_counter = 0
    max_map_counter = 0

    # constant
    alpha_yaw = 0.1  # perceived yaw smoothing alpha
    hybrid_alpha = 0.7  # blend position with first frame and int  # MS was 0.3


    node_name = os.path.splitext(os.path.basename(__file__))[0]

    cim = camera_info_manager.CameraInfoManager("picamera", "package://pidrone_pkg/params/picamera.yaml")
    cim.loadCameraInfo()
    if not cim.isCalibrated():
        rospy.logerr("warning, could not find calibration for the camera.")

    try:
        bridge = CvBridge()
        # Create the in-memory stream
        stream = io.BytesIO()
        with picamera.PiCamera(framerate=90) as camera:
            camera.resolution = (CAMERA_WIDTH, CAMERA_HEIGHT)
            with picamera.array.PiRGBArray(camera) as stream:     
                detector = cv2.ORB_create(nfeatures=NUM_FEATURES, scoreType=cv2.ORB_FAST_SCORE)
                map_kp, map_des, map_image = create_map('map.jpg')
                estimator = Single_Map_Localization(map_kp, map_des)
                estimator.set_map_image(map_image)
                print "Starting Single Map Localization"
            
                while True:  # Do forever

                    camera.capture(stream, format='bgr')
                    # At this point the image is available as stream.array
                    image = stream.array            # Get a single image
                    stream.seek(0)  # Rewind the stream
                    estimator.set_cur_image(image)
                    curr_kp, curr_des = detector.detectAndCompute(image, None)
                    img_keypoints = np.empty((image.shape[0], image.shape[1], 3), dtype=np.uint8)
                    cv2.drawKeypoints(image, curr_kp, img_keypoints)
                    cv2.namedWindow('Current image', cv2.WINDOW_NORMAL)
                    cv2.imshow('Current image',img_keypoints)
                    cv2.waitKey(50)

                    if curr_kp is not None and curr_des is not None:
                                                
                        new_pos, weight = estimator.update(z, angle_x, angle_y,
                                                         curr_kp, curr_des)


                        # update position
                        if new_pos is not None:
                            pos = [hybrid_alpha * new_pos[0] + (1.0 - hybrid_alpha) * pos[0],
                                        hybrid_alpha * new_pos[1] + (1.0 - hybrid_alpha) * pos[1],
                                        z,
                                        alpha_yaw * new_pos[3] + (1.0 - alpha_yaw) * pos[3]]

                            print '--pose', 'x ', pos[0], 'y ', pos[1], 'z', pos[2], 'yaw ',pos[3]
                            map_counter = min(map_counter + 1, -MAX_BAD_COUNT)  

                        else:
                            map_counter = map_counter - 1
                            
                        # if it's been a while without a significant average weight
                        if map_counter < MAX_BAD_COUNT:
                            locate_position = False
                            map_counter = 0
                            print 'Lost, leaving position control'

                        print 'count', map_counter
                    else:
                        print "CANNOT FIND ANY FEATURES !!!!!"

    
        print "Shutdown Received"
    except Exception:
        print "Cancel Received"
        raise


if __name__ == '__main__':
    main()
