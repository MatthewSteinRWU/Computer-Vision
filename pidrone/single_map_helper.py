#!/usr/bin/env python
"""""

Tests feature location and tracking
"""""

import math
import numpy as np
import cv2
import sys
import random

# ---------- map parameters ----------- #

MAP_PIXEL_WIDTH = 1155  # in pixel
MAP_PIXEL_HEIGHT = 847
MAP_REAL_WIDTH = 1.1  # in meter
MAP_REAL_HEIGHT = .76
# -------------------------- #

# ----- camera parameters DO NOT EDIT ----- #
CAMERA_WIDTH = 320
CAMERA_HEIGHT = 240
CAMERA_CENTER = np.float32([(CAMERA_WIDTH - 1) / 2., (CAMERA_HEIGHT - 1) / 2.]).reshape(-1, 1, 2)
CAMERA_SCALE = 290.
METER_TO_PIXEL = (float(MAP_PIXEL_WIDTH) / MAP_REAL_WIDTH + float(MAP_PIXEL_HEIGHT) / MAP_REAL_HEIGHT) / 2.
# ----------------------------- #

# ----- feature parameters DO NOT EDIT ----- #

MATCH_RATIO = 0.7
MIN_MATCH_COUNT = 10  
PROB_THRESHOLD = 0.001
MAP_FEATURES = 6000
# -------------------------- #


class Single_Map_Localization:
    """
    Single Map for localization.
    """

    def __init__(self, map_kp, map_des):
        self.map_kp = map_kp
        self.map_des = map_des

        index_params = dict(algorithm=6, table_number=6, key_size=12, multi_probe_level=1)
        search_params = dict(checks=50)
        self.matcher = cv2.FlannBasedMatcher(index_params, search_params)

        self.z = 0.33
        #MS Hardcode height of test stand 
        self.angle_x = 0.0
        self.angle_y = 0.0


    def update(self, z, angle_x, angle_y, kp, des):
        """
        kp is the position of detected features
        des is the description of detected features
        """
        # update parameters
        self.z = z
        self.angle_x = angle_x
        self.angle_y = angle_y
        weights = []
        poses = []
        weights_sum = 0.0
        
  
        p, w = self.compute_location(kp, des, self.map_kp, self.map_des)

            
        return p, w
    

    def compute_location(self, kp1, des1, kp2, des2):
        """
        compute the global location of center of current image
        :param kp1: captured keyPoints
        :param des1: captured descriptions
        :param kp2: map keyPoints
        :param des2: map descriptions
        :return: global pose
        """

        good = []
        pose = None

        if des1 is not None and des2 is not None:

            if len(des2) > 0:
                matches = self.matcher.knnMatch(des1, des2, k=2)
             
                for match in matches:
                    if len(match) > 1 and match[0].distance < MATCH_RATIO * match[1].distance:
                        good.append(match[0])

            if len(good) > MIN_MATCH_COUNT:

                src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
                dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
                
                transform = cv2.estimateRigidTransform(src_pts, dst_pts, False)
                

                if transform is not None:
                    transformed_center = cv2.transform(CAMERA_CENTER, transform)  # get global pixel
                    transformed_center = [transformed_center[0][0][0] / METER_TO_PIXEL,  # map to global pose
                                          (MAP_PIXEL_HEIGHT - 1 - transformed_center[0][0][1]) / METER_TO_PIXEL]
                    yaw = np.arctan2(transform[1, 0], transform[0, 0])  # get global heading

                    # correct the pose if the drone is not level
                    z = math.sqrt(self.z ** 2 / (1 + math.tan(self.angle_x) ** 2 + math.tan(self.angle_y) ** 2))
                    offset_x = np.tan(self.angle_x) * z
                    offset_y = np.tan(self.angle_y) * z
                    global_offset_x = math.cos(yaw) * offset_x + math.sin(yaw) * offset_y
                    global_offset_y = math.sin(yaw) * offset_x + math.cos(yaw) * offset_y
                    pose = [transformed_center[0] + global_offset_x, transformed_center[1] + global_offset_y, z, yaw]
            
        return pose, len(good)


def create_map(file_name):
    """
    create a single feature map presuming map is not much bigger than viewport 
    :param file_name: the image of map
    :return: kp and des of map
    """

    # read image and extract features
    image = cv2.imread(file_name)
    # the edgeThreshold and patchSize can be tuned if the gap between cell is too large
    # MS Did just that, set edgeThreshold from 31 to 8 to get more features
    detector = cv2.ORB_create(nfeatures=MAP_FEATURES, scoreType=cv2.ORB_FAST_SCORE, edgeThreshold=8)
    #kp = detector.detect(image, None)
    kp, des = detector.detectAndCompute(image, None)
        
    return kp, des, image



