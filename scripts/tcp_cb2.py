#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
import numpy as np
from Robot.UR.URRobot import URRobot
host = "192.168.178.4"
robot = URRobot(host)
tcp=robot.get_tcp_position()

def Joints():
    pub1 = rospy.Publisher('X', Float64, queue_size=10)
    pub2 = rospy.Publisher('Y', Float64, queue_size=10)
    pub3 = rospy.Publisher('Z', Float64, queue_size=10)
    rospy.init_node('UR10', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        X = tcp[0]
        Y = tcp[1]
        Z = tcp[2]
        rospy.loginfo("X: %s, Y: %s, Z: %s", X , Y, Z)
        pub1.publish(X)
        pub2.publish(Y)
        pub3.publish(Z)
        rate.sleep()


if __name__ == '__main__':
    try:
        Joints()
    except rospy.ROSInterruptException:
        pass
