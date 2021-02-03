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
    pub1 = rospy.Publisher('B', Float64, queue_size=10)
    pub2 = rospy.Publisher('S', Float64, queue_size=10)
    pub3 = rospy.Publisher('E', Float64, queue_size=10)
    rospy.init_node('UR10', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        target = rtde_r.getActualQ()
        B = target[0]*57.29
        S = target[1]*57.29
        E = target[2]*57.29
        rospy.loginfo("Joints")
        rospy.loginfo("Base: %s, Shoulder: %s, Elbow: %s", B , S, E)
        pub1.publish(B)
        pub2.publish(S)
        pub3.publish(E)
        rate.sleep()


if __name__ == '__main__':
    try:
        Joints()
    except rospy.ROSInterruptException:
        pass
