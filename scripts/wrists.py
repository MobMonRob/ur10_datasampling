#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64
import rtde_io
import rtde_control
import rtde_receive
import time
pi = 3.141592654

rtde_r = rtde_receive.RTDEReceiveInterface("0.0.0.0")
init_q = rtde_r.getActualQ()

target = rtde_r.getJointMode()

def Joints():
    pub1 = rospy.Publisher('W1', Float64, queue_size=10)
    pub2 = rospy.Publisher('W2', Float64, queue_size=10)
    pub3 = rospy.Publisher('W3', Float64, queue_size=10)
    rospy.init_node('UR10', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        target = rtde_r.getActualQ()
        W1 = target[3]*57.29
        W2 = target[4]*57.29
        W3 = target[5]*57.29
        rospy.loginfo("Joints")
        rospy.loginfo("Wrist1: %s, Wrist2: %s, Wrist3: %s", W1 , W2, W3)
        pub1.publish(W1)
        pub2.publish(W2)
        pub3.publish(W3)
        rate.sleep()


if __name__ == '__main__':
    try:
        Joints()
    except rospy.ROSInterruptException:
        pass
