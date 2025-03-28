#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from sensor_msgs.msg import Imu
import tf
import os
from tf.transformations import euler_from_quaternion
from math import pi


class IMUParser:
    def __init__(self):
        rospy.init_node('imu', anonymous=True)
        self.image_sub = rospy.Subscriber("/imu", Imu, self.callback)
        self.is_imu = False

        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            os.system('clear')
            if not self.is_imu:
                print("[1] can't subscribe '/imu' topic... \n    please check your IMU sensor connection")

            self.is_imu = False
            rate.sleep()

    def callback(self,data):
        self.is_imu = True
        quaternion=(data.orientation.x, data.orientation.y, data.orientation.z, data.orientation.w)
        roll,pitch,yaw = euler_from_quaternion(quaternion)
        
        roll_deg=roll / pi * 180
        pitch_deg=pitch / pi * 180
        yaw_deg=yaw / pi * 180

         # 각속도 z 성분 추출 (yaw 방향 각속도)
        yaw_rate = data.angular_velocity.z
        yaw_rate_deg = yaw_rate / pi * 180  # rad/s를 deg/s로 변환

        os.system('clear')
        print(f'''
        --------------[ IMU data ]---------------
             Roll  (deg) = {roll_deg:.2f}
             Pitch (deg) = {pitch_deg:.2f}
             Yaw   (deg) = {yaw_deg:.2f}
             Yaw Rate (deg/s) = {yaw_rate_deg:.2f}
        -----------------------------------------
        ''')
        self.prev_time = rospy.get_rostime()


if __name__ == '__main__' :
    try:
        imu_parser = IMUParser()
    except rospy.ROSInterruptException:
        pass
