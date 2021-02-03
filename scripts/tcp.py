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

target = rtde_r.getActualTCPPose()
def TCP():
    pub1 = rospy.Publisher('TCP_X', Float64, queue_size=10)
    pub2 = rospy.Publisher('TCP_Y', Float64, queue_size=10)
    pub3 = rospy.Publisher('TCP_Z', Float64, queue_size=10)
    rospy.init_node('UR10', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        target = rtde_r.getActualTCPPose()
        x = target[0]*1000
        y = target[1]*1000
        z = target[2]*1000
        rospy.loginfo("TCP Position")
        rospy.loginfo("X: %s, Y: %s, Z: %s", x , y, z)
        pub1.publish(x)
        pub2.publish(y)
        pub3.publish(z)
        rate.sleep()

if __name__ == '__main__':
    try:
        TCP()
    except rospy.ROSInterruptException:
        pass
