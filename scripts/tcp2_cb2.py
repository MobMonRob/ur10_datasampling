#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
import numpy as np
from Robot.UR.URRobot import URRobot
host = "192.168.178.4"
robot = URRobot(host)
tcp=robot.get_tcp_position()

def wrist():
    pub1 = rospy.Publisher('RX', Float64, queue_size=10)
    pub2 = rospy.Publisher('RY', Float64, queue_size=10)
    pub3 = rospy.Publisher('RZ', Float64, queue_size=10)
    rospy.init_node('UR10', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        RX = tcp[3]
        RY = tcp[4]
        RZ = tcp[5]
        rospy.loginfo("RX: %s, RY: %s, RZ: %s", RX , RY, RZ)
        pub1.publish(RX)
        pub2.publish(RY)
        pub3.publish(RZ)
        rate.sleep()


if __name__ == '__main__':
    try:
        wrist()
    except rospy.ROSInterruptException:
        pass
