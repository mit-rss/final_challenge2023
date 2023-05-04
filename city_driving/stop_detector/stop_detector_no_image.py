#!/usr/bin/env python

import cv2
import rospy

import numpy as np
import math
from sensor_msgs.msg import Image
from std_msgs.msg import Bool
from std_msgs.msg import Int32
from std_msgs.msg import Float64MultiArray

class SignDetector:
    def __init__(self):
        self.bb_publisher = rospy.Publisher("/stop_sign_detector/stop_sign_bb", Float64MultiArray, queue_size=1)
        self.subscriber = rospy.Subscriber("/stop_sign_dist", Int32, self.dist_callback)
        self.subscriber = rospy.Subscriber("/stop_sign_angle", Int32, self.angle_callback)

        self.dist = 0
        self.angle = 0
        self.has_dist = False
        self.has_angle = False

    def dist_callback(self, dist):
        self.dist = dist
        self.has_dist = True

        if (self.has_angle):
            self.publish_bb()

    def angle_callback(self, angle):
        self.angle = angle
        self.has_angle = True

        if (self.has_dist):
            self.publish_bb()

    def publish_bb(self):
        # Takes in real world distance and angle from center of camera 
        # Returns real world 3D coordinates of bounding box

        my_msg = Float64MultiArray()
        shift = math.sin(math.radians(self.angle))*self.dist
        bb_x1 = -4+shift
        bb_x2 = 4+shift
        my_msg.data = [[bb_x1, 12, self.dist], [bb_x2, 12, self.dist], [bb_x1, 20, self.dist], [bb_x2, 20, self.dist]]
        self.bb_publisher.publish(my_msg)
        self.has_dist = False
        self.has_angle = False


if __name__=="__main__":
    rospy.init_node("stop_sign_detector_no_image")
    detect = SignDetector()
    rospy.spin()
